-- Creates a new database and user, with full privileges on the new db
-- and SELECT privileges on the 'performance_schema' db.
-- New database: hbnb_test_db | New user: hbnb_test@localhost (hbnb_test_pwd)

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';
SET PASSWORD FOR 'hbnb_test'@'localhost' = 'hbnb_test_pwd';
GRANT ALL ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
