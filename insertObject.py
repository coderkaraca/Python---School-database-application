import mysql.connector
from datetime import datetime


class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        # Veritabanına bağlanmak için bir bağlantı nesnesi oluşturur
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        # Bağlantı nesnesinden bir imleç nesnesi oluşturur
        self.cursor = self.connection.cursor()

    def close(self):
        # Bağlantıyı kapatır
        self.connection.close()

    def insert(self, sql, values):
        # Veritabanına kayıt eklemek için SQL sorgusunu çalıştırır
        self.cursor.executemany(sql, values)
        # Değişiklikleri kaydeder
        self.connection.commit()
        # Eklenen kayıt sayısını döndürür
        return self.cursor.rowcount


# Database sınıfından bir örnek oluşturur
db = Database(host="localhost", user="root",
              password="passww*", database="schooldb")
# Veritabanına bağlanır
db.connect()
# SQL sorgusunu ve değerleri tanımlar
sql = "INSERT INTO Student (StudentNumber, Name, Surname, Birthdate, Gender) VALUES(%s,%s,%s,%s,%s)"
ogrenciler = [
    ("101", "Ahmet", "AA", datetime(2000, 5, 17), "E"),
    ("102", "Mehmet", "BB", datetime(2002, 2, 12), "E"),
    ("103", "Yavuz", "CC", datetime(2001, 7, 23), "E"),
    ("104", "Zeynep", "DD", datetime(1999, 4, 30), "K"),
    ("105", "Ayşe", "EE", datetime(1997, 3, 19), "K"),
    ("106", "Nurgül", "FF", datetime(2000, 10, 5), "K")
]
# Veritabanına kayıt ekler
count = db.insert(sql, ogrenciler)
# Eklenen kayıt sayısını yazdırır
print(f"{count} tane kayıt eklendi.")
# Veritabanından çıkar
db.close()
