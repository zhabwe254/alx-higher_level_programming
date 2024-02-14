-- Create table id_not_null with required constraints

CREATE TABLE IF NOT EXISTS `id_not_null` (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `name` VARCHAR(256) DEFAULT NULL
);
