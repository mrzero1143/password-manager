import threading
import schedule
import time
import logging
from authentication import verify_master_password
from encryption import load_key
from data_handler import save_data, load_data
from password_generator import generate_strong_password
from cloud_sync import upload_to_cloud, download_from_cloud
from backup import create_backup

# Konfigurasi logging
logging.basicConfig(
    filename="logs/app.log",  # File log utama
    level=logging.INFO,      # Level logging (INFO, DEBUG, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(levelname)s - %(message)s"  # Format log
)

def add_account():
    key = load_key()
    accounts = load_data()

    site = input("Masukkan nama situs: ")
    username = input("Masukkan username: ")
    generate_pass = input("Apakah Anda ingin menghasilkan password acak? (y/n): ").lower()

    if generate_pass == "y":
        password = generate_strong_password()
        logging.info(f"Password acak dihasilkan untuk situs '{site}'.")
        print(f"Password acak yang dihasilkan: {password}")
    else:
        password = input("Masukkan password: ")

    if site in accounts:
        logging.warning(f"Akun untuk situs '{site}' sudah ada.")
        print("Akun untuk situs ini sudah ada.")
    else:
        accounts[site] = {"username": username, "password": password}
        save_data(accounts)
        logging.info(f"Akun berhasil ditambahkan untuk situs '{site}'.")
        print("Akun berhasil ditambahkan!")

def view_accounts():
    accounts = load_data()
    if not accounts:
        logging.info("Tidak ada akun yang tersimpan.")
        print("Tidak ada akun yang tersimpan.")
    else:
        print("\nDaftar Akun:")
        for site, info in accounts.items():
            print(f"Situs: {site}")
            print(f"  Username: {info['username']}")
            print(f"  Password: {info['password']}\n")
        logging.info("Daftar akun berhasil ditampilkan.")

def delete_account():
    accounts = load_data()
    site = input("Masukkan nama situs yang ingin dihapus: ")

    if site in accounts:
        del accounts[site]
        save_data(accounts)
        logging.info(f"Akun untuk situs '{site}' berhasil dihapus.")
        print(f"Akun untuk situs '{site}' berhasil dihapus.")
    else:
        logging.warning(f"Akun untuk situs '{site}' tidak ditemukan.")
        print("Akun tidak ditemukan.")

def automated_backup():
    try:
        logging.info("Memulai backup otomatis...")
        print("Memulai backup otomatis...")
        create_backup()
        logging.info("Backup otomatis selesai.")
        print("Backup otomatis selesai.")
    except Exception as e:
        logging.error(f"Gagal menjalankan backup otomatis: {e}")
        print(f"Gagal menjalankan backup otomatis: {e}")

def run_scheduler():
    # Jadwalkan backup otomatis setiap hari pada jam 02:00
    schedule.every().day.at("02:00").do(automated_backup)

    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except KeyboardInterrupt:
            logging.info("Scheduler dihentikan oleh pengguna.")
            print("\nScheduler dihentikan oleh pengguna.")
            break
        except Exception as e:
            logging.error(f"Terjadi kesalahan pada scheduler: {e}")
            print(f"Terjadi kesalahan pada scheduler: {e}")

def main_menu():
    # Autentikasi pengguna
    if not verify_master_password():
        logging.warning("Autentikasi gagal. Keluar dari aplikasi.")
        print("Autentikasi gagal. Keluar dari aplikasi.")
        return

    # Jalankan scheduler di thread terpisah
    scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
    scheduler_thread.start()
    logging.info("Scheduler dimulai di thread terpisah.")

    while True:
        print("\n--- Password Manager ---")
        print("1. Tambah Akun")
        print("2. Lihat Akun")
        print("3. Hapus Akun")
        print("4. Sinkronisasi Cloud")
        print("5. Backup Data")
        print("6. Keluar")
        choice = input("Pilih opsi (1/2/3/4/5/6): ")

        if choice == "1":
            add_account()
        elif choice == "2":
            view_accounts()
        elif choice == "3":
            delete_account()
        elif choice == "4":
            action = input("Upload (u) atau Download (d) dari cloud? ").lower()
            if action == "u":
                try:
                    upload_to_cloud()
                    logging.info("Data berhasil diunggah ke cloud.")
                except Exception as e:
                    logging.error(f"Gagal mengunggah data ke cloud: {e}")
            elif action == "d":
                try:
                    download_from_cloud()
                    logging.info("Data berhasil diunduh dari cloud.")
                except Exception as e:
                    logging.error(f"Gagal mengunduh data dari cloud: {e}")
            else:
                logging.warning("Pilihan sinkronisasi cloud tidak valid.")
                print("Pilihan tidak valid.")
        elif choice == "5":
            try:
                create_backup()
                logging.info("Backup manual berhasil dibuat.")
                print("Backup berhasil disimpan.")
            except Exception as e:
                logging.error(f"Gagal membuat backup manual: {e}")
                print(f"Gagal membuat backup manual: {e}")
        elif choice == "6":
            logging.info("Keluar dari aplikasi.")
            print("Terima kasih telah menggunakan Password Manager!")
            break
        else:
            logging.warning("Pilihan menu tidak valid.")
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    # Pastikan folder logs ada
    import os
    if not os.path.exists("logs"):
        os.makedirs("logs")
        logging.info("Folder 'logs' berhasil dibuat.")

    main_menu()