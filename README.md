# rock-paper-scissors-game
 Rock paper scissors game written in Python.
 
Oyunun genel hattı:
Karşılama Mesajı: Oyun başlatıldığında kullanıcıya kurallar açıklanır.
Seçenek Listesi: 'taş', 'kağıt', 'makas' seçimleri mevcuttur.
Ana Döngü: Oyun, kullanıcı ya da bilgisayar iki tur kazanana kadar devam eder.
Seçim Alınması: Kullanıcıdan geçerli bir seçim alındıktan sonra bilgisayar rastgele bir seçim yapar.
Kazanan Belirlenmesi: Her turda kazanan belirlenir ve skor güncellenir.
Oyunun Devamı: Oyunun sonunda kullanıcıya ve bilgisayara oyuna devam etmek isteyip istemedikleri sorulur.

"Taş, Kağıt, Makas" oyunu Python kullanarak geliştirilen basit bir oyun uygulamasıdır. Uygulama, kullanıcı ile bilgisayar arasında bir karşılaşma simüle eder ve temel Python kavramlarını (döngüler, koşullu ifadeler, kullanıcı girişi gibi) pekiştirmek için tasarlanmıştır.
random modülü, bilgisayarın taş, kağıt, makas seçeneklerinden birini rastgele seçmesi için kullanılır.
Fonksiyon, oyunun ana mantığını kapsar ve tas_kagit_makas_SEVVAL_CETINKAYA() şeklinde çağrılabilir.
Kullanıcıya oyunun kuralları ve nasıl oynanacağı hakkında bilgi veren bir mesaj görüntülenir.
Oyun için kullanılacak seçenekler ('taş', 'kağıt', 'makas') bir liste olarak tanımlanır. oyun_sayisi ile kaç oyun oynandığı sayılır.
Ana döngü, kullanıcı oyundan çıkana kadar devam eder. Her oyunda oyuncu_galibiyetleri ve bilgisayar_galibiyetleri sıfırlanır. Oyun sayısı artırılır ve yeni bir oyunun başladığı ekrana yazdırılır.
İkinci bir döngü, oyuncu ya da bilgisayar iki tur kazanana kadar devam eder. Bu döngüde her turda bir seçim yapılır.
Kullanıcıdan geçerli bir seçim yapılması istenir. Eğer kullanıcı "x" tuşuna basarsa, oyun sonlandırılır. Kullanıcı geçersiz bir seçim yaparsa tekrar seçim yapması istenir. Bilgisayar, random.choice(choices) ile rastgele bir seçim yapar ve bu seçim ekrana yazdırılır.
Kullanıcının ve bilgisayarın seçimleri karşılaştırılır. Kazanan belirlenir ve ilgili galibiyet sayacı artırılır. O turdaki skor ekrana yazdırılır.
İki galibiyet alan taraf oyunu kazanır ve bu sonuç ekrana yazdırılır. Kullanıcıya yeni bir oyun oynamak isteyip istemediği sorulur. Eğer kullanıcı veya bilgisayar oyuna devam etmek istemezse oyun sona erer.

Bu kod, kullanıcının taş, kağıt, makas oynayabileceği bir terminal uygulamasıdır. Oyunu kullanıcı kazandığında veya bilgisayar kazandığında sonuç ekrana yazdırılır ve yeni bir oyun oynanıp oynanmayacağı sorulur. 
