


# DERS 34 NESNEYE YÖNELİK PROGLAMLAMA  OOP 
"""
class Otomobil():
    
    klima=" klima yok"
    teker_sayisi=4

    # kurucu fonksiyon
    def __init__(self,marka,model,yil,kilometre): 
        # self bir objeyi temsil eder this->  gibi 
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
"""
# DERS 35 OOP 2 KALITIM 


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
        #kalıtım aldığımız sınıfın kurucu fonksiyonunu çağırmak için 
        kara_Araci.__init__(self, beygir_gucu, teker_sayisi)
        #kendi özelliklerimizi ekliyoruz
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
"""
# metin dosyası oluşturma 


# OGRENCİLER İSMİNDE BİR TXT DOSYASI OLUŞTURDUK MEVCUT DİZİNE 
ogrenci_dosyasi = os.open("ogrenciler.txt",os.O_RDWR|os.O_CREAT) #  DOSYA YOKSA HEM OKUMA HEM YAZMA YETKİSİ VEREREK OLUŞTUR
# DOSYA VARSADA AÇ 


# OGRENCİLER.TXT DOSASINDA OGRENCİ YAZALIM İSİM NOT BİLGİSİ 


os.write(ogrenci_dosyasi, "Ali Er , 87\n".encode()) #wrie ile yazmada bytes ile yazmank lazım normalde 10101 gibi 
#.encode yazınca bizim yerimize byte e çeviriyor stringimizi 
 

os.write(ogrenci_dosyasi, "Ali Er , 87 \n".encode())
os.write(ogrenci_dosyasi, "Metehan baln , 17 \n".encode())
os.write(ogrenci_dosyasi, "Haktuy Bulat , 50 \n".encode())
os.write(ogrenci_dosyasi, "Hasan Akca Er , 42 \n".encode())
os.write(ogrenci_dosyasi, "Hnil Bayern , 32 \n".encode())


os.close(ogrenci_dosyasi)

"""




#ogrencilre.txt dosyasını ***sadece okuma yapmak için açma

ogrenci_dosyasi=os.open("ogrenciler.txt",os.O_RDONLY)

# dosyada kaç byte var uzuluğunu hesaplama 
dosya_uzunluk=os.stat(ogrenci_dosyasi).st_size

#okuma işelmi byte ile okuyor!
icerik=os.read(ogrenci_dosyasi, dosya_uzunluk)# dosya okundu burda byte olarak okudu

# "print(icerik.decode())"
 # normalde byte olaraka yazar
#b'Ali Er , 87 \nmehmet can , 17 \nhakk\xc4\xb1 bulut , 50 \nhasan akca Er , 42 \nanil bayern , 32 \n'
# bunun yazar normalde biz stringe çevireceğiz decode ile encode yazarken decode okurken 

ogrenciler=icerik.decode()
print(ogrenciler)



""" DERS 37 DOSYA İŞLEMLERİ 2 QUİZ ortalama hesaplama """


ogrenciler_list=ogrenciler.split("\n")

print(ogrenciler_list)# yazdırmak için listemizi 
ogrenci_sayisi=len(ogrenciler_list)-1


index=0
toplam_notlar=0
while(index<ogrenci_sayisi):
    ogrencinotu=ogrenciler_list[index].split(",") 
    toplam_notlar+=int(ogrencinotu[1])
    index+=1
    

print("ortalama : ",toplam_notlar/ogrenci_sayisi)
#DOSYAYI SİLMEK İÇİN KULLANILIR 
#os.unlink("ogrenciler.txt") 



os.close(ogrenci_dosyasi) # işimiz bittiiğinde dosyayı kapatmalıyız

























 






