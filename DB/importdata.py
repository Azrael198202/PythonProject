import sqlite3

def convert(value):
    if value.startswith('~'):
        return value.strip('~')
    if not value.strip('\n') :
        value = '0'
        return value
    else :
        return float(value.strip('\n'))

conn = sqlite3.connect("food.db")
curs = conn.cursor()

curs.execute('DROP table food')

curs.execute('''
CREATE TABLE food(
    id TEXT PRIMARY KEY,
    div TEXT,
    desc TEXT,
    desc_big TEXT,
    water FLOAT,
    kcal FLOAT,
    exi TEXT,
    unknown FLOAT,
    protein FLOAT,
    fat FLOAT,
    ash FLOAT,
    carbs FLOAT,
    fiber FLOAT,
    sugar FLOAT
)
''')

query = 'INSERT INTO food VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)'

field_count = 14
for line in open('DB\Data\FOOD_DES.txt') :
    fields = line.split('^')
    vals = [convert(f) for f in fields[:field_count]]
    curs.execute(query,vals)

conn.commit()
conn.close()