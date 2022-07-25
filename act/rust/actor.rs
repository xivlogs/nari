use crate::parser;
use pyo3::prelude::*;

/// Get actor type from tuple
#[pyfunction]
#[pyo3(text_signature = "(name_id_pair: list[str]) -> (int, str)")]
pub(crate) fn parse_actor(inp: Vec<&str>) -> (u32, &str) {
    (
        parser::param_to_4_byte_int(inp.first().unwrap()),
        inp.last().unwrap(),
    )
}
