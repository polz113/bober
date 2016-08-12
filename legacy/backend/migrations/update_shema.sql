/* Dodali smo še državo v težavnostne kategorije, da bi lahko določili težavnost na nivoju posamezne države */
ALTER TABLE  `competition_question_difficulty` ADD  `country_id` INT NOT NULL DEFAULT  '1' AFTER  `id`;
ALTER TABLE  `competition_question_difficulty` ADD INDEX (  `country_id` );
ALTER TABLE  `competition_question_difficulty` ADD FOREIGN KEY (  `country_id` ) REFERENCES  `bober`.`country` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION ;

/* Dodali smo še en nivo, torej sistemski administrator in administrator države */
UPDATE `profiles_fields` SET `range` = '1==Contestant;5==Teacher;10==Country Administrator;15==System Administrator' WHERE `varname` = 'user_role';

/* 2013-07-12: Dodali še relacijo pri težavnostnih stopnjah na državo) */
ALTER TABLE `competition_category` ADD `country_id` INT NOT NULL DEFAULT '1' AFTER `active` , ADD INDEX ( `country_id` ) ;
ALTER TABLE `competition_category` ADD FOREIGN KEY ( `country_id` ) REFERENCES `bober`.`country` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION ;

/* 2013-07-17 Spremembe zaradi načina shranjevanja vprašanj, vprašanja se da uporabiti na večih tekmovanjih */
ALTER TABLE `competition_question` CHANGE `question` `question_id` INT NOT NULL;
ALTER TABLE `competition_question` ADD INDEX ( `question_id` ) ;
RENAME TABLE `bober`.`competition_question_answer` TO `bober`.`question_answer` ;
SET FOREIGN_KEY_CHECKS=0;
SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";
DROP TABLE IF EXISTS `question`;
CREATE TABLE IF NOT EXISTS `question` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `country_id` int(11) NOT NULL,
  `type` int(1) NOT NULL DEFAULT '1' COMMENT '1==Normalna naloga v našem sistemu,2==Interaktivna naloga',
  `title` varchar(255) NOT NULL,
  `text` text,
  `data` text,
  `version` varchar(255) DEFAULT NULL,
  `verification_function_type` int(1) DEFAULT '0' COMMENT '0=Internal,1==JavaScript',
  `verification_function` text,
  `last_change_date` timestamp NULL DEFAULT NULL,
  `authors` text,
  PRIMARY KEY (`id`),
  KEY `country_id` (`country_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;
ALTER TABLE `question`
  ADD CONSTRAINT `question_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION;
SET FOREIGN_KEY_CHECKS=1;
ALTER TABLE `question_answer` DROP FOREIGN KEY `question_answer_ibfk_1` ;
ALTER TABLE question_answer DROP INDEX competition_question_id;
ALTER TABLE `question_answer` CHANGE `competition_question_id` `question_id` INT( 11 ) NOT NULL ;
ALTER TABLE `question_answer` ADD INDEX ( `question_id` ) ;
ALTER TABLE `question_answer` ADD FOREIGN KEY ( `question_id` ) REFERENCES `bober`.`question` ( `id` ) ON DELETE CASCADE ON UPDATE NO ACTION ;
ALTER TABLE `competition_question` ADD FOREIGN KEY ( `question_id` ) REFERENCES `bober`.`question` ( `id` ) ON DELETE CASCADE ON UPDATE NO ACTION ;
ALTER TABLE `competition_question_answer_translation` DROP FOREIGN KEY `competition_question_answer_translation_ibfk_1` ;
ALTER TABLE competition_question_answer_translation DROP INDEX competition_question_answer_id_2;
ALTER TABLE competition_question_answer_translation DROP INDEX competition_question_answer_id;
ALTER TABLE `competition_question_answer_translation` CHANGE `competition_question_answer_id` `question_answer_id` INT( 11 ) NOT NULL ;
ALTER TABLE `competition_question_answer_translation` ADD UNIQUE ( `question_answer_id` , `language_id` );
ALTER TABLE `competition_question_answer_translation` ADD INDEX ( `question_answer_id` ) ;
ALTER TABLE `competition_question_answer_translation` ADD FOREIGN KEY ( `question_answer_id` ) REFERENCES `bober`.`question_answer` ( `id` ) ON DELETE CASCADE ON UPDATE NO ACTION ;
RENAME TABLE `bober`.`competition_question_answer_translation` TO `bober`.`question_answer_translation` ;
ALTER TABLE `competition_question_translation` DROP FOREIGN KEY `competition_question_translation_ibfk_1` ;
ALTER TABLE competition_question_translation DROP INDEX competition_question_id_2;
ALTER TABLE competition_question_translation DROP INDEX competition_question_id;
ALTER TABLE `competition_question_translation` CHANGE `competition_question_id` `question_id` INT( 11 ) NOT NULL ;
ALTER TABLE `competition_question_translation` ADD INDEX ( `question_id` ) ;
ALTER TABLE `competition_question_translation` ADD UNIQUE ( `question_id` , `language_id` );
ALTER TABLE `competition_question_translation` ADD FOREIGN KEY ( `question_id` ) REFERENCES `bober`.`question` ( `id` ) ON DELETE CASCADE ON UPDATE NO ACTION ;
RENAME TABLE `bober`.`competition_question_translation` TO `bober`.`question_translation` ;

/* 2013-07-17 Dodatna relacija country_language, da vemo katere jezike imajo v posamezni državi */
SET FOREIGN_KEY_CHECKS=0;
SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";
CREATE TABLE IF NOT EXISTS `country_language` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `country_id` int(11) NOT NULL,
  `language_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `country_id_2` (`country_id`,`language_id`),
  KEY `country_id` (`country_id`),
  KEY `language_id` (`language_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;
ALTER TABLE `country_language`
  ADD CONSTRAINT `country_language_ibfk_2` FOREIGN KEY (`language_id`) REFERENCES `language` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `country_language_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION;
SET FOREIGN_KEY_CHECKS=1;
ALTER TABLE `question_translation` CHANGE `question` `text` TEXT CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ;
ALTER TABLE `question_translation` ADD `title` VARCHAR( 255 ) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL AFTER `language_id` ;
ALTER TABLE `question_translation` ADD `data` TEXT CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL ;
ALTER TABLE `question_translation` CHANGE `text` `text` TEXT CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL ;
SET FOREIGN_KEY_CHECKS=0;
SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";
CREATE TABLE IF NOT EXISTS `question_resource` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question_id` int(11) NOT NULL,
  `filename` varchar(512) NOT NULL,
  `data` longblob NOT NULL,
  PRIMARY KEY (`id`),
  KEY `question_id` (`question_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;
ALTER TABLE `question_resource`
  ADD CONSTRAINT `question_resource_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `question` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION;
SET FOREIGN_KEY_CHECKS=1;

/* 2013-07-17 12:40 Popravek sheme za odgovore na vprašanja */
ALTER TABLE competition_user_question_answer DROP INDEX competition_user_question_id_2;
ALTER TABLE `competition_user_question_answer` DROP FOREIGN KEY `competition_user_question_answer_ibfk_2` ;
ALTER TABLE competition_user_question_answer DROP INDEX competition_question_answer_id;
ALTER TABLE `competition_user_question_answer` CHANGE `competition_question_answer_id` `question_answer_id` INT( 11 ) NOT NULL ;
ALTER TABLE `competition_user_question_answer` ADD UNIQUE ( `competition_user_question_id` , `question_answer_id` );
ALTER TABLE `competition_user_question_answer` ADD INDEX ( `question_answer_id` ) ;
ALTER TABLE `competition_user_question_answer` ADD FOREIGN KEY ( `question_answer_id` ) REFERENCES `bober`.`question_answer` ( `id` ) ON DELETE CASCADE ON UPDATE NO ACTION ;
ALTER TABLE `competition_user_question` DROP FOREIGN KEY `competition_user_question_ibfk_3` ;
ALTER TABLE competition_user_question DROP INDEX competiton_question_answer_id ;
ALTER TABLE `competition_user_question` CHANGE `competiton_question_answer_id` `question_answer_id` INT( 11 ) NULL DEFAULT NULL ;
ALTER TABLE `competition_user_question` ADD INDEX ( `question_answer_id` ) ;
ALTER TABLE `competition_user_question` ADD FOREIGN KEY ( `question_answer_id` ) REFERENCES `bober`.`question_answer` ( `id` ) ON DELETE SET NULL ON UPDATE NO ACTION ;

/* 2013-07-18 13:06 Dodani file_type za question_resource */
ALTER TABLE  `question_resource` ADD  `file_type` VARCHAR( 255 ) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL AFTER  `filename`;

/* 2013-07-18 13:22 -- dodano za potrebe določanja nivoja izobrazbe na šoli */
ALTER TABLE `school` ADD `level_of_education` INT( 1 ) NOT NULL DEFAULT '0' COMMENT '0 == Osnovna šola, 1 == srednja šola' AFTER `school_category_id` ;

/* 2013-07-18 13:44 Nastavitev jezika uporabnika */
ALTER TABLE `profiles` ADD `language_id` INT NOT NULL DEFAULT '1' AFTER `country_id` , ADD INDEX ( `language_id` ) ;
ALTER TABLE `profiles` CHANGE `country_id` `country_id` INT( 10 ) NULL DEFAULT '1';
ALTER TABLE `profiles` CHANGE `language_id` `language_id` INT( 11 ) NULL DEFAULT '1';
ALTER TABLE `profiles` DROP FOREIGN KEY `profiles_ibfk_1` , ADD FOREIGN KEY ( `country_id` ) REFERENCES `bober`.`country` ( `id` ) ON DELETE SET NULL ON UPDATE NO ACTION ;
ALTER TABLE `profiles` ADD FOREIGN KEY ( `language_id` ) REFERENCES `bober`.`language` ( `id` ) ON DELETE SET NULL ON UPDATE NO ACTION ;
INSERT INTO `profiles_fields` (`id`, `varname`, `title`, `field_type`, `field_size`, `field_size_min`, `required`, `match`, `range`, `error_message`, `other_validator`, `default`, `widget`, `widgetparams`, `position`, `visible`) VALUES (5, 'language_id', 'Language', 'INTEGER', 10, 0, 1, '', '', 'Choose language', '', '1', 'UWrelBelongsTo', '{"modelName":"Language","optionName":"name","emptyField":"---","relationName":"language"}', 0, 3);
INSERT INTO `profiles_fields` (`id`, `varname`, `title`, `field_type`, `field_size`, `field_size_min`, `required`, `match`, `range`, `error_message`, `other_validator`, `default`, `widget`, `widgetparams`, `position`, `visible`) VALUES (6, 'timezone', 'Timezone', 'VARCHAR', 255, 0, 0, '', '', '', '', '', '', '', 0, 3);
ALTER TABLE `profiles` ADD `timezone` VARCHAR( 255 ) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL ;

/* 2013-07-22 15:46 Dodan path pri question resourcih */
ALTER TABLE `question_resource` ADD `path` VARCHAR( 250 ) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL AFTER `question_id` ;
ALTER TABLE `question_resource` CHANGE `filename` `filename` VARCHAR( 250 ) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ;
ALTER TABLE `question_resource` ADD UNIQUE ( `question_id` , `path` , `filename` );
ALTER TABLE `question_resource` CHANGE `path` `path` VARCHAR( 250 ) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '';

/* 2013-07-24 10:03 Dodan language_id pri virih vprašanj */
ALTER TABLE `question_resource` ADD `language_id` INT NOT NULL DEFAULT '1' AFTER `question_id` ;
ALTER TABLE question_resource DROP INDEX question_id_2;
ALTER TABLE `question_resource` ADD INDEX ( `language_id` ) ;
ALTER TABLE `question_resource` ADD UNIQUE ( `question_id` , `language_id` , `path` , `filename` );
ALTER TABLE `question_resource` ADD FOREIGN KEY ( `language_id` ) REFERENCES `bober`.`language` ( `id` ) ON DELETE CASCADE ON UPDATE NO ACTION ;

/*2013-07-25 14:08 Označitev namena resoursov */
ALTER TABLE `question_resource` ADD `type` INT( 1 ) NOT NULL AFTER `language_id` ;
ALTER TABLE `question_resource` CHANGE `type` `type` INT( 1 ) NOT NULL COMMENT '1 == task; 2 == solution; 3 == grader';
ALTER TABLE `question_resource` ADD `start_up` INT( 1 ) NOT NULL COMMENT '1 == start document of task';
ALTER TABLE `question_resource` CHANGE `start_up` `start_up` INT( 1 ) NOT NULL DEFAULT '0' COMMENT '1 == start document of task';
ALTER TABLE `question` CHANGE `last_change_date` `last_change_date` TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ;

/*2013-07-29 14:04 Dodali unikatni identifier naloge */
ALTER TABLE `question` ADD `identifier` VARCHAR( 255 ) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL AFTER `country_id` ;
ALTER TABLE `question` ADD UNIQUE (`country_id` ,`identifier`);

/*2013-08-19 14:25 Popravljena relacija v bazi*/
ALTER TABLE  `competition_category_school_mentor` DROP FOREIGN KEY  `competition_category_school_mentor_ibfk_2` ,
ADD FOREIGN KEY (  `competition_category_school_id` ) REFERENCES  `bober`.`competition_category_school` (
`id`
) ON DELETE CASCADE ON UPDATE NO ACTION ;

/*2013-08-22 14:02 v tabelo competiton dodali atribut časovno trajanje tekmovanja */
ALTER TABLE `competition` ADD `duration` INT NOT NULL DEFAULT '45';

/* 2013-08-20 15:26 Random seed for question randomization */
ALTER TABLE `competition_user_question` ADD `random_seed` DECIMAL( 11, 10 ) NOT NULL DEFAULT '0.0' AFTER `last_change` ) ON DELETE CASCADE ON UPDATE NO ACTION ;

/* 2013-09-05 18:23 Phone number user field */
INSERT INTO `profiles_fields` (`id`, `varname`, `title`, `field_type`, `field_size`, `field_size_min`, `required`, `match`, `range`, `error_message`, `other_validator`, `default`, `widget`, `widgetparams`, `position`, `visible`) VALUES
(7, 'phone_number', 'Phone number', 'VARCHAR', 255, 0, 0, '', '', 'Wrong phone number', '', '', '', '', 0, 3);
ALTER TABLE `profiles` ADD `phone_number` VARCHAR( 255 ) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '';

/* 2013-09-05 19:35 Filed gender added to table competition-user*/
ALTER TABLE  `competition_user` ADD  `gender` TINYINT( 1 ) NOT NULL DEFAULT  '0' AFTER  `first_name`;

/* 2013-10-05 10:56 Added support for custom css push to each question */
ALTER TABLE `question` ADD `css` TEXT NULL DEFAULT NULL AFTER `authors`;

/* 2013-10-19 Session moved to database */
CREATE TABLE IF NOT EXISTS `YiiSession` (
  `id` char(32) NOT NULL,
  `expire` int(11) DEFAULT NULL,
  `data` longblob,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/* 2013-11-21 dodatni indexi za hitrejše poizvedbe */
ALTER TABLE `competition_category` ADD INDEX(`name`);
ALTER TABLE `competition` ADD INDEX(`name`);
ALTER TABLE `profiles` ADD INDEX( `first_name`, `last_name`);
ALTER TABLE `competition_category` ADD INDEX( `id`, `name`);

/* 2013-11-27 dodani atributi pri tekmovanju za kontrolo prikaza rezultatov, priznanj in napredovanja na naslednji nivo */
ALTER TABLE `competition` ADD `timestamp_mentor_results` DATETIME NULL DEFAULT NULL;
ALTER TABLE `competition` ADD `timestamp_mentor_awards` DATETIME NULL DEFAULT NULL;
ALTER TABLE `competition` ADD `timestamp_mentor_advancing_to_next_level` DATETIME NULL DEFAULT NULL;

/* 2014-01-18 IP tracking */
ALTER TABLE `competition_user` ADD `ip_start` VARCHAR( 15 ) NULL DEFAULT NULL ,
ADD `ip_stop` VARCHAR( 15 ) NULL DEFAULT NULL