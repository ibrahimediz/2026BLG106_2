# Bölüm 4: Veritabanı (Database)

Veri saklama işlemleri için Flask-SQLAlchemy ve veritabanı migrasyonları (Flask-Migrate) kullanımı işlenmektedir.

## Özet
*   **Flask-SQLAlchemy:** Flask ile bir veri tabanı (genellikle SQLite) üzerinde işlem yapmayı kolaylaştıran bir ORM'dir (Object Relational Mapper).
*   **Modeller:** Python class'ları ile tablo yapısı tanımlanır. Örneğin: `User` (Kullanıcı) ve `Post` (Gönderi) modelleri.
*   **İlişkiler (Relationships):** Tablolar arası `one-to-many` (bire-çok) ilişkiler modeller üzerinde `db.Relationship` ile kurulur.
*   **Flask-Migrate:** Veritabanı şemasındaki değişikliklerin (yeni tablo, yeni sütun vb.) takibi için kullanılır:
    *   `flask db init` (başlangıç)
    *   `flask db migrate` (değişiklikleri şablonlaştır)
    *   `flask db upgrade` (değişiklikleri veritabanına uygula)
*   **Flask Shell:** Python terminalinden veritabanı sorguları (`sa.select`, `db.session.add`, `db.session.commit`) yapılabilir.

---
**Kaynak:** [Notion - Bölüm 4](https://www.notion.so/4-B-l-m-3314dab0fd23801cbf33d4908e75b92c)
