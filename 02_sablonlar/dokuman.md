# Bölüm 2: Şablonlar (Templates)

Flask uygulamalarında HTML içeriğini Python kodundan ayırmak için Jinja2 şablon motorunun kullanımı ele alınmaktadır.

## Özet
*   **render_template():** Flask'ın bu fonksiyonu ile HTML dosyalarını tarayıcıya döndürebilirsiniz. Dosyalar varsayılan olarak `templates/` klasöründe aranır.
*   **Değişkenler:** Jinja2 sözdizimi olan `{{ ... }}` ile Python'dan şablona veri aktarımı yapabilirsiniz.
*   **Kontrol Yapıları:** Şablonlar içinde `{% if ... %}` (koşullu durumlar) ve `{% for ... %}` (döngüler) gibi mantıksal yapılar kurabilirsiniz.
*   **Şablon Kalıtımı (Inheritance):** 
    *   **base.html:** Uygulamanın ortak iskeletini (navbar, footer vb.) oluşturur.
    *   **block:** Alt şablonların içerik ekleyebileceği alanları tanımlar.
    *   **extends:** Alt şablonun `base.html`'i miras aldığını belirtir.

---
**Kaynak:** [Notion - Bölüm 2](https://www.notion.so/2-B-l-m-3314dab0fd2380ecb4a9c245a9f847c3)
