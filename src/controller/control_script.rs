use std::process::{Command, Stdio};
use std::path::Path;
use std::fs;
use std::io;
use rfd::FileDialog;
use native_dialog::{MessageDialog, MessageType};
use std::sync::Mutex;

lazy_static::lazy_static! {
    static ref OPTIONS: Mutex<Vec<String>> = Mutex::new(new![]);
}

fn exec_script(script_path: &str) -> Result<(), io::Error>  {
    let path = Path::new(script_path);

    if !path.exists() {
        return Err(io::Error::new(io::ErrorKind::NotFound, "Arquivo não encontrado"));
    }

    let ext = path.extension().and_then(|e| e.to_str()).unwrap_or("").to_lowercase();

    let command = if ext == "cmd" {
        format!("cmd /c start cmd /k \"{}\"", path.display())
    } else {
        format!("cmd /c start powershell -NoExit -File \"{}\"", path.display())
    };

    let result = Command::new("cmd")
        .args(&["/c", &command])
        .stdout(Stdio::inherit())
        .stderr(Stdio::inherit())
        .spawn();

    match result {
        Ok(_) => Ok(()),
        Err(error) => {
            MessageDialog::new()
                .set_type(MessageType::Error)
                .set_title("Erro ao executar script")
                .set_text(&format!("Ocorreu um erro ao executar o script: {}", error))
                .show_alert()
                .unwrap();
            Err(error)
        }
    }
}

fn exec_button(select: &str) {
    match exec_script(select) {
        Ok(_) => (),
        Err(error) => {
            MessageDialog::new()
            .set_type(MessageType::Error)
            .set_title("Erro")
            .set_text(&error.to_string())
            .show_alert()
            .unwrap();
        }
    }
}

fn search_button() -> Option<String> {
    let file_path = FileDialog::new().pick_file();

    if let Some(path) = file_path {
        let path_str = path.display().to_str();
        OPTIONS.lock().unwrap().push(path_str.clone());
        exec_button(&path_str);
        Some(path_str)
    } else {
        None
    }
}