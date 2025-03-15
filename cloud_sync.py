import dropbox
import os

DROPBOX_ACCESS_TOKEN = ""

def upload_to_cloud():
    try:
        dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)
        file_path = "passwords.txt"
        if not os.path.exists(file_path):
            print("File passwords.txt tidak ditemukan.")
            return

        with open(file_path, "rb") as file:
            dbx.files_upload(file.read(), "/passwords.txt", mode=dropbox.files.WriteMode.overwrite)
        print("Data berhasil diunggah ke cloud.")
    except dropbox.exceptions.AuthError:
        print("Gagal mengunggah data: Token akses Dropbox tidak valid atau scope tidak diaktifkan.")
    except dropbox.exceptions.ApiError as api_err:
        print(f"Gagal mengunggah data: {api_err.error}")
    except Exception as e:
        print(f"Gagal mengunggah data: {e}")

def download_from_cloud():
    try:
        dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)
        try:
            metadata, response = dbx.files_download("/passwords.txt")
            with open("passwords.txt", "wb") as file:
                file.write(response.content)
            print("Data berhasil diunduh dari cloud.")
        except dropbox.exceptions.ApiError:
            print("File tidak ditemukan di Dropbox.")
    except dropbox.exceptions.AuthError:
        print("Gagal mengunduh data: Token akses Dropbox tidak valid atau scope tidak diaktifkan.")
    except Exception as e:
        print(f"Gagal mengunduh data: {e}")