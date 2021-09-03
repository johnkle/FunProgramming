class Array():
    def __init__(self,data):
        self.data=data
        self.size=len(data)
    
    def traverse(self):
        for i in range(0,len(self.data)):
            L.append(self.data[i])

    def add(self,k,e):
        self.data.append(e)#数组如何增加空间？
        for i in range(len(self.data)-1,k,-1):
            self.data[i] = self.data[i-1]
        self.size += 1
        self.data[k] = e

    def remove(self,k):
        for i in range(k+1,len(self.data)):
            self.data[i-1] = self.data[i]
            self.size -= 1
    
    def replace(self,p,q):
        for i in range(0,len(self.data)):
            if self.data[i]==p:
                self.data[i] = q
    
    def contain(self,e):
        for i in range(0,len(self.data)):
            if self.data[i] == e:
                return True
        return False
    
    def find(self,e):
        for i in range(0,len(self.data)):
            if self.data[i] == e:
                return i
        return -1

L=[1,3,6,7,2]
array=Array(L)
array.add(2,9)
print(L)
array.remove(2)
print(L)

    