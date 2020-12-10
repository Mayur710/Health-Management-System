patients = ["mayur", "mansi", "yogita", "ronaldo"]
print("Hi I am your assistant jarvis ")
print("welcome to health management system ")
print("I appreciate you that you are very responsible for your health ")
def getdate():
    import  datetime
    return datetime.datetime.now()

date = getdate()
var1 = int(input("for diet please type 1 or for exercise please type 2 : \n"))
while(patients):
    if var1==1:
        patients = input("enter patient name to proceed further \n")
        if patients=="mayur":
                with open("mayur diet.txt")as f:
                    b = f.read(10000000)
                    print(b)
                    break
        elif patients=="mansi":
                with open("mansi diet.txt")as f:
                    b = f.read(100000)
                    print(b)
                    break
        elif patients=="yogita":
                with open("yogitadiet.txt")as f:
                    b = f.read(10000)
                    print(b)
                    break
        elif patients=="ronaldo":
            with open("ronaldo diet.txt")as f:
                b = f.read(10000000)
                print(b)
                break
        else:
            print("please first do entry of customer")
    if var1==2:
        patients = input("please enter the name of the patient to proceed further \n")
        if patients=="mayur":
            with open("mayur EX.txt")as f:
                b = f.read(100000)
                print(b)
                break
        elif patients=="mansi":
            with open("mansi EX.txt")as f:
                b = f.read(100000)
                print(b)
                break
        elif patients=="yogita":
            with open("yogita EX.txt")as f:
                b = f.read(1000000)
                print(b)
                break
        elif patients=="ronaldo":
            with open("ronaldo.EX.txt")as f:
                b = f.read(100000)
                print(b)
                break
        else:
            print("please first register the name of the patient \n")

print("thank you and have a nice day \n")





