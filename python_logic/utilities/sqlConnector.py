import mysql.connector
import pyodbc
import config
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'localhost'
database = 'stock_proj'
username = config.settings['username']
password = config.settings['password']
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                      server + ';DATABASE=' + database + ';UID=' + username +
                      ';PWD=' + password)
cursor = cnxn.cursor()
cursor.execute("SELECT * FROM dbo.stocks")
row = cursor.fetchone()
while row:
	print(row[0])
	row = cursor.fetchone()
