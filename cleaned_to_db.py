import sqlite3
import json

with open('withoutsource.json','r') as f:
    content = json.load(f)

conn = sqlite3.connect('game.db')
cur = conn.cursor()

for v, k in content.items():
    if len(v) == 4:
        cur.execute("""INSERT INTO four(word, definition) VALUES (?, ?)""", (v,k))
    if len(v) == 5:
        cur.execute(
            """INSERT INTO five(word, definition) VALUES (?, ?)""", (v, k))
    if len(v) == 6:
        cur.execute(
            """INSERT INTO six(word, definition) VALUES (?, ?)""", (v, k))
    if len(v) == 7:
        cur.execute(
            """INSERT INTO seven(word, definition) VALUES (?, ?)""", (v, k))
    if len(v) == 8:
        cur.execute(
            """INSERT INTO eight(word, definition) VALUES (?, ?)""", (v, k))
    if len(v) == 9:
        cur.execute(
            """INSERT INTO nine(word, definition) VALUES (?, ?)""", (v, k))
    if len(v) == 10:
        cur.execute(
            """INSERT INTO ten(word, definition) VALUES (?, ?)""", (v, k))
    else:
        continue

conn.commit()

conn.close()

