import time

class FiboIter():

    def __iter__(self):
        self.__n1 = 0
        self.__n2 = 2
        self.__counter = 0
        return self
        

    def __nex__(self):
        if self.__counter == 0:
            self.__counter +=1
            return self.__n1
        elif self.__counter ==1:
            self.__conter += 1
            return self.__n2
        else:
            self.__aux = self.__n1 + self.__n2
            # self.__n1= self.__n2 
            # self.__n2= self.__aux
            self.__n1,self.__n2 = self.__n2,self.__aux
            self.counter += 1
            return self.__aux

if __name__=="__main__":
    fibonachi = FiboIter()
    for element in fibonachi:
        print(element)