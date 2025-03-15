import schedule
import time
import logging
from backup import create_backup

# Konfigurasi logging
logging.basicConfig(
    filename="logs/backup.log",  # File log khusus untuk backup
    level=logging.INFO,         # Level logging (INFO, DEBUG, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(levelname)s - %(message)s"  # Format log
)

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

# Jadwalkan backup otomatis setiap hari pada jam 02:00
schedule.every().day.at("02:00").do(automated_backup)

def run_scheduler():
    logging.info("Scheduler dimulai. Menunggu jadwal backup otomatis...")
    print("Scheduler dimulai. Menunggu jadwal backup otomatis...")
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