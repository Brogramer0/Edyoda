CREATE TABLE IF NOT EXISTS `customer` (
 `id` int(11) NOT NULL AUTO_INCREMENT,
 `Name` varchar(50) NOT NULL,
 `Gender` varchar(50) NOT NULL,
 `Age` INT NOT NULL,
 `phone_num` varchar(13) NOT NULL,
 `seat_no`  INT UNIQUE,
 `ticket_price` INT,

 PRIMARY KEY (`id`)
 );