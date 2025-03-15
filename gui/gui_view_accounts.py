import tkinter as tk
from tkinter import messagebox
from data_handler import load_data

def view_accounts_gui():
    try:
        accounts = load_data()
        if not accounts:
            messagebox.showinfo("Info", "Tidak ada akun yang tersimpan.")
            return

        # Jendela utama untuk melihat akun
        view_window = tk.Toplevel()
        view_window.title("Lihat Akun")
        view_window.geometry("500x400")
        view_window.configure(bg="#f0f0f0")

        # Area teks untuk menampilkan daftar akun
        text_area = tk.Text(
            view_window,
            font=("Arial", 12),
            wrap="word",
            bg="#ffffff",
            fg="#333333",
            padx=10,
            pady=10
        )
        text_area.pack(fill="both", expand=True, padx=20, pady=20)

        # Menambahkan header
        text_area.insert("end", "Daftar Akun:\n\n", "header")
        text_area.tag_configure("header", font=("Arial", 14, "bold"), foreground="#0078D4")

        # Menampilkan data akun
        for site, info in accounts.items():
            text_area.insert("end", f"Situs: {site}\n", "site")
            text_area.insert("end", f"  Username: {info['username']}\n", "details")
            text_area.insert("end", f"  Password: {info['password']}\n\n", "details")

        # Konfigurasi tag untuk estetika
        text_area.tag_configure("site", font=("Arial", 12, "bold"), foreground="#2E7D32")
        text_area.tag_configure("details", font=("Arial", 12), foreground="#333333")

        # Nonaktifkan area teks agar tidak dapat diedit
        text_area.config(state="disabled")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan saat memuat akun: {e}")