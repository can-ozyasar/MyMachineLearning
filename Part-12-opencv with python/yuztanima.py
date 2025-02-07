import cv2

# Yüz tanıma için gerekli Haarcascade xml dosyası 
cizimxml = "haarcascade_frontalface_default.xml"
yuzCascadeClassifier = cv2.CascadeClassifier(cizimxml)

# Python kodunuzu çalıştırmadan önce mutlaka çalışır bir webcam pc'nize bağlamanız gerekiyor..
video_capture = cv2.VideoCapture(0)

# sonsuz Loop içinde videoda yakalanan tüm frame'ler işleniyor
# Loop tan çıkmak için q tuşuna basın..
while True:    
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # detectMultiScale bize eger frame içinde bir yuz varsa onu tespit edip
    # yuzun ozelliklerini barındıran bir tuple tipinde sonuc dönüyor 
    # Parametrelerin detayı için link:
    # https://docs.opencv.org/3.4/d1/de5/classcv_1_1CascadeClassifier.html#aaf8181cb63968136476ec4204ffca498
    faceDetected = yuzCascadeClassifier.detectMultiScale(
        gray,         
        minSize=(35, 35)
    )
    
    #print(type(faceDetected))

    # Yüzün çerçeve içine alınması
    for (x, y, w, h) in faceDetected:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, "Face Detected", (x+50 , y+120 ), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 1)

    # Başlık yazalım
    cv2.imshow('Python Yüz Tanıma - Image Processing', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# çıkışta bağladığımız kaynakları serbest bırakıyoruz (kamera ve açık pencereler varsa bağlantılar kapatılır)
video_capture.release()
cv2.destroyAllWindows()