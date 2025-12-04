import psycopg2
import csv

# CONNECT DB
def conn():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        database="postgres",
        user="zhanel",
        password=""
    )


# Insert from CSV
def insert_from_csv(path):
    with conn() as c:
        with c.cursor() as cur, open(path, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                cur.execute("CALL phonebook_upsert_user(%s, %s);",
                            (row["name"], row["phone"]))
    print("CSV inserted")


# Insert ONE user
def insert_console():
    name = input("Name: ")
    phone = input("Phone: ")
    with conn() as c:
        with c.cursor() as cur:
            cur.execute("CALL phonebook_upsert_user(%s, %s);", (name, phone))
    print("Inserted")


# Insert MANY users
def insert_many_console():
    count = int(input("How many users do you want to add? "))

    names = []
    phones = []

    for i in range(count):
        print(f"\nUser {i+1}:")
        name = input("Name: ")
        phone = input("Phone: ")
        names.append(name)
        phones.append(phone)

    with conn() as c:
        with c.cursor() as cur:
            cur.execute(
                "CALL phonebook_bulk_insert_users(%s, %s);",
                (names, phones)
            )
    print("Inserted!")


# Update
def update_phone(name, new_phone):
    with conn() as c:
        with c.cursor() as cur:
            cur.execute("UPDATE phonebook SET phone=%s WHERE name=%s;",
                        (new_phone, name))
    print("Phone updated")


# Query
def show_all():
    with conn() as c:
        with c.cursor() as cur:
            cur.execute("SELECT id, name, phone FROM phonebook ORDER BY name;")
            for row in cur.fetchall():
                print(row)


def search(pattern):
    with conn() as c:
        with c.cursor() as cur:
            cur.execute("SELECT * FROM phonebook_search(%s);", (pattern,))
            for row in cur.fetchall():
                print(row)


def paginated(limit, offset):
    with conn() as c:
        with c.cursor() as cur:
            cur.execute("SELECT * FROM phonebook_paginated(%s, %s);", (limit, offset))
            for row in cur.fetchall():
                print(row)


# Delete 
def delete_by_name(name):
    with conn() as c:
        with c.cursor() as cur:
            cur.execute("CALL phonebook_delete_user(%s, NULL);", (name,))
    print("Deleted")


def delete_by_phone(phone):
    with conn() as c:
        with c.cursor() as cur:
            cur.execute("CALL phonebook_delete_user(NULL, %s);", (phone,))
    print("Deleted")


# MENU 
def main():
    while True:
        print(" PHONEBOOK MENU ")
        print("1 - Show all users")
        print("2 - Search by pattern")
        print("3 - Insert ONE user")
        print("4 - Insert MANY users")
        print("5 - Insert from CSV")
        print("6 - Update phone")
        print("7 - Delete by name")
        print("8 - Delete by phone")
        print("9 - Pagination")
        print("0 - Exit")

        choice = input("Choose option: ")

        if choice == "1":
            show_all()
        elif choice == "2":
            search(input("Enter pattern: "))
        elif choice == "3":
            insert_console()
        elif choice == "4":
            insert_many_console()
        elif choice == "5":
            insert_from_csv(input("CSV path: "))
        elif choice == "6":
            update_phone(input("Name: "), input("New phone: "))
        elif choice == "7":
            delete_by_name(input("Name to delete: "))
        elif choice == "8":
            delete_by_phone(input("Phone to delete: "))
        elif choice == "9":
            paginated(int(input("Limit: ")), int(input("Offset: ")))
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()