-- create_database.sql
CREATE DATABASE IF NOT EXISTS apivinoc;
CREATE USER 'chokos'@'%' IDENTIFIED BY 'appvinoc';
GRANT ALL PRIVILEGES ON mydatabase.* TO 'chokos'@'%';
FLUSH PRIVILEGES;