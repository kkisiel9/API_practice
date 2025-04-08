import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="persondb"
)

def add_cat(fname, lname, age, description):
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = "INSERT INTO Cats (CatName, CatSurname, CatAge,CatDescription) VALUES (%s, %s, %s, %s)"
    val = (fname, lname, age,description)
    cursor.execute(sql, val)

    conn.commit()
def main():
    print(mydb)

    cursor = mydb.cursor()
    sql = "INSERT INTO person (firstname, lastname, age) VALUES (%s, %s, %s)"
    val = ("Fred", "Flintstone", 40)
    cursor.execute(sql, val)

    mydb.commit()
    print(cursor.rowcount, "record inserted.")
    add_cat("Fluffy","Flufferson", 3, "White fur and big eyes")


def get_db_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="persondb"
    )

    return mydb


def add_person(fname, lname, age=25):
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = "INSERT INTO person (firstname, lastname, age) VALUES (%s, %s, %s)"
    val = (fname, lname, age)
    cursor.execute(sql, val)

    conn.commit()




def get_people():
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = "Select ID, Firstname, Lastname from person"
    cursor.execute(sql)

    result_set = cursor.fetchall()
    person_list = []
    for person in result_set:
        person_list.append({'ID': person[0], 'Firstname': person[1], 'Lastname': person[2]})
    return person_list


def get_cats():
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = "SELECT CatID, CatName, CatSurname, CatAge, CatDescription FROM Cats"
    cursor.execute(sql)

    result_set = cursor.fetchall()
    cat_list = []
    for cat in result_set:
        cat_list.append({
            'CatID': cat[0],
            'CatName': cat[1],
            'CatSurname': cat[2],
            'CatAge': cat[3],
            'CatDescription': cat[4]
        })
    conn.close()
    return cat_list


def get_cat_by_id(cat_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = "SELECT CatID, CatName, CatSurname, CatAge, CatDescription FROM Cats WHERE CatID = %s"
    cursor.execute(sql, (cat_id,))
    result = cursor.fetchone()

    conn.close()

    if result:
        return {
            'CatID': result[0],
            'CatName': result[1],
            'CatSurname': result[2],
            'CatAge': result[3],
            'CatDescription': result[4]
        }
    return None


if __name__ == "__main__":
    main()
