import sys
import os
import tkinter as tk
from tkinter import messagebox

# Tambahkan root direktori ke sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

from gui_add_account import open_add_account_window
from gui_view_accounts import view_accounts_gui
from gui_delete_account import delete_account_gui
from backup import create_backup
from cloud_sync import upload_to_cloud, download_from_cloud

def main_menu():
    def backup_data():
        try:
            create_backup()
            messagebox.showinfo("Sukses", "Backup berhasil dibuat!")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal membuat backup: {e}")

    def sync_with_cloud():
        action = messagebox.askquestion("Sinkronisasi Cloud", "Upload (Ya) atau Download (Tidak)?")
        if action == "yes":
            try:
                upload_to_cloud()
                messagebox.showinfo("Sukses", "Data berhasil diunggah ke cloud!")
            except Exception as e:
                messagebox.showerror("Error", f"Gagal mengunggah data: {e}")
        else:
            try:
                download_from_cloud()
                messagebox.showinfo("Sukses", "Data berhasil diunduh dari cloud!")
            except Exception as e:
                messagebox.showerror("Error", f"Gagal mengunduh data: {e}")

    # Fungsi untuk menangani penutupan aplikasi
    def on_closing():
        if messagebox.askokcancel("Keluar", "Apakah Anda yakin ingin keluar?"):
            root.destroy()

    # Konfigurasi jendela utama
    root = tk.Tk()
    root.title("Password Manager - Menu Utama")
    root.geometry("400x300")
    root.protocol("WM_DELETE_WINDOW", on_closing)  # Tangani tombol close window

    # Tombol menu
    tk.Button(root, text="Tambah Akun", command=open_add_account_window, width=20).pack(pady=10)
    tk.Button(root, text="Lihat Akun", command=view_accounts_gui, width=20).pack(pady=10)
    tk.Button(root, text="Hapus Akun", command=delete_account_gui, width=20).pack(pady=10)
    tk.Button(root, text="Backup Data", command=backup_data, width=20).pack(pady=10)
    tk.Button(root, text="Sinkronisasi Cloud", command=sync_with_cloud, width=20).pack(pady=10)
    tk.Button(root, text="Keluar", command=root.quit, width=20).pack(pady=10)

    # Jalankan loop utama GUI
    root.mainloop()

if __name__ == "__main__":
    main_menu()