import time

name= input("Hello,  what is your name?")
print(f"welcome,{name},this is a programm that will help you with your anxiety and will walk you through relaxation" )

time.sleep(5)

print(f"Ready when you are {name}.")

time.sleep (5)

print("This program will start by going through with you as you take deep breaths, please work with me.")
time .sleep(5)
print("Can we take 5 deep breaths?")
time.sleep(3)

print("1")
time.sleep(3)
print("2")
time.sleep(3)
print("3")
time.sleep(3)
print("4")
time.sleep(3)
print("5")
time.sleep(3)

print(f"How do you feel? {name}")
time.sleep(3)
answer =input("feeling relaxed enough? do we carry on?")
if answer== 'yes':
    print("lovely, you are doing well, see you in the next phase, be rest assured you will be fine.")
else:
    print(f"goodbye and Take care, {name}")

