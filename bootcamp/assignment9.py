'''
API creation
- Write four different APIs to perform CRUD (Create, Read, Update, Delete) operations.
- Use infrastructure created in the assignment number 7 to host APIs.
- Login to DB VM and connect to mysql server through command line in order to execute below set of commands.
a. CREATE DATABASE IF NOT EXISTS testdb; 
b. USE testdb;
c. CREATE TABLE IF NOT EXISTS employee ( emp_id INT(10) NOT NULL AUTOINCREMENT, emp_name VARCHAR(100) NOT NULL, PRIMARY KEY(emp_id));
d. INSERT INTO employee VALUES ('Ram'); INSERT INTO employee VALUES ('Mark');
- Write an API to read all the record from this table (Read operation)   
- Write an API to insert new record into this table (Create operation) 
- Write an API to update one record in this table (Update operation)                                                                                                                                     
- Write an API to delete one record from this table (Delete operation)
'''

CREATE TABLE member (id INT(10), username VARCHAR(20), password VARCHAR(20), activated INT(10));

CREATE TABLE IF NOT EXISTS users (
id INT(11) NOT NULL AUTO_INCREMENT,
username VARCHAR(100) NOT NULL,
email VARCHAR(100) NOT NULL,
password VARCHAR(255) NOT NULL,
PRIMARY KEY (id)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS prof (
  id int(11) NOT NULL AUTO_INCREMENT,
  username varchar(20) NOT NULL,
  email text,
  fname text,
  lname text,
  country text,
  password text NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY username (username)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;
