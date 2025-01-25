# metin tabanlı içeriklerde desen arama REGEX



       # REGEX MODULÜ  DESEN EŞLEŞTİRME 
        
       
import re



cumle = " Guido van Rossum , 1980'lerin sonlarında ABC programlama dilinin halefi olarak Python üzerinde çalışmaya başladı ve ilk olarak 1991'de Python 0.9.0 olarak yayınladı. [ 35 ] Python 2.0, 2000 yılında yayınlandı. 2008'de yayınlanan Python 3.0, önceki sürümlerle tamamen geriye dönük uyumlu olmayan büyük bir revizyondu . 2020'de yayınlanan Python 2.7.18, Python 2'nin son sürümüydü. [ 36 ]"
      
pattern ="Python"

#isteneni ilk bulduğu yeri yazar durur
print( re.search(pattern, cumle) )

sonuc=re.search(pattern, cumle) #BULUNAN I SONUÇ A ATIYORUZ END VE START İLE BAŞLANGIÇ BİTİŞ İNDİSLERİNİ YAZIYORUZ 
print("başlangıç indis : ",sonuc.start()," son indis : ",sonuc.end(),"\n \n")


# TÜM BULUNAN DEĞERİ YAZDIRMAK İÇİN (FİNDİTER(PATTERN,CUMLE))
count=0;
for bulunan in re.finditer(pattern, cumle):
    print(bulunan.span(),bulunan.group(),"\n") # metinde bulduğu tüm pythonları yazar .
    count+=1
    
print("Python kelimesi metinde toplam  :",count," adet var \n")







# DESEN EŞLEŞTİRME İŞLEMLERİ 

cumle2 ="merhaba benim cep numaram 532-1112233 beni öğleden sonra arayabilirsiniz 532-1178243 "

#aradığımız içeriği tam olarka bilmiyorsak ama ne tür olduğunu biiyorsak desenler kullanırız : 
    
    
    #$$ rakamlar için \d
    #$$ boşluk için \s
    #$$ harfler için \w
    #$$ ...... gerisini internetten arştırabilirsin 
    
    

 # neyi aradığımızı tam olarka bilmiyorduk ama aşşağı yukarı nasıl bişey olduğunu biliyorduk 
 # örnek 11 haneli tc no gibi 
 
 
pattern2="\d\d\d-\d\d\d\d\d\d\d" # bu tarz birşey arıyorum demek bu 
print(re.search(pattern2, cumle2))

for bulunan in re.finditer(pattern2, cumle2):
    print(bulunan.span(),bulunan.group(),"\n") # metinde bulduğu tüm desenlerimizi yazar .
    count+=1
    
    
    
    
    
    
    
   
     
  #► proglamlama SINAV 
        
  
    
  
    
  #SORU 1 :  YARIÇAP DAN ALAN VE ÇEVRE HESAPLAMA 10 P 
  
  
  
import math 

yaricap = float(input("Dairenin Yarıçapını Giriniz: "))
cevre = ( 2 * 3.14 * yaricap )
alan = 3.14 * yaricap * yaricap
print("nDairenin Alanı : ", alan )
print("nDairenin Çevresi : ", cevre)
   
      
        
      
        
      # SORU 2 ÖĞRENCİ NO AYIRMA MANTIKLI YAZMA ANLAMIYLA 
        

okul_numarasi=input("Okul numaranızı giriniz:")
no=str(okul_numarasi)
ogrno = dict(GirisYili=no[:4], FakulteNo=no[4:6], BolumNo=no[6:8], OgrenimNo=no[8:9], OgrenciGirisSirasi=no[10:12])
print("NUMARANIN ACILIMI:")
print(type(ogrno))
for i in ogrno.items():
    print (i[0]+": "+i[1])
    






      
        
      
        
   #$$ SORU 3  5 İN KATLARINI EKRANA YAZDIRAN PROGRAM 
      
   
sayilar = [17,23,15,75,55,30,10,21,20,34,28,107,5,4,32]
sayac = 0
for sayi in sayilar:
    if sayi%5 == 0:
        print(sayi, ": 5'in katıdır.")
        sayac = sayac+1
    
# Döngü sonu
print("5'in katı olan sayı adeti : "+str(sayac))
        


# SORU 4 TAMSAYI DİZİSİ OLSUN İÇİNDEKİ 0 ELEMANLARI DİZİNİNİ EN SONUDA OLSUN 


def moveZeroes(sayilar):    
    j = 0
    for sayi in sayilar:
        if(sayi != 0):
            sayilar[j] = sayi
            j += 1
 
    for x in range(j, len(sayilar)):
        sayilar[x] = 0
 
sayilar = [0,1,0,3,11]
moveZeroes(sayilar)
print(sayilar)


#SORU 5 DAĞ DİZİSİ TANIMINA UYAN DİZİYİ BULAN FONKSİYON ARTTMALI VE AZALMALI ARADA ARTMA AZALMA SADECE TEK BİR YERDE OLMALI .
#♣KISACA ARTMA İŞELMİ VE SONRASINDA AZALMA İŞLEMİ OLAN DİZİYİ BULUR 

def validMountainArray(arr):
    if(len(arr)<3):
        return False
    
    # Arrayin yükselen kısmının bittiği noktayı bulalım..
    i = 1
    while(i<len(arr) and arr[i]>arr[i-1]):
        i+=1
 
    #  Dizinin sonuna geldiysek sadece yükselme işlemi var alçalan kısım yok False döndür..        
    if(i==1 or i==len(arr)):
        return False
        
    # Arrayin azalan kismina bakalım nereye kadar azalma olacak
    while(i<len(arr) and arr[i]<arr[i-1]):
        i+=1
        
    # Eğer alçalan kısmın bitişi dizinin sonu ise bu bir Mountain Array'dir..
    # Aksi takdirde tekrar bir yükselme veya eşitlik olacaktır ki Mountain Array tanımına 
    # uymaz...
    if (i==len(arr)):
        return True
    else:
        return False
 
 
lst = [0,4,2,1]     
print(validMountainArray(lst))    

      