class NodePelanggan:
    def __init__(self, namaPelanggan):
        self._namaPelanggan = namaPelanggan

    def getNamaPelanggan(self):
        return self._namaPelanggan

class WarungMakan:
    DEFAULT_CAPACITY = 5
    def __init__(self): #tidak boleh mengganti / menambah metode init
        self._data = [None] * WarungMakan.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0
    
    def dequeue(self):
        # if self.is_empty():
        #     print("Kosong")
        # a = self._data[self._front]
        # self._data[self._front] = None
        # self._front =(self._front+1) % len(self._data)
        # self._size -=1
        # return a
        data = self._data[0]
        self._data.remove(data)
        print(f"### Pelanggan {NodePelanggan.getNamaPelanggan(data)}Selesai Membayar ###")
        print()
        return data
    
    def enqueue(self, namaPelanggan):
        new = NodePelanggan(namaPelanggan)
        if self.__len__() >= self.DEFAULT_CAPACITY:
            self.resizeBy3()
        self._data.append(new)

    def resizeBy3(self):
        # a = self._data
        # self._data =[None]*self.DEFAULT_CAPACITY
        # b = self._front
        # for k in range (self._size):
        #     self._data[k] = a[b]
        #     b = (1 + b) % len(a)
        # self._front = 0
        self.DEFAULT_CAPACITY = self.DEFAULT_CAPACITY + 3
        print("### Melakukan Resize 3 ###")
        print()

    def printAll(self):
        print("\n=== WarungMakan ===")
        for i in range(len(self._data)):
            if self._data[i] != None:
                print(i+1,end=". ")
                print(self._data[i].getNamaPelanggan())
            else:
                print(i+1,end=". ")
                print("Kosong")

# test case program
wm = WarungMakan()
wm.enqueue("Pelanggan A")
wm.enqueue("Pelanggan B")
wm.enqueue("Pelanggan C")
wm.enqueue("Pelanggan D")
wm.enqueue("Pelanggan E")
wm.printAll()
wm.enqueue("Pelanggan F")
wm.enqueue("Pelanggan G")
wm.printAll()
wm.dequeue()
wm.dequeue()
wm.dequeue()
wm.printAll()
    
