'''
================================================================================================================================================

Program ini merupakan unit test dari program keranjang belanja.

================================================================================================================================================
'''

import unittest
from trisna_app import CartItem, ShoppingCart


class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_menambah_barang(self):
        self.cart.items = []  
        result = self.cart.menambah_barang("Jeruk", 20000)  
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0].nama, "Jeruk")
        self.assertEqual(result, 'Barang "Jeruk" berhasil dimasukkan ke keranjang.')

    def test_hapus_barang(self):
        item_to_remove = CartItem("Apel", 10000)
        self.cart.items = [item_to_remove]
        self.cart.hapus_barang("Apel")
        self.assertEqual(len(self.cart.items), 0)

    def test_tampilkan_barang(self):
        self.cart.items = [CartItem("Mangga", 30000), CartItem("Kiwi", 50000)]
        result = self.cart.tampilkan_barang()
        expected_result = "Barang di Keranjang Belanja:\n1. Mangga - Rp 30000.00\n2. Kiwi - Rp 50000.00\n"
        self.assertEqual(result, expected_result)

    def test_hitung_total_belanja(self):
        self.cart.items = [CartItem("Sirsak", 20000), CartItem("Durian", 40000)]
        result = self.cart.hitung_total_belanja()
        expected_result = "Total belanja: Rp 60000.00"
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
