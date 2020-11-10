import sqlite3


def dbConnect():
    return sqlite3.connect('game.db')

def getRowCount(table):
    conn = dbConnect()
    cur = conn.cursor()
    count = cur.execute('SELECT COUNT(*) FROM ' + table).fetchone()[0]
    conn.commit()
    conn.close()
    return count

def getWordDetails(table,id):
    cur = dbConnect().cursor()
    word, definition = cur.execute('SELECT word, definition FROM ' + table + ' WHERE id=?', (id,)).fetchone()
    cur.close()
    return word, definition

def getPlayerId(name):
    conn = dbConnect()
    cur = conn.cursor()
    id = cur.execute('SELECT id FROM players WHERE name=?', (name,)).fetchone()
    if id:
        conn.close()
        return id[0]
    else:
        return False


def getLastUser():
    conn = dbConnect()
    cur = conn.cursor()
    id = cur.execute('SELECT * FROM scores ORDER BY id DESC').fetchone()[0]
    conn.close()
    return id


def updateScore(score):
    con = dbConnect()
    cur = con.cursor()
    id = getLastUser()
    cur.execute('UPDATE scores SET score = ? WHERE id = ?', (score, id))
    con.commit()
    con.close()
    print('done')

def addPlayer(name):
    con = dbConnect()
    con.cursor().execute('INSERT INTO players (name) VALUES (?)', (name,))
    con.commit()
    con.close()


def getHighscore():
    conn = dbConnect()
    cur = conn.cursor()
    score = cur.execute('SELECT * FROM scores ORDER BY score DESC').fetchone()[2]
    conn.close()
    return score


def createScore(p_id, score):
    conn = dbConnect()
    cur = conn.cursor()
    cur.execute('INSERT INTO scores(player_id, score) VALUES(?,?)',(p_id, score))
    conn.commit()
    conn.close()



def getTopTen():
    conn = dbConnect()
    cur = conn.cursor()
    top = cur.execute(
        'SELECT players.name, scores.score FROM players JOIN scores ON players.id = scores.player_id ORDER BY scores.score DESC').fetchall()[:10]
    conn.close()
    return top






