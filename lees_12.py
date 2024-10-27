import sqlite3
import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.bbc.com/ukrainian/features-66330880")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    films = soup.find_all('h2')

    conn = sqlite3.connect("films.db")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS films ( id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT UNIQUE)''')

    for film in films:
        title = film.get_text(strip=True)
        try:

            cursor.execute("INSERT OR IGNORE INTO films (title) VALUES (?)", (title,))
            print(f"Saved in the BD: {title}")
        except sqlite3.IntegrityError:
            print(f"Film already exists in the BD: {title}")
    conn.commit()
    conn.close()
else:
    print("Response code is not 200")
connection = sqlite3.connect("films.db", 5)
cur = connection.cursor()


