class Pizza:
    
    def __init__(self, açıklama, fiyat):
        self.açıklama = açıklama
        self.fiyat = fiyat
 
    def get_açıklama(self):
        return self.açıklama
    
    def get_fiyat(self):
        return self.fiyat

class Decorator(Pizza):
    def __init__(self, component):
        self.component = component
        
class Turk_pizza(Pizza):
  def __init__(self):
        açıklama = "Türk Pizza"
        fiyat = 109.0
        super().__init__(açıklama, fiyat)

class Klasik_pizza(Pizza):
  def __init__(self):
        açıklama = "Klasik Pizza"
        fiyat = 99.0
        super().__init__(açıklama, fiyat)

class Margherita_pizza(Pizza):
  def __init__(self):
        açıklama = "Margherita Pizza"
        fiyat = 119.0
        super().__init__(açıklama, fiyat)

class Sade_pizza(Pizza):
  def __init__(self):
        açıklama = "Sade Pizza"
        fiyat = 99.0
        super().__init__(açıklama, fiyat)

class Zeytin_sos(Decorator):
    def __init__(self, component):
        self.__cost = 6.0
        self.__description = "Zeytin"
        super().__init__(component)
    
    def get_fiyat(self):
        return self.component.get_fiyat() + self.fiyat
    
    def get_açıklama(self):
        return  self.component.get_açıklama() + ' ' + self.açıklama


class Mantar_sos(Decorator):
    def __init__(self, component):
        self.fiyat = 6.0
        self.açıklama = "Mantar"
        super().__init__(component)
   
    def get_fiyat(self):
         return self.component.get_fiyat() + self.fiyat
     
    def get_açıklama(self):
         return  self.component.get_açıklama() + ' ' + self.açıklama

class Keci_Peynir_sos(Decorator):
    def __init__(self, component):
        self.fiyat = 6.0
        self.açıklama = "Keçi Peyniri"
        super().__init__(component)
    
    def get_fiyat(self):
         return self.component.get_fiyat() + self.fiyat
     
    def get_açıklama(self):
         return  self.component.get_açıklama() + ' ' + self.açıklama

class Et_sos(Decorator):
    def __init__(self, component):
        self.fiyat = 12.0
        self.açıklama = "Et"
        super().__init__(component)

    def get_fiyat(self):
         return self.component.get_fiyat() + self.fiyat
     
    def get_açıklama(self):
         return  self.component.get_açıklama() + ' ' + self.açıklama

class Sogan_sos(Decorator):
    def __init__(self, component):
        self.fiyat = 4.5
        self.açıklama = "Soğan"
        super().__init__(component)
    
    def get_fiyat(self):
         return self.component.get_fiyat() + self.fiyat
     
    def get_açıklama(self):
         return  self.component.get_açıklama() + ' ' + self.açıklama

class Misir_sos(Decorator):
    def __init__(self, component):
        self.fiyat = 5.0
        self.açıklama = "Mısır"
        super().__init__(component)
    
    def get_cost(self):
        return self.component.get_cost() + self.__cost

    def get_description(self):
        return self.component.get_description() + ' ' + self.__description

