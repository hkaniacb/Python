import sqlite3
import openpyxl
connection = sqlite3.connect('sqlite3_chat_bot_4.db')
cursor = connection.cursor()



cursor.execute(""" CREATE TABLE IF NOT EXISTS QandA (
                     id INTEGER PRIMARY KEY,
                     answer NOT NULL,
                     question TEXT NOT NULL,
                     keyword VARCHAR
           );""")

wb=openpyxl.load_workbook(r'C:\Users\Admin\Desktop\aas.xlsx')
sheet = wb.worksheets[0]
cursor.execute('SELECT * FROM QandA')
rows = cursor.fetchall()
licznik = len(rows)
print(licznik)
status_first_row = True
# for row in sheet.iter_rows():
#
#     if status_first_row == False:
#
#         licznik = licznik + 1
#         cursor.execute('INSERT INTO QandA VALUES(?, ?, ?, ?)', (licznik, row[0].value, row[1].value, row[2].value ))
#         connection.commit()
#     status_first_row = False
cursor.execute('SELECT * FROM QandA')
rows = cursor.fetchall()


def prepare_word(text):
    #print(type(text))
    text = text.replace("?","")
    text = text.lower()
    text = text.strip()
    return text

while True:
    input_question = input("Zadaj pytanie ?")
    #print(type(input_question))
    input_question = prepare_word(str(input_question))
    #print(input_question)
    for row in rows:
        #print(prepare_word(row[1]))
        if input_question == prepare_word(row[1]):
            print(r"$$$$$$$$$$$", row[2])

