import _mysql_connector 
conn = _mysql_connector.connect( user='root', host = 'localhost', passwd='',database="countries")

mycursor = conn.cursor()

mycursor.execute("CREATE DATABASE countries")
mycursor.execute("CREATE TABLE countries (name VARCHAR(255),id INT AUTO_INCREMENT PRIMARY KEY),language_id INT,currencies_id INT,flags_id INT")
query = 'ALTER TABLE countries ADD foreign key(language_id) references language(id)'
mycursor.execute(query)

mycursor.execute("CREATE DATABASE language")
mycursor.execute("CREATE TABLE language (name VARCHAR(255),id INT AUTO_INCREMENT PRIMARY KEY)")

mycursor.execute("CREATE DATABASE currencies")
mycursor.execute("CREATE TABLE currencies (name VARCHAR(255),id INT AUTO_INCREMENT PRIMARY KEY)")

mycursor.execute("CREATE DATABASE flags")
mycursor.execute("CREATE TABLE flags (name VARCHAR(255),id INT AUTO_INCREMENT PRIMARY KEY)")

mycursor.execute("CREATE DATABASE map")
mycursor.execute("CREATE TABLE map (name VARCHAR(255),id INT AUTO_INCREMENT PRIMARY KEY)")

mycursor.execute("CREATE DATABASE timezones")
mycursor.execute("CREATE TABLE timezones (name VARCHAR(255),id INT AUTO_INCREMENT PRIMARY KEY)")
