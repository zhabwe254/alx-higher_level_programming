-- Create table unique_id with required constraints

CREATE TABLE IF NOT EXISTS `unique_id` (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `name` VARCHAR(256) DEFAULT NULL,
  UNIQUE KEY `id_UNIQUE` (`id`)
);
