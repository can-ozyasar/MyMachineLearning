# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 11:28:50 2024

@author: canoz
"""

#-----------------------
#-----------------------
#-   ANA MODÜLÜ -
#-----------------------
#-----------------------
 
#$$$$**$$$ ÖNEMLİ BİLGİLER KESİN OKU DİKKAT ETTT !!!!!!!!!!!!!



import aritmetik # bu yöntemle kullanabiliyoruz o dosyadaki fonksiyonları
import AritmetikMesaj 
import math  # pythonunu kendi kütüphanesi 

"""

from aritmetik import*

"""

 # bu yöntem sanki o fonksiyonları buraya kopyalıyormuş gibi oluyor o yüzden 
# aritmetik.  diye yazmaya gerek kalmaz direkt ismi ile çağırabiliriz fonku  örnek kup_hesapla(10) gibi yazabiliriz

# her iki yöntem de ayrı ayrı olarak kullanılabiliyor 
# eğer ayrı ayrı dosyalarda aynı isimli fonklar olsaydı 2. yöntem patlayabilir 
# ama 1. fonnksiyon daha garanti çünkü dosya ismi ile kullanıyoruz fonku


"""
from aritmetik import kare_hesaplayici ,kup_hesaplayici
"""
# bu da sadece karehesapla ve kuphesapla  fonksiyonunu almak için kullanılır  arttırıp azaltılabilir , ile
"""
AritmetikMesaj.mesaj_yaz("HOŞGELDİNİZ")
kullanici_sayi=int(input("bir sayı giriniz : "))

print("kare :",aritmetik.kare_hesaplayici(kullanici_sayi))
print("kup :",aritmetik.kup_hesaplayici(kullanici_sayi))




# PYTHON KENDİ KÜTÜPHANELERİNDEN KULLANMA
# ÖRNEK OLARAK MATH KÜTÜPHANESİ 
#import math  ekeldik en üste 
# internette detayları var ordan kulanıma bakılabilir 



print("\n64'ün karekökü math kütüphanesi ile :",math.sqrt(64))
"""

# DERS  21  22 veri tipleri LİSTELER
#-----------------------
#--                   --
#--   VERİ TİPLERİ    --
#--                   --
#-----------------------


#  LİSTELER
"""
list=[24,32,14,25,40,"izmir",32.8]

print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])

print()


print(list[-1]) # 40 yazar 0 indexten 1 önceye gider yani
print(list[-2])


print(list[2]+list[6])

print(len(list)) #◘ listenin eleman sayısını verir 

"""




#♠ TUPLE : eleman İÇERİĞİ DEĞİŞTİRİLEMEYEN LİSTELERE DENİR 
"""

tuplelist={24,32,14,25,40,"izmir",32.8}

# LİSTEDEKİ ÖZELLİKLER AYNEN DEVAM EDİYOR 
# İÇİERİK DEĞİŞMEZ ÖRNEK 

tuplelist[0]=10
print(tuplelist[0])
#TypeError: 'set' object does not support item assignment   hatası verir


"""

# DERS 23 QUİZ


# bir paragraftaki kelime sayısını ekrana yazdıran programı bul

"""

metin ="Dünyamızda 1900’lü yıllardan günümüze kadar dil öğretiminde çeşitli metinler kullanılmıştır. Bunlar “ edebi metinler, üretilmiş metinler, özgün ve özel metinler ” başlıkları altında toplanmıştır. Metinlerin seçimi dil öğretim yaklaşım ve yöntemlerine göre değişmektedir. Her yaklaşım kendine özgü metin kullanmıştır. Geleneksel yaklaşımda dil bilgisi kuralları, atasözleri, edebiyat, genel kültür gibi konuların öğretimine ağırlık verildiğinden edebi metinler kullanılmıştır. Davranışçı yaklaşımda dil davranış olarak ele alınmış, tekrar, taklit ve ezberleme yoluyla öğretilmiştir. Bu yaklaşımda edebi metinler yerine üretilmiş metinler kullanılmıştır. Bilişsel yaklaşımda “dil iletişim aracıdır” görüşü yayılmış ve özgün metinler kullanılmaya başlanmıştır. Günümüzde ise yapılandırıcı yaklaşımdan hareketle "


print("kelime sayısı ",len(metin.split()))# kelimeleri ayırma split içine nerelerden ayırmak istediğimizi yazıyoruz


print("0. indesli kelimemiz: ",metin.split()[0])
"""



# VERİ TİPLERİ DİCTİONARY OBJELERİ TUTAR 

# bu şekilde kullanılır
# Mydictionary ={'anahtar ':'deger ','anahtar ':'deger ','anahtar ':'deger '}
"""

Mydictionary ={'isim':'muhammed',
               'soyad':'ozyasar',
               'ogrencino':2135,
               'yas':19,
               'sehir':'izmir'}

Mydictionary2 ={'isim':'can',
               'soyad':'akın',
               'ogrencino':4720,
               'yas':20,
               'sehir':'ankara'}

# göze güzel gözükmesi açısından bu şekilde altalta yaznmak daha iyi ollur 


print(Mydictionary['isim'])
print(Mydictionary2['isim'])


#  değere erişmenin 2. yolu get ile
print(Mydictionary.get('yas'))
print(Mydictionary2.get('yas'),"\n")


# dictionary nini tüm  anahtar değerlerine erişme
print(Mydictionary.keys())
# bu işleme veri çekerken dictionary verisi çekersek içnde hangi anahtaralar var görmek için kulanılır


# dictionary içindeki tüm değerleri döndürmek içn kullanılılr 
print(Mydictionary.values())


# dictionary içindeki tüm value ve anahtar isimleri kısaca tüm listeyi döndürmek için kullanılır
print(Mydictionary.items())

""" 

# DERS 25 FOR DÖNGÜSÜ
"""

ogrenci_list=["Ahmet Emre","Kenan Yıldız","Anıl Karadeniz","Arda Güler","Kerem Aktürkoğlu"]

sayac=0

for item in ogrenci_list:
    sayac+=1
    print(item)
    
print("listedeki eleman sayısı . ",sayac,"\nlen fonk : ",len(ogrenci_list))
    
    
    
aranan_isim = input("Lütfen sınıfta Aranacak ad soyad giriniz:")

ogrenci_listede_mevcut = False

for ogrenci in ogrenci_list:
    if (ogrenci == aranan_isim):
        ogrenci_listede_mevcut = True



if (ogrenci_listede_mevcut == True) :
    print("Öğrenci sınıfımızda mevcuttur!")
else:
    print("Öğrenci msınıfmızda kayıtlı değildir")
    
    
 
    # forun 2. kulanımı range ile  1 - 9 a kadar yazar
   #for(int i=0;i<10;i++){
          # cout<<i;} diğer dillerdeki bu işlem "
    
for i in range(10):
    print(i)
    
    
    
    """
    
    # DERS26 WHİLE LOOP 
"""
sayi=0
while (sayi<10):
    print(sayi)
    sayi+=1
    """
# kendisine gönderilen sayının faktöriyelini hesaplayan while 
"""

def faktoriel_hesapla(sayi):
    
    faktoriel=1
    while (sayi>1):
        faktoriel*=sayi
        sayi-=1
        
    return faktoriel    
    
    
    
print(faktoriel_hesapla(6))
"""
#$ QUİZ DERS 26  ECHO PROGRAMI KULLANICI NE YAZARSA EKRANA ONU YAZACAK 
# PROGRAM SÜREKLİ ÇALIŞSIN ANCAK "KAPAT"  YAZINCA PROGRAM DURSUN 

"""
def echo_program(kelime):
    while (kelime!="kapat"):
        kelime=input("yazılmasını istediğiniz kelimeyi yazın: \n")
        print(kelime)
        
    
echo_program("1")
   
sayi=int(input("faktorile için sayi yazın: \n"))
faktoriel=1;

for i in range(sayi):
    faktoriel*=sayi

print(faktoriel)
"""

# DERS 29 ASAL SAYI BULAN PROGRAM

"""
def asal_mi(sayi):
    if (sayi <= 1):
        return False
    for i in range(2, sayi):
        if (sayi % i) == 0:
            return False
    return True

print(asal_mi(2))

   """
 # 1 DEN 100 E KADAR ASALLARI YAZAN 
    """
for i in range(1,101):
    if(asal_mi(i)):
        print(str(i) ,end=" , ") 
        # yanyana yazmak için end="," yazdık 
        
        
        """
        

    #• DERS 30  LAMDA MAP FİLTER ÖZELLİKLERİ 
        
    """
def kup_al(sayi):
    return sayi**3

liste=[1,2,3,4,5]

for item in liste:
    print(kup_al(item))
    
    """
    #♦ bu işlemi map( eşleştirme haritalama) ile yapma  tek satırda 
  # map bize bir obje döndürür onu çevirmemi lazım   
    """
yeni_list=list( map(kup_al, liste))

print(yeni_list) 
    
  
    """
  
    
  # lambda hızlıca fonksiyon yazmak içn kullanılır 
    """
yeni_list2=list( map(lambda sayi:sayi**3, liste))

print(yeni_list2)    
    
"""

# filter 
    """"

def tek_sayi_filtreleme(sayi):
    if(sayi%2==1):
        return sayi
    else:
        return None
        
        
print(tek_sayi_filtreleme(7))

yeni_liste =list( filter(tek_sayi_filtreleme , liste))
    
    
print(yeni_liste)   

    """

# DERS 31 TRY EXCEPT  FİNALLY
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



