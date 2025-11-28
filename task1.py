import psycopg2
import csv

# Database connection function
def connect():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        database="postgres",  
        user="zhanel",  
        password=""   
        )

# Create PhoneBook table
def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS PhoneBook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            phone VARCHAR(20)
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

# Insert from CSV file
def insert_from_csv(file_path):
    conn = connect()
    cur = conn.cursor()
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            cur.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()
    cur.close()
    conn.close()
    print("CSV-тен сәтті жүктелді.")

# Insert from console
def insert_from_console():
    name = input("Атыңызды енгізіңіз: ")
    phone = input("Телефон нөмірін енгізіңіз: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("Консолдан сәтті енгізілді.")

# Update user data
def update_user():
    name = input("Қай қолданушыны жаңартқыңыз келеді (аты): ")
    field = input("Қай өрісті өзгерткіңіз келеді? (name/phone): ")
    new_value = input("Жаңа мәнді енгізіңіз: ")
    
    conn = connect()
    cur = conn.cursor()
    if field == 'name':
        cur.execute("UPDATE PhoneBook SET name = %s WHERE name = %s", (new_value, name))
    elif field == 'phone':
        cur.execute("UPDATE PhoneBook SET phone = %s WHERE name = %s", (new_value, name))
    else:
        print("Қате өріс.")
    conn.commit()
    cur.close()
    conn.close()
    print("Мәлімет сәтті жаңартылды.")

# Query data with optional filter
def query_data():
    keyword = input("Іздеу сөзін енгізіңіз (немесе бос қалдырыңыз): ")
    conn = connect()
    cur = conn.cursor()
    if keyword:
        cur.execute("SELECT * FROM PhoneBook WHERE name ILIKE %s OR phone ILIKE %s", 
                    (f'%{keyword}%', f'%{keyword}%'))
    else:
        cur.execute("SELECT * FROM PhoneBook")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

# Delete by name or phone
def delete_data():
    method = input("Қалай өшіргіңіз келеді? (name/phone): ")
    value = input("Мәнді енгізіңіз: ")
    conn = connect()
    cur = conn.cursor()
    if method == 'name':
        cur.execute("DELETE FROM PhoneBook WHERE name = %s", (value,))
    elif method == 'phone':
        cur.execute("DELETE FROM PhoneBook WHERE phone = %s", (value,))
    else:
        print("Қате әдіс.")
    conn.commit()
    cur.close()
    conn.close()
    print("Сәтті өшірілді.")

# Main menu
def main():
    create_table()
    while True:
        print("\n📱 PhoneBook мәзірі:")
        print("1. CSV-тен дерек жүктеу")
        print("2. Консолдан дерек енгізу")
        print("3. Мәлімет жаңарту")
        print("4. Мәліметтерді көру")
        print("5. Мәлімет жою")
        print("0. Шығу")
        choice = input("Таңдауыңызды енгізіңіз: ")

        if choice == '1':
            path = input("CSV файл жолын енгізіңіз: ")
            insert_from_csv(path)
        elif choice == '2':
            insert_from_console()
        elif choice == '3':
            update_user()
        elif choice == '4':
            query_data()
        elif choice == '5':
            delete_data()
        elif choice == '0':
            print("Бағдарлама аяқталды.")
            break
        else:
            print("Қате таңдау. Қайталап көріңіз.")

if __name__ == '__main__':
    main()

