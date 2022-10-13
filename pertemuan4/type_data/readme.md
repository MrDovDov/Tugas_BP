# Rangkuman Type data
di perkuliahan bahasa pemograman saya dapat mengetaui beberapa jenis tipe data yang sebelumnya saya tidak ketahui
seperti dibawah :

string adalah bahasa pemrograman Python disebut sebagai kumpulan karakter yang dikelilingi oleh tanda kutip tunggal, tanda kutip ganda bahkan tanda kutip tiga.
# contoh string
a = "hello"
print (a)
print (type(a))

interger merupakan tipe data numerik yang mewakili seluruh bilangan bulat. Tipe data ini tidak memiliki angka desimal. Tipe data ini memiliki beberapa macam tipe data lagi, seperti Int, Long, Byte dan Short. Semakin besar tipe data maka akan semakin besar juga nilai yang ditampung.
# contoh interger
b = 12
print (b)
print (type(b))

Float adalah data type numerik yang digunakan untuk menyimpan angka yang mungkin memiliki komponen pecahan seperti nilai moneter (707.07, 0.7, 707.00)
# contoh float
c = 10.5
print (c)
print (type(c))

tuple adalah Data untaian yang menyimpan berbagai tipe data tapi isinya tidak bisa diubah
# contoh tuple
d = 20,5
print (d)
print (type(d))

# contoh tuple
tuple_f = 1,2,3
print (tuple_f[0])

complex adalah untuk Menyatakan pasangan angka real dan imajiner
# contoh data complex
e = 1j
print (e)
print (type(e))
z = complex ('5-9j')
print (z)

list adalah Data untaian yang menyimpan berbagai tipe data dan isinya bisa diubah-ubah
# contoh type data list
f = ["a","b","c"]
print (f)
print (type(f))
# contoh list
list_f = [1,2,3]
print (list_f[0])

Tipe data set merupakan tipe data yang digunakan untuk menyimpan banyak nilai dalam satu variabel dan yang tidak beraturan serta memiliki nilai yang unik (tidak ada duplikasi).
# contoh type data set
g = {"a","b","c"}
print (g)
print (type(g))
# contoh set
set_f = {1,2,3}
print (set_f)

berfungsi untuk mengubah iterable menjadi objek set yang tidak bisa diubah (immutable). Frozenset adalah versi immutable dari set
# contoh type data frozenset
h = frozenset({1,2,3})
print (type(h))

boolean untuk Menyatakan benar True yang bernilai 1, atau salah False yang bernilai 0
# contoh type data boolean
i = True
j = False
print (i,j)
print (type(i))
print (type(j))