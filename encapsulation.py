class store:
    def __init__(self):
        self._appleprice = 2    

    def __init__(self):
        self.__pearprice = 4

    def getpearprice(self):
        print(self.__pearprice)

    def setpearprice(self,private):
        self.__pearprice = private


obj = store()
obj._appleprice = 3
print(obj._appleprice)
obj.getpearprice()
obj.setpearprice(12)
obj.getpearprice()
        
