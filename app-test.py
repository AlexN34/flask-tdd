#!/usr/bin/python3
from app import app
import MySQLdb
import unittest

class BasicTestCase(unittest.TestCase):
    server = 'localhost'
    user = 'root'
    password = 'cookies'
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 404)

    def test_database(self):
        conn = MySQLdb.Connect(self.server, self.user, self.password)
        cursor = conn.cursor()
        table = "university"
        try:
            cursor.execute("""
            SELECT NULL FROM %d
            """ % (table)
        except MySQLdb.DatabaseError:
            print("ERROR %d IN DATABASE: %s" % (e.args[0], e.args[1]))
        except MySQLdb.Error:
            print("ERROR %d IN CONNECTION: %s" % (e.args[0], e.args[1]))
        finally:
            # test there is a database at localhost

if __name__ == '__main__':
    unittest.main()
