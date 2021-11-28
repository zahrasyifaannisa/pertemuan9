# Buat sebuah list sebanyak 5 elemen dengan nilai bebas
a = [1,2,3,4,5]
print ("a=[1,2,3,4,5]")
# akses list:
print ("\nakses list")
# tampilkan elemen ke 3
print ("tampilkan elemen ke 3=",a[2])
# ambil nilai elemen ke 2 sampai elemen ke 4
del a[1:4]
print ("ambil nilai elemen ke 2 sampai elemen ke 4=", a)
# ambil elemen terakhir
del a[1]
print ("ambil elemen terakhir=",a)
# ubah elemen list:
print ("\nubah elemen")
# ubah elemen ke 4 dengan nilai lainnya
a = [1,2,3,4,5]
a [3]=2
print ("ubah elemen ke 4 dengan nilai lainnya=",a)
# ubah elemen ke 4 sampai dengan elemen terakhir
a [3:6]=7,8
print("ubah elemen ke 4 sampai dengan elemen terakhir=",a)
# tambah elemen list:
print ("\ntambah elemen list")
# ambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B)
a = [1,2,3,4,5]
b = []
b.extend(a[1:3])
print ("ambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B)=",b)
# tambah list B dengan nilai string
b.append ("s")
print("tambah list B dengan nilai string=",b)
# tambah list B dengan 3 nilai
b.extend([1,5,6])
print ("tambah list B dengan 3 Nilai=",b)
# gabungkan list B dengan list A
t=a+b
print ("gabungkan list B dengan list =",t)