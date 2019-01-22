import os
# os.getcwd()
# print(os.getcwd()) # To check the current working directory and print it on screen
# os.mkdir("movies")
# print(os.path.exists("movies"))    # To check if folder movies exits already or not? True means exists already.
# if os.path.exists("movies"):          # To put custom message for already existing folder we create our own function.
#     print("already exists")
# else:
#     os.mkdir("movies")
# open("file.txt","a").close()     # To create files we use this function in os module
# os.mkdir("kale")                # To create folder with name of kale.
# print(os.listdir())   # To print list of all folders in current working directory.
# print(os.listdir("/root/"))             # To print list of all folders in root directory
for kale in os.listdir(os.getcwd()):
    path =os.path.join(os.getcwd(),"kale")
print(path)