import sys
import os
import tkinter as tk
from tkinter import messagebox

# Tambahkan root direktori ke sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

from data_handler import save_data, load_data
from encryption import load_key

def open_add_account_window():
    def add_account():
        try:
            key = load_key()
            accounts = load_data()

            site = site_entry.get().strip()  # Menghapus spasi ekstra di awal/akhir input
            username = username_entry.get().strip()
            password = password_entry.get().strip()

            # Validasi input kosong
            if not site or not username or not password:
                messagebox.showwarning("Peringatan", "Semua field harus diisi.")
                return

            # Validasi akun duplikat
            if site in accounts:
                messagebox.showwarning("Peringatan", "Akun untuk situs ini sudah ada.")
                return

            # Simpan akun baru
            accounts[site] = {"username": username, "password": password}
            save_data(accounts)
            messagebox.showinfo("Sukses", "Akun berhasil ditambahkan!")
            window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

    # GUI untuk menambah akun
    window = tk.Tk()
    window.title("Tambah Akun")
    window.geometry("400x250")  # Ukuran lebih besar untuk tampilan lebih nyaman

    # Label dan Entry untuk Nama Situs
    tk.Label(window, text="Nama Situs:", font=("Arial", 12)).pack(pady=5)
    site_entry = tk.Entry(window, font=("Arial", 12))
    site_entry.pack(pady=5)

    # Label dan Entry untuk Username
    tk.Label(window, text="Username:", font=("Arial", 12)).pack(pady=5)
    username_entry = tk.Entry(window, font=("Arial", 12))
    username_entry.pack(pady=5)

    # Label dan Entry untuk Password
    tk.Label(window, text="Password:", font=("Arial", 12)).pack(pady=5)
    password_entry = tk.Entry(window, show="*", font=("Arial", 12))
    password_entry.pack(pady=5)

    # Tombol Simpan
    tk.Button(window, text="Simpan", command=add_account, font=("Arial", 12), width=15).pack(pady=15)

    # Jalankan loop utama GUI
    window.mainloop()