# Belajar input data number

# input default sebagai string
# harus ditambah int agar hasilnya number, perlu di konfersi 

from os import uname_result

"""
print("angka pertama : ")

a = input()

print ("angka kedua")

b = input()

hasil = a + b
print (f" {a} + {b} = {hasil}") # akan mencetak hasilnya string bukan number

print("angka pertama : ")

a = int (input()) #PENAMBAHAN TYPE DATA INT (UNTUK MENGHASILKAN DATA NUMBER)

print ("angka kedua")

b = int (input())

hasil = a + b
print (f" {a} + {b} = {hasil}") # integer hasilkan data number

"""

print("masukan ungka pertama : ")

pertma = int (input())

print("masukan ungka kedua : ")

kedua = int (input())

hasil = pertma + kedua

print(f"total angka yang anda input = {hasil}")