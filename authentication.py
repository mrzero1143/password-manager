from getpass import getpass
import hashlib
import os

MASTER_PASSWORD_FILE = "master_password.txt"

def set_master_password():
    if os.path.exists(MASTER_PASSWORD_FILE):
        print("Kata sandi master sudah diatur.")
        return

    master_password = getpass("Atur kata sandi master baru: ")
    hashed_password = hashlib.sha256(master_password.encode()).hexdigest()
    with open(MASTER_PASSWORD_FILE, "w") as file:
        file.write(hashed_password)
    print("Kata sandi master berhasil diatur.")

def verify_master_password():
    if not os.path.exists(MASTER_PASSWORD_FILE):
        print("Kata sandi master belum diatur. Silakan atur terlebih dahulu.")
        set_master_password()

    stored_password = open(MASTER_PASSWORD_FILE, "r").read().strip()
    entered_password = getpass("Masukkan kata sandi master: ")
    hashed_password = hashlib.sha256(entered_password.encode()).hexdigest()

    return hashed_password == stored_password