#Health Management System
# 3 clients - 1-Harry, 2-Rohan and 3-Hammad

"""
TOTAL 6 files( 3 files - food, 3 files - exercise)
Write a function that when executed takes as input client name
1 for exercise, 2 for diet


Use:

def getDate():
      import dateTime
      return dateTime.dateTime.now()

[time] chicken roti

# One more function to retrieve exercise or food for any client
# """


def getTime():
    import datetime
    return datetime.datetime.now()

def log():
    y = int(input("Enter your client: 1)Harry 2)Rohan 3)Hammad 4)Exit: "))
    if(y==1):
        z = int(input("Enter choice: 1) Exercise 2) Diet 3)Exit:"))
        if(z==1):
            f =open("Harry_exercise.txt","a")
            data1 = input("Enter your exercise: ")
            f.write(str(getTime())+" "+data1+"\n")
            f.close()
            exit()
        elif(z==2):
            f = open("Harry_diet.txt","a")
            data2 = input("Enter your diet: ")
            f.write(str(getTime()) + " " + data2 + "\n")
            f.close()
            exit()
        else:
            exit()

    elif(y == 2):
        z = int(input("Enter choice: 1) Exercise 2) Diet 3)Exit:"))
        if (z == 1):
            f = open("Rohan_exercise.txt", "a")
            data3 = input("Enter your exercise: ")
            f.write(str(getTime()) + " " + data3 + "\n")
            f.close()
            exit()
        elif (z == 2):
            f = open("Rohan_diet.txt", "a")
            data4 = input("Enter your diet: ")
            f.write(str(getTime()) + " " + data4 + "\n")
            f.close()
            exit()
        else:
            exit()
    elif (y == 3):
        z = int(input("Enter choice: 1) Exercise 2) Diet 3)Exit:"))
        if (z == 1):
            f = open("Hammad_diet.txt_exercise.txt", "a")
            data5 = input("Enter your exercise: ")
            f.write(str(getTime()) + " " + data5 + "\n")
            f.close()
            exit()
        elif (z == 2):
            f = open("Hammad_diet.txt_diet.txt", "a")
            data6 = input("Enter your diet: ")
            f.write(str(getTime()) + " " + data6 + "\n")
            f.close()
            exit()
        else:
            exit()
    else:
        exit()


def retrieve():
    y = int(input("Enter your client: 1)Harry 2)Rohan 3)Hammad  4)Exit: "))
    if(y==1):
        x = int(input("Enter choice: 1)Exercise 2)Diet 3)exit"))
        if(x==1):
            f=open("Harry_exercise.txt","r")
            print(f.read())
            f.close()
            exit()
        elif(x==2):
            f = open("Harry_diet.txt", "r")
            print(f.read())
            f.close()
            exit()
        else:
            exit()
    elif (y == 2):
        x = int(input("Enter choice: 1)Exercise 2)Diet 3)exit"))
        if (x == 1):
            f = open("Rohan_exercise.txt", "r")
            print(f.read())
            f.close()
            exit()
        elif (x == 2):
            f = open("Rohan_diet.txt", "r")
            print(f.read())
            f.close()
            exit()
        else:
            exit()
    elif (y == 3):
        x = int(input("Enter choice: 1)Exercise 2)Diet 3)exit"))
        if (x == 1):
            f = open("Hammad_exercise.txt", "r")
            print(f.read())
            f.close()
            exit()
        elif (x == 2):
            f = open("Hammad_diet.txt", "r")
            print(f.read())
            f.close()
            exit()
        else:
            exit()
    else:
        exit()

print("HEALTHCARE SYSTEM")
x = int(input("Do you want to: 1)Log  2)Retrieve 3)Exit: "))
while(x!=3):
    if(x==1):
        log()
    elif(x==2):
        retrieve()
    else:
        x = int(input("Choose again: "))









