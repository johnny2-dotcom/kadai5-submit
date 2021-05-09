import eel

class Menu:
    def __init__(self,code,name,price):
        self.code = code
        self.name = name
        self.price = price
    
    def menu_disp(self):
        return str(self.code)+'. '+self.name+': ¥'+str(self.price)
    
    def get_total(self,count):
        total_price = self.price * count
        return total_price
