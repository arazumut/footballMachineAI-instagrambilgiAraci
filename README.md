SkorTahmin Sınıfı: Bir Web Scraping ve Tahmin Uygulaması

Bu makalede, Python kullanarak bir futbol maçının skorlarını tahmin eden bir programın nasıl geliştirileceğini inceleyeceğiz. Program, Selenium ile web scraping yaparak gerekli verileri toplar ve daha sonra bu veriler üzerinde makine öğrenimi algoritmaları kullanarak skor tahminleri yapar.
Giriş

Futbol maçları için skor tahmini, spor analitiği alanında oldukça popüler bir konudur. Bu makalede, belirli bir futbol maçının istatistiksel verilerini bir web sitesinden çekerek, geçmiş maç sonuçlarına dayalı olarak gelecekteki skorları tahmin eden bir Python uygulaması geliştireceğiz.
Gerekli Kütüphanelerin İçe Aktarılması

İlk adım olarak, Selenium, Scikit-Learn, Numpy ve Matplotlib gibi gerekli kütüphaneleri içe aktarıyoruz. Selenium, web scraping için kullanılırken, Scikit-Learn makine öğrenimi algoritmaları için, Numpy veri manipülasyonu için ve Matplotlib grafik çizimi için kullanılacaktır.
SkorTahmin Sınıfı

Bu projede, tüm işlemleri bir sınıf yapısı içinde organize ettik. SkorTahmin sınıfı, veri toplama, işleme ve tahmin yapma işlevlerini içerir.
Tarayıcının Başlatılması ve Veri Toplama

Sınıfın __init__ metodunda, Firefox tarayıcısı başlatılır ve belirtilen URL'deki istatistiksel veriler çekilir. Bu işlem için Selenium kullanılır. Tarayıcıya belirli bir süre beklemesi için time.sleep(5) komutu verilir. Bu süre, sayfanın tam olarak yüklenmesini beklemek içindir.
Tabloların Bulunması ve İşlenmesi

Veriler iki ayrı tabloda toplanır: Ev sahibi takım ve deplasman takımı için. Bu tabloların bulunması ve işlenmesi için tablo_1 ve tablo_2 metodları kullanılır. Bu metodlar, her iki takımın son maçlarının skorlarını çeker ve bu verileri liste olarak saklar.
Skorların Ayrıştırılması

Toplanan veriler işlenir ve skorlar ayrıştırılır. adim1_ ve adim_2 metodları, ev sahibi ve deplasman takımlarının skorlarını belirlemek için kullanılır. Bu metodlar, belirli bir takımın maç sonuçlarını filtreler ve bu sonuçları skor listelerine ekler.
Skor Tahminleri

Lineer regresyon modeli kullanılarak gelecekteki skor tahminleri yapılır. ev_Shabi_tahimi ve deplasman_tahmin metodları, sırasıyla ev sahibi ve deplasman takımlarının gelecekteki gol tahminlerini hesaplar. Bu tahminler, geçmiş maç sonuçlarına dayalı olarak yapılır.
Grafiklerin Çizilmesi

Son olarak, Matplotlib kullanarak verilerin görselleştirilmesi yapılır. grafik_evsahibi_deplasman metodu, ev sahibi ve deplasman takımlarının skorlarını grafikler üzerinde gösterir. Bu grafikler, geçmiş performansların görsel bir temsilini sunar ve tahminlerin doğruluğunu değerlendirmeye yardımcı olur.



![Ekran görüntüsü 2024-05-28 120654](https://github.com/arazumut/footballMachineAI-instagrambilgiAraci/assets/150933483/d9ab9186-8310-43a9-9706-a21b9f5c4696)
![Ekran görüntüsü 2024-05-28 120704](https://github.com/arazumut/footballMachineAI-instagrambilgiAraci/assets/150933483/fcfebb17-28e8-4e42-9461-ce048d40492d)
![Ekran görüntüsü 2024-05-28 120825](https://github.com/arazumut/footballMachineAI-instagrambilgiAraci/assets/150933483/f8d9aaec-2109-4c1c-8456-78e9accdfe64)


<h1>instagram adresinden bilgi çeker. takipçi sayısı,takip sayısı ve post sayısını gösterir.</h1>

![Ekran görüntüsü 2024-04-21 171629](https://github.com/arazumut/footballMachineAI-instagrambilgiAraci/assets/150933483/536553ba-d4f2-4a37-92c7-7ccf3ce3c74d)

