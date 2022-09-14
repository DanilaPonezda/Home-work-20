from datetime import datetime
import time
from time import ctime, time





class TimeWork:
    @staticmethod
    def get_now():
        now = datetime.now()
        return str(now)

class FileWork:
    def __init__(self, name_file, text = None):
        self.name_file = name_file
        self.text = text

    def my_write(self):
        with open(self.name_file, "wt") as file:
            file.write(self.text)

    def my_read(self):
        with open(self.name_file, "rt") as file:
            result = file.read()
            return str(result)
    
class Users:
    nameUser = "unknw"

    def __init__(self, user):
        self.user = user

           




def main():
    print(f"\t\t\t\t\t\t\t\t EditorProgram v.0.0.1 alpha")
    print("-"*100)
    print()
    username = Users(str(input("Write username name >>>: ")))  #Программа просит пользователя ввести свой username
    print(f"Hello, {username.user}")
    prog_live = True
    while prog_live:
        print("Оберіть функцію программи:\n\n \n1 - Працювання з файлами")
        choice = input(">>: ")
        if choice == "1":
            name_file = input("Впишіть назву файла.  ")
            print("Оберіть що ви хочете зробити з файлом\n1 - Записати інформацію в файл\n2 - Прочитати інформацію із файла ")
            choice = input(">>: ")
            if choice == "1":
                write_text_to_file = input("Введіть текст для запису: ")
                file = FileWork(name_file, text = write_text_to_file)
                file.my_write()
                stroka = TimeWork.get_now()
                with open(name_file, "a+") as file_time:
                    file_time.write("\n\n\n\t\t\t\t\t\t\t\t\t")
                    file_time.write(stroka)
            elif choice == "2":
                try:
                    file = FileWork(name_file)
                    result = file.my_read()
                    print(result)
                except:
                    print("Невідома помилка")

main()




