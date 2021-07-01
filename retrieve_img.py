# Import the required modules
import mysql.connector
import base64
from PIL import Image
import io
from pprint import pprint
import pymysql
import json

# For security reasons, never expose your password

# Create a connection
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="fask" # Name of the database
)

# Create a cursor object
cursor = mydb.cursor()


# def getImage():
	# Prepare the query
query = 'SELECT file FROM streetset'

	# Execute the query to get the file
cursor.execute(query)
data = cursor.fetchall()
items = []
for row in data:
  	items.append(row)
mydb.close()
		# The returned data will be a list of list


with open('sexy.json', 'w') as outfile:
    json.dump(items, outfile)




