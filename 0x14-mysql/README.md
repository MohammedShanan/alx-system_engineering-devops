# Mysql
CREATE USER 'replica_user'@'%' IDENTIFIED BY 'replica_user';
GRANT ALL PRIVILEGES ON *.* TO 'holberton_user'@'localhost';
CREATE DATABASE tyrell_corp;
USE tyrell_corp;
DROP DATABASE tyrell_corp;
sudo ufw allow from 54.89.30.232 to any port 3306
mysql-bin.000001 154
scp db.sql ubuntu@54.89.30.232:/tmp/
sudo mysql tyrell_corp < /tmp/db.sql
SHOW SLAVE STATUS\G;
CHANGE MASTER TO
    MASTER_HOST='52.87.233.150',
    MASTER_USER='replica_user',
    MASTER_PASSWORD='replica_user',
    MASTER_LOG_FILE='mysql-bin.000001',
    MASTER_LOG_POS=3718;

CREATE TABLE users (
name varchar(30)
);