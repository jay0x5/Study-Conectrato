'''This is custom version here you can set custom time like 25 minutes and then use it unlike the more dangerous version main.py'''



from tkinter import*
import random
import time
import webbrowser


print("Welcome Please Enter The Number Of Minutes You Want to Study without losing concentration \n")
min = int(input("Number Of Minutes : \n"))
print("\n")
print("\n")
print("\n")

print("Starting up in 60 seconds so do whatever you want to and come in a minute and dont u dare move your mouse or the unexpected will happen lol i am not joking i am serious ")
time.sleep(60)
print("Haha your time ends less go")

def func_test_1():
    webbrowser.open("https://www.youtube.com/watch?v=rwSJwzE7lAg")

def func_test_2():
    webbrowser.open("https://www.youtube.com/watch?v=fcZXfoB2f70")

def func_test_3():
    webbrowser.open("https://www.youtube.com/watch?v=tZGpRd-t7jg")

def func_test_4():
    webbrowser.open("https://www.youtube.com/watch?v=ZYzbalQ6Lg8")

root = Tk()


def current_position():
    return [root.winfo_pointerx(), root.winfo_pointery()]

pos1 = current_position()

t_end = time.time() + 60 * min
while time.time() < t_end :

    time.sleep(0.5)
    pos2 = current_position()
    if not pos1 == pos2:
       # run a command:
        my_list = [func_test_1, func_test_2, func_test_3, func_test_4]
        random.choice(my_list)()
        
        pos1 = pos2

else:
    webbrowser.open("https://www.youtube.com/watch?v=Zd9muK2M36c")
