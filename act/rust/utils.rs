use md5::{Digest, Md5};
use pyo3::prelude::*;
use sha2::Sha256;
use std::num::ParseIntError;

#[pyfunction]
#[pyo3(text_signature = "(time_str: str) -> int")]
pub(crate) fn date_from_act_timestamp(time_str: &str) -> i64 {
    let str_len = time_str.len();
    let date_time_str = &mut time_str[..str_len - 7].to_owned();
    date_time_str.push_str(&time_str[str_len - 6..]);
    let time = chrono::DateTime::parse_from_str(date_time_str.as_str(), "%Y-%m-%dT%H:%M:%S%.f%:z")
        .unwrap();
    time.timestamp_millis()
}

fn decode_hex(s: &str) -> Result<Vec<u8>, ParseIntError> {
    (0..s.len())
        .step_by(2)
        .map(|i| u8::from_str_radix(&s[i..i + 2], 16))
        .collect()
}

/// Pads string to 4 length with 0 in front
#[pyfunction]
#[pyo3(text_signature = "(src_str: str) -> str")]
pub(crate) fn pad4(str: &str) -> String {
    format!("{:0>4}", str)
}

/// Pads string to 8 length with 0 in front
#[pyfunction]
#[pyo3(text_signature = "(src_str: str) -> str")]
pub(crate) fn pad8(str: &str) -> String {
    format!("{:0>8}", str)
}

pub(crate) fn parse_float(inp: &str) -> f32 {
    unsafe { std::mem::transmute::<u32, f32>(parse_int(inp)) }
}

pub(crate) fn parse_int(inp: &str) -> u32 {
    let res = u32::from_str_radix(inp, 10);
    if res.is_ok() {
        res.unwrap()
    } else {
        0
    }
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
