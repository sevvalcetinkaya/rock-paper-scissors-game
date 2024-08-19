import random

def tas_kagit_makas_SEVVAL_CETINKAYA():
    print("Taş, Kağıt, Makas oyununa hoş geldiniz!")
    print("Oyun kuralları: Taş makası yener, makas kağıdı yener, kağıt taşı yener.")
    print("İlk iki turu kazanan oyunun galibi olur.")
    print("Oyundan çıkmak için 'x' tuşuna basabilirsiniz.\n")
    choices = ['taş', 'kağıt', 'makas']
    oyun_sayisi = 0
    while True:
        oyuncu_galibiyetleri = 0
        bilgisayar_galibiyetleri = 0
        oyun_sayisi += 1
        print(f"\n{oyun_sayisi}. oyun başladı!")
        while True:
            tur_sayisi = 0
            while oyuncu_galibiyetleri < 2 and bilgisayar_galibiyetleri < 2:
                tur_sayisi += 1
                oyuncu_secimi = input("Taş, Kağıt, Makas? (Çıkmak için 'x' tuşuna basın): ").lower()
                if oyuncu_secimi == 'x':
                    print("Oyundan çıktınız. Teşekkürler!")
                    return

                if oyuncu_secimi not in choices:
                    print("Geçersiz bir seçenek girdiniz, lütfen tekrar deneyin.")
                    continue

                bilgisayar_secimi = random.choice(choices)
                print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")
                if oyuncu_secimi == bilgisayar_secimi:
                    print("Berabere!")
                elif (oyuncu_secimi == 'taş' and bilgisayar_secimi == 'makas') or \
                     (oyuncu_secimi == 'makas' and bilgisayar_secimi == 'kağıt') or \
                     (oyuncu_secimi == 'kağıt' and bilgisayar_secimi == 'taş'):
                    print("Turun galibi: Siz!")
                    oyuncu_galibiyetleri += 1
                else:
                    print("Turun galibi: Bilgisayar!")
                    bilgisayar_galibiyetleri += 1

                print(f"Skor -> Siz: {oyuncu_galibiyetleri}, Bilgisayar: {bilgisayar_galibiyetleri}")
            if oyuncu_galibiyetleri == 2:
                print("Tebrikler! Oyunu kazandınız!")
            else:
                print("Bilgisayar oyunu kazandı!")

            devam = input("Başka bir oyun oynamak ister misiniz? (evet/hayır): ").lower()
            if devam != 'evet':
                print("Oyunu bitirdiniz. Teşekkürler!")
                return

            bilgisayar_devam = random.choice(['evet', 'hayır'])
            print(f"Bilgisayar oyuna devam etmek istiyor mu? {bilgisayar_devam.capitalize()}")
            if bilgisayar_devam == 'hayır':
                print("Bilgisayar oyundan çıkmak istedi. Oyun sona erdi.")
                return
            break
tas_kagit_makas_SEVVAL_CETINKAYA()