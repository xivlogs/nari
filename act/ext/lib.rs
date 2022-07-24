mod actor;
mod lines_to_params;
mod param_to_struct;
mod util;

use pyo3::prelude::*;

#[pymodule]
fn nari_act_ext(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(actor::parse_actor, m)?)?;
    m.add_function(wrap_pyfunction!(lines_to_params::ability_from_params, m)?)?;
    m.add_function(wrap_pyfunction!(
        lines_to_params::action_effect_from_params,
        m
    )?)?;
    m.add_function(wrap_pyfunction!(
        lines_to_params::status_effect_from_params,
        m
    )?)?;
    m.add_function(wrap_pyfunction!(
        lines_to_params::statuslist_from_params,
        m
    )?)?;
    m.add_function(wrap_pyfunction!(param_to_struct::param_to_2_byte_int, m)?)?;
    m.add_function(wrap_pyfunction!(param_to_struct::param_to_2x2_byte_int, m)?)?;
    m.add_function(wrap_pyfunction!(param_to_struct::param_to_4_byte_float, m)?)?;
    m.add_function(wrap_pyfunction!(param_to_struct::param_to_4_byte_int, m)?)?;
    m.add_function(wrap_pyfunction!(param_to_struct::param_to_4x1_byte_int, m)?)?;
    m.add_function(wrap_pyfunction!(param_to_struct::params_to_8_byte_int, m)?)?;
    m.add_function(wrap_pyfunction!(param_to_struct::params_to_param, m)?)?;
    m.add_function(wrap_pyfunction!(util::get_time_milliseconds, m)?)?;
    m.add_function(wrap_pyfunction!(util::validate_checksum, m)?)?;
    m.add_function(wrap_pyfunction!(util::pad4, m)?)?;
    m.add_function(wrap_pyfunction!(util::pad8, m)?)?;
    Ok(())
}
