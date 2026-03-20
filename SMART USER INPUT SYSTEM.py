import json

def is_valid_email(email):
    return '@' in email and '.' in email
def delete_user(name,age,email):
    USER.remove({"name":name,"age":age,"email":email})
USER=[]
while True:
    print("1.Add user")
    print("2.View user")
    print("3.Analyze data")
    print("4. search user by its name")
    print("5. delete user")
    print("6.Exit")
    Task=input("Enter your choice: ")
    if Task=="1":
        name=input("Enter your name: ")
        try:
            age=int(input("Enter your age: "))
        except:
            print("Please enter a valid age")
            continue
        email=input("Enter your email: ")
        if not is_valid_email(email):
            print("Please enter a valid email")
            continue
        USER.append({"name":name,"age":age,"email":email})
        choice=input("Would you like to add another user? (y/n): ")
        if choice=="n":
            break
    elif Task == "2":

        with open("USER.json","w")as f:
            json.dump(USER,f)
        with open("USER.json","r")as f:
            data=json.load(f)
        print(data)
    elif Task == "3":
        ages=[]
        for a in USER:
            ages.append(a["age"])

        avg_age=sum(ages)/len(ages)
        oldest= max(ages)
        print("average age:",avg_age)
        print("oldest age:",oldest)
    elif Task == "4":
        search=input("Enter your search name: ")
        na=[]
        for n in USER:
            na.append(n["name"])
            if search in na:
                print("User found")
            else:
                print("User not found")
    elif Task == "5":
        de_name=input("Enter your user name to be deleted: ")
        de_age = input("Enter your user age to be deleted: ")
        de_email = input("Enter your user email to be deleted: ")
        delete_user(de_name,de_age,de_email)

    elif Task == "6":
        break
    else:
        print("Please enter a valid Task")

