import sqlite3

con = sqlite3.connect('pets.db')

person = (
    (1, 'James', 'Smith', 41),
    (2, 'Diana', 'Greene', 23),
    (3, 'Sara', 'White', 27),
    (4, 'William', 'Gibson', 23)
    )

pet = (
    (1, 'Rusty', 'Dalmation', 4, 1),
    (2, 'Bella', 'Alaskan Malamute', 3, 0),
    (3, 'Max', 'Cocker Spaniel', 1, 0),
    (4, 'Rocky', 'Beagle', 7, 0),
    (5, 'Rufus', 'Cocker Spaniel', 1, 0),
    (6, 'Spot', 'Bloodhound', 2, 1)
    )
person_pet = (
    (1, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 5),
    (4, 6)
    )

if __name__ == "__main__":
    cur = con.cursor()

    cur.executemany("INSERT INTO person VALUES(?, ?, ?, ?)", person)
    cur.executemany("INSERT INTO pet VALUES(?, ?, ?, ?, ?)", pet)
    cur.executemany("INSERT INTO person_pet VALUES(?, ?)", person_pet)

    con.commit()
    con.close()
