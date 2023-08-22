#!/usr/bin/python3
""" DB STORAGE TEST CLASS"""
from models.state import State
from models.engine.db_storage import DBStorage
import unittest
import MySQLdb
import pep8
import os

type_storage = os.getenv('HBNB_TYPE_STORAGE')


@unittest.skipIf(type_storage != 'db', "apply for db")
class TestDataBase(unittest.TestCase):
    """this will test the console"""

    def test001(self):
        """ Test pass """
        pass

    @classmethod
    def setUp(self):
        """Set up MySQL"""
        self.db = MySQLdb.connect(host="localhost",
                                  port=3306,
                                  user='hbnb_test',
                                  passwd='hbnb_test_pwd',
                                  db='hbnb_test_db',
                                  charset='utf8')
        self.cur = self.db.cursor()
        self.storage = DBStorage()
        self.storage.reload()

    @classmethod
    def tearDown(self):
        """Tear down MySQL"""
        self.cur.close()
        self.db.close()

    @unittest.skipIf(type_storage != 'db', 'db')
    def test_add(self):
        """Test add method"""
        self.cur.execute("""
        INSERT INTO states (id, created_at, updated_at, name)
        VALUES (1, '2017-11-10 00:53:19', '2017-11-10 00:53:19', "California")
        """)
        self.cur.execute('SELECT * FROM states')
        rows = self.cur.fetchall()
        self.assertEqual(len(rows), 1)
