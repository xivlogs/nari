use pyo3::prelude::*;
use crate::param_to_struct;

/// Get actor type from tuple
#[pyfunction]
pub fn parse_actor(inp: Vec<&str>) -> (u32, &str){
    (param_to_struct::param_to_4_byte_int(inp.first().unwrap()), inp.last().unwrap())
}

