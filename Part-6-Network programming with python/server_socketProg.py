# bilgisayarda toplamda 65535 port vardır. Bu portlar 0-65535 arasında numaralandırılır.
# Port numarası 0-1023 arasında ise bu portlar özel portlardır ve genellikle sistem tarafından kullanılır.
# 49152-65535 arası portlar ise dinamik portlardır ve kullanılabilir.
#0-1024 arası portlar kullanmayız çünkü bu portlar sistem tarafından kullanılır ve bu portları kullanırsak sistemde hata oluşabilir.



# udp ve tcp protokolleri vardır. udp protokolü hızlıdır ve veri kaybı olabilir. 
# tcp protokolü ise veri kaybı olmaz ve veri doğrulaması yapar.
# örnek olarak udp protokolü dns sorgularında kullanılır. tcp protokolü ise web sayfalarında kullanılır.


#
# TCP SERVER
# 

 
import socket
#socket nesnesi oluşturulur.
server_socket = socket.socket()

server_socket.bind(("localhost", 50000))

#5 taneye kadar client bağlantısı kabul edilir.
server_socket.listen(5)

print("Server is waiting for client to connect")

#server hep çalışır ve client bağlantısı bekler.sonsuz döngü oluşturulur.
while True:
    #client bağlantısı geldiğinde accept() fonksiyonu ile bağlantı kabul edilir.
    client_socket, addres = server_socket.accept()
    print("Connection from:", addres)
   
    #client ile bağlantı kurulduktan sonra recv() fonksiyonu ile client tarafından gönderilen veri alınır. 
    #gelen mesaj max 1024 byte olabilir.biz 1024 byte olarak belirledik.
    #decode() fonksiyonu ile byte olan veriyi stringe çeviririz
    gelen_veri = client_socket.recv(1024).decode()
    print("Client:", gelen_veri)

    #client kapatıldı ama server hala çalışıyor.whike döngüsü sayesinde sürekli client bağlantısı bekler.
    client_socket.close()

#while döngüsünde server sürekli çalışır ve client bağlantısı bekler.
#while döngüsü programımızın takılıp kalmaması için client den exit mesajı geldiğinde çıkıyoruz ve server artık 50000 portundan dinlemeyi bırakıyor.
#bu kısım önemli çünkü bu kısmı yapmazssak 50000 portundan sürekli dinleme yapmaya devam eder ve programımız kapanmaz.

    if gelen_veri == "exit":
        break

    print("hoşçakalın \n")
    server_socket.close()