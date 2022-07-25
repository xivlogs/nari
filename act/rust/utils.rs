use pyo3::prelude::*;
use std::num::ParseIntError;

#[pyfunction]
#[pyo3(text_signature = "(time_str: str) -> int")]
pub(crate) fn get_time_milliseconds(time_str: &str) -> i64 {
    let str_len = time_str.len();
    let date_time_str = &mut time_str[..str_len - 7].to_owned();
    date_time_str.push_str(&time_str[str_len - 6..]);
    let time = chrono::DateTime::parse_from_str(date_time_str.as_str(), "%Y-%m-%dT%H:%M:%S%.f%:z")
        .unwrap();
    time.timestamp_millis()
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
