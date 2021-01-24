import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS counts')
cur.execute('CREATE TABLE counts(email TEXT, count INTEGER)')

fname = input('enter file name: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'
fhandle = open(fname)
for line in fhandle:
    if not line.startswith('From: '):
        continue
    words = line.split()
    email = words[1]

    cur.execute('SELECT count from counts where email = ?', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO counts (email, count) VALUES (?, ?)', (email, 1))
    else:
        cur.execute('UPDATE counts set count = count + 1 where email = ?', (email,))
    conn.commit()

sqlstr = 'SELECT email, count from counts ORDER BY count DESC'
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
