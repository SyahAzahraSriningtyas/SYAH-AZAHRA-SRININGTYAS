# UAS-Struktur-Data-SYAH-AZAHRA-SRININGTYAS
# Sistem Marketplace Sederhana

## Deskripsi

Sistem Marketplace Sederhana adalah aplikasi berbasis Python yang digunakan untuk mengelola data produk dan pesanan menggunakan database CSV. Aplikasi ini mendukung operasi CRUD (Create, Read, Update, Delete), Searching, Sorting, serta menggunakan struktur data Hash Map dan Queue untuk mengelola data secara efisien.

---

## Fitur

* Tambah Produk (Create)
* Tampilkan Produk (Read)
* Update Produk (Update)
* Hapus Produk (Delete)
* Cari Produk (Searching)
* Urutkan Produk (Sorting)
* Buat Pesanan
* Proses Pesanan
* Lihat Antrian Pesanan
* Export Data ke Excel

---

## Struktur Data yang Digunakan

### 1. Hash Map (Dictionary)

Hash Map diimplementasikan menggunakan Dictionary Python untuk menyimpan data produk berdasarkan ID produk sebagai key. Struktur data ini memungkinkan proses pencarian, penambahan, pembaruan, dan penghapusan data dilakukan dengan cepat.

Fungsi:

* Menyimpan data produk.
* Mempercepat proses CRUD.
* Mempermudah pencarian produk berdasarkan ID.

### 2. Queue (Deque)

Queue diimplementasikan menggunakan `collections.deque` untuk mengelola antrean pesanan pelanggan menggunakan metode FIFO (First In First Out). Pesanan yang masuk lebih dahulu akan diproses lebih dahulu.

Fungsi:

* Menyimpan antrean pesanan.
* Mengatur urutan pemrosesan pesanan.
* Mensimulasikan sistem antrean pada marketplace.

### 3. Searching

Searching digunakan untuk mencari produk berdasarkan ID produk atau nama produk yang dimasukkan pengguna.

### 4. Sorting

Sorting digunakan untuk mengurutkan data produk berdasarkan:

* Nama Produk
* Harga Produk
* Stok Produk

---

## Database

Data disimpan menggunakan file CSV:

* `produk.csv`

Selain itu, data juga otomatis diekspor ke file Excel:

* `laporan_produk.xlsx`

---

## Operasi CRUD

### Create

Menambahkan data produk baru ke dalam sistem.

### Read

Menampilkan seluruh data produk yang tersimpan.

### Update

Mengubah data produk yang sudah ada.

### Delete

Menghapus data produk dari sistem.

---

## Cara Menjalankan Program

1. Pastikan Python sudah terinstal.
2. Install library yang dibutuhkan:

```bash
pip install pandas openpyxl
```

3. Jalankan program:

```bash
python main.py
```

---

## Struktur Folder

```text
SISTEM MARKETPLACE SEDERHANA/
│
├── main.py
├── produk.csv
├── laporan_produk.xlsx
├── README.md
└── flowchart.png
```

---

## Author

Nama : Syah Azahra Sriningtyas
NIM : 25416255201018
Kelas : IF25B
Mata Kuliah : Struktur Data
Final Project - Aplikasi Manajemen dengan Database Flat File (CSV)
