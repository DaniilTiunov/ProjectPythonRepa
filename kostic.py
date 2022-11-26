from operator import attrgetter
class klass(object):
    def __init__(self,num,symbol,boys,girls):
        self.__num    = num
        self.__symbol = symbol
        self.__boys   = boys
        self.__girls  = girls
        self.students = self.students()
        self.percent  = self.guys()
            
    def num(self):
        return self.__num
    def num(self, n):
        if isinstance(n, int):
            self:__num = n
        else:
            raise ValueError
            
    def symbol(self):
        return self.__symbol
    def symbol(self, SP):
        if isinstance(SP, str):
            self.__symbol = FN
        else:
            raise ValueError
    
    def boys(self):
        return self.__boys
    def boys(self, b):
        if isinstance(b, int):
            self:__boys = b
        else:
            raise ValueError
            
    def girls(self):
        return self.__girls
    def girls(self, g):
        if isinstance(g, int):
            self:__girls = g
        else:
            raise ValueError
            
    def students(self):
        return self.__boys+self.__girls
    
    def guys(self):
        return (self.__boys / self.students)*100
    def showklass(self):
        print("Класс: ",self.__num,"-",self.__symbol," Кол-во учащихся: ", self.students,"Процент пацанов: ", self.percent,"%")
def get_klass_list(klasses):
    if isinstance(klasses,list):
        return sorted(klasses, key=lambda x: x.percent,reverse=True)
    else:
        raise ValueError
klasses =[
            klass(1,'A',13,7),
            klass(2,'D',10,10),
            klass(3,'B',7,13),
          ]
klasslist = get_klass_list(klasses)
for klass in klasslist:
    klass.showklass()
