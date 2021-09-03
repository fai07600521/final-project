# Import the required modules
import mysql.connector
import base64
from PIL import Image
import io
import os
from pprint import pprint

# For security reasons, never expose your password

# Create a connection
mydbCloud = mysql.connector.connect(
	host="103.74.253.121",
	user="root",
	password="123456",
	database="fask" # Name of the database
)

mydbLocal = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="fask" # Name of the database
)

cursor = mydbLocal.cursor()
cursorCloud = mydbCloud.cursor()

query = 'SELECT * FROM street LIMIT 5000 OFFSET 0'

	# Execute the query to get the file
cursor.execute(query)
data = cursor.fetchall()
items = []
for row in data:
  args = (row[1], row[2])
  query2 = 'INSERT INTO street (name, file) VALUES(%s, %s)'
  cursorCloud.execute(query2, args)
  mydbCloud.commit()
mydbLocal.close()
mydbCloud.close()
# Create a cursor object



def storee():
  cursor = mydb.cursor()
  path = r"D:\New folder (3)\folderImg\classy"
  fileList = [file for file in os.listdir(path) if file.endswith('.png')]
  i = 0
  for	i in range(len(fileList)):

      # Open a file in binary mode
    file = open(os.path.join(path, fileList[i]),'rb').read()

      # We must encode the file to get base64 string
    file = base64.b64encode(file).decode('utf-8')
      # Sample data to be inserted
    args = (i, 'Sample Name', file)

      # Prepare a query
    query = 'INSERT INTO test VALUES(%s, %s, %s)'

      # Execute the query and commit the database.
    cursor.execute(query,args)
    mydb.commit()


if __name__ == "__main__":
  storee()