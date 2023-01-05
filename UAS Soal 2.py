class Node:
    def __init__(self,data,priority) -> None:
        self._data = data
        self._priority = priority
        self._next = None
        self._prev = None

class PQSTugas:
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0

    def isEmpty(self):
        if self._size == 0:
            return True
        else:
            return False

    def add(self,data,priority):
        baru = Node(data,priority)
        if self.isEmpty():
            self._head = baru
            self._tail = baru
        elif self._size == 1:
            if self._head._priority>priority:
                baru._next = self._head
                self._head._prev = baru
                self._head = baru
            else:
                self._head._next = baru
                baru._prev = self._head
                self._tail = baru
        else:
            if self._head._priority>priority:
                baru._next = self._head
                self._head._prev = baru
                self._head = baru
            elif self._tail._priority<=priority:
                self._tail._next = baru
                baru._prev = self._tail
                self._tail = baru
                self._tail._next = None
            else:
                bantu = self._head
                while bantu._priority < priority:
                    bantu = bantu._next
                bantu2 = bantu._prev
                baru._next = bantu
                baru._prev = baru
                bantu2._next = baru
                baru._prev = bantu2
        self._size = self._size + 1
        
    def remove(self):
        self._data.pop(0)
        # if self.isEmpty() == False:
        #     hapus = self._head
        #     if self._size ==1:
        #         self._head = None
        #     else:
        #         self._head = self._head._next
        #         self._head._prev = None
        #     del hapus
        #     self._size = self._size-1

    def removePriority(self, priority):
        bantu = 0
        while self._data[bantu][1] != priority:
            bantu +=1
        self._data.pop(bantu)

    def printAll(self):
        print("=== Prioritas : Tugas ===", end=" ")
        for i in range(0, len(self._data)-1):
            print(self._data[i],end= "")
        print(self._data[-1])

    def _addHead(self, newNode):
    def _addTail(self, NewNode):
    def _addMiddle(self, newNode):


if __name__ == "__main__":
    tugasKu = PQSTugas()
    tugasKu.add("StrukDat",1)
    tugasKu.add("Menyapu", 5)
    tugasKu.add("Cuci Baju", 4)
    tugasKu.add("Beli Alat Tulis", 3)
    tugasKu.add("Cuci Sepatu", 4)
    tugasKu.printAll()
    tugasKu.remove()
    tugasKu.printAll()
    tugasKu.removePriority(2)
    tugasKu.removePriority(4)
    tugasKu.printtAll()