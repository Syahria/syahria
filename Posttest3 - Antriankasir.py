import time

try:
    class Queue:
        def __init__(self, n=None):
            self.size = n
            self.current_size = 0
            self.data = []
            self.barang = []
        
        def isFull(self):
            if self.current_size ==  self.size:
                return True
            else:
                return False
            
        def isEmpty(self):
            if self.current_size == 0:
                return True
            else:
                return False
            
        def enqueue(self, n, brg):
            if self.isFull():
                print("Mohon maaf antrian sudah penuh")
            else:
                self.data.append(n)
                self.barang.append(brg)
                self.current_size = len(self.data)
                self.current_size = len(self.barang)
                print("Antrian dengan nama", n, "telah di tambahkan")
            input()
            self.menu()

        def dequeue(self):
            if self.isEmpty():
                print("Maaf antrian masih kosong")
                return None
            else:
                datakeluar = self.data.pop(0)
                datakeluar1 = self.barang.pop(0)
                self.current_size = len(self.data)
                self.current_size = len(self.barang)
                print("----------------------------------------------------------------------")
                print("Antrian dengan nama:",datakeluar,"dengan barang belanjaan:",datakeluar1)
                print("Di Mohon untuk Membayar barang belanjaannya di kasir")
                print("----------------------------------------------------------------------")
                time.sleep(1)
                print("Antrian setelah ini adalah: ",self.data)
            input()
            self.menu()

        def view(self):
            if self.isEmpty():
                print("Mohon maaf antrian masih kosong")
            else:
                print("========== DAFTAR ANTRIAN ==========")
                x = 1
                for i in self.data:
                    print(" "+str(x)+". ", i,)
                    x += 1
                print("----------------------------")
                print("Total Antrian: ",len(self.data))
            input()
            self.menu()

        def Exit(self):
            print("Anda telah keluar dari program")
            import sys
            sys.exit()

        def menu(self):
            import os
            os.system ('cls')
            print("=========================")
            print("|    PROGRAM ANTRIAN    |")
            print("|----- Daftar Menu -----|")
            print("|1. Tambah antrian      |")
            print("|2. Panggil antrian     |")
            print("|3. Lihat antrian       |")
            print("|4. Exit                |")
            print("=========================")
            pil = int(input("Masukkan no.menu yang ingin di pilih: "))

            if pil == 1:
                data = input("Masukkan daftar nama antrian: ")
                barang = input("Masukkan nama barang belanjaan: ")
                self.enqueue(data, barang)
            elif pil == 2:
                self.dequeue()
            elif pil == 3:
                self.view()
            elif pil == 4:
                self.Exit
            else:
                print("Mohon maaf pilihan yang anda pilih tidak ada silahkan ulangi kembali")
                print("Tekan [enter] untuk kembali ke menu")
                input()
                self.menu()

    q = Queue()
    q.menu()
except ValueError:
    print("Program hanya bertipe integer")
    print("Silahkan mulai kembali program")

            


            

        