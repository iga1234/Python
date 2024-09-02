import CRUD1


def main():
    data = []
    choice = ''
    while choice != '8':
        choice = input("Choose option:\n"
                        "1 - Load the database from a file\n"
                        "2 - Enter data into the database via the console\n"
                        "3 - Read data\n"
                        "4 - Update data\n"
                        "5 - Delete a record\n"
                        "6 - Calculate the average age of people in the database\n"
                        "7 - Calculate the number of women and men in the database\n"
                        "8 - Exit\n"
                        "Enter number: ")
        print("")
        if choice == '1':
            plik = input("Enter file name with extension: ")
            data = CRUD1.create(plik, data)
        if choice == '2':
            data = CRUD1.write(data)
        if choice == '3':
            CRUD1.read(data)
        if choice == '4':
            data = CRUD1.update(data)
        if choice == '5':
            data = CRUD1.delete(data)
        if choice == '6':
            print("Average age: ", CRUD1.average(data))
        if choice == '7':
            CRUD1.count(data)


main()
