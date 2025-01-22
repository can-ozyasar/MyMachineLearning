# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 17:42:40 2024

@author: canoz
"""

import random


"""
# 0 ile 1 arasında rastegele sayılar üretmek iiçin
print(random.random())

# iki sayı arasında rastgele sayılar üretme 
print(random.uniform(10,20))

# 2 sayı arasından tamsayı üretme 
print(random.randint(10,20))


# 0 dan 9 a kadar sayıları yazar 
print(*range(10))


# verilen listeden otomatik sayı seçiyor  0 1 2 3 4 5 6 7 8 9 verdik range 10 ile 
print(random.choice(range(10)))

mylist=list(range(10))
print(mylist)
# listenin içindeki değerleri karıştırır 
random.shuffle(mylist)
print(mylist)
"""

# MATEMATİK KÜTÜPHANESİ 

"""
import math 

#karekök alma
print(math.sqrt(25))

print(round(8.7)) # yuvarlama işlemi yapar 

print(math.ceil(8.67)) # bir üst tamsayıya çeker (9)
print(math.floor(8.87)) # bir alt tamsayıya çeker (8) 

print(math.sin(math.pi/2)) # sin hesaplama örenk 
print(math.cos(0)) # sin hesaplama örenk 
"""


# ders 33 verilen listede çift sayıları bulan program 
"""
liste={1,2,3,4,5,6,7,8,9,10,11,12,13,14,16}


def cift_adedi(sayilar):
    sayac_cift=0

    for index in liste:
        if(index%2==0):
            sayac_cift+=1
    
    
    return sayac_cift
        

print("cift sayi adedi : ",cift_adedi(liste))
"""





# DERS 34 NESNEYE YÖNELİK PROGLAMLAMA  OOP 
"""
class Otomobil():
    
    klima=" klima yok"
    teker_sayisi=4
    # kurucu fonksiyon
    def __init__(self,marka,model,yil,kilometre): 
        self.marka=marka
        self.model=model
        self.yil=yil
        self.kilometre=kilometre
        
    def km_degisti(self,yenikm):
        self.kilometre=yenikm



audi_auto = Otomobil("Audi","A3",2019,250000)

opel_auto=Otomobil("Opel" , "Astra" , 2020 , 45000)
sahin_auto=Otomobil("tofas", "sahin", 1999, 2000)

print(opel_auto.marka)
sell_car_list=[audi_auto,opel_auto,sahin_auto]

for item in sell_car_list:
    print(item.marka,item.model,item.yil,item.kilometre)


audi_auto.km_degisti(500)
print(audi_auto.kilometre)

"""

# DERS 35 OOP 2 KALITIM 
"""

class kara_Araci():
    hiz=0
    
    def __init__(self,beygir_gucu,teker_sayisi):
        self.beygir_gucu=beygir_gucu
        self.teker_sayisi=teker_sayisi
        
    def hizi_Ayarla(self,deger):
        self.hiz = deger
        return self.hiz
        
        
        
        
        
class otobus(kara_Araci):#kara aracından türettik kalıtım aldık 
    def __init__(self,beygir_gucu,teker_sayisi,yolcu_kapasitesi):
        kara_Araci.__init__(self, beygir_gucu, teker_sayisi)
        self.yolcu_kapasitesi=yolcu_kapasitesi
        
        
class otomobil(kara_Araci):
    def __init__(self,beygir_gucu,teker_sayisi,sunroof):
        kara_Araci.__init__(self,beygir_gucu,teker_sayisi)
        self.sunroof=sunroof
        
    

    

otobus1=otobus(500,6,21)

print("otobusun beygir gucu : hp ",otobus1.beygir_gucu)
print("otobusun hizi ",otobus1.hizi_Ayarla(120))


otomobil=otomobil(500,6,"otomatik sunroof")

print("otomobil sunroof : ",otomobil.sunroof)


"""


 # DERS 36 DOSYALARA YAZMA OKUMA VS ...
 
 
import os 


# o dizinde hangi dosyalar var onu yazıyor    os.listdir()
print(os.listdir())

# metin dosyası oluşturma 

"""
# OGRENCİLER İSMİNDE BİR TXT DOSYASI OLUŞTURDUK MEVCUT DİZİNE 
ogrenci_dosyasi = os.open("ogrenciler.txt",os.O_RDWR|os.O_CREAT) #  DOSYA YOKSA HEM OKUMA HEM YAZMA YETKİSİ VEREREK OLUŞTUR
# DOSYA VARSADA AÇ 


# OGRENCİLER.TXT DOSASINDA OGRENCİ YAZALIM İSİM NOT BİLGİSİ 


os.write(ogrenci_dosyasi, "Ali Er , 87".encode()) #wrie ile yazmada bytes ile yazmank lazım normalde 10101 gibi 
#.encode yazınca bizim yerimize bytes e çeviriyor stringimizi 
 

os.write(ogrenci_dosyasi, "Ali Er , 87 \n".encode())
os.write(ogrenci_dosyasi, "mehmet can , 17 \n".encode())
os.write(ogrenci_dosyasi, "hakkı bulut , 50 \n".encode())
os.write(ogrenci_dosyasi, "hasan akca Er , 42 \n".encode())
os.write(ogrenci_dosyasi, "anil bayern , 32 \n".encode())

"""




#ogrencilre.txt dosyasını ***sadece okuma yapmak için açma

"""
ogrenci_dosyasi=os.open("ogrenciler.txt",os.O_RDONLY)

# dosyada kaç byte var 


dosya_uzunluk=os.stat(ogrenci_dosyasi).st_size
icerik=os.read(ogrenci_dosyasi, dosya_uzunluk)# dosya okundu burda byte olarak okudu

# "print(icerik.decode())"
 # normalde byte olaraka yazar
#b'Ali Er , 87 \nmehmet can , 17 \nhakk\xc4\xb1 bulut , 50 \nhasan akca Er , 42 \nanil bayern , 32 \n'
# bunun yazar normalde biz stringe çevireceğiz decode ile encode yazarken decode okurken 
ogrenciler=icerik.decode()
ogrenciler_list=ogrenciler.split("\n")

ogrenci_sayisi=len(ogrenciler_list)-1


index=0
while(index<ogrenci_sayisi):
    ogrencinotu=ogrenciler_list[index].split(",") 
    print(int(ogrencinotu[1]))
    index+=1
    


"""
#os.unlink("ogrenciler.txt") DOSYAYI SİLMEK İÇİN KULLANILIR 
"""


os.close(ogrenci_dosyasi) # işimiz bittiiğinde dosyayı kapatmalıyız

"""
























 






