import cv2
import numpy as np

def count_rice_grains(image_path):
    
    img = cv2.imread(image_path)

   
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    
    blurred = cv2.GaussianBlur(gray, (15, 15), 0)  # Gürültüyü azaltmak için Gaussian Blur uygula

    
    _, thresh = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY)  # Eşikleme uygula

    # Morfolojik işlemleri uygula (istenmeyen arka planları temizle)
    kernel = np.ones((5, 5), np.uint8)
    closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    # Etiketleme işlemi yaparak nesneleri ayır
    _, labels, stats, _ = cv2.connectedComponentsWithStats(closing, connectivity=8)

    # İlk etiket istenmeyen arka plan olduğu için onu atla
    stats = stats[1:]

    # Pirinç tanesi sayısı
    rice_count = len(stats)

    # Sonuçları ekrana yazdır
    print(f"Pirinç Sayısı: {rice_count}")

    # Görüntüdeki pirinçleri dikdörtgenlerle çiz
    for stat in stats:
        x, y, w, h, area = stat
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Görüntüleri göster
    cv2.imshow('Original Image', img)
    cv2.imshow('Thresholded Image', thresh)
    cv2.imshow('Cleaned Image', closing)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Resim dosyasının yolunu belirtin
image_path = "path/to/your/image.jpg"

# Fonksiyonu çağırarak pirinç sayısını ve görüntüyü işleyin
count_rice_grains(image_path)