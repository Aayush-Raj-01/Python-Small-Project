from cryptography.fernet import Fernet

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("What is the master pssword: ")
key = load_key()
fer = Fernet(key)

# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key","wb") as key_file:
#         key_file.write(key)

# write_key()




def view():
    with open('passwords.txt','r') as f: 
        for line in f.readlines():
            data = line.rstrip()
            user,passw = data.split("|")
            print("User: ",fer.decrypt(user.encode()).decode(),"Password: ",fer.decrypt(passw.encode()).decode())

def add():
    name = input("ACCOUNT NAME: ")
    pwd = input("Password: ")

    with open('passwords.txt','a') as f: 
        f.write(fer.encrypt(name.encode()).decode() + "|" + fer.encrypt(pwd.encode()).decode() + "\n")



while True:
    if master_pwd != "1234":
        print("Worng Master Password !! Inruduter !!!! PROGRAM EXITING!!")
        break
    mode = input("Would you like to add a new password orr view existing ones (view,add)? press q for quit : ").lower()
    if mode == "q":
        break
    

    if mode == "view":
        view()
    elif mode ==  "add":
        add()
    else:
        print("invalid mode")
        continue