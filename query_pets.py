import sqlite3


def main():
    con = sqlite3.connect('pets.db')
    cur = con.cursor()

    idnum = input("Select ID number, enter -1 for close")
    while idnum != '-1':
        cur.execute("""
            SELECT first_name, last_name, dead, name, breed,
                person.age, pet.age
            FROM person, pet, person_pet
            WHERE person.id = ?
            AND person.id = person_pet.person_id
            AND pet.id = person_pet.pet_id
            """, (idnum,))
        try:
            data = cur.fetchall()
            frow = data[0]
            hadpt = "{} {} owned {}, a {}, that was {} years old"
            haspt = "{} {} owns {}, a {}, that is {} years old"
            print("{} {} is {} years old.".format(frow[0], frow[1], frow[5]))
            for row in data:
                if row[2] == 1:
                    print(hadpt.format(row[0], row[1], row[3], row[4], row[6]))
                else:
                    print(haspt.format(row[0], row[1], row[3], row[4], row[6]))

        except IndexError as e:
            print("ERROR: {}".format(e))

        idnum = input("Select ID number, enter -1 for close")


if __name__ == "__main__":
    main()
