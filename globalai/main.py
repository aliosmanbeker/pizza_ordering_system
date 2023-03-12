import csv
from datetime import datetime
from pizza_sos import *
import os

def main():
    with open('orders.csv', 'w', newline='') as orders_file:
        writer = csv.writer(orders_file)
        writer.writerow(['ID','isim','Pizza','Açıklama','Tutar','kredi kartı numarası', 'kredi kartı son kullanma tarihi', 'kredi kartı CVV numarası', 'sipariş tarihi'])
    
    with open("Menu.txt", "w") as file:
        file.write("* Lütfen Bir Pizza Tabanı Seçiniz:\n1: Klasik\n2: Margarita\n3: TürkPizza\n4: Sade Pizza\n* ve seçeceğiniz sos:\n11: Zeytin\n12: Mantarlar\n13: Keçi Peyniri\n14: Et\n15: Soğan\n16: Mısır\n* Teşekkür ederiz!")  
    with open('Menu.txt', 'r') as menu_file:
        menu = menu_file.read()
        print(menu)
    while True:
        pizza_choice = int(input('Lütfen pizzanızı seçiniz (1-4): '))
        if pizza_choice == 1:
            pizza = Klasik_pizza()
            break
        elif pizza_choice == 2:
            pizza = Margherita_pizza()
            break
        elif pizza_choice == 3:
            pizza = Turk_pizza()
            break
        elif pizza_choice == 4:
            pizza = Sade_pizza()
            break
        else:   
            print('Hatalı seçim! Lütfen 1 den 4 e kadar seçim yapınız.')
    sos = None
    while True:
        sos_seçimi = int(input("Lütfen sos seçiminizi yapın (11-16) Sos istemiyorsanız 0 ' ı tuşayınız.: "))

        if sos_seçimi == 0:
            break
        elif sos_seçimi == 1:
                sos = Zeytin_sos(pizza)
        elif sos_seçimi == 2:
                sos = Mantar_sos(pizza)
        elif sos_seçimi == 3:
                sos = Keci_Peynir_sos(pizza)
        elif sos_seçimi == 4:
                sos = Et_sos(pizza)
        elif sos_seçimi == 5:
                sos = Sogan_sos(pizza)
        elif sos_seçimi == 6:
                sos = Misir_sos(pizza)
        else:        
            print('Hatalı seçim! Lütfen 1 den 6ya  kadar seçim yapınız.')
    tutar = sos.get_fiyat()
    print('Toplam fiyat : ' , tutar)
    
    print("-------------------------------------------------------------")
    print("-------------------------------------------------------------")
    print("-------------------------------------------------------------")
    print("PİZZA BİLGİLERİ")
    print('Toplam fiyat : ' , tutar)
    print("Seçilen Pizza ve Sos: {}".format(sos.get_açıklama()))
    print("-------------------------------------------------------------")
    print("-------------------------------------------------------------")
    print("-------------------------------------------------------------")

    isim = input('Adınız: ')
    tc_num = input('TC Kimlik Numaranız: ')
    kk_numarası = input('Kredi Kartı Numaranız: ')
    kk_skt = input('Kredi Kartı Son Kullanma Tarihi: ')
    kk_cvvno = input('Kredi Kartı CVV: ')
    
    print("-------------------------------------------------------------")
    print("MÜŞTERİ BİLGİLERİ")
    print("Müşteri İsmi ve Soyadı: {}".format(isim,tc_num))
    print("-------------------------------------------------------------")
    print("ÖDEME BİLGİLERİ")
    print("Kredi Kartı Numarası: {}\nKredi Kartı Son Kullanma Tarihi: {}".format(kk_numarası,kk_skt))
    print("-------------------------------------------------------------")

    current_time = datetime.now()
    current_time.strftime("%Y-%m-%d %H:%M")
    
    with open('orders.csv', 'a', newline='') as orders_file:
        writer = csv.writer(orders_file)
        writer.writerow([tc_num, isim, pizza.get_açıklama(), sos.get_açıklama(), tutar, kk_numarası, kk_numarası, kk_cvvno, current_time])
            
if __name__ == '__main__':
    main()
            
        