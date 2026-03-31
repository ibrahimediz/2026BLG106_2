# Bölüm 5: Kullanıcı Giriş Sistemi

Kullanıcı oturum yönetimi ve kayıt özellikleri Flask-Login eklentisi kullanılarak anlatılmaktadır.

## Özet
*   **Şifre Güvenliği:** Şifreler veritabanına asla düz metin olarak kaydedilmez. `Werkzeug` kütüphanesi (`generate_password_hash`, `check_password_hash`) ile hash'lenir.
*   **Flask-Login:** Kullanıcı oturumlarını (sessions) yönetmek için kullanılır.
    *   `UserMixin`: Login özellikleri için model sınıfına eklenir.
    *   `login_user()`, `logout_user()`: Oturum açıp kapama işlemleri.
    *   `current_user`: Giriş yapmış kullanıcıya her yerden erişim sağlar.
*   **Erişim Kısıtlama:** `@login_required` dekoratörü ile sadece giriş yapmış kullanıcıların görebileceği sayfalar belirlenir.
*   **Giriş ve Kayıt Formları:** `LoginForm` ve `RegistrationForm` ile kullanıcı etkileşimi yönetilir. 
*   **Özel Doğrulayıcılar:** Kayıt sırasında e-posta veya kullanıcı adı çakışmalarını önlemek için modellerde özel validasyon metodları tanımlanır.

---
**Kaynak:** [Notion - Bölüm 5](https://www.notion.so/5-B-l-m-3314dab0fd2380a68f1ecea3f30f2da4)
