# İnternet Programcılığı Ders Planı (Syllabus)

Bu döküman, 12 haftalık programlama ve web geliştirme dersinin detaylı müfredatını içerir. Program, hiç bilmeyenler için Python temellerinden başlayarak, Flask ile modern web uygulamaları geliştirmeye, veritabanı bağlantısına ve projenin canlıya alınmasına (Deployment) kadar uzanır.

## Ders Bilgileri
- **Ders Adı:** İnternet Programcılığı
- **Süre:** 12 Hafta
- **Amaç:** Öğrencilere algoritmik düşünme yetisi kazandırmak ve Python/Flask kullanarak uçtan uca web projeleri geliştirmeyi öğretmek.

---

## HAFTALIK PROGRAM

### 1. Hafta: Programlamaya Giriş ve Temeller
**Klasör:** `Ders_01`
- Programlama nedir? Neden Python?
- Python Kurulumu ve Geliştirme Ortamı (IDE)
- **Değişkenler ve Veri Tipleri**:
  - Temel Tipler: `int`, `float`, `str`, `bool`
  - **İleri Tipler (Giriş)**: `list`, `tuple`, `set`, `dict`
- Temel Giriş/Çıkış İşlemleri (`print`, `input`)

### 2. Hafta: Karar Yapıları (Koşullar)
**Klasör:** `Ders_02`
- Algoritma Mantığı: Akış diyagramları
- Karşılaştırma Operatörleri (`==`, `!=`, `>`, `<`)
- Mantıksal Operatörler (`and`, `or`, `not`)
- `if`, `elif`, `else` blokları ile karar verme mekanizmaları
- Örnek: Ehliyet kontrolü, Not hesaplama

### 3. Hafta: Döngüler (Loops)
**Klasör:** `Ders_03`
- Döngü mantığı ve kullanım alanları
- `for` döngüsü: Belirli bir aralıkta veya liste üzerinde gezinme
- `while` döngüsü: Koşula bağlı tekrar
- `range()` fonksiyonu
- Döngü kontrol ifadeleri: `break`, `continue`
- Örnek: Sayı tahmin oyunu

### 4. Hafta: Veri Yapıları (Detaylı)
**Klasör:** `Ders_04`
- **Listeler (Lists)**: Ekleme, silme, sıralama, dilimleme (slicing)
- **Sözlükler (Dictionaries)**: Anahtar-Değer ilişkisi, JSON benzeri yapı, `get`, `items`, `update` metotları
- **Demetler (Tuples)**: Değiştirilemez (Immutable) listeler
- **Kümeler (Sets)**: Eşsiz elemanlar ve küme işlemleri (Birleşim, Kesişim)
- Örnek: Alışveriş listesi uygulaması

### 5. Hafta: Fonksiyonlar (Metotlar)
**Klasör:** `Ders_05`
- Fonksiyon tanımlama (`def`) ve çağırma
- Parametreler ve Argümanlar
- `return` ifadesi ve değer döndürme
- Varsayılan parametreler
- Yerel ve Global değişken kapsamı (Scope)
- Örnek: Hesap makinesi

### 6. Hafta: Modüller ve Dosya İşlemleri
**Klasör:** `Ders_06`
- Modül kavramı: Kodları parçalara bölme
- Hazır modüller: `math`, `random`, `os`, `datetime`
- Kendi modülünü yazma ve çağırma (`import`)
- **Dosya I/O**:
  - Dosya oluşturma ve yazma (`w`, `a` modları)
  - Dosya okuma (`r` modu)
  - `with open(...)` bloğu ile güvenli dosya işlemleri

---

### 7. Hafta: Web Geliştirmeye Giriş ve Flask
**Klasör:** `Ders_07`
- Web nasıl çalışır? (Client-Server, HTTP Request/Response)
- HTML ve CSS'e Hızlandırılmış Bakış
- **Flask Çatısı**:
  - Flask kurulumu ve Sanal Ortamlar (venv)
  - İlk "Merhaba Dünya" uygulaması
  - **Routing (Rotalama)** Detayları:
    - Statik ve Dinamik URL'ler (`<id>`)
    - URL Parametre Tipleri (`int`, `float`, `string`)
    - HTTP Metodları (`GET`, `POST`)

### 8. Hafta: Şablonlar ve Form İşlemleri
**Klasör:** `Ders_08`
- **Jinja2 Şablon Motoru**:
  - Python verilerini HTML'e gönderme (`{{ degisken }}`)
  - HTML içinde döngüler (`{% for %}`) ve koşullar (`{% if %}`)
- **Formlar**:
  - HTML Form yapısı
  - Kullanıcıdan veri alma (`request.form`)
  - GET ve POST isteklerini işleme

### 9. Hafta: Veritabanı ve Konteynerizasyon (Docker)
**Klasör:** `Ders_09`
- Veritabanı nedir? İlişkisel Veritabanları (RDBMS)
- **Docker**:
  - Konteyner mantığı nedir?
  - `docker-compose` ile PostgreSQL veritabanı ayağa kaldırma
- SQL Temelleri ve Python ile veritabanı bağlantısı (`psycopg2`)

### 10. Hafta: ORM ile Veritabanı Yönetimi
**Klasör:** `Ders_10`
- **ORM (Object Relational Mapping)** Nedir?
- **Flask-SQLAlchemy**:
  - Veritabanı modellerini (Tabloları) Python sınıfı (Class) olarak tasarlama
  - Veritabanı bağlantı konfigürasyonu
- **CRUD İşlemleri**:
  - Veri Ekleme (Create)
  - Veri Listeleme/Okuma (Read)
  - Veri Güncelleme (Update) - *Opsiyonel*
  - Veri Silme (Delete)

### 11. Hafta: REST API Geliştirme
**Klasör:** `Ders_11`
- **API** Kavramı ve Kullanım Alanları
- **REST Mimarisi**: Kaynaklar ve Standartlar
- JSON Veri Formatı
- Flask ile JSON cevap döndürme (`jsonify`)
- API Uç Noktaları (Endpoints) yazma
- Postman ile API testi

### 12. Hafta: Projeyi Canlıya Alma (Deployment)
**Klasör:** `Ders_12`
- Geliştirme (Development) vs Prodüksiyon (Production) ortam farkları
- **WSGI Sunucusu**: `Gunicorn` kullanımı ve konfigürasyonu
- Bulut Platformları (Örn: Render, Railway, Heroku) mantığı
- Gerekli Dosyalar: `requirements.txt`, `Procfile`
- Ortam Değişkenleri (Environment Variables) güvenliği

---
*Bu müfredat, internet programcılığına giriş seviyesindeki öğrenciler için hazırlanmıştır.*
