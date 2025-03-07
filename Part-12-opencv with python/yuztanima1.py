import cv2
print("başlatıldı") 

# Yüz tanıma için gerekli Haarcascade xml dosyası 
cizimxml = "haarcascade_frontalface_default.xml"
yuzCascadeClassifier = cv2.CascadeClassifier(cizimxml)

# Kamerayı açıyoruz (doğru indeksi seçtiğinden emin ol)
video_capture = cv2.VideoCapture(0)

# Kameranın açılıp açılmadığını kontrol et
if not video_capture.isOpened():
    print("Kamera açılamadı.")
    exit()

# Sonsuz loop
while True:
    ret, frame = video_capture.read()

    # Kameradan frame alınamadıysa devam etme
    if not ret:
        print("Frame alınamadı.")
        break
    
    # Gri tonlamaya çevirme
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Yüz tespiti
    faceDetected = yuzCascadeClassifier.detectMultiScale(
        gray,
        minSize=(35, 35)
    )
    
    # Yüzün çerçeve içine alınması
    for (x, y, w, h) in faceDetected:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, "Face Detected", (x+50 , y+120 ), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 1)

    # Frame gösterimi
    cv2.imshow('Python Yüz Tanıma - Image Processing', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# çıkışta bağladığımız kaynakları serbest bırakıyoruz
video_capture.release()
cv2.destroyAllWindows()
