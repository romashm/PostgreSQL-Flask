from flask import Flask, render_template
import psycopg2
from configparser import ConfigParser
from operator import itemgetter
import psycopg2.extras

app = Flask(__name__)

@app.route("/Settings")
def config(filename="database.ini", section="postgresql"):
    # Create a parser
    parser = ConfigParser()
    # Read config file
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} is not found in the {1} file.'.format(section, filename))

    return db

# Find a last index to create several dict
def MaxValue():
    maxValue = []
    crsr = connection.cursor()
    with crsr as cursor:
        cursor.execute (
                """SELECT * FROM basicForm ;"""
        )      

        for j in cursor.fetchall():
            maxValue.append(j[0]) 
            
    return maxValue[-1]

# Receive values from PostgreSQL 
connection = psycopg2.connect(**config())

@app.route("/")
def Main():
    # Place for saving information
    dictValue = {}
    dictr = {}
    dictKeys = {}
    valuesForRange = []
    datas = []    

    crus = connection.cursor()
    # Find a amount of colums & their information inside
    with crus as cursor:
        cursor.execute (
            """
                select column_name  
                from information_schema."columns" 
                where table_name = 'basicform' and table_schema = 'public'
            """
        )
        
        for i in cursor.fetchall():
            valuesForRange.append(i[0])
            dictValue[i[0]] = ''
            
    # Parse information from * table, inject it in empty dicts & arrays
    crsr = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    with crsr as cursor:
        for _ in range(3):
            cursor.execute(f'SELECT * FROM basicform WHERE ids = {_+1}')
            datas.append(cursor.fetchall())

        # Input a function MaxValue ( )
        count = 1
        while count <= int(MaxValue()):
            dictValue = dict(datas[count-1][0])
            dictr[count] = dictValue
            count += 1

        print(dictr)    

    return dictr

# Sorted dictionary from last to beggin
@app.route('/SortedEnd')
def SortedlistEnd():
    print(dict(sorted(Main().items(), reverse = True)))
    return dict(sorted(Main().items(), reverse = True))

# Trying find user via using link
@app.route('/<ids>')
def FindaHotel(ids):
    try:
        cur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute('SELECT * FROM basicform WHERE ids = %s', (ids))
        return cur.fetchall()[0]
    except:
        return "We dont have this user id. Try again"


if __name__ == "__main__":
    app.run(debug=True)