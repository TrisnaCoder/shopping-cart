'''
================================================================================================================================================

Program ini merupakan keranjang belanja sederhana di mana user dapat menambah barang, menghapus barang, menampilkan barang dan menghitung total belanja.

================================================================================================================================================
'''


class CartItem:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

class ShoppingCart:
    def __init__(self):
        self.items = []

    def menambah_barang(self, nama_barang, harga_barang):
        '''
        Fungsi ini digunakan untuk menambahkan item barang ke dalam keranjang. Dengan memberikan nama dan harga barang sebagai input, fungsi ini membuat objek CartItem, menambahkannya ke daftar items, dan mengembalikan sebuah pesan konfirmasi.

        '''
        item = CartItem(nama_barang, harga_barang)  
        self.items.append(item)
        return f'Barang "{nama_barang}" berhasil dimasukkan ke keranjang.'
    
    def hapus_barang(self, nama_barang):
        '''
        Fungsi ini digunakan untuk mencari dan menghapus barang berdasarkan nama barang yang terdapat dalam keranjang belanja. Selain itu, untuk mengembalikan pesan konfirmasi tentang berhasil atau tidaknya penghapusan barang tersebut.

        '''
        removed_item = None
        for item in self.items:
            if item.nama == nama_barang:
                removed_item = item
                self.items.remove(item)
                break
        if removed_item:
            return f'Barang "{nama_barang}" berhasil dihapus di keranjang belanja.'
        else:
            return f'Barang "{nama_barang}" tidak ditemukan di keranjang belanja.'

    def tampilkan_barang(self):
        '''
        Fungsi ini digunakan untuk menampilkan daftar barang dalam keranjang belanja beserta nomor indeks, nama, dan harga masing-masing barang. Jika keranjang kosong, fungsi akan memberikan pesan yang sesuai.
        '''
        if not self.items:
            return 'Keranjang belanja kosong.'
        else:
            result = 'Barang di Keranjang Belanja:\n'
            for j, item in enumerate(self.items, start=1):
                result += f'{j}. {item.nama} - Rp {item.harga:.2f}\n'
            return result

    def hitung_total_belanja(self):
        '''
        Fungsi ini menghitung jumlah total harga dari setiap barang dalam keranjang belanja dan mengembalikan hasilnya dalam bentuk format dua desimal.

        '''
        total = sum(item.harga for item in self.items)
        return f'Total belanja: Rp {total:.2f}'



if __name__ == '__main__':

    cart = ShoppingCart()
    print("Selamat Datang di Keranjang Belanja Toko Makmur!\n")

    while True:
        print('Menu:')
        print('1. Menambah Barang')
        print('2. Hapus Barang')
        print('3. Tampilkan Barang di Keranjang')
        print('4. Lihat Total Belanja')
        print('5. Exit\n')

        pilihan = input('Pilihan: ')

        if pilihan == '1':
            nama_barang = input('Masukkan nama barang: ')
            harga_barang = int(input('Masukkan harga: '))
            item = CartItem(nama_barang, harga_barang)
            pesan = cart.menambah_barang(nama_barang, harga_barang)
            print(pesan)

        elif pilihan == '2':
            nama_barang_hapus = input('Masukan nama barang yang ingin dihapus: ')
            pesan_hapus = cart.hapus_barang(nama_barang_hapus)
            print(pesan_hapus)

        elif pilihan == '3':
            tampilan = cart.tampilkan_barang()
            print(tampilan)

        elif pilihan == '4':
            total = cart.hitung_total_belanja()
            print(total)

        elif pilihan == '5':
            print('Sampai Jumpa! Terima kasih sudah belanja di Toko Makmur.')
            break
        
        else:
            print("Pilihan salah. Coba lagi ya.")


