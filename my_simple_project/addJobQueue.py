import shutil
import os
import subprocess
import shlex
import time
import schedule
import queue


def add_task(): # Dodowanie zadań do kolejki
    queue_task = queue.Queue()
    while 1:

        print("1. Wykonaj pierwszy projekt "
              "2. Wykonaj drugi projekt "
              "3. Zakończ dodawanie tasków")

        choose_number = int(input("Podaj Number czynności: "))

        if choose_number == 1:
            queue_task.put(1)
        elif choose_number == 2:
            queue_task.put(2)
        else:
            print("qqloop", queue_task.qsize())
            return queue_task

def delay(): # Fukncja do opóźnienia 
    timer2 = time.time()
    while True:
        if time.time() - timer2 > 5:
            print("1 sekundy ")
            break
def job():
    print("I'm working...")
    os.system('start /d "C://Program Files (x86)//NICE Systems//Real-Time Designer" RTClient.exe')

s = schedule
s.every(1).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("12:06").do(job)

def choose_project_queue(choose_project):
    if choose_project == 1:
        shutil.copy('D:/conf/FirstProject/RTClient.exe.config',
                    'C:Users/huber/AppData/Roaming/Nice_Systems/Real-Time/RTClient.exe.config') # kopiowanie pliku config z odpowiednim projektem 
    elif choose_project == 2:
        shutil.copy('D:/conf/SecondProject/RTClient.exe.config',
                    'C:Users/huber/AppData/Roaming/Nice_Systems/Real-Time/RTClient.exe.config')

    else:
        print("Podany  zły numer!!!")


while True:
    os.chdir('D:/')
    queue_task_main = queue.Queue() #inicjalizacja pustej kolejki
    try:
        print("1. Pierwszy projekt "
              "2. Drugi projekt "
              "3.Podaj kolejke")

        choose_project = int(input('Podaj numer zadania: '))
        if choose_project == 1:
            shutil.copy('D:/conf/FirstProject/RTClient.exe.config',
                        'C:Users/huber/AppData/Roaming/Nice_Systems/Real-Time/RTClient.exe.config')
            break
        elif choose_project == 2:
            shutil.copy('D:/conf/SecondProject/RTClient.exe.config',
                        'C:Users/huber/AppData/Roaming/Nice_Systems/Real-Time/RTClient.exe.config')

            break

        elif choose_project == 3:
            queue_task_main = add_task()
            print("qqMain",queue_task_main.qsize())
            break
        else:
            print("Podany  zły numer!!!")

    except Exception as e:
        print("Podaj wartość cyfrowo")
        print(e)



while True:
    command = shlex.split("tasklist")
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    output, err = process.communicate() # pobierania instniejące procesy na komputerze 
    print(str(output).count("RTClient"))
    print(queue_task_main.empty())
    if str(output).count("RTClient") == 0 and queue_task_main.empty() == True :
        s.run_pending()
    if str(output).count("RTClient") == 0 and queue_task_main.empty() == False:
        choose_project_queue(queue_task_main.get())
        job()


