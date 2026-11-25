# İltisak Çalışması Haritası

GitHub Pages üzerinde yayınlanmaya hazır statik harita arayüzü.

## Dosyalar

- `index.html`: Yayınlanacak tek sayfa harita uygulaması.
- `.nojekyll`: GitHub Pages'in dosyaları değiştirmeden servis etmesi için.
- `.gitignore`: Yerel üretim scriptlerini ve geçici dosyaları repoya almamak için.

## GitHub Pages ile yayınlama

1. Bu klasörü yeni bir GitHub reposuna yükleyin.
2. GitHub'da repo sayfasında `Settings > Pages` bölümüne girin.
3. `Build and deployment` altında `Deploy from a branch` seçin.
4. Branch olarak `main`, klasör olarak `/root` seçin.
5. Kaydettikten sonra birkaç dakika içinde Pages linki oluşur.

## Not

Harita verisi `index.html` içine gömülüdür. Bu yüzden deploy için ekstra veri dosyası gerekmez.
