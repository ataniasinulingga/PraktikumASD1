class Jastip:
    def __init__(self):
        self.jastip_harga = {
            "tas dior": 1500000,
            "sepatu nike": 1000000,
            "hoodie gucci": 1000000,
        }

    def jastip_barang(self):
        item_nama = input("Masukkan nama barang yang ingin anda jastip dari Singapore: ")
        berat = float(input("Masukkan berat barang (kg): "))

        jastip_harga = self.get_jastip_item_harga(item_nama)
        if jastip_harga is None:
            print("Barang yang anda jastip tidak tersedia")
            return

        ongkir_harga = self.menghitung_ongkir_harga(berat)

        total_harga = jastip_harga + ongkir_harga
        print(f"Total harga yang harus anda bayar adalah {total_harga} Rupiah")

    def tambah_item(self):
        item_nama = input("Masukkan nama barang yang ingin ditambahkan: ")
        if item_nama in self.jastip_harga:
            print("Item sudah ada dalam daftar.")
            return
        harga = float(input("Masukkan harga barang (Rupiah): "))
        self.jastip_harga[item_nama] = harga
        print(f"Item '{item_nama}' berhasil ditambahkan.")

    def lihat_daftar_item(self):
        print("Daftar Item yang Tersedia:")
        for nama, harga in self.jastip_harga.items():
            print(f"{nama}: {harga} Rupiah")

    def ubah_harga_item(self):
        item_nama = input("Masukkan nama barang yang ingin diubah harganya: ")
        if item_nama not in self.jastip_harga:
            print("Item tidak ditemukan.")
            return
        harga_baru = float(input("Masukkan harga baru untuk item tersebut (Rupiah): "))
        self.jastip_harga[item_nama] = harga_baru
        print(f"Harga untuk item '{item_nama}' berhasil diubah.")

    def hapus_item(self):
        item_nama = input("Masukkan nama barang yang ingin dihapus dari daftar: ")
        if item_nama not in self.jastip_harga:
            print("Item tidak ditemukan.")
            return
        del self.jastip_harga[item_nama]
        print(f"Item '{item_nama}' berhasil dihapus dari daftar.")

    def get_jastip_item_harga(self, item_nama):
        return self.jastip_harga.get(item_nama)

    def menghitung_ongkir_harga(self, berat):
        ongkir_harga_per_kg = 28000  # Rupiah per kilogram
        return berat * ongkir_harga_per_kg


def main():
    jastip = Jastip()

    while True:
        print("\nPilihan Menu:")
        print("1. Jastip Barang")
        print("2. Tambah Item")
        print("3. Lihat Daftar Item")
        print("4. Ubah Harga Item")
        print("5. Hapus Item")
        print("6. Keluar")
        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == '1':
            jastip.jastip_barang()
        elif pilihan == '2':
            jastip.tambah_item()
        elif pilihan == '3':
            jastip.lihat_daftar_item()
        elif pilihan == '4':
            jastip.ubah_harga_item()
        elif pilihan == '5':
            jastip.hapus_item()
        elif pilihan == '6':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
