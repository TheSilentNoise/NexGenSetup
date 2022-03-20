create database prod_iearn_tech;

create database dev_iearn_tech;

create database qa_iearn_tech;

create user 'dev_user'@'%' IDENTIFIED BY 'DevP@$$+';

create user 'qa_user'@'%' IDENTIFIED BY 'QaP@$$+';

create user 'prod_user'@'%' IDENTIFIED BY 'ProdP@$$+';

create user 'super_admin'@'%' IDENTIFIED BY 'Super@dmin+';

GRANT ALL PRIVILEGES ON dev_iearn_tech.* TO 'dev_user'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;

GRANT ALL PRIVILEGES ON qa_iearn_tech.* TO 'qa_user'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;

GRANT ALL PRIVILEGES ON prod_iearn_tech.* TO 'prod_user'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;

GRANT ALL PRIVILEGES ON *.* TO 'super_admin'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
