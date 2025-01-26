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


#program bitişinde bağlantı kapatılmaalıdır .
if (sqlite_connection):
    sqlite_connection.close()
    print("The SQLite connection is closed...")