use crate::util;
use pyo3::prelude::*;

/// Param to 2-byte integer
#[pyfunction]
pub fn param_to_2_byte_int(inp: &str) -> u16 {
    u16::from_str_radix(inp, 16).unwrap()
}

/// Param to two 2-byte integers
#[pyfunction]
pub fn param_to_2x2_byte_int(inp: &str) -> (u16, u16) {
    let num = u32::from_str_radix(inp, 16).unwrap();
    let param0 = (num >> 16) as u16;
    let param1 = num as u16;
    (param0, param1)
}

/// Param to 4-byte float
#[pyfunction]
pub fn param_to_4_byte_float(inp: &str) -> f32 {
    unsafe { std::mem::transmute::<u32, f32>(u32::from_str_radix(inp, 16).unwrap()) }
}

/// Param to 4-byte integer
#[pyfunction]
pub fn param_to_4_byte_int(inp: &str) -> u32 {
    u32::from_str_radix(inp, 16).unwrap()
}

/// Param to four 1-byte integers
#[pyfunction]
pub fn param_to_4x1_byte_int(inp: &str) -> (u8, u8, u8, u8) {
    let num = u32::from_str_radix(inp, 16).unwrap();
    let param0 = (num >> 24) as u8;
    let param1 = (num >> 16) as u8;
    let param2 = (num >> 8) as u8;
    let param3 = num as u8;
    (param0, param1, param2, param3)
}

/// Two params to 8-byte integers
#[pyfunction]
pub fn params_to_8_byte_int(inp: Vec<&str>) -> u64 {
    (u64::from_str_radix(inp.get(0).unwrap(), 16).unwrap() << 32)
        + u64::from_str_radix(inp.get(1).unwrap(), 16).unwrap()
}

/// Two params to param
#[pyfunction]
pub fn params_to_param(inp: Vec<&str>) -> String {
    inp.iter()
        .map(|x| util::pad8(x))
        .collect::<Vec<String>>()
        .join("")
}
