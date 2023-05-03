import sqlite3

# Connect to the database
conn = sqlite3.connect('customers.db')

# Create a customers table if it doesn't already exist
conn.execute('''CREATE TABLE IF NOT EXISTS customers
             (ID INTEGER PRIMARY KEY,
             Name TEXT,
             Phone TEXT,
             Email TEXT);''')

# Insert some example customer records
conn.execute("INSERT INTO customers (Name, Phone, Email) VALUES (?, ?, ?)",
             ('Alice', '9876543210', 'alice@example.com'))
conn.execute("INSERT INTO customers (Name, Phone, Email) VALUES (?, ?, ?)",
             ('Bob', '1234567890', 'bob@example.com'))
conn.execute("INSERT INTO customers (Name, Phone, Email) VALUES (?, ?, ?)",
             ('Charlie', '123456789', 'charlie@example.com'))

# Commit the changes to the database
conn.commit()

# Fetch all the phone numbers and email addresses from the customers table
cursor = conn.execute('SELECT Phone, Email FROM customers')
records = cursor.fetchall()

# Prompt the user to enter a phone number or email address to validate
input_str = input("Enter a phone number or email address to validate: ")

# Check if the input matches any phone numbers or email addresses in the database
if input_str in [record[0] for record in records] or input_str in [record[1] for record in records]:
    print(f"{input_str} is present in the customer database.")
else:
    print(f"{input_str} is not present in the customer database.")

# Close the database connection
conn.close()
