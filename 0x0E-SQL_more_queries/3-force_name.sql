-- Create table force_name with required constraints

CREATE TABLE IF NOT EXISTS `force_name` 
(
	`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	`name` VARCHAR(256) NOT NULL
);
