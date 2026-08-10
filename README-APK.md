# EICAR Test APK

## Açık Kaynak Kodlu Antivirüs Test Uygulaması

Bu uygulama, mobil antivirüs yazılımlarının çalışıp çalışmadığını test etmek için tasarlanmıştır.

## Ne Yapar?

1. Depolama izni ister
2. İzin verilirse Downloads klasörüne 3 dosya oluşturur:
   - eicar.txt
   - eicar.com
   - eicar.zip (içinde eicar.txt)
3. Hiçbir verinize veya sistem dosyanıza dokunmaz
4. Tamamen açık kaynak kodludur

## Güvenlik

- Kaynak kodları tamamen açıktır
- Verilerinize erişmez
- Sadece Downloads klasörüne yazar
- Data/OBB klasörlerine dokunmaz

## Neden Kullanmalısınız?

- Antivirüsünüzün çalışıp çalışmadığını test edin
- Güvenlik yazılımlarının nasıl çalıştığını öğrenin
- Tamamen zararsızdır

## İzinler

- WRITE_EXTERNAL_STORAGE: Downloads klasörüne dosya yazmak için

## Derleme

GitHub Actions ile otomatik derlenir veya Android Studio ile manuel derlenebilir.

## Lisans

Eğitim amaçlıdır. Sorumluluk kullanıcıya aittir.

__________________________________________

Android/APK/
├── app/
│   ├── src/
│   │   └── main/
│   │       ├── AndroidManifest.xml
│   │       ├── java/com/eicar/test/
│   │       │   └── MainActivity.java
│   │       └── res/
│   │           ├── layout/
│   │           │   └── activity_main.xml
│   │           └── values/
│   │               └── strings.xml
│   ├── build.gradle
│   ├── settings.gradle
│   └── gradle.properties
└── README-APK.md (açıklama dosyası)
