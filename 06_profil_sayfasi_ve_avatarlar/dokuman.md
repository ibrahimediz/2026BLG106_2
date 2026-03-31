# Bölüm 6: Profil Sayfası ve Avatarlar

Kullanıcı profillerinin oluşturulması ve avatar desteği eklenmesi anlatılmaktadır.

## Özet
*   **Profil Sayfası:** Dinamik URL yapısı (`/user/<username>`) kullanılarak her kullanıcı için özel bir profil sayfası oluşturulur.
*   **Avatarlar:** Kullanıcı resimleri için Gravatar servisi kullanılır. E-posta adresinin MD5 hash'i oluşturulur ve Gravatar URL'sine eklenir.
*   **Jinja2 Alt Şablonları:** `_post.html` gibi alt şablonlar (sub-templates) oluşturularak, gönderilerin listelendiği farklı yerlerde (anasayfa, profil sayfası) kod tekrarı önlenir.
*   **Son Görülme (Last Seen):** `@before_request` dekoratörü kullanılarak, kullanıcının her isteğinde veritabanındaki `last_seen` alanı otomatik olarak güncellenir.
*   **Profil Düzenleme:** `EditProfileForm` ile kullanıcıların kullanıcı adı ve "Hakkımda" (about me) bilgilerini güncelleyebilmesi sağlanır.

---
**Kaynak:** [Notion - Bölüm 6](https://www.notion.so/6-B-l-m-3314dab0fd2380fc839ac6c0dbe66865)
