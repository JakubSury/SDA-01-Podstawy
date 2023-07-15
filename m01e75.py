# Baza studentów z ocenami
def insert_grade():
    possible_grades = ["2", "3", "3.5", "4", "4.5", "5"]
    while True:
        grade=input("Podaj ocenę studenta: ")
        if not possible_grades.count(grade):
            print("Nie ma takiej oceny")
        else:
            break
    return grade

students_grades = {}
file_name = "students_grades.txt"

print("\nCo chcesz zrobić?")
print("1. Dodaj nowego studenta")
print("2. Usunąć studenta")
print("3. Zmienić ocenę")
print("4. Wydrukuj listę studentów")
print("5. Zapisz listę studentów do pliku")
print("6. Wczytaj listę studentów z pliku")
print("0. Przerwij działanie programu")
print("\nMożliwe oceny: 2, 3, 3.5, 4, 4.5, 5")

while True:
    n_option = input("\nWybierz numer z listy: ")
    match n_option:
        case "1":
            name = input("Podaj nazwisko studenta do dodania: ")
            if name in students_grades:
                print("Student jest już zapisany w bazie")
            else:
                students_grades[name] = insert_grade()
        case "2":
            name = input("Podaj nazwisko studenta do usunięcia: ")
            if name not in students_grades:
                print("Studenta nie ma w bazie")
            else:
                del students_grades[name]
        case "3":
            name = input("Podaj nazwisko studenta któremu będzie zmieniana ocena: ")
            if name not in students_grades:
                print("Studenta nie ma w bazie")
            else:
                students_grades[name] = insert_grade()
        case "4":
            if not students_grades:
                print("Baza studentów jest pusta")
            else:
                for name, grade in sorted(students_grades.items()):
                    print(f"{name} - {grade}")
        case "5":
            with open(file_name, "w") as file:
                for name, grade in sorted(students_grades.items()):
                    file.write(f"{name} - {grade}\n")
            print(f"Bazę studentów z ocenami zapisano do pliku '{file_name}'")
        case "6":
            students_grades = {}
            with open("students_grades.txt") as file:
                while True:
                    line = file.readline()
                    if not line:
                        break
                    line = line.split(" - ")
                    students_grades[line[0]] = line[1][0:-1]
            print(f"Bazę studentów z ocenami wczytano z pliku '{file_name}'")
        case "0":
            print("Do zobaczenia!")
            break
        case _:
            print("Podano niepoprawny numer z listy")