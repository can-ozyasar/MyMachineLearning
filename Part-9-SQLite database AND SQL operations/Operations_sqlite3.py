import sqlite3
from sqlite3 import Error




# daha sonra oluşturacağımız tabloları oluşturmak için bir bağlantı oluşturuyoruz.
#bir connection oluştururan bir metod yazıyoruz.
def connection_olustur(db_File):
    con=None
    try:
        con= sqlite3.connect(db_File)
        print("conexion is successful")
    except Error as e:
        print("eror : ",e)
    return con


# veritabanı bağlantısını oluşturuyoruz veritabanı da oluşur
sqlite_connection = connection_olustur("kutuphane.db")


#oluşan .db uzantılı dosyayı DBBROVSER ile açıp kontrol edebiliriz.

# eğr veritabanı bağlantısı oluşturulduysa bu durumda bir hata mesajı vermek gerekir kullanıcıya 
#programdan çıkış yapılmalıdır.

# hata oluşursa aşağıdaki kodlar çalışır.
if (sqlite_connection==None):
    print("The SQLite connection is closed...")
    exit()



# TABLO OLUŞTURMA

cursor =sqlite_connection.cursor()

# tablo oluşturmak için bir cursor oluşturuyoruz.
def tablo_olustur(curs):
   try:
       curs.execute("CREATE TABLE IF NOT EXISTS kitaplar (kitapAdi TEXT, Yazar TEXT, kitapno INT, SayfaSayisi INT)")
   except Error as e:
       print("Error : ",e)



tablo_olustur(cursor)

# COMMİT İŞLEMİ YAPMANIN AMACI VERİTABANINA YAZILAN DEĞERLERİ KAYDETMEKTİR.
# AKSİ HALDE DEĞİŞİKLİKLER VERİTABANINA KAYDEDİLMEZ !!!!!
sqlite_connection.commit()



                        #TABLOYA VERİ EKLEME İŞLEMİ 


cursor.execute("INSERT INTO kitaplar VALUES ('Da Vinci Sifresi','Dan Brown',1000,495)")
sqlite_connection.commit()

cursor.execute("INSERT INTO kitaplar VALUES ('Dune','Frank Herbert ',1001,217)")
sqlite_connection.commit()

cursor.execute("INSERT INTO kitaplar VALUES ('YUZUKLERİN EFENDİSİ','J.R.R Toiken',1003,1027)")
sqlite_connection.commit()






                        # TABLODAN VERİ OKUMA İŞLEMİ VERİ ÇEKME İŞLEMİ

cursor.execute("SELECT * FROM kitaplar")
sqlite_connection.commit()


#çekilen değerlerin saklamak için bir değişken oluşturuyoruz.
cekilen_veriler=cursor.fetchall() #lliste şekilnde

#çekilen verileri ekrana yazdırıyoruz.döngü ile
for veri in cekilen_veriler:
    print(veri)


print("\n**************************************************\n")

    #istenen kayıtların çekilmesi temel sql sorgusu işemleri ile yapılır.
cursor.execute("SELECT * FROM kitaplar WHERE Yazar='Dan Brown'")
sqlite_connection.commit()

cekilen_veriler_istenen=cursor.fetchall() #lliste şekilnde

#çekilen verileri ekrana yazdırıyoruz.döngü ile
for veri in cekilen_veriler_istenen:
    print(veri)




                        #TABLODAN VERİ GÜNCELLEMESİ YAPMA İŞLEMİ

cursor.execute("UPDATE kitaplar SET kitapAdi='Dune' WHERE kitapno=1001")
sqlite_connection.commit()


                        #TABLODAN VERİ SİLME İŞLEMİ
cursor.execute("DELETE FROM kitaplar WHERE kitapno=1003")
sqlite_connection.commit()











#program bitişinde bağlantı kapatılmaalıdır .
if (sqlite_connection):
    sqlite_connection.close()
    print("The SQLite connection is closed...")

























