# Bölüm 3: Web Formları

Kullanıcı girişleri için form yönetimi ve doğrulaması Flask-WTF eklentisi kullanılarak gerçekleştirilir.

## Özet
*   **Flask-WTF:** WTForms kütüphanesini Flask ile entegre eder. Form sınıfları tanımlayarak HTML formlarını kolayca yönetmeyi sağlar.
*   **Güvenlik (CSRF):** Formların güvenliği için `config.py` içinde `SECRET_KEY` tanımlanmalı ve her formda `{{ form.hidden_tag() }}` kullanılmalıdır.
*   **Alanlar ve Doğrulamalar:** `StringField`, `PasswordField`, `BooleanField` ve `SubmitField` gibi alanlar ile `DataRequired` gibi doğrulayıcılar (validators) kullanılır.
*   **validate_on_submit():** Formun gönderilip gönderilmediğini ve geçerli olup olmadığını kontrol eden temel fonksiyondur.
*   **Flash Mesajları:** `flash()` fonksiyonu ile kullanıcıya işlem sonucu (başarı, hata vb.) hakkında kısa bildirimler gösterilir.
*   **Yönlendirme:** `url_for()` fonksiyonu ile rotalar arası güvenli geçiş ve `redirect()` ile sayfa yönlendirmesi yapılır.

---
**Kaynak:** [Notion - Bölüm 3](https://www.notion.so/3-B-l-m-3314dab0fd2380cb8bf3c45d995e5799)
