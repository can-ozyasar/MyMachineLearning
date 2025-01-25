# -*- coding: utf-8 -*-
"""
print("merhaba Python") #klasik yazma işlemi her print de alt satıra geçer 

print(" merhaba \n Python") #alt satıra geçmek için \n
 
print(" merhaba \t Python") #alt satıra geçmek için \t

print("Merhaba {}".format("**deger ile yazildi")) #değişken ile yazmak  için 
print()
# comment oluşturmak için kullanılır

""" 
#comment yapmak için kullanılır 

"""

 #¶ konsola cls yazarak konsolu temizleyebiliriz 

### DERS 6 DEĞİŞKENLER 
# Değişkenlerin tipini belirtmeye gerek yok pythonun özelliği

x=20
y="hello"
z=1.35
print(x)
print(type(x))# x eğişkenininn tipini belirtmek için kullanılır
print(type(y))
print(type(z))
print()


#DERS 7 ARİTMETİK İŞLEMLER

# 5**2 üs alma işlemi için ** kullanılır 
#5//

a=14
b=3

print("toplama +: ",a+b)
print("cikarma -: ",a-b)
print("carpma *: ",a*b)
print("bolme /: ",a/b)
print("ust alma ^: ",a**b)
print("mod alma +: ",a%b)
print("bolum yuvarlama +: ",a//b)

print()
print()

#♦ DERS 8 PYTHON PROGRAM DOSYALARI
# cmd ekrenaından kodu çalıştırmak için cd ile kodun bulunduğu dosyaya giriyoruz 
# sonra python (.py uzantılı dosyayı yazıyoruz )
# örnek  cd desktop  python PthonDersleri.py   şeklinde 





# DERS 9 KULANICIDAN VERİ ALMA KULLANMA 

sehir =input("enter the city you live in: ")
print("the city you live in: {}".format(sehir))
print("yaşadığınız şehir  : ",sehir)
print()

#6python bu yas girdisini string olarak algılar onu isteğe göre çevirmeliyiz int'e 
yas=int(input("enter your age : "))
print("Age : ",yas )
print("in there years you will be {}  years old".format(yas+3))

print("the city you live in is:",sehir," and your age is: ",yas)


# ders ödevi alınan bir sayının karesini ekrana yazdırma 
print("square of to age : ",yas**2)

"""
# DERS 10 PYTHON BASİT QUİZ  -- FAHRENEİT TO CELSİUS TRANSLATE PROGRAM 

# kulanıcının girdiği fahreneit değerini celsius a çeviren kodu yazınız
#write the code that converts the fahrenheit value entered by the users to celsius
"""
print("welcome to program of to heat conversation")
print()

fahrenheit=int(input("please enter the fahrenheit value you want to convert to celsius : " ))
print()

celsius=(fahrenheit-32)*5/9

print(fahrenheit," degrees fahrenheit is ",celsius," degrees celsius")
"""


# İF ELSE KULLANIMI 

"""
username =input("please enter your username : ")
print()
if(username=="admin" or username=="Admin"):
    print("welcome ",username)

else:
    print("you entered an incorrect username ")
    
    
    
   
    


age = int(input("enter your age : "))

if(age<10):
    print("children's menu : " )
    
else:
    print("big menu :")   
   """ 
    
    # and or not operatörleri
    # (8<10) and (6>5) ve
    # (5==5) or (6==5) veya
    # not(5==5) değil
    
    
  # örnek ototmobil vergisi hesaplama
# 100 bin tl üstü %1.70
# 50 bin 100 bin arası %1.54  
# 0 50 bin arası %1.49

"""
limit =int(input(" vergi hesaplanacak olan otomobil fiyatını giriniz : "))

if(limit>=100000):
    print(limit," için vergi miktarı (%1.70) : ",limit*1.70/100)
elif(limit<100000 and limit>=50000):
    print(limit," için vergi miktarı  (%1.54) : ",limit*1.54/100)
else:
    print(limit," için vergi miktarı  (%1.49) : ",limit*1.49/100)

"""

# DERS 12 VUCUT KİTLE ENDEKSİ HESAPLAYAN PROGRAM ÇIKTISI 
# BEN YAZMADIM BASİT BİR ÖRNEK ÜSTETKİNE BENZER



# DERS 13 STRİNG VERİ TİPİ 
"""
kelime1 ="merhaba"
kelime2='dunya'

print(len(kelime1)) # stringin uzunluğunu verir (7)

print(kelime1[0])# string in 0. indexli elemanını verir dizi gibi görür (m)
print(kelime1[1:3])# string in 1. indexli elemanından 3. indexli elemanına kadar yazar (er) 
print(kelime1[3:])# string in 3. indexli elemanından son elemanına kadar yazar (haba)

print(kelime1[0:5:2])# string in 0. indexli elemanından 5.index  elemanına kadar 2 şer atlayarak yazar 


kelime3=kelime1+" "+kelime2 # stirng birleştirme
print(kelime3.upper()) # string tüm harfleri büyültme
print(kelime3.lower()) # string tüm harfleri küçültme

print(kelime3.split())# kelimeleri ayırma split içine nerelerden ayırmak istediğimizi yazıyoruz

kelime4="merhaba,adam,ad,soyad"
print(kelime4.split(","))

#  DERS 14 QUİZ

# kullanıcının girdiği kelimeyi harfleri ters olacak şekilde yazan program

print("TERSTEN YAZAN PROGRAM")
print()

kelime=input("tersten yazılmasını istediğiniz kelimeyi yazınız: ")

kelime[::1] #tamamını yaz demek başlangıç ve bitişi boş bıraktık 
kelime[::-1] # tamamını tersten yaz demek -1 olduğu için

#adımımız -1 oldu hep geriye doğru gidiyor
print(kelime[::-1])

"""

# # DERS 15 FONKSİYONLAR: 
"""
def fonksiyon_adi (argümanlar):
    fonksiyonun yapacağı işlemler

"""
"""
# ekrana merhaba yazan fonksiyon

def merhaba_yaz ():
    print("\n FONKSİYON KULLANARAK YAZILAN METİN -> MERHABA !")


# ÇAĞIRMA
merhaba_yaz()
merhaba_yaz()


# kare hesaplayan fonk.

def kare_hesaplayici(sayi):
    return (sayi**2)


# ÇAĞIRMA

print("11 in karesi fonksiyon ile hesaplanan değeri : ",kare_hesaplayici(11) )


# iki parametre lan fonk.
def ekrana_yazdirici(yas,isim):
    print("İsminiz: ",isim," Yasiniz: ",yas)


# ÇAĞIRMA
ekrana_yazdirici(19,"Muhammed Can")



# Sayininn ciftmi tekmi bulan fonksiyon 

def ciftmi_tekmi(sayi):
    if(sayi%2==0):
        return "cift"
    else:
        return "tek"
    

print(" 15 sayisi ",ciftmi_tekmi(15),)    
print(" 14 sayisi ",ciftmi_tekmi(14),)
"""


# # DERS 15 FONKSİYONLAR:


#ekrana yazdırma ve hesaplatma fonksiyonları ayrı olacak şekilde 
"""

def kup_al(sayi):
    return (sayi**3)


def kup_yazici(sayi1):
    print(sayi1," sayisinin kubu :",kup_al(sayi1) )



kup_yazici(10)
"""


# iki değer döndüren fonksiyonlar bazı dillerde var sadece
"""
def kare_kup_hesapla(sayi):
    kare=sayi**2 
    kup=sayi**3 
    return kare,kup
    

sayi=5
sayinin_karesi,sayininn_kubu=kare_kup_hesapla(sayi)

print(" 5 sayisinin karesi ",sayinin_karesi,"\n 5 sayisinin kubu ",sayininn_kubu)


 # DERS 17 FAKTORİEL HESABI 
 
def faktoriel_hesapla(sayi):
     if(sayi==1 or sayi==0):
         return 1
     return sayi*faktoriel_hesapla(sayi-1)


print("6!:",faktoriel_hesapla(6))

"""
# DERS 18-19 HESAP MAKİNESİ PROGRAMI 
"""

print("HESAPLAMA UYGULAMASI \n")
sayi1=int(input("lütfen işlem yapacağınız ilk sayiyi giriniz : "))
print("islem yapacağınız işlem no seçiniz  \n  0 toplama \n 1 çıkarma \n 2 çarpma \n 3 bolme ")

islemno=int(input(" giriniz : "))

def hesaplama(sayi1,sayi2,islemno):
    if(islemno==0):
        print(sayi1 ," + ",sayi2," = ",sayi1+sayi2)
    elif(islemno==1):
        print(sayi1 ," - ",sayi2," = ",sayi1-sayi2)
    elif(islemno==2):
        print(sayi1 ," * ",sayi2," = ",sayi1*sayi2)
    elif(islemno==3):
        print(sayi1 ," / ",sayi2," = ",sayi1/sayi2)
    else:
        print(islemno ," islemno hatalı")






#TEKRAR ÇALIŞTIRMAK İÇİN CONSOLE DE YUKARI OK TUŞU VE ENTERE BASINCA RUN EDER PROGRAMI YADA F5 İLE DE RUN EDİLEBİLİR 

sayi2=int(input("lütfen işlem yapacağınız ikinci sayiyi giriniz : "))

hesaplama(sayi1, sayi2, islemno)

"""


#  Ders 20 Python temel bilgiler 


#-----------------------
#-----------------------
#-     MODÜLLER        -
#-----------------------
#-----------------------




















