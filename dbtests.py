import mysql.connector
import unittest
import pymysql

class TestDatabaseSchema(unittest.TestCase):

    def setUp(self):
        # Set up the database connection
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="subscriptions"
        )
        self.cursor = self.db.cursor()

    def test_schema_structure(self):
        # Check if 'subscribers' table exists
        self.cursor.execute("SHOW TABLES LIKE 'subscribers'")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result, "Table 'subscribers' does not exist!")

        # Check if 'subscription_date' column exists
        self.cursor.execute("DESCRIBE subscribers")
        columns = [column[0] for column in self.cursor.fetchall()]
        self.assertIn('subscription_date', columns, "Column 'subscription_date' is missing!")

    def test_subscription_date(self):
        # Insert a new subscriber and check if the 'subscription_date' is populated
        self.cursor.execute("INSERT INTO subscribers (email) VALUES ('testuser@example.com')")
        self.db.commit()

        # Fetch the newly inserted row
        self.cursor.execute("SELECT subscription_date FROM subscribers WHERE email = 'testuser@example.com'")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result[0], "Subscription date was not automatically populated!")

    def tearDown(self):
        # Close the cursor and database connection
        self.cursor.close()
        self.db.close()

if __name__ == "__main__":
    unittest.main()

