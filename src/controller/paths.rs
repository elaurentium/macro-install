use pyo3::prelude::*;
use pyo3::wrap_pyfunction;
use serde::{Deserialize, Serialize};
use std::fs;
use std::fs::File;
use std::io::{self, Read, Write};
use std::path::{Path, PathBuf};

#[derive(Serialize, Deserialize, Debug)]
struct Paths {
    pub path_name: String,
    pub path_value: String,
}

fn get_path_file() -> PathBuf {
    if cfg!(target_os = "windows") {
        PathBuf::from(r".\src\paths\paths.json")
    } else {
        PathBuf::from("./src/paths/paths.json")
    }
}

#[pyfunction]
fn load_paths() -> PyResult<String> {
    let path_file = get_path_file();

    if path_file.exists() {
        let mut file = File::open(path_file)?;
        let mut content = String::new();
        file.read_to_string(&mut content)?;

        Ok(content)
    } else {
        Ok("[]".to_string())
    }
}

#[pyfunction]
fn save_path(paths: String) -> PyResult<()> {
    let path_file = get_path_file();

    if let Some(parent_dir) = path_file.parent() {
        fs::create_dir_all(parent_dir)?;
    }

    let file = File::create(path_file)?;
    let paths_data: Vec<Paths> = serde_json::from_str(&paths).unwrap();

    serde_json::to_writer(file, &paths_data)?;
    Ok(())
}

#[pymodule]
fn rust_python_integration(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(load_paths, m)?)?;
    m.add_function(wrap_pyfunction!(save_path, m)?)?;
    Ok(())
}
