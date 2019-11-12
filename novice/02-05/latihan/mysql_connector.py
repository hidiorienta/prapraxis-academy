import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='hidiorienta', password='070394', database='mysql')
cursor = mariadb_connection.cursor()