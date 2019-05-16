-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema nubank
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `nubank` ;

-- -----------------------------------------------------
-- Schema nubank
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `nubank` DEFAULT CHARACTER SET utf8 ;
USE `nubank` ;

-- -----------------------------------------------------
-- Table `nubank`.`movement`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `nubank`.`movement` ;

CREATE TABLE IF NOT EXISTS `nubank`.`movement` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `original_name` VARCHAR(200) NULL,
  `edited_name` VARCHAR(200) NULL,
  `date` DATETIME NULL,
  `value` DECIMAL(10,2) NULL,
  `status` ENUM('SHOW', 'HIDE') NULL,
  `type` ENUM('INCOME', 'OUTCOME', 'REVERSAL') NULL,
  `hash` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  INDEX `hash` (`hash` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `nubank`.`category`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `nubank`.`category` ;

CREATE TABLE IF NOT EXISTS `nubank`.`category` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `nubank`.`movement_has_category`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `nubank`.`movement_has_category` ;

CREATE TABLE IF NOT EXISTS `nubank`.`movement_has_category` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `movement_id` INT UNSIGNED NOT NULL,
  `category_id` INT NOT NULL,
  INDEX `fk_movement_has_category_movement_idx` (`movement_id` ASC),
  INDEX `fk_movement_has_category_category1_idx` (`category_id` ASC),
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_movement_has_category_movement`
    FOREIGN KEY (`movement_id`)
    REFERENCES `nubank`.`movement` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_movement_has_category_category1`
    FOREIGN KEY (`category_id`)
    REFERENCES `nubank`.`category` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
