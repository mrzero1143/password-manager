from encryption import encrypt_password, decrypt_password, load_key
import os
import json

def save_data(data):
    try:
        key = load_key()
        # Ubah data menjadi format JSON sebelum dienkripsi
        encrypted_data = encrypt_password(json.dumps(data), key)
        with open("passwords.txt", "wb") as file:
            file.write(encrypted_data)
        print("Data berhasil disimpan.")
    except Exception as e:
        print(f"Gagal menyimpan data: {e}")

def load_data():
    try:
        if not os.path.exists("passwords.txt"):
            return {}

        key = load_key()
        with open("passwords.txt", "rb") as file:
            encrypted_data = file.read()

        decrypted_data = decrypt_password(encrypted_data, key)

        # Gunakan json.loads untuk menghindari eval (lebih aman)
        return json.loads(decrypted_data)
    except Exception as e:
        print(f"Gagal memuat data: {e}")
        return {}