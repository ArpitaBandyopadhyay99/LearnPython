def read_file():
    file = open("MyData", "r")
    data = file.read()
    for i in data:
        print(i, end=" ")


def append_file():
    file_app = open("MyData", "a")
    file_app.write("Dum dum diga diga\n")


read_file()
append_file()
print("Now.....")
read_file()
