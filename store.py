# Import the required modules
from pprint import pprint
import mysql.connector
import base64
from PIL import Image
import io
import os
from pprint import pprint
from app import imagelist
# For security reasons, never expose your password

# Create a connection
mydbCloud = mysql.connector.connect(
	host="103.74.253.121",
	user="root",
	password="123456",
	database="fask" # Name of the database
)

# Create a cursor object

def storee():
  cursor = mydbCloud.cursor()
  path =  r"D:\New folder (3)\results-classy-generated-0.7"
  fileList = [file for file in os.listdir(path) if file.endswith('.png')]
  mydbCloud.commit()
  i = 0
  for	i in range(len(fileList)):

      # Open a file in binary mode
    file = open(os.path.join(path, fileList[i]),'rb').read()

      # We must encode the file to get base64 string
    file = base64.b64encode(file).decode('utf-8')
      # Sample data to be inserted
    args = (file, 'Sample Name')
    
      # Prepare a query
    query = 'INSERT INTO classy(file,name) VALUES(%s, %s)'

      # Execute the query and commit the database.
    cursor.execute(query,args)
    mydbCloud.commit()


if __name__ == "__main__":
  storee()