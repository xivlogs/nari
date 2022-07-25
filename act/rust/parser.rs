use crate::utils;
use md5::{Digest, Md5};
use pyo3::prelude::*;
use sha2::Sha256;
use std::num::ParseIntError;

fn decode_hex(s: &str) -> Result<Vec<u8>, ParseIntError> {
    (0..s.len())
        .step_by(2)
        .map(|i| u8::from_str_radix(&s[i..i + 2], 16))
        .collect()
}

/// Param to 2-byte integer
#[pyfunction]
#[pyo3(text_signature = "(params: list[str]) -> int")]
pub(crate) fn param_to_2_byte_int(inp: &str) -> u16 {
    u16::from_str_radix(inp, 16).unwrap()
}

/// Param to two 2-byte integers
#[pyfunction]
#[pyo3(text_signature = "(params: list[str]) -> (int, int)")]
pub(crate) fn param_to_2x2_byte_int(inp: &str) -> (u16, u16) {
    let num = u32::from_str_radix(inp, 16).unwrap();
    let param0 = (num >> 16) as u16;
    let param1 = num as u16;
    (param0, param1)
}

/// Param to 4-byte float
#[pyfunction]
#[pyo3(text_signature = "(params: list[str]) -> float")]
pub(crate) fn param_to_4_byte_float(inp: &str) -> f32 {
    unsafe { std::mem::transmute::<u32, f32>(u32::from_str_radix(inp, 16).unwrap()) }
}

/// Param to 4-byte integer
#[pyfunction]
#[pyo3(text_signature = "(params: list[str]) -> int")]
pub(crate) fn param_to_4_byte_int(inp: &str) -> u32 {
    u32::from_str_radix(inp, 16).unwrap()
}

/// Param to four 1-byte integers
#[pyfunction]
#[pyo3(text_signature = "(params: list[str]) -> list[int]")]
pub(crate) fn param_to_4x1_byte_int(inp: &str) -> (u8, u8, u8, u8) {
    let num = u32::from_str_radix(inp, 16).unwrap();
    let param0 = (num >> 24) as u8;
    let param1 = (num >> 16) as u8;
    let param2 = (num >> 8) as u8;
    let param3 = num as u8;
    (param0, param1, param2, param3)
}

/// Two params to 8-byte integers
#[pyfunction]
#[pyo3(text_signature = "(params: list[str]) -> int")]
pub(crate) fn params_to_8_byte_int(inp: Vec<&str>) -> u64 {
    (u64::from_str_radix(inp.get(0).unwrap(), 16).unwrap() << 32)
        + u64::from_str_radix(inp.get(1).unwrap(), 16).unwrap()
}

/// Two params to param
#[pyfunction]
#[pyo3(text_signature = "(params: list[str]) -> str")]
pub(crate) fn params_to_param(inp: Vec<&str>) -> String {
    inp.iter()
        .map(|x| utils::pad8(x))
        .collect::<Vec<String>>()
        .join("")
}

/// Gets [to_hash, check] from a line based on algo
#[pyfunction]
#[pyo3(text_signature = "(line: str, index: int, algo: str) -> bool")]
pub(crate) fn validate_checksum(line: &str, index: i32, alg: &str) -> bool {
    let (md5, sub) = match alg {
        "md5" => (true, 32),
        _ => (false, 16),
    };
    let last = line.len();
    if md5 {
        let mut hasher = Md5::new();
        hasher.update(&line[..last - sub]);
        hasher.update(&index.to_string());
        &hasher.finalize()[..] == decode_hex(&line[last - sub..]).unwrap()
    } else {
        let mut hasher = Sha256::new();
        hasher.update(&line[..last - sub]);
        hasher.update(&index.to_string());
        &hasher.finalize()[..] == decode_hex(&line[last - sub..]).unwrap()
    }
}
