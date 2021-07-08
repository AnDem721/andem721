from dateutil import relativedelta
from datetime import datetime

class Pracownik: 
    def __init__(self, imie, data_zatr):
        self.imie = imie
        self.data_zatr = data_zatr
        self.base_wypl = 1500

    def work_staz(self):
        data_zatr_obj = datetime(self.data_zatr)
        today = datetime.today()
        return relativedelta(today, data_zatr_obj).years

    def payment(self):
        return base_wypl
        
class Manager(Pracownik):
    def __init__(self,imie, data_zatr, data_obj_sta):
        super().__init__(imie, data_zatr)
        self.data_obj_sta = data_obj_sta
        self.base_wypl = 2500

    def payment(self):
        return self.base_wypl * 1.5

    


if __name__ == '__main__':
    prac1 = Pracownik("Andrzej", "2001, 04, 02")
    print(prac1.work_staz())