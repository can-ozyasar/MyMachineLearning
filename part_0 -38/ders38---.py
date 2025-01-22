# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 22:00:10 2024

@author: canoz
"""



       # REGEX MODULÜ  DESEN EŞLEŞTİRME 
       
       
import re
"""


cumle = " Guido van Rossum , 1980'lerin sonlarında ABC programlama dilinin halefi olarak Python üzerinde çalışmaya başladı ve ilk olarak 1991'de Python 0.9.0 olarak yayınladı. [ 35 ] Python 2.0, 2000 yılında yayınlandı. 2008'de yayınlanan Python 3.0, önceki sürümlerle tamamen geriye dönük uyumlu olmayan büyük bir revizyondu . 2020'de yayınlanan Python 2.7.18, Python 2'nin son sürümüydü. [ 36 ]"
      
pattern ="Python"

#isteneni ilk bulduğu yeri yazar durur
print( re.search(pattern, cumle) )
sonuc=re.search(pattern, cumle)
print("başlangıç indis : ",sonuc.start()," son indis : ",sonuc.end(),"\n \n")

count=0;
for bulunan in re.finditer(pattern, cumle):
    print(bulunan.span(),bulunan.group(),"\n") # metinde bulduğu tüm pythonları yazar .
    count+=1
    
print("Python kelimesi metinde toplam  :",count," adet var \n")





cumle2 ="merhaba benim cep numaram 532-1112233 beni öğleden sonra arayabilirsiniz 532-1178243 "
"
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
    
     """   
     
  #► proglamlama SINAV 
        
  
    
  
    
  #SORU 1 :  YARIÇAP DAN ALAN VE ÇEVRE HESAPLAMA 10 P 
  
  
  
import math 
"""
 
yari_cap = int(input("lutfen yaricap giriniz : "))
  

print("alan : ",math.pi*yari_cap*yari_cap ,"cevre : ", math.pi*yari_cap*2)


cumle=" yarıçap dan alan ve çevre hesaplama 10 p "
print(cumle.upper())
   
      """
        
      
        
      # SORU 2 ÖĞRENCİ NO AYIRMA MANTIKLI YAZMA ANLAMIYLA 
        
"""
ogrenci_No = int(input("lutfen ogrenci no giriniz : "))





for rakamlar in ogrenci_No:
    rakamlar

print("giriş yili : ","fakulte no : ","bolum no" ,"ogrenim no :" , "ogrenci no  :" )

      """
        
      
        
   #$$ SORU 3  5 İN KATLARINI EKRANA YAZDIRAN PROGRAM 
      
"""      
liste=[5,4,6,8,15,7,65,48,40,41,25,20,23,10]    

for index in liste:
    if(index%5==0):
        print(index)
        
    index+=1
        
"""    

# SORU 4 TAMSAYI DİZİSİ OLSUN İÇİNDEKİ 0 ELEMANLARI DİZİNİNİ EN SONUDA OLSUN 



moveZeroes=[5,0,4,6,8,15,7,0,65,48,40,0,41,25,0,20,23,0,10]

j=len(moveZeroes) # eleman sayisi
i=0


for sayilar in moveZeroes:
    
    if(sayilar!=0):
        moveZeroes[i]=sayilar
        i+=1

for x in range(i,j):
    moveZeroes[x]=0


print(moveZeroes)
print(len(moveZeroes))
    
        
      