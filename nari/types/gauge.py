"""Stuff for gauge of actors"""
from datetime import datetime
from struct import unpack
from typing import Dict, List, Any

from nari.types.event import Event
from nari.types.actor import Actor
from nari.types.classjoblevel import Job
from nari.util.exceptions import JobGaugeNotFound


class Gauge(Event):  # pylint: disable=too-few-public-methods
    """Event represents the gauge of an actor
    Because Gauge data differs per job, each gauge will be stored as a dict with the details as keys.

    """

    job_gauge_definitions: Dict[int, str] = {
        Job.RDM: "<BBBxxxxx",
        Job.WAR: "<BBxxxxxx",
        Job.DRK: "<BBxHxxx",
        Job.PLD: "<BBxxxxxx",
        Job.GNB: "<BBxHBxx",
        Job.BRD: "<BHBBBxxx",
        Job.DNC: "<BBxBBBBB",
        Job.DRG: "<BHBBxxx",
        Job.NIN: "<BIBBx",
        Job.THM: "<BxHbxxx",  # TODO: Confirm this
        Job.BLM: "<BBHHbBBB",  # TODO: Check Memory Size
        Job.WHM: "<BxHBBxx",
        Job.ACN: "<BxxxxBxx",
        Job.SMN: "<BHBBBxx",
        Job.SCH: "<BxxBBHB",
        Job.PGL: "<BHBxxxx",  # TODO: Confirm what happened to GL Stacks
        Job.MNK: "<BHBBxxx",
        Job.MCH: "<BHHBBx",
        Job.AST: "<BxxxBBBB",  # TODO: Check Memory Size
        Job.SAM: "<BxxxBBxx",
    }

    def __init__(self, *,
                 timestamp: datetime,
                 source_actor: Actor,
                 ):
        super().__init__(timestamp)
        self.source_actor = source_actor
        self.data = None

    def __repr__(self):
        return '<StatusApply>'

    @staticmethod
    def convert_line_to_gauge(params: List[str]) -> tuple:
        """Combines the two gauge data fields into a bytearray to be processed depending on job"""
        gauge_data = "".join([params[4], params[3].zfill(8)])
        intdata = int(gauge_data, 16)
        job_num = intdata & 0xFF

        try:
            unpack_str = Gauge.job_gauge_definitions[job_num]
        except KeyError:
            raise JobGaugeNotFound

        return unpack(unpack_str, intdata.to_bytes(8, "little"))

    @staticmethod
    def convert_bytes_to_data(gauge_bytes: tuple[int]) -> Dict[str, Any]:

        # TODO: Write functions for each job
        memory_defs: Dict[int, tuple[str]] = {
            Job.RDM: ("JobID", "White_Mana", "Black_Mana"),
            Job.WAR: ("JobID", "Beast_Gauge"),
            Job.DRK: ("JobID", "Blood_Gauge", "Darkside_ms"),
            Job.PLD: ("JobID", "Oath_Gauge"),
            Job.GNB: ("JobID", "Cartridges", "Continuation_ms", "Continuation_State"),
            Job.BRD: ("JobID", "Song_ms", "Song_Procs", "Soul_Gauge", "Song"),
            Job.DNC: ("JobID", "Feathers", "Step1", "Step2", "Step3", "Step4", "Current_Step"),
            Job.DRG: ("JobID", "Blood_or_life_ms", "Stance", "Eyes_Amount"),
            Job.NIN: ("JobID", "Huton_ms", "Ninki", "Huton_Count"),
            Job.THM: ("JobID", "Umbral_ms", "Umbral_Stacks"),
            Job.BLM: (
                "JobID", "Next_Poly_ms", "Umbral_ms", "Umbral_Stacks", "Umbral_Hearts", "Foul_Count", "Enochian_State"),
            Job.WHM: ("JobID", "Lily_ms", "Lily_Stacks", "Blood_Lily_Stacks"),
            Job.ACN: ("JobID", "Aetherflow_Stacks"),
            Job.SMN: ("JobID", "Stance_ms", "Bahamut_Stance", "Bahamut_Summoned", "SMN_stacks"),
            # SMN stacks are special
            Job.SCH: ("JobID", "Aetherflow_Stacks", "Fairy_Gauge", "Fairy_ms", "Fairy_Status"),
            Job.PGL: ("JobID", "Lightning_ms", "Lightning_Stacks"),  # TODO: Confirm this
            Job.MNK: ("JobID", "Lightning_ms", "Lightning_Stacks", "Chakra Stacks"),  # TODO: Confirm this
            Job.MCH: ("JobID", "Overheat_ms", "Battery_ms", "Heat", "Battery"),
            Job.AST: ("JobID", "Card", "Arcanum_1", "Arcanum_2", "Arcanum_3"),
            Job.SAM: ("JobID", "Kenki", "Sen_Bits")
        }
        job_id = gauge_bytes[0]
        data_names = memory_defs[job_id]
        data = {name: gauge_bytes[pos] for pos, name in enumerate(data_names)}

        """TODO: Jobs that require extra data formatting functions (SAM (Splitting Sen), AST (Card Enum), SMN (Stack 
        Split), BLM (Polyglot/Eno-chan, DRG (eyes), DNC (steps), BRD (songs) """

        return data
