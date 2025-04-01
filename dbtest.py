import pymysql
import mysql.connector

# Connect to MySQL
conn = pymysql.connect(host='localhost', user='root', password='password', database='subscriptions')
cursor = conn.cursor()

# Check if the table exists
cursor.execute("SHOW TABLES LIKE 'subscribers';")
if not cursor.fetchone():
    print("❌ Table 'subscribers' does not exist!")
    exit(1)

# Check if the column exists
cursor.execute("SHOW COLUMNS FROM subscribers LIKE 'subscription_date';")
if not cursor.fetchone():
    print("❌ Column 'subscription_date' does not exist!")
    exit(1)

print("✅ Database validation successful!")

conn.close()
