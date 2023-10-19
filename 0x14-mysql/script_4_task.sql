-- This for task 1 for the two server web-01(done) and web-02

CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';

GRANT REPLICATION CLIENT ON *. * TO 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';

-- This is for task 2 web-01

CREATE DATABASE IF NOT EXISTS `tyrell_corp`;

USE `tyrell_corp`;

DROP TABLE IF EXISTS `nexus6`;

CREATE TABLE `nexus6` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL,
  PRIMARY KEY (`id`)
);

LOCK TABLES `nexus6` WRITE;

INSERT INTO `nexus6` VALUES (1,'Leon');

UNLOCK TABLES;

GRANT SELECT ON `tyrell_corp`.`nexus6` TO 'holberton_user'@'localhost';

-- This is for task 3 web-01

CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'projectcorrection280hbtn';

GRANT REPLICATION SLAVE, REPLICATION CLIENT ON *. * TO 'replica_user'@'%' IDENTIFIED BY 'projectcorrection280hbtn';

GRANT SELECT ON `mysql`.`user` TO 'holberton_user'@'localhost';
