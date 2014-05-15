#test.py

import os
import unittest

from views import app, db
from models import User
from config import basedir

TEST_DB = 'test.db'

class Users(unittest.TestCase):

	# this is a special method that is executed prior to each test
	#The setUp method() was invoked which created a test database (if it doesn’t exist yet) and initialized the database schema from the main database (e.g., creates the tables, relationships, etc.).

	def setUp(self):
		app.config['TESTING'] = True
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
		os.path.join(basedir, TEST_DB)
		self.app = app.test_client()
		db.create_all()

	# this is a special method that is executed after each test
	#Lastly, the tearDown() method was invoked which dropped all the tables in the test database.
	def tearDown(self):
		db.drop_all()

	# each test should start with 'test'
	#The test_user_setup() method was called, inserting data to the “users” table.
	def test_users_can_register(self):
		new_user = User("mherman","michael@mherman.org","michaelherman")
		db.session.add(new_user)
		db.session.commit()
		test = db.session.query(User).all()
		for t in test:
			t.name
		assert t.name == "mherman"

if __name__ == "__main__":
	unittest.main()