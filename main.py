import csv
import pandas as pd
from collections import deque

FILE_CSV = "produk.csv"
FILE_EXCEL = "laporan_produk.xlsx"

# Queue Pesanan
antrian = deque()

# ==========================
# LOAD DATA CSV
# ==========================

def load_produk():
    produk = {}

    try:
        with open(FILE_CSV, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                produk[row["id_produk"]] = {
                    "nama": row["nama_produk"],
                    "harga": int(row["harga"]),
                    "stok": int(row["stok"])
                }

    except FileNotFoundError:
        pass

    return produk


# ==========================
# EXPORT KE EXCEL
# ==========================

def export_excel(produk):

    data = []

    for id_produk, item in produk.items():
        data.append({
            "ID Produk": id_produk,
            "Nama Produk": item["nama"],
            "Harga": item["harga"],
            "Stok": item["stok"]
        })

    df = pd.DataFrame(data)

    df.to_excel(
        FILE_EXCEL,
        index=False
    )


# ==========================
# SAVE CSV + EXCEL
# ==========================

def save_produk(produk):

    with open(FILE_CSV, mode="w", newline="", encoding="utf-8") as file:

        fieldnames = [
            "id_produk",
            "nama_produk",
            "harga",
            "stok"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for id_produk, item in produk.items():
            writer.writerow({
                "id_produk": id_produk,
                "nama_produk": item["nama"],
                "harga": item["harga"],
                "stok": item["stok"]
            })

    export_excel(produk)


# ==========================
# CREATE
# ==========================

def tambah_produk(produk):

    print("\n=== TAMBAH PRODUK ===")

    id_produk = input("ID Produk : ")

    if id_produk in produk:
        print("ID sudah digunakan!")
        return

    nama = input("Nama Produk : ")
    harga = int(input("Harga : "))
    stok = int(input("Stok : "))

    produk[id_produk] = {
        "nama": nama,
        "harga": harga,
        "stok": stok
    }

    save_produk(produk)

    print("Produk berhasil ditambahkan.")


# ==========================
# READ
# ==========================

def tampil_produk(produk):

    print("\n=== DAFTAR PRODUK ===")

    if len(produk) == 0:
        print("Data kosong.")
        return

    print("-" * 60)

    for id_produk, item in produk.items():

        print(
            f"{id_produk} | "
            f"{item['nama']} | "
            f"Rp{item['harga']} | "
            f"Stok: {item['stok']}"
        )


# ==========================
# SEARCHING
# ==========================

def cari_produk(produk):

    keyword = input(
        "\nMasukkan ID atau Nama Produk : "
    ).lower()

    ditemukan = False

    for id_produk, item in produk.items():

        if keyword in id_produk.lower() or \
           keyword in item["nama"].lower():

            print("\nProduk Ditemukan")
            print("------------------")
            print("ID    :", id_produk)
            print("Nama  :", item["nama"])
            print("Harga :", item["harga"])
            print("Stok  :", item["stok"])

            ditemukan = True

    if not ditemukan:
        print("Produk tidak ditemukan.")


# ==========================
# SORTING
# ==========================

def sorting_produk(produk):

    print("\n=== SORTING PRODUK ===")
    print("1. Nama Produk")
    print("2. Harga")
    print("3. Stok")

    pilih = input("Pilih : ")

    data = list(produk.items())

    if pilih == "1":
        data.sort(key=lambda x: x[1]["nama"])

    elif pilih == "2":
        data.sort(key=lambda x: x[1]["harga"])

    elif pilih == "3":
        data.sort(key=lambda x: x[1]["stok"])

    else:
        print("Pilihan tidak valid.")
        return

    print("\nHASIL SORTING")
    print("-" * 60)

    for id_produk, item in data:
        print(
            f"{id_produk} | "
            f"{item['nama']} | "
            f"{item['harga']} | "
            f"{item['stok']}"
        )


# ==========================
# UPDATE
# ==========================

def update_produk(produk):

    id_produk = input(
        "\nMasukkan ID Produk : "
    )

    if id_produk not in produk:
        print("Produk tidak ditemukan.")
        return

    produk[id_produk]["nama"] = input(
        "Nama Baru : "
    )

    produk[id_produk]["harga"] = int(
        input("Harga Baru : ")
    )

    produk[id_produk]["stok"] = int(
        input("Stok Baru : ")
    )

    save_produk(produk)

    print("Data berhasil diperbarui.")


# ==========================
# DELETE
# ==========================

def hapus_produk(produk):

    id_produk = input(
        "\nMasukkan ID Produk : "
    )

    if id_produk not in produk:
        print("Produk tidak ditemukan.")
        return

    del produk[id_produk]

    save_produk(produk)

    print("Produk berhasil dihapus.")


# ==========================
# QUEUE PESANAN
# ==========================

def buat_pesanan(produk):

    print("\n=== BUAT PESANAN ===")

    id_produk = input(
        "ID Produk : "
    )

    if id_produk not in produk:
        print("Produk tidak ditemukan.")
        return

    jumlah = int(
        input("Jumlah Pesanan : ")
    )

    if jumlah > produk[id_produk]["stok"]:
        print("Stok tidak mencukupi.")
        return

    pembeli = input(
        "Nama Pembeli : "
    )

    antrian.append({
        "pembeli": pembeli,
        "id_produk": id_produk,
        "jumlah": jumlah
    })

    print("Pesanan berhasil masuk antrian.")


def proses_pesanan(produk):

    if len(antrian) == 0:
        print("Antrian kosong.")
        return

    pesanan = antrian.popleft()

    produk[
        pesanan["id_produk"]
    ]["stok"] -= pesanan["jumlah"]

    save_produk(produk)

    print("\nPesanan Diproses")
    print("------------------")
    print("Pembeli :", pesanan["pembeli"])
    print("ID Produk :", pesanan["id_produk"])
    print("Jumlah :", pesanan["jumlah"])


def lihat_antrian():

    print("\n=== ANTRIAN PESANAN ===")

    if len(antrian) == 0:
        print("Antrian kosong.")
        return

    for i, item in enumerate(
            antrian,
            start=1):

        print(
            f"{i}. "
            f"{item['pembeli']} - "
            f"{item['id_produk']} "
            f"({item['jumlah']})"
        )


# ==========================
# MENU UTAMA
# ==========================

def menu():

    produk = load_produk()

    export_excel(produk)

    while True:

        print("\n")
        print("=" * 45)
        print("     SISTEM MARKETPLACE")
        print("=" * 45)
        print("1. Tambah Produk")
        print("2. Tampilkan Produk")
        print("3. Cari Produk")
        print("4. Sorting Produk")
        print("5. Update Produk")
        print("6. Hapus Produk")
        print("7. Buat Pesanan")
        print("8. Proses Pesanan")
        print("9. Lihat Antrian")
        print("10. Keluar")

        pilih = input("\nPilih Menu : ")

        if pilih == "1":
            tambah_produk(produk)

        elif pilih == "2":
            tampil_produk(produk)

        elif pilih == "3":
            cari_produk(produk)

        elif pilih == "4":
            sorting_produk(produk)

        elif pilih == "5":
            update_produk(produk)

        elif pilih == "6":
            hapus_produk(produk)

        elif pilih == "7":
            buat_pesanan(produk)

        elif pilih == "8":
            proses_pesanan(produk)

        elif pilih == "9":
            lihat_antrian()

        elif pilih == "10":
            print("Program selesai.")
            break

        else:
            print("Menu tidak tersedia.")


menu()