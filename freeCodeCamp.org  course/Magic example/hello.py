import tensorflow as tf

# İki sabit tanımla
a = tf.constant(5)
b = tf.constant(3)

# Toplama işlemi
c = a + b

# Sonucu yazdır
print("Toplam:", c.numpy())  # .numpy() ile sonucu alıyoruz
