## ⏰️ ZENITH TIME OS V2
---
**Sebuah alat terminal imersif yang mengubah sesi CLI biasa menjadi dashboard futuristik penuh layar. Dirancang dengan estetika retro‑themes dan animasi sinematik, aplikasi ini membawa empat alat esensial langsung ke terminal Anda :**

- **Digital Clock** — 12/24 jam, efek *glow*, tanggal, animasi berkedip, mode fullscreen.
- **Alarm** — Atur beberapa alarm, *snooze*, notifikasi suara + efek berkedip terminal.
- **Stopwatch** — Presisi milidetik, catatan *lap*, animasi halus.
- **Timer / Pewaktu** — Hitung mundur dengan *progress bar* animatif, mode Pomodoro.
- **8 Tema Premium** — Matrix Green, Cyberpunk Neon, Vaporwave, Retro Amber, RGB Dynamic, dll.
- **Fullscreen Engine** — Rendering penuh terminal, deteksi ukuran dinamis, layout responsif.
- **Cross‑Platform** — Berjalan mulus di Linux, Windows (CMD, PowerShell), dan Termux Android.
- **Animasi Sinematik** — Efek *pulse*, *scanline*, *CRT flicker*, border animatif.

---

## 📥 INSTALASI

## Prasyarat Umum
- **Python 3.8+** (disarankan 3.12+)
- **pip** (manajer paket Python)
- **Terminal dengan dukungan warna 256** (Windows Terminal, GNOME Terminal, Termux, dll.)

## 1️⃣ Linux (Ubuntu / Xubuntu / Kali Linux)

**Langkah 1 :** Clone repositori
```bash
git clone https://github.com/123tool/ZENITH-TIME-OS-V2.git
cd ZENITH-TIME-OS-V2
```
**Langkah 2 :** Jalankan installer otomatis

```bash
chmod +x install.sh
bash install.sh
```

*Installer akan mendeteksi OS, menginstal Python jika belum ada, lalu menginstal dependensi.*

**Langkah 3 :** Luncurkan aplikasi

```bash
bash start.sh
```

**Alternatif manual (jika installer gagal) :**

```bash
sudo apt update
sudo apt install python3 python3-pip -y
pip3 install -r requirements.txt
python3 main.py
```

---

## 2️⃣ Windows (CMD / PowerShell)

**Langkah 1 :** Pastikan Python sudah terinstal.
   - Unduh dari python.org (centang Add Python to PATH).
   - Buka Command Prompt atau PowerShell.

**Langkah 2 :** Clone atau unduh repositori, lalu masuk ke folder.

```powershell
git clone https://github.com/123tool/ZENITH-TIME-OS-V2.git
cd ZENITH-TIME-OS-V2
```

**Langkah 3 :** Instal dependensi.

```powershell
pip install -r requirements.txt
```

**Langkah 4 :** Jalankan aplikasi.

```powershell
python main.py
```

*Atau gunakan start.bat dengan mengklik ganda file tersebut.*

**Catatan :** *Untuk pengalaman terbaik, gunakan Windows Terminal (bukan CMD bawaan) karena dukungan warna dan Unicode lebih baik.*

---

## 3️⃣ Termux Android

**Langkah 1 :** Buka Termux, perbarui paket.

```bash
pkg update && pkg upgrade -y
pkg install python git -y
```

**Langkah 2 :** Clone repositori.

```bash
git clone https://github.com/123tool/ZENITH-TIME-OS-V2.git
cd ZENITH-TIME-OS-V2
```

**Langkah 3 :** Instal dependensi.

```bash
pip install -r requirements.txt
```

**Langkah 4 :** Jalankan.

```bash
python main.py
```

**Tips :** *Gunakan mode layar penuh Termux (geser dari atas, pilih Fullscreen) untuk pengalaman maksimal.*

---

## 🕹️ PANDUAN

**Kontrol Keyboard Global**

```Tombol Aksi
↑ ↓ Navigasi menu
Enter Pilih / Konfirmasi
Q / ESC Kembali ke menu / Keluar dari fullscreen
Ctrl+C Keluar paksa (safe exit)
```
**Kontrol Spesifik Tiap Alat**

```Digital Clock
· M : Ubah mode 12/24 jam
```
```Alarm
· A : Tambah alarm (masukkan format HH:MM)
· Enter : Simpan alarm / Matikan alarm berbunyi
· D : Hapus semua alarm
```
```Stopwatch
· Spasi : Mulai / Jeda
· L : Catat lap
· R : Reset
```
```Timer
· Spasi : Mulai / Jeda
· S : Ubah durasi (siklus 30 detik)
· R : Reset ke durasi semula
```
---

## 🛠️ TROUBLESHOOTING

**Masalah Umum**

1. Terminal tidak fullscreen / ukuran kacau
   - Pastikan menggunakan terminal yang mendukung alternate screen buffer (hampir semua terminal modern).
   - Resize terminal sebelum menjalankan, aplikasi akan otomatis menyesuaikan.

2. Warna tidak muncul / kacau
   - Pastikan terminal mendukung 256 color atau true color.
   - Di Windows, gunakan Windows Terminal bukan cmd.exe lama.

3. Error ModuleNotFoundError: No module named 'blessed'
   - Jalankan pip install -r requirements.txt kembali.
   - Di Termux, jika gagal, coba pip install blessed --no-cache-dir.

4. Suara tidak berfungsi
   - Alarm menggunakan terminal bell (\a). Pastikan terminal kamu mengaktifkan bell/notifikasi suara.
   - Di Termux, suara bell biasanya tidak didukung; aplikasi akan tetap berjalan tanpa suara.

5. Tombol tidak responsif di Termux
   - Gunakan kombinasi Volume Down + C untuk mensimulasikan Ctrl+C jika perlu.
   - Beberapa tombol fungsi mungkin perlu penekanan lebih lama.
