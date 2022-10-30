Readers
=======

Nari readers are based off the base reader class


Guide: Creating a custom reader
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's say you have a fictitious xml format that documents casts and actions:

.. code-block:: xml

    <Log>
        <Actors type="Party">
            <Actor id="2329" name="Danger Duck" />
            <Actor id="539" name="Lethal Lizard" />
        </Actors>
        <Actors type="Enemies">
            <Actor id="23de" name="Alte Roite" />
        </Actors>
        <Events>
            <BeginCast timestamp="1590687335012" source="2329" target="23de" ability_id="25865" duration="2.41" />
            <Action timestamp="1590687337512"  source="2329" target="23de" ability_id="25865" sequence="22">
                <ActionEffect category="3" severity="1" value="1234" multiplier="0" />
            </Action>
        </Events>
    </Log>

This data is somewhat basic, but we can corral this into a nari format with a little bit of work. The first thing to
note is that the ``BeginCast`` element seems to line up with nari's ``CastStart`` event; the ``Action`` element also
lines up with the ``Ability`` event. Next, we note that this format separates 'actors' out into two groups: party
characters and NPCs/enemies. nari does not make a distiction, but it does have an ``Actor`` type to encapsulate that
data.

Let's start by laying out the scaffolding of this "fake xml reader" and processing the actors, along with
getting the events ready to process into nari events. We'll use python's native xml parser from ``xml.etree``
to accomplish this:

.. code-block:: python

    import xml.etree.ElementTree as ETree # reading xml
    from xml.etree.ElementTree import Element # type annotations

    from nari.io.reader import Reader # nari reader class

    def get_actor_id(actor_element: Element, attrib: str = 'id') -> int:
        """Helpful utility function that takes an xml element and parses out an id from it"""
        return int(
            actor_element.attrib.get(attrib, 'E0000000'), # fallback to an unknown id if we cannot find one
            16 # actor id are in hex
        )

    class FakeXMLReader(Reader):
        def __init__(self, xmlfile: Path | str):
            # parse xml
            if isinstance(xmlfile, str):
                xmlfile = Path(xmlfile)
            if not xmlfile.exists():
                raise Exception(f'file {xmlfile} not found')
            self.tree = ETree.parse(xmlfile)

            # parse actors from xml
            self.actors = {}
            for actorlist in self.tree.findall('Actors'):
                # it doesn't matter if type is party or enemies, we're treating
                # this as an implementation detail
                for actor in actorlist:
                    actor_id = get_actor_id(actor)
                    actor_name = actor.attrib.get('name', '')
                    self.actors[actor_id] = Actor(id=actor_id, name=actor_name)

            # store events and our index in the events
            self.events = self.tree.find('Events')
            self.events_len = len(self.events)
            self.index = 0


Next, we need to process the events. To do that, you need to write a ``read_next`` method, which returns a nari event.

.. caution::

    The ``read_next`` method should endeavor to return a nari event where possible; if you cannot determine the type of
    event, it's best to generate a dummy ``Event`` with only the timestamp filled in. If you return ``None``, this
    prompts the reader to assume there are no more events to process and stop processing.
