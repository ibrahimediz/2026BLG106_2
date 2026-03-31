# Bölüm 1: Giriş ve Kurulum

Bu bölümde Python ve Flask kurulumu, sanal ortam (virtual environment) oluşturma ve ilk "Hello, World!" uygulamasının yapılandırılması anlatılmaktadır.

## Özet
*   **Python Kurulumu:** Python'un sistemde yüklü olduğundan emin olun ve `python --version` ile kontrol edin.
*   **Sanal Ortam (venv):** Projeye özel bağımlılıkları yönetmek için `python -m venv venv` ile izole bir çalışma alanı oluşturun.
*   **Flask Kurulumu:** Sanal ortamı aktif ettikten sonra `pip install flask` komutuyla Flask'ı kurun.
*   **Uygulama Yapısı:** 
    *   `app/` klasörü içinde çekirdek uygulama mantığı.
    *   `__init__.py` ile Flask instance'ının oluşturulması.
    *   `routes.py` ile URL yönlendirmelerinin tanımlanması.
*   **Çalıştırma:** `flask run` komutuyla sunucuyu başlatın. Ortam değişkenlerini yönetmek için `.flaskenv` dosyasını kullanabilirsiniz.

---
**Kaynak:** [Notion - Bölüm 1](https://www.notion.so/1-B-l-m-3314dab0fd238040907fc45ed0149682)
