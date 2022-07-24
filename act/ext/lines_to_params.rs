use pyo3::prelude::*;
use crate::util;
use crate::param_to_struct;

/// Params to ability
#[pyfunction]
pub fn ability_from_params(inp: Vec<&str>) -> ((u32, &str), Vec<u32>, Vec<f32>, (u32, &str), Vec<u32>, Vec<f32>, Vec<&str>, Vec<(u8, u8, u8, u8, u16, u8, u8)>, u32) {
    let mut col = inp;
    let source_actor = col.drain(..2).collect::<Vec<&str>>();
    let ability = col.drain(..2).collect::<Vec<&str>>();
    let target_actor = col.drain(..2).collect::<Vec<&str>>();
    let action_effects = col.drain(..16).collect::<Vec<&str>>();
    let source_resources = col.drain(..6).collect::<Vec<&str>>();
    let source_position = col.drain(..4).collect::<Vec<&str>>();
    let target_resources = col.drain(..6).collect::<Vec<&str>>();
    let target_position = col.drain(..4).collect::<Vec<&str>>();
    let sequence = param_to_struct::param_to_4_byte_int(col.first().unwrap());
    (parse_actor(source_actor),
     source_resources.iter().map(|x| util::parse_int(x)).collect(),
     source_position.iter().map(|x| util::parse_float(x)).collect(),
     parse_actor(target_actor),
     target_resources.iter().map(|x| util::parse_int(x)).collect(),
     target_position.iter().map(|x| util::parse_float(x)).collect(),
     ability,
     action_effects.chunks(2).map(|x| action_effect_from_params(x.to_vec())).collect::<Vec<(u8, u8, u8, u8, u16, u8, u8)>>(),
     sequence)
}

/// Params to action_effect
#[pyfunction]
pub fn action_effect_from_params(inp: Vec<&str>) -> (u8, u8, u8, u8, u16, u8, u8) {
    let num = param_to_struct::params_to_8_byte_int(inp);
    let param0 = (num >> 56) as u8;
    let param1 = (num >> 48) as u8;
    let param2 = (num >> 40) as u8;
    let param3 = (num >> 32) as u8;
    let param4 = (num >> 16) as u16;
    let param5 = (num >> 8) as u8;
    let param6 = num as u8;
    (param0, param1, param2, param3, param4, param5, param6)
}

/// Params to status_effect
#[pyfunction]
pub fn status_effect_from_params(inp: Vec<&str>) -> (u16, u16, f32, u32) {
    let (param0, param1) = param_to_struct::param_to_two_2_byte_int(inp.get(0).unwrap());
    (param0, param1, param_to_struct::param_to_4_byte_float(inp.get(1).unwrap()), param_to_struct::param_to_4_byte_int(inp.get(2).unwrap()))
}

/// Params to statuslist
#[pyfunction]
pub fn statuslist_from_params(inp: Vec<&str>) -> ((u32, &str), &str, Vec<u32>, Vec<f32>, Vec<(u16, u16, f32, u32)>) {
    let mut col = inp;
    let actor = col.drain(..2).collect::<Vec<&str>>();
    let class = col.drain(..1).collect::<Vec<&str>>();
    let resources = col.drain(..6).collect::<Vec<&str>>();
    let position = col.drain(..4).collect::<Vec<&str>>();
    let status_effects = col.drain(..col.len()-1).collect::<Vec<&str>>();
    (parse_actor(actor),
     class.first().unwrap(),
     resources.iter().map(|x| util::parse_int(x)).collect(),
     position.iter().map(|x| util::parse_float(x)).collect(),
     status_effects.chunks(3).map(|x| status_effect_from_params(x.to_vec())).collect())
}
