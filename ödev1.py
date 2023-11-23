# Uygulama içerisinde kullanacağımız kütüphaneleri import ediyoruz

import matplotlib.pyplot as plt
import cv2 as cv
import numpy as nmp
import numpy as np

# Histogramını hesaplamak istediğimiz resmi okuyoruz

resim = cv.imread('sincap.jpg')

# Okunan resim dosyasının yükseklik ve genişlik değerlerini bir diziye atıyoruz

yukseklik = resim.shape[0]
genişlik = resim.shape[1]

# Belilenen değer boyutunda 0 matrisi oluşturuyoruz.
histogam = np.zeros([256],np.int32)

# For döngüsü yardımıyla tüm hücreleri tek tek gezerek
# renk yoğunlıuklarını kaydediyoruz
for i in range(yukseklik):
    for j in range(genişlik):
        histogam[resim[i,j]] += 1

# Grafiğimizi ekrana çizdiriyoruz
plt.plot(histogam)
# Grafik başlığı
plt.title("Histogram Çizimi")
plt.show()