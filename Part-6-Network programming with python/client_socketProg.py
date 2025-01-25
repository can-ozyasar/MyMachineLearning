
#TCP SOCKET 
# 
# # client socketin amacı server ile client arasında veri alışverişi yapmaktır.

import socket
#socket nesnesi oluşturulur.
client_socket = socket.socket()

#server ile bağlantı kurulur.bağlanılacak serverın ip adresi ve port numarası girilir.
#biz localhost ve 50000 portunu girdik.kendi bilgisayarımızı server olarak kabul ettik.hemde client olarak.
client_socket.connect(("localhost", 50000))

#mesajlar oluşturulur.
mesaj = "Merhaba ben client"
cikis_mesaj = "exit"

#mesajlar byte türüne çevrilir.
#servera mesaj gönderilir.

client_socket.send(bytes(mesaj, encoding="utf-8"))


#exit mesajı gönderilince serverde yaptığımız while döngüsü sayesinde serverdan çıkış yaparız.
#
# client_socket.send(bytes(cikis_mesaj, encoding="utf-8"))


client_socket.close()


