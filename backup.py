import shutil
import os
import datetime
import logging

# Pastikan folder logs dan backups ada
os.makedirs("logs", exist_ok=True)
os.makedirs("backups", exist_ok=True)

# Konfigurasi logging
logging.basicConfig(
    filename="logs/backup.log",  # File log khusus untuk backup
    level=logging.INFO,         # Level logging (INFO, DEBUG, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(levelname)s - %(message)s"  # Format log
)

def create_backup():
    try:
        # Buat timestamp untuk nama file backup
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        backup_file = f"backups/backup_{timestamp}.txt"

        # Pastikan folder backups ada
        if not os.path.exists("backups"):
            os.makedirs("backups")
            logging.info("Folder 'backups' berhasil dibuat.")

        # Periksa apakah file passwords.txt ada
        if not os.path.exists("passwords.txt"):
            logging.error("File passwords.txt tidak ditemukan. Backup gagal.")
            print("File passwords.txt tidak ditemukan. Backup gagal.")
            return

        # Salin file passwords.txt ke file backup
        shutil.copyfile("passwords.txt", backup_file)
        logging.info(f"Backup berhasil disimpan sebagai {backup_file}")
        print(f"Backup berhasil disimpan sebagai {backup_file}")

    except Exception as e:
        logging.error(f"Gagal membuat backup: {e}")
        print(f"Gagal membuat backup: {e}")

def restore_backup(backup_file):
    try:
        # Periksa apakah file backup ada
        if not os.path.exists(backup_file):
            logging.warning(f"File backup '{backup_file}' tidak ditemukan.")
            print(f"File backup '{backup_file}' tidak ditemukan.")
            return

        # Pulihkan data dari file backup ke passwords.txt
        shutil.copyfile(backup_file, "passwords.txt")
        logging.info(f"Data berhasil dipulihkan dari {backup_file}")
        print(f"Data berhasil dipulihkan dari {backup_file}")

    except Exception as e:
        logging.error(f"Gagal memulihkan data dari backup: {e}")
        print(f"Gagal memulihkan data dari backup: {e}")