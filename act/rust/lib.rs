mod actor;
mod lines_to_params;
mod parser;
mod utils;

use pyo3::prelude::*;

#[pymodule]
fn nari_act_ext(py: Python, m: &PyModule) -> PyResult<()> {
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

    let parser_module = PyModule::new(py, "parser")?;
    parser_module.add_function(wrap_pyfunction!(parser::param_to_2_byte_int, m)?)?;
    parser_module.add_function(wrap_pyfunction!(parser::param_to_2x2_byte_int, m)?)?;
    parser_module.add_function(wrap_pyfunction!(parser::param_to_4_byte_float, m)?)?;
    parser_module.add_function(wrap_pyfunction!(parser::param_to_4_byte_int, m)?)?;
    parser_module.add_function(wrap_pyfunction!(parser::param_to_4x1_byte_int, m)?)?;
    parser_module.add_function(wrap_pyfunction!(parser::params_to_8_byte_int, m)?)?;
    parser_module.add_function(wrap_pyfunction!(parser::params_to_param, m)?)?;
    parser_module.add_function(wrap_pyfunction!(parser::validate_checksum, m)?)?;
    m.add_submodule(parser_module)?;

    let utils_module = PyModule::new(py, "utils")?;
    utils_module.add_function(wrap_pyfunction!(utils::get_time_milliseconds, m)?)?;
    utils_module.add_function(wrap_pyfunction!(utils::pad4, m)?)?;
    utils_module.add_function(wrap_pyfunction!(utils::pad8, m)?)?;
    m.add_submodule(utils_module)?;

    // HACK: abuse python imports to make `from rustext.utils import validate_checksum` work
    let sys: &PyModule = py.import("sys").unwrap();
    sys.getattr("modules")?.set_item("nari_act_ext.parser", parser_module)?;
    sys.getattr("modules")?.set_item("nari_act_ext.utils", utils_module)?;

    Ok(())
}
