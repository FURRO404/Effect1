#=============FURRO404=============#
#Effect1.py
import time
#----------------------------------#
t = str(input("Enter 1 character: "))
much = int(input("How many lines? "))
long = int(input("How fast do you want it to go? (Between 1 and 10) "))
bruh = (much - 2)

value = (t)
ran = []
long2 = long/10
#-----------------------------------#
for i in range (0, 100):
    print("")

while True:
    for i in range(0, much):
        ran.append(value)
        print(str(ran))
        time.sleep(long2)
            
    for i in range(0, bruh):
        del(ran[1])
        print(ran)
        time.sleep(long2)
        
    ran.clear()
#=============FURRO404=============#
