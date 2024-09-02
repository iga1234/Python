import os


def create(file, data):
    array = []
    if os.path.isfile(file):
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.replace("\n", "")
                array.append(line.split(";"))
    else:
        print("File doesn't exist.")

    for j in range(len(array)):
        x = True
        for i in range(len(data)):
            if data[i][0] == array[j][0]:
                x = False
        if x:
            data.append(array[j])

    return data


def write(data):
    array = []
    unique_number = input("\nEnter ID: ")
    for i in range(len(data)):
        if data[i][0] == unique_number:
            print("The ID is already provided in the database.")
            return write(data)
    array.append(unique_number)
    name = input("Enter name: ")
    array.append(name)
    surname = input("Enter surname: ")
    array.append(surname)
    pesel = input("Enter pesel: ")
    array.append(pesel)
    data.append(array)

    return data


def read(data):
    for i in range(len(data)):
        print("Id:", data[i][0], "Name:", data[i][1], "Surname:", data[i][2], "Pesel:", data[i][3])
    print("")


def update(data):
    unique_number = input("Enter ID: ")
    for i in range(len(data)):
        if data[i][0] == unique_number:
            name = input("Enter name: ")
            data[i][1] = name
            surname = input("Enter surname: ")
            data[i][2] = surname
            pesel = input("Enter pesel: ")
            data[i][3] = pesel
            return data

    print("There is no specified ID in the database.")
    return update(data)


def delete(data):
    unique_number = input("Enter ID: ")
    for i in range(len(data)):
        if data[i][0] == unique_number:
            del data[i]
            return data

    print("There is no specified ID in the database.")
    return delete(data)


def average(data):
    age = 0
    for i in range(len(data)):
        pesel = data[i][3]
        if int(pesel[2:4]) > 12:
            age = age + (2021 - (2000+int(pesel[:2])))
        elif int(pesel[:2]) <= 99:
            age = age + (2021 - (1900+int(pesel[:2])))

    age = age/len(data)
    return age


def count(data):
    men = 0
    women = 0
    for i in range(len(data)):
        pesel = data[i][3]
        if int(pesel[9]) % 2 == 0:
            women += 1
        elif int(pesel[9]) % 2 != 0:
            men += 1
    print("Number of women:", women)
    print("Number of men:", men)
