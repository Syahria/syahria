A. Penjelasan Program
	linked list program saya menggunakan implementasi Queue.Queue adalah barisan elemen/data di mana proses memasukkan/menambah elemen/data dilakukan pada posisi belakang (rear) dan proses mengeluarkan/mengambil elemen/data di lakukan pada posisi depan (fron). Konsep queue menggunakan konsep FIFO (First In First Out) yang artinya masuk awal keluar awal.
	Operasi dalam Queue
	- isFull : Untuk memeriksa apakah Queue sudah penuh.
	- isEmpty : Untuk memeriksa apakah Queue masih kosong.
	- enqueue : Untuk menambahkan data.
	- dequeue : Untuk mengeluarkan data.

B. Cara Kerja Program
    - Pada Awal membuat program kita harus membuat sebuah class yang bernama queue
	- Setelah itu class di isi dengan berbagai macam atribut diantaranya 
	1. def__init__(self, n=30)
		def init adalah metode khusus yang secara otomatis di panggil ketika objek class itu di buat dan memiliki parameter 30 artinya antrian dalam program ini dibatasi sebanyak 30 antrian.lalu parameter n di simpan di self.size.
	2. def isFull (self): 
		atribut ini adalah sebuah operasi dalam queue yang berguna untuk memeriksa apakah queue sudah penuh atau tidak.
	3. def isEmpty (self)
		atribut ini adalah sebuah operasi dalam queue untuk memeriksa apakah queue masih kosong atau sudah terisi.
	4. def enqueue(self, n, brg)
		atribut ini adalah sebuah operasi dalam queue untuk menambahkan data. Dalam atribut ini kita memiliki sebuah parameter n dan brg, di mana n dan brg ini akan menjadi sebuah variabel untuk menampung data nantinya. dan ketika kita menambahkan data maka kita akan melihat apakah antrian tersebut sudah penuh atau tidak. jika antriannya sudah penuh maka otomatis kita tidak akan bisa menambahkan data lagi. maka program akan mencetak mohon maaf antrian sudah penuh.
	5. def dequeue(self)
	    dequeue adalah sebuah operasi dalam queue untuk mengeluarkan data.
	6. def view(self): 
		atribut ini berguna untuk menampilkan daftar menu pada program antrian
    7. def Exit(self): Untuk keluar dari program.


B. Fungsionalitas Program
	Fungsional program adalah sebuah paradigma pemrograman, di mana dalam mengkonstruksi program kita dapat membuat solusi dengan membuat definisi daan spesifikasi fungsi, kemudian mengimplementasikan fungsi tersebut dengan bahasa fungsional. Program ini berguna untuk menambahkan antrian ataupun untuk mengeluarkan antrian juga untuk mempermudah suatu pekerjaan agar lebih efisien dan juga agar aktifitas yang kita lakukan dapat lebih tertib.
   - def__init__(self, n=30) : untuk menyimpan atribut data
   - def isFull (self): Untuk memeriksa apakah Queue sudah penuh.
   - def isEmpty (self) : Untuk memeriksa apakah Queue masih kosong.
   - def enqueue(self, n, brg): Untuk menambahkan data.
   - def dequeue(self): Untuk mengeluarkan data.
   - def view(self): Untuk menampilkan daftar menu program antrian
   - def Exit(self): Untuk keluar dari program.


D. Output Program
    jika user menjalankan program maka nanti akan muncul daftar menu dari program antrian, yaitu tambah  
    antrian, panggil antrian, lihat antrian dan exit. lalu kita akan di minta untuk memasukkan no.menu yang ingin kita pilih.
  - jika kita memilih 1 yaitu tambah data maka kita akan di minta untuk memasukkan daftar nama antrian yaitu nama 
    kita sendiri lalu setelah itu kita juga akan di minta untuk memasukkan nama barang belanjaan yang kita pilih. jika kita klik enter maka antrian sudah berhasil di tambahkan.
  - jika kita memilih 2 yaitu panggil antrian maka user akan memanggil nama yang sebelumnya sudah di tambahkan 
    dengan barang belanjaannya untuk membayar barang belanjaan di kasir. lalu user akan memanggil antrian selanjutnya.
  - jika kita memilih 3 yaitu lihat data maka user akan menampilkan nama antrian dan jumlah antriannya. jika kita
    belum ada menambahkan nama antrian maka outputnya maaf antrian masih kosong.
  - jika kita memilih 4 yaitu exit maka kita akan otomatis keluar dari program.

    


