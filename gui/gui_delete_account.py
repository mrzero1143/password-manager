import tkinter as tk
from tkinter import messagebox
from data_handler import save_data, load_data

def delete_account_gui():
    def delete_account():
        try:
            site = site_entry.get().strip()  # Menghapus spasi ekstra di awal/akhir input
            if not site:
                messagebox.showwarning("Input Error", "Nama situs harus diisi!")
                return

            accounts = load_data()
            if site not in accounts:
                messagebox.showwarning("Error", "Akun tidak ditemukan.")
                return

            # Konfirmasi penghapusan akun
            confirm = messagebox.askyesno("Konfirmasi", f"Apakah Anda yakin ingin menghapus akun untuk situs '{site}'?")
            if not confirm:
                return

            del accounts[site]
            save_data(accounts)
            messagebox.showinfo("Sukses", f"Akun untuk situs '{site}' berhasil dihapus!")
            delete_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

    # Jendela utama untuk menghapus akun
    delete_window = tk.Toplevel()
    delete_window.title("Hapus Akun")
    delete_window.geometry("400x200")
    delete_window.configure(bg="#f0f0f0")

    # Label dan Entry untuk Nama Situs
    tk.Label(delete_window, text="Nama Situs:", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)
    site_entry = tk.Entry(delete_window, font=("Arial", 12))
    site_entry.pack(fill="x", padx=20)

    # Tombol Hapus Akun
    delete_button = tk.Button(
        delete_window,
        text="Hapus Akun",
        font=("Arial", 12),
        command=delete_account,
        bg="#f44336",
        fg="white"
    )
    delete_button.pack(fill="x", padx=20, pady=20)

    # Jalankan loop utama GUI
    delete_window.mainloop()