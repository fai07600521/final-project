# Import the required modules
import mysql.connector
import base64
from PIL import Image
import io
import os
from pprint import pprint

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
path = r"C:\Users\Admin\temp\stylegan2-ada-pytorch\static\images\result\street"
fileList = [file for file in os.listdir(path) if file.endswith('.png')]
i = 0
for	i in range(len(fileList)):

		# Open a file in binary mode
	file = open(os.path.join(path, fileList[i]),'rb').read()

		# We must encode the file to get base64 string
	file = base64.b64encode(file).decode('utf-8')
	pprint(file)
		# Sample data to be inserted
	args = (i, 'Sample Name', file)

		# Prepare a query
	query = 'INSERT INTO street VALUES(%s, %s, %s)'

		# Execute the query and commit the database.
	cursor.execute(query,args)
	mydb.commit()


