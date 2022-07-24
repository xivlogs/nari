use crate::param_to_struct;
use pyo3::prelude::*;

/// Get actor type from tuple
#[pyfunction]
pub(crate) fn parse_actor(inp: Vec<&str>) -> (u32, &str) {
    (
        param_to_struct::param_to_4_byte_int(inp.first().unwrap()),
        inp.last().unwrap(),
    )
}
