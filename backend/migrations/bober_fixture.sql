-- MySQL dump 10.13  Distrib 5.5.38, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: bober
-- ------------------------------------------------------
-- Server version	5.5.38-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `YiiSession`
--

DROP TABLE IF EXISTS `YiiSession`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `YiiSession` (
  `id` char(32) NOT NULL,
  `expire` int(11) DEFAULT NULL,
  `data` longblob,
  PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `YiiSession`
--

LOCK TABLES `YiiSession` WRITE;
/*!40000 ALTER TABLE `YiiSession` DISABLE KEYS */;
INSERT INTO `YiiSession` VALUES ('03ibk95ggbosgepeughbt89cn6',1408355167,''),('12o6cifmsusk1g6klbvtcr8596',1408354727,'competition_user_id|s:3:\"834\";'),('1j51471gpvm02i2atbqqu19oq3',1408354727,'competition_user_id|s:3:\"835\";'),('27k09lafbgt5efujfencai6ft2',1408354725,'competition_user_id|s:3:\"829\";'),('37ng3ofmh7dh8a36brpndb7776',1408354727,'competition_user_id|s:3:\"837\";'),('3ebassoi58frjggt6e0sesfsf6',1408355167,''),('6dddeco9771ooaqgeoaof3ocl1',1408355165,''),('78d4i75ksmbdev0990kou8hrq4',1408355166,''),('99pg299ua42p4hi2tb272u8bg3',1408354727,'competition_user_id|s:3:\"836\";'),('9uqahm9jirvguk9ll5lvq1ib23',1408355167,''),('c4or5fhfg6elbsd8k55nqlkio7',1408354727,'competition_user_id|s:3:\"838\";'),('e7sd81is8q6lv7t2et04l2oej1',1408355168,''),('eepemkgc26s2d4eihbkslc1f77',1408355167,''),('eo3i6fl5faagksbtb2l3lnh511',1408355166,''),('eve98r63bcf563eeo9hrr64h70',1408482729,''),('j3ivmesfue9cbif2b0628k5oa3',1408354727,'competition_user_id|s:3:\"833\";'),('ku1kresprhpv6vc243o9kjlm73',1408355167,''),('l1lgbugughv5lvjlgbqb802ks0',1408354726,'competition_user_id|s:3:\"831\";'),('o9ek8kmir16lob348ajqikf1q2',1408482845,'7440c6cde45975f2d04f3e79977466f1__returnUrl|s:28:\"/index.php/competition/admin\";7440c6cde45975f2d04f3e79977466f1__id|s:1:\"1\";7440c6cde45975f2d04f3e79977466f1__name|s:5:\"admin\";7440c6cde45975f2d04f3e79977466f1__states|a:0:{}7440c6cde45975f2d04f3e79977466f1email|s:17:\"admin@example.net\";7440c6cde45975f2d04f3e79977466f1username|s:5:\"admin\";7440c6cde45975f2d04f3e79977466f1create_at|s:19:\"2013-11-09 19:19:50\";7440c6cde45975f2d04f3e79977466f1lastvisit_at|s:19:\"0000-00-00 00:00:00\";7440c6cde45975f2d04f3e79977466f1user_id|s:1:\"1\";7440c6cde45975f2d04f3e79977466f1first_name|s:5:\"Admin\";7440c6cde45975f2d04f3e79977466f1last_name|s:5:\"admin\";7440c6cde45975f2d04f3e79977466f1country_id|s:1:\"2\";7440c6cde45975f2d04f3e79977466f1language_id|s:1:\"3\";7440c6cde45975f2d04f3e79977466f1user_role|s:2:\"15\";7440c6cde45975f2d04f3e79977466f1timezone|s:0:\"\";7440c6cde45975f2d04f3e79977466f1phone_number|s:0:\"\";'),('q9spbq54ma5sdmu660pcjodlp4',1408355167,''),('rn07k8vgjhrr5ribscmajgbig1',1408354726,'competition_user_id|s:3:\"832\";'),('sjgochr8ejdabglbfqf95ebsn7',1408539017,'7440c6cde45975f2d04f3e79977466f1__id|s:1:\"1\";7440c6cde45975f2d04f3e79977466f1__name|s:5:\"admin\";7440c6cde45975f2d04f3e79977466f1__states|a:0:{}7440c6cde45975f2d04f3e79977466f1email|s:17:\"admin@example.net\";7440c6cde45975f2d04f3e79977466f1username|s:5:\"admin\";7440c6cde45975f2d04f3e79977466f1create_at|s:19:\"2013-11-09 19:19:50\";7440c6cde45975f2d04f3e79977466f1lastvisit_at|s:19:\"0000-00-00 00:00:00\";7440c6cde45975f2d04f3e79977466f1user_id|s:1:\"1\";7440c6cde45975f2d04f3e79977466f1first_name|s:5:\"Admin\";7440c6cde45975f2d04f3e79977466f1last_name|s:5:\"admin\";7440c6cde45975f2d04f3e79977466f1country_id|s:1:\"2\";7440c6cde45975f2d04f3e79977466f1language_id|s:1:\"3\";7440c6cde45975f2d04f3e79977466f1user_role|s:2:\"15\";7440c6cde45975f2d04f3e79977466f1timezone|s:0:\"\";7440c6cde45975f2d04f3e79977466f1phone_number|s:0:\"\";7440c6cde45975f2d04f3e79977466f1__returnUrl|s:21:\"/index.php/site/index\";'),('t8mtvbeojjfpmc8cm38tb6j2u0',1408381403,''),('te8mfnfpcql0e6ecgmh66kdj40',1408381778,'faba2fa98de5af4b5945951de38423df__returnUrl|s:48:\"/index.php/competitionCategorySchoolMentor/admin\";'),('uteqdfs967bh9bnaigokd6se91',1408354726,'competition_user_id|s:3:\"830\";');
/*!40000 ALTER TABLE `YiiSession` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `award`
--

DROP TABLE IF EXISTS `award`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `award` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `competition_user_id` int(11) NOT NULL,
  `type` int(11) NOT NULL COMMENT '1 == Priznanje za udeleÅ¾bo, 5 == Bronasto, 10 == Srebrno, 15 == Zlato',
  `serial` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `serial` (`serial`),
  UNIQUE KEY `competition_user_id_type` (`competition_user_id`,`type`),
  KEY `competition_user_id` (`competition_user_id`),
  CONSTRAINT `award_ibfk_1` FOREIGN KEY (`competition_user_id`) REFERENCES `competition_user` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `award`
--

LOCK TABLES `award` WRITE;
/*!40000 ALTER TABLE `award` DISABLE KEYS */;
/*!40000 ALTER TABLE `award` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `competition`
--

DROP TABLE IF EXISTS `competition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `competition` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `active` tinyint(1) NOT NULL DEFAULT '0',
  `timestamp_start` datetime NOT NULL,
  `timestamp_stop` datetime NOT NULL,
  `type` int(2) NOT NULL DEFAULT '1' COMMENT '1==Å¡olsko tekmovanje;2 == drÅ¾avno tekmovanje',
  `public_access` tinyint(1) NOT NULL DEFAULT '0',
  `duration` int(11) NOT NULL DEFAULT '45',
  `timestamp_mentor_results` datetime DEFAULT NULL,
  `timestamp_mentor_awards` datetime DEFAULT NULL,
  `timestamp_mentor_advancing_to_next_level` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `name` (`name`)
) AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `competition`
--

LOCK TABLES `competition` WRITE;
/*!40000 ALTER TABLE `competition` DISABLE KEYS */;
INSERT INTO `competition` VALUES (5,'Bober - test',1,'2014-08-01 01:55:00','2015-01-01 01:55:00',1,1,45,NULL,NULL,NULL);
/*!40000 ALTER TABLE `competition` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `competition_category`
--

DROP TABLE IF EXISTS `competition_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `competition_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `active` tinyint(1) NOT NULL DEFAULT '1',
  `country_id` int(11) NOT NULL DEFAULT '1',
  `name` varchar(255) NOT NULL,
  `level_of_education` int(1) NOT NULL DEFAULT '0' COMMENT '0 == Osnovna Å¡ola, 1 == srednja Å¡ola',
  `class_from` int(3) NOT NULL,
  `class_to` int(3) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `country_id` (`country_id`),
  KEY `name` (`name`),
  KEY `id` (`id`,`name`),
  CONSTRAINT `competition_category_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `competition_category`
--

LOCK TABLES `competition_category` WRITE;
/*!40000 ALTER TABLE `competition_category` DISABLE KEYS */;
INSERT INTO `competition_category` VALUES (10,1,4,'Benjamin',1,5,6),(11,1,4,'Cadet',1,7,8),(12,1,4,'Senior',2,1,2);
/*!40000 ALTER TABLE `competition_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `competition_category_active`
--

DROP TABLE IF EXISTS `competition_category_active`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `competition_category_active` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `competition_id` int(11) NOT NULL,
  `competition_category_id` int(11) NOT NULL,
  `number_of_questions` int(11) DEFAULT NULL,
  `minimum_points_for_bronze_award` decimal(10,4) DEFAULT NULL,
  `maximum_bronze_awards` int(11) NOT NULL DEFAULT '0',
  `minimum_points_for_silver_award` decimal(10,4) DEFAULT NULL,
  `maximum_silver_awards` int(11) NOT NULL DEFAULT '0',
  `minimum_points_for_gold_award` decimal(10,4) DEFAULT NULL,
  `maximum_gold_awards` int(11) NOT NULL DEFAULT '0',
  `total_contestants_to_advance_to_next_level` int(11) NOT NULL DEFAULT '0',
  `available_contest_time` int(11) NOT NULL DEFAULT '45',
  PRIMARY KEY (`id`),
  UNIQUE KEY `competition_id_competition_category_id` (`competition_id`,`competition_category_id`),
  KEY `competition_id` (`competition_id`),
  KEY `competition_category_id` (`competition_category_id`),
  CONSTRAINT `competition_category_active_ibfk_1` FOREIGN KEY (`competition_id`) REFERENCES `competition` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `competition_category_active_ibfk_2` FOREIGN KEY (`competition_category_id`) REFERENCES `competition_category` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `competition_category_active`
--

LOCK TABLES `competition_category_active` WRITE;
/*!40000 ALTER TABLE `competition_category_active` DISABLE KEYS */;
/*!40000 ALTER TABLE `competition_category_active` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `competition_category_school`
--

DROP TABLE IF EXISTS `competition_category_school`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `competition_category_school` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `competition_id` int(11) NOT NULL,
  `competition_category_id` int(11) NOT NULL,
  `school_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `competition_id_2` (`competition_id`,`competition_category_id`,`school_id`),
  KEY `competition_id` (`competition_id`),
  KEY `competition_category_id` (`competition_category_id`),
  KEY `school_id` (`school_id`),
  CONSTRAINT `competition_category_school_ibfk_1` FOREIGN KEY (`competition_id`) REFERENCES `competition` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `competition_category_school_ibfk_2` FOREIGN KEY (`competition_category_id`) REFERENCES `competition_category` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `competition_category_school_ibfk_3` FOREIGN KEY (`school_id`) REFERENCES `school` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) AUTO_INCREMENT=1659 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `competition_category_school`
--

LOCK TABLES `competition_category_school` WRITE;
/*!40000 ALTER TABLE `competition_category_school` DISABLE KEYS */;
INSERT INTO `competition_category_school` VALUES (1658,5,10,1058);
/*!40000 ALTER TABLE `competition_category_school` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `competition_category_school_mentor`
--

DROP TABLE IF EXISTS `competition_category_school_mentor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `competition_category_school_mentor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `competition_category_school_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `access_code` varchar(20) DEFAULT NULL,
  `disqualified` tinyint(1) NOT NULL DEFAULT '0',
  `disqualified_by` int(11) DEFAULT NULL,
  `disqualified_reason` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `competition_category_school_id_2` (`competition_category_school_id`,`user_id`),
  UNIQUE KEY `access_code` (`access_code`),
  KEY `competition_category_school_id` (`competition_category_school_id`),
  KEY `user_id` (`user_id`),
  KEY `disqualified_by` (`disqualified_by`),
  CONSTRAINT `competition_category_school_mentor_ibfk_1` FOREIGN KEY (`disqualified_by`) REFERENCES `users` (`id`) ON DELETE SET NULL ON UPDATE NO ACTION,
  CONSTRAINT `competition_category_school_mentor_ibfk_3` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `competition_category_school_mentor_ibfk_4` FOREIGN KEY (`competition_category_school_id`) REFERENCES `competition_category_school` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) AUTO_INCREMENT=552 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `competition_category_school_mentor`
--

LOCK TABLES `competition_category_school_mentor` WRITE;
/*!40000 ALTER TABLE `competition_category_school_mentor` DISABLE KEYS */;
INSERT INTO `competition_category_school_mentor` VALUES (550,1658,2,'gV9mW3qy4G',0,NULL,'');
/*!40000 ALTER TABLE `competition_category_school_mentor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `competition_category_translation`
--

DROP TABLE IF EXISTS `competition_category_translation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `competition_category_translation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `competition_category_id` int(11) NOT NULL,
  `language_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `competition_category_id_language_id` (`competition_category_id`,`language_id`),
  KEY `competition_category_id` (`competition_category_id`),
  KEY `language_id` (`language_id`),
  CONSTRAINT `competition_category_translation_ibfk_1` FOREIGN KEY (`competition_category_id`) REFERENCES `competition_category` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `competition_category_translation_ibfk_2` FOREIGN KEY (`language_id`) REFERENCES `language` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `competition_category_translation`
--

LOCK TABLES `competition_category_translation` WRITE;
/*!40000 ALTER TABLE `competition_category_translation` DISABLE KEYS */;
/*!40000 ALTER TABLE `competition_category_translation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `competition_committee`
--

DROP TABLE IF EXISTS `competition_committee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `competition_committee` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `competition_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `president` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `competition_id_2` (`competition_id`,`user_id`),
  KEY `competition_id` (`competition_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `competition_committee_ibfk_1` FOREIGN KEY (`competition_id`) REFERENCES `competition` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `competition_committee_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `competition_committee`
--

LOCK TABLES `competition_committee` WRITE;
/*!40000 ALTER TABLE `competition_committee` DISABLE KEYS */;
/*!40000 ALTER TABLE `competition_committee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `competition_country`
--

DROP TABLE IF EXISTS `competition_country`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `competition_country` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `competition_id` int(11) NOT NULL,
  `country_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `competition_id_2` (`competition_id`,`country_id`),
  KEY `competition_id` (`competition_id`),
  KEY `country_id` (`country_id`),
  CONSTRAINT `competition_country_ibfk_1` FOREIGN KEY (`competition_id`) REFERENCES `competition` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `competition_country_ibfk_2` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `competition_country`
--

LOCK TABLES `competition_country` WRITE;
/*!40000 ALTER TABLE `competition_country` DISABLE KEYS */;
/*!40000 ALTER TABLE `competition_country` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `competition_question`
--

DROP TABLE IF EXISTS `competition_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `competition_question` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `competition_id` int(11) NOT NULL,
  `question_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `competition_id` (`competition_id`),
  KEY `question_id` (`question_id`),
  CONSTRAINT `competition_question_ibfk_2` FOREIGN KEY (`competition_id`) REFERENCES `competition` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `competition_question_ibfk_3` FOREIGN KEY (`question_id`) REFERENCES `question` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) AUTO_INCREMENT=434 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `competition_question`
--

LOCK TABLES `competition_question` WRITE;
/*!40000 ALTER TABLE `competition_question` DISABLE KEYS */;
INSERT INTO `competition_question` VALUES (431,5,94),(433,5,260);
/*!40000 ALTER TABLE `competition_question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `competition_question_category`
--

DROP TABLE IF EXISTS `competition_question_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `competition_question_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `competition_question_id` int(11) NOT NULL,
  `competition_category_id` int(11) NOT NULL,
  `competiton_question_difficulty_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `competition_question_id_2` (`competition_question_id`,`competition_category_id`),
  KEY `competition_question_id` (`competition_question_id`),
  KEY `competition_category_id` (`competition_category_id`),
  KEY `competiton_question_difficulty` (`competiton_question_difficulty_id`),
  CONSTRAINT `competition_question_category_ibfk_1` FOREIGN KEY (`competition_question_id`) REFERENCES `competition_question` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `competition_question_category_ibfk_2` FOREIGN KEY (`competition_category_id`) REFERENCES `competition_category` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `competition_question_category_ibfk_3` FOREIGN KEY (`competiton_question_difficulty_id`) REFERENCES `competition_question_difficulty` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) AUTO_INCREMENT=624 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `competition_question_category`
--

LOCK TABLES `competition_question_category` WRITE;
/*!40000 ALTER TABLE `competition_question_category` DISABLE KEYS */;
INSERT INTO `competition_question_category` VALUES (620,431,11,4),(621,433,12,5),(622,431,10,3),(623,433,10,4);
/*!40000 ALTER TABLE `competition_question_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `competition_question_difficulty`
--

DROP TABLE IF EXISTS `competition_question_difficulty`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `competition_question_difficulty` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `country_id` int(11) NOT NULL DEFAULT '1',
  `active` tinyint(1) NOT NULL DEFAULT '1',
  `name` varchar(255) NOT NULL,
  `correct_answer_points` decimal(10,4) NOT NULL DEFAULT '0.0000',
  `wrong_answer_points` decimal(10,4) NOT NULL DEFAULT '0.0000',
  PRIMARY KEY (`id`),
  KEY `country_id` (`country_id`),
  CONSTRAINT `competition_question_difficulty_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `competition_question_difficulty`
--

LOCK TABLES `competition_question_difficulty` WRITE;
/*!40000 ALTER TABLE `competition_question_difficulty` DISABLE KEYS */;
INSERT INTO `competition_question_difficulty` VALUES (3,1,1,'Lahka',6.0000,-2.0000),(4,1,1,'Srednja',9.0000,-3.0000),(5,1,1,'TeÅ¾ka',12.0000,-4.0000);
/*!40000 ALTER TABLE `competition_question_difficulty` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `competition_question_difficulty_translation`
--

DROP TABLE IF EXISTS `competition_question_difficulty_translation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `competition_question_difficulty_translation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `competition_question_difficulty_id` int(11) NOT NULL,
  `language_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `competition_question_difficult_2` (`competition_question_difficulty_id`,`language_id`),
  KEY `competition_question_difficulty_id` (`competition_question_difficulty_id`),
  KEY `language_id` (`language_id`),
  CONSTRAINT `competition_question_difficulty_translation_ibfk_1` FOREIGN KEY (`competition_question_difficulty_id`) REFERENCES `competition_question_difficulty` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `competition_question_difficulty_translation_ibfk_2` FOREIGN KEY (`language_id`) REFERENCES `language` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `competition_question_difficulty_translation`
--

LOCK TABLES `competition_question_difficulty_translation` WRITE;
/*!40000 ALTER TABLE `competition_question_difficulty_translation` DISABLE KEYS */;
/*!40000 ALTER TABLE `competition_question_difficulty_translation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `competition_translation`
--

DROP TABLE IF EXISTS `competition_translation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `competition_translation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `competition_id` int(11) NOT NULL,
  `language_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `competition_id_2` (`competition_id`,`language_id`),
  KEY `competition_id` (`competition_id`),
  KEY `language_id` (`language_id`),
  CONSTRAINT `competition_translation_ibfk_1` FOREIGN KEY (`competition_id`) REFERENCES `competition` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `competition_translation_ibfk_2` FOREIGN KEY (`language_id`) REFERENCES `language` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `competition_translation`
--

LOCK TABLES `competition_translation` WRITE;
/*!40000 ALTER TABLE `competition_translation` DISABLE KEYS */;
/*!40000 ALTER TABLE `competition_translation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `competition_user`
--

DROP TABLE IF EXISTS `competition_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `competition_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `competition_id` int(11) NOT NULL,
  `competition_category_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `competition_category_school_mentor_id` int(11) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `first_name` varchar(255) DEFAULT NULL,
  `gender` tinyint(1) NOT NULL DEFAULT '0',
  `class` varchar(20) DEFAULT NULL,
  `school_id` int(11) NOT NULL,
  `disqualified_request` tinyint(1) NOT NULL DEFAULT '0',
  `disqualified_request_by` int(11) DEFAULT NULL,
  `disqualified` tinyint(1) NOT NULL DEFAULT '0',
  `disqualified_by` int(11) DEFAULT NULL,
  `disqualified_reason` text,
  `advancing_to_next_level` tinyint(1) NOT NULL DEFAULT '0',
  `award` int(2) DEFAULT NULL COMMENT '1 == Priznanje za udeleÅ¾bo, 5 == Bronasto, 10 == Srebrno, 15 == Zlato',
  `start_time` datetime DEFAULT NULL,
  `finish_time` datetime DEFAULT NULL,
  `finished` tinyint(1) NOT NULL DEFAULT '0',
  `total_points_via_answers` decimal(10,4) NOT NULL DEFAULT '0.0000',
  `total_points_via_time` decimal(10,4) NOT NULL DEFAULT '0.0000',
  `total_points_manual` decimal(10,4) NOT NULL DEFAULT '0.0000',
  `total_points` decimal(10,4) NOT NULL DEFAULT '0.0000',
  `ip_start` varchar(15) DEFAULT NULL,
  `ip_stop` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `competition_id_2` (`competition_id`,`competition_category_id`,`user_id`,`competition_category_school_mentor_id`,`last_name`,`first_name`,`class`,`school_id`),
  KEY `user_id` (`user_id`),
  KEY `competition_id` (`competition_id`),
  KEY `competition_category_id` (`competition_category_id`),
  KEY `competition_category_school_mentor_id` (`competition_category_school_mentor_id`),
  KEY `school_id` (`school_id`),
  KEY `disqualified_request_by` (`disqualified_request_by`),
  KEY `disqualified_by` (`disqualified_by`),
  CONSTRAINT `competition_user_ibfk_1` FOREIGN KEY (`competition_id`) REFERENCES `competition` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `competition_user_ibfk_2` FOREIGN KEY (`competition_category_id`) REFERENCES `competition_category` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `competition_user_ibfk_3` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE SET NULL ON UPDATE NO ACTION,
  CONSTRAINT `competition_user_ibfk_4` FOREIGN KEY (`competition_category_school_mentor_id`) REFERENCES `competition_category_school_mentor` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `competition_user_ibfk_5` FOREIGN KEY (`school_id`) REFERENCES `school` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `competition_user_ibfk_6` FOREIGN KEY (`disqualified_request_by`) REFERENCES `users` (`id`) ON DELETE SET NULL ON UPDATE NO ACTION,
  CONSTRAINT `competition_user_ibfk_7` FOREIGN KEY (`disqualified_by`) REFERENCES `users` (`id`) ON DELETE SET NULL ON UPDATE NO ACTION
) AUTO_INCREMENT=853 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `competition_user`
--

LOCK TABLES `competition_user` WRITE;
/*!40000 ALTER TABLE `competition_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `competition_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `competition_user_question`
--

DROP TABLE IF EXISTS `competition_user_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `competition_user_question` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `competition_user_id` int(11) NOT NULL,
  `competition_question_id` int(11) NOT NULL,
  `ordering` int(11) NOT NULL,
  `question_answer_id` int(11) DEFAULT NULL,
  `last_change` datetime DEFAULT NULL,
  `random_seed` decimal(11,10) NOT NULL DEFAULT '0.0000000000',
  `custom_answer` text COMMENT 'For future usage',
  PRIMARY KEY (`id`),
  KEY `competition_user_id` (`competition_user_id`),
  KEY `competition_question_id` (`competition_question_id`),
  KEY `question_answer_id` (`question_answer_id`),
  CONSTRAINT `competition_user_question_ibfk_1` FOREIGN KEY (`competition_user_id`) REFERENCES `competition_user` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `competition_user_question_ibfk_2` FOREIGN KEY (`competition_question_id`) REFERENCES `competition_question` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `competition_user_question_ibfk_3` FOREIGN KEY (`question_answer_id`) REFERENCES `question_answer` (`id`) ON DELETE SET NULL ON UPDATE NO ACTION
) AUTO_INCREMENT=262 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `competition_user_question`
--

LOCK TABLES `competition_user_question` WRITE;
/*!40000 ALTER TABLE `competition_user_question` DISABLE KEYS */;
/*!40000 ALTER TABLE `competition_user_question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `competition_user_question_answer`
--

DROP TABLE IF EXISTS `competition_user_question_answer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `competition_user_question_answer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `competition_user_question_id` int(11) NOT NULL,
  `question_answer_id` int(11) NOT NULL,
  `ordering` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `competition_user_question_id_2` (`competition_user_question_id`,`question_answer_id`),
  KEY `competition_user_question_id` (`competition_user_question_id`),
  KEY `question_answer_id` (`question_answer_id`),
  CONSTRAINT `competition_user_question_answer_ibfk_1` FOREIGN KEY (`competition_user_question_id`) REFERENCES `competition_user_question` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `competition_user_question_answer_ibfk_2` FOREIGN KEY (`question_answer_id`) REFERENCES `question_answer` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `competition_user_question_answer`
--

LOCK TABLES `competition_user_question_answer` WRITE;
/*!40000 ALTER TABLE `competition_user_question_answer` DISABLE KEYS */;
/*!40000 ALTER TABLE `competition_user_question_answer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `country`
--

DROP TABLE IF EXISTS `country`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `country` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `country` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `country` (`country`)
) AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `country`
--

LOCK TABLES `country` WRITE;
/*!40000 ALTER TABLE `country` DISABLE KEYS */;
INSERT INTO `country` VALUES (4,'Butalia'),(2,'Cambodia'),(1,'Slovenija'),(3,'Srbija');
/*!40000 ALTER TABLE `country` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `country_administrator`
--

DROP TABLE IF EXISTS `country_administrator`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `country_administrator` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `country_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `country_id_2` (`country_id`,`user_id`),
  KEY `country_id` (`country_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `country_administrator_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `country_administrator_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `country_administrator`
--

LOCK TABLES `country_administrator` WRITE;
/*!40000 ALTER TABLE `country_administrator` DISABLE KEYS */;
INSERT INTO `country_administrator` VALUES (1,1,1),(2,3,1),(3,4,1);
/*!40000 ALTER TABLE `country_administrator` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `country_language`
--

DROP TABLE IF EXISTS `country_language`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `country_language` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `country_id` int(11) NOT NULL,
  `language_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `country_id_2` (`country_id`,`language_id`),
  KEY `country_id` (`country_id`),
  KEY `language_id` (`language_id`),
  CONSTRAINT `country_language_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `country_language_ibfk_2` FOREIGN KEY (`language_id`) REFERENCES `language` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `country_language`
--

LOCK TABLES `country_language` WRITE;
/*!40000 ALTER TABLE `country_language` DISABLE KEYS */;
/*!40000 ALTER TABLE `country_language` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `language`
--

DROP TABLE IF EXISTS `language`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `language` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `short` varchar(5) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`,`short`)
) AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `language`
--

LOCK TABLES `language` WRITE;
/*!40000 ALTER TABLE `language` DISABLE KEYS */;
INSERT INTO `language` VALUES (2,'English','en'),(1,'SlovenÅ¡Äina','sl'),(3,'Srpski','sr');
/*!40000 ALTER TABLE `language` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `municipality`
--

DROP TABLE IF EXISTS `municipality`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `municipality` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `country_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`,`country_id`),
  KEY `country_id` (`country_id`),
  CONSTRAINT `municipality_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) AUTO_INCREMENT=262 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `municipality`
--

LOCK TABLES `municipality` WRITE;
/*!40000 ALTER TABLE `municipality` DISABLE KEYS */;
INSERT INTO `municipality` VALUES (261,'Butale',4);
/*!40000 ALTER TABLE `municipality` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profiles`
--

DROP TABLE IF EXISTS `profiles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `profiles` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `country_id` int(10) DEFAULT '1',
  `language_id` int(11) DEFAULT '1',
  `user_role` int(1) NOT NULL DEFAULT '1',
  `timezone` varchar(255) DEFAULT NULL,
  `phone_number` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`user_id`),
  KEY `country_id` (`country_id`),
  KEY `language_id` (`language_id`),
  KEY `first_name` (`first_name`,`last_name`),
  CONSTRAINT `profiles_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `profiles_ibfk_3` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`) ON DELETE SET NULL ON UPDATE NO ACTION,
  CONSTRAINT `profiles_ibfk_4` FOREIGN KEY (`language_id`) REFERENCES `language` (`id`) ON DELETE SET NULL ON UPDATE NO ACTION
) AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profiles`
--

LOCK TABLES `profiles` WRITE;
/*!40000 ALTER TABLE `profiles` DISABLE KEYS */;
INSERT INTO `profiles` VALUES (1,'Admin','admin',2,3,15,'',''),(2,'Kozmijan','Buta',4,1,5,'','');
/*!40000 ALTER TABLE `profiles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profiles_fields`
--

DROP TABLE IF EXISTS `profiles_fields`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `profiles_fields` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `varname` varchar(50) NOT NULL DEFAULT '',
  `title` varchar(255) NOT NULL DEFAULT '',
  `field_type` varchar(50) NOT NULL DEFAULT '',
  `field_size` int(3) NOT NULL DEFAULT '0',
  `field_size_min` int(3) NOT NULL DEFAULT '0',
  `required` int(1) NOT NULL DEFAULT '0',
  `match` varchar(255) NOT NULL DEFAULT '',
  `range` varchar(255) NOT NULL DEFAULT '',
  `error_message` varchar(255) NOT NULL DEFAULT '',
  `other_validator` text,
  `default` varchar(255) NOT NULL DEFAULT '',
  `widget` varchar(255) NOT NULL DEFAULT '',
  `widgetparams` text,
  `position` int(3) NOT NULL DEFAULT '0',
  `visible` int(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profiles_fields`
--

LOCK TABLES `profiles_fields` WRITE;
/*!40000 ALTER TABLE `profiles_fields` DISABLE KEYS */;
INSERT INTO `profiles_fields` VALUES (1,'first_name','First Name','VARCHAR',255,3,2,'','','Incorrect First Name (length between 3 and 50 characters).','','','','',1,3),(2,'last_name','Last Name','VARCHAR',255,3,2,'','','Incorrect Last Name (length between 3 and 50 characters).','','','','',2,3),(3,'country_id','Country','INTEGER',10,0,1,'','','Choose country','','1','UWrelBelongsTo','{\"modelName\":\"Country\",\"optionName\":\"country\",\"emptyField\":\"---\",\"relationName\":\"country\"}',0,3),(4,'user_role','User Role','INTEGER',1,1,3,'','1==Contestant;5==Teacher;10==Country Administrator;15==System Administrator','Invalid user role.','','1','','',0,1),(5,'language_id','Language','INTEGER',10,0,1,'','','Choose language','','1','UWrelBelongsTo','{\"modelName\":\"Language\",\"optionName\":\"name\",\"emptyField\":\"---\",\"relationName\":\"language\"}',0,3),(6,'timezone','Timezone','VARCHAR',255,0,0,'','','','','','','',0,3),(7,'phone_number','Phone number','VARCHAR',255,0,0,'','','Wrong phone number','','','','',0,3);
/*!40000 ALTER TABLE `profiles_fields` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question`
--

DROP TABLE IF EXISTS `question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `question` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `country_id` int(11) NOT NULL,
  `identifier` varchar(255) NOT NULL,
  `type` int(1) NOT NULL DEFAULT '1' COMMENT '1==Normalna naloga v naÅ¡em sistemu,2==Interaktivna naloga',
  `title` varchar(255) NOT NULL,
  `text` text,
  `data` text,
  `version` varchar(255) DEFAULT NULL,
  `verification_function_type` int(1) DEFAULT '0' COMMENT '0=Internal,1==JavaScript',
  `verification_function` text,
  `last_change_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `authors` text,
  `css` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `country_id_2` (`country_id`,`identifier`),
  KEY `country_id` (`country_id`),
  CONSTRAINT `question_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) AUTO_INCREMENT=272 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question`
--

LOCK TABLES `question` WRITE;
/*!40000 ALTER TABLE `question` DISABLE KEYS */;
INSERT INTO `question` VALUES (94,4,'50',2,'ÄŒrviva vrtavka','',' ie 6 windows ','4',1,'a:1:{i:0;s:3:\"638\";}','2014-08-11 11:38:59','Milutin Spasic','@import url(https://fonts.googleapis.com/css?family=Lato);\r\n\r\nbody {\r\n    font-size: 15px;\r\n    line-height: 21px;\r\n    font-family: Lato, Helvetica;\r\n}'),(260,4,'1316',2,'Popravljanje jeza','',' ie 6 windows ','8',1,'a:1:{i:0;s:5:\"13162\";}','2014-08-11 11:38:38','Cerar, Demsar','@import url(https://fonts.googleapis.com/css?family=Lato);\r\n\r\nbody {\r\n    font-size: 15px;\r\n    line-height: 21px;\r\n    font-family: Lato, Helvetica;\r\n}');
/*!40000 ALTER TABLE `question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question_answer`
--

DROP TABLE IF EXISTS `question_answer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `question_answer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question_id` int(11) NOT NULL,
  `type` tinyint(1) NOT NULL DEFAULT '0' COMMENT '0 == wrong; 1 == correct',
  `value` text NOT NULL,
  PRIMARY KEY (`id`),
  KEY `question_id` (`question_id`),
  CONSTRAINT `question_answer_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `question` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question_answer`
--

LOCK TABLES `question_answer` WRITE;
/*!40000 ALTER TABLE `question_answer` DISABLE KEYS */;
/*!40000 ALTER TABLE `question_answer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question_answer_translation`
--

DROP TABLE IF EXISTS `question_answer_translation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `question_answer_translation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question_answer_id` int(11) NOT NULL,
  `language_id` int(11) NOT NULL,
  `value` text NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `question_answer_id` (`question_answer_id`,`language_id`),
  KEY `language_id` (`language_id`),
  KEY `question_answer_id_2` (`question_answer_id`),
  CONSTRAINT `question_answer_translation_ibfk_2` FOREIGN KEY (`language_id`) REFERENCES `language` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `question_answer_translation_ibfk_3` FOREIGN KEY (`question_answer_id`) REFERENCES `question_answer` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question_answer_translation`
--

LOCK TABLES `question_answer_translation` WRITE;
/*!40000 ALTER TABLE `question_answer_translation` DISABLE KEYS */;
/*!40000 ALTER TABLE `question_answer_translation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question_resource`
--

DROP TABLE IF EXISTS `question_resource`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `question_resource` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question_id` int(11) NOT NULL,
  `language_id` int(11) NOT NULL DEFAULT '1',
  `type` int(1) NOT NULL COMMENT '1 == task; 2 == solution; 3 == grader',
  `path` varchar(250) NOT NULL DEFAULT '',
  `filename` varchar(250) NOT NULL,
  `file_type` varchar(255) DEFAULT NULL,
  `data` longblob NOT NULL,
  `start_up` int(1) NOT NULL DEFAULT '0' COMMENT '1 == start document of task',
  PRIMARY KEY (`id`),
  UNIQUE KEY `question_id_2` (`question_id`,`language_id`,`path`,`filename`),
  KEY `question_id` (`question_id`),
  KEY `language_id` (`language_id`),
  CONSTRAINT `question_resource_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `question` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `question_resource_ibfk_2` FOREIGN KEY (`language_id`) REFERENCES `language` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) AUTO_INCREMENT=1211 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question_resource`
--

LOCK TABLES `question_resource` WRITE;
/*!40000 ALTER TABLE `question_resource` DISABLE KEYS */;
INSERT INTO `question_resource` VALUES (430,94,1,1,'','index.html','text/html','<!DOCTYPE html>\r\n<html>\r\n<head>\r\n    <title>ÄŒrviva vrtavka</title>\r\n    <meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">\r\n\r\n    <script type=\"text/javascript\" src=\"lib/jquery.min.js\"></script>\r\n    <script src=\"https://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js\"></script>\r\n\r\n    <script type=\"text/javascript\">\r\n        /* <![CDATA[ */\r\n        var task = {\r\n            /*This is called after the task html has been loaded into the DOM\r\n             The parameter randomSeed is an integer that can used to shuffle choices or add other types randomness\r\n             The field mode is a string and can have 2 values: \"question\" or \"solution\"\r\n             question => means that only the task content are loaded, and user is expected to find the answer without any help\r\n             sloution => means that the solution is displayed, so both the task and solution contents are loaded in the page\r\n             */\r\n            load: function (randomSeed, mode) {\r\n                task.randomizeAnswers(randomSeed);\r\n            },\r\n\r\n            /*This is called befor the task html has been removed from the DOM\r\n             It a retuns boolean, if the task is ready to unload\r\n             false => the platform is expected to try again one second later\r\n             true => the second attempt should always return true\r\n             */\r\n            unload: function () {\r\n\r\n                return true;\r\n            },\r\n\r\n            /**\r\n             * Returns current task answer\r\n             *\r\n             * @returns {String|@exp;@call;jQuery@call;val}\r\n             */\r\n            getAnswer: function () {\r\n                var answer = jQuery(\"input[name=\'answer\']:checked\");\r\n                if (answer.length > 0) {\r\n                    return jQuery(answer[0]).val();\r\n                } else {\r\n                    return \'\';\r\n                }\r\n            },\r\n\r\n            /*\r\n             * It is called previously saved answer is loaded.\r\n             * It can be used if the existing answer is deleted by the platform for some reason\r\n             */\r\n            reloadAnswer: function (answer) {\r\n                if (answer) {\r\n                    jQuery(\"input[name=\'answer\']\").each(function () {\r\n                        if (jQuery(this).val() === answer) {\r\n                            jQuery(this).prop(\'checked\', true);\r\n                        }\r\n                    });\r\n                } else {\r\n                    jQuery(\"input[name=\'answer\']\").prop(\'checked\', false);\r\n                }\r\n            },\r\n\r\n            /*display some standar message or button within the task.\r\n             type may have the following values\r\n             -\"validate\": the html is a validate button\r\n             -\"cancel\": the html is a cancel button\r\n             -\"saved\": the message indicates that the answer has been saved\r\n             -\"changed\": the message indicates that the answer has been changed\r\n             -\"deleted\": the message indicates taht the answer has been deleted\r\n\r\n             The validate button should call platformValidate(\'next\'), when actived\r\n             The cancel button chould call taskReloadAnswer(), platform(\'stay\'), when actived\r\n             If isOption parameter is true, it means that can choose not to display the content\r\n             */\r\n            displayMessage: function (type, html, isOptional) {\r\n                if (type === \'validate\') {\r\n                    // no idea what\r\n                } else if (type === \'cancel\') {\r\n                    if (confirm(\'Ali Å¾elite poenostaviti odgovore?\')) {\r\n                        taskReloadAnswer(\'\');\r\n                    }\r\n                } else if (type === \'saved\') {\r\n                    // ni potrebno povedat userju\r\n                } else if (type === \'changed\') {\r\n                    // no idea what\r\n                } else if (type === \'deleted\') {\r\n                    // odgovor izbrisan\r\n                }\r\n            },\r\n\r\n             /**\r\n                 * Function that does cycle randomization based on supplied seed\r\n                 *\r\n                 * @param float seed Value between 0..1\r\n                 */\r\n                randomizeAnswers: function (seed) {\r\n                    this.shuffle(\"answersTable\", seed);\r\n                },\r\n                \r\n                shuffle: function (tblName, seed) {\r\n                    var list = jQuery(\"#\"+tblName+\" > tbody > tr > td.content\");\r\n                    var rows = jQuery(\"#\"+tblName+\" > tbody > tr\");\r\n                    var columnsPerRow = list.length/rows.length;\r\n                    jQuery(\"#\"+tblName+\" > tbody > tr > td\").remove();     \r\n    \r\n                    var rand = new task.RandomNumberGenerator(seed);\r\n                    for (var j, x, i = list.length; i>0; i--) {\r\n j = parseInt(rand.next() * i);\r\n if (j < 0) j = 0;\r\n if (j >= i) j =i-1;\r\n x = list[i-1]; list[i-1] = list[j]; list[j] = x\r\n}\r\n                    var c = 0;\r\n                    for (i = 0; i < rows.length; i++){\r\n                        for(j = 0; j < columnsPerRow;j++){\r\n                            $(rows[i]).append(list[c]);\r\n                            // $(rows[i]).append(\"<td>&nbsp;&nbsp;&nbsp;&nbsp;</td>\")\r\n                            c++;\r\n                        }\r\n                    }       \r\n                },\r\n\r\n                nextRandomNumber: function(){\r\n                    var hi = this.seed / this.Q;\r\n                    var lo = this.seed % this.Q;\r\n                    var test = this.A * lo - this.R * hi;\r\n                    if(test > 0){\r\n                        this.seed = test;\r\n                    } else {\r\n                        this.seed = test + this.M;\r\n                    }\r\n                    return (this.seed * this.oneOverM);\r\n                },\r\n\r\n                RandomNumberGenerator: function(s){\r\n                    var d = new Date();\r\n                    this.seed = s;\r\n                    this.A = 48271;\r\n                    this.M = 2147483647;\r\n                    this.Q = this.M / this.A;\r\n                    this.R = this.M % this.A;\r\n                    this.oneOverM = 1.0 / this.M;\r\n                    this.next = task.nextRandomNumber;\r\n                    return this;\r\n                }\r\n        };\r\n\r\n        /* ]]> */\r\n    </script>\r\n    <style type=\"text/css\">\r\n        label {\r\n            padding-left: 10px;\r\n        }\r\n\r\n        ul {\r\n            list-style-type: none;\r\n        }\r\n        .answer{\r\n            background: whitesmoke;\r\n            border-radius: 10px;\r\n            margin-bottom: 20px;\r\n            padding: 20px;\r\n            border: grey 1px solid;\r\n        }\r\n		\r\n    </style>\r\n</head>\r\n<body>\r\n<div>\r\n    <table>\r\n<tbody>\r\n<tr>\r\n\r\n<td><img class=\"2\" src=\"resources/crviva_v1.png\" alt=\"\" width=\"404\" height=\"536\" /></td>\r\n<td>&nbsp; &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td><td>\r\n<td valign=\"top\">\r\n<p>Bobri se igrajo s kosom lesa, ki so ga navrtali Ärvi. Iz njega so izrezali kolo in ga postavili v stojalo, da ga lahko obraÄajo levo in desno. V luknjo na sredini dajo kroglico. Nato obraÄajo krog levo in desno, dokler kroglica ne pripotuje po Ärvjih kanalih ven iz kroga. S kak&scaron;nim zaporedjem obratov jim bo to uspelo?</p>\r\n<p>D pomeni, da krog obrnejo za 90 stopinj na desno, L na levo.</p>\r\n<form action=\"get\" onsubmit=\"return false;\" style=\"margin-top: 20px\">\r\n    <div id=\"answers\">\r\n            <div class=\"answer\" style=\"width: 200px\">\r\n                <input type=\"radio\" name=\"answer\" value=\"640\" id=\"answer1\">\r\n                <label for=\"answer1\"><strong><span style=\"font-size: 12pt;\">L D D L D</span></strong></label>\r\n            </div>\r\n            <div class=\"answer\" style=\"width: 200px\">\r\n                <input type=\"radio\" name=\"answer\" value=\"639\" id=\"answer2\">\r\n                <label for=\"answer2\"><strong><span style=\"font-size: 12pt;\">D L D L L</span></strong></label>\r\n            </div>\r\n            <div class=\"answer\" style=\"width: 200px\">\r\n                <input type=\"radio\" name=\"answer\" value=\"638\" id=\"answer3\">\r\n                <label for=\"answer3\"><span style=\"font-size: 12pt;\"><strong>L D D L D L</strong></span></label>\r\n            </div>\r\n            <div class=\"answer\" style=\"width: 200px\">\r\n                <input type=\"radio\" name=\"answer\" value=\"637\" id=\"answer4\">\r\n                <label for=\"answer4\"><strong><span style=\"font-size: 12pt;\">L D D D D L</span></strong></label>\r\n            </div>\r\n    </div>\r\n</form>\r\n</td>\r\n</tr>\r\n</tbody>\r\n</table>\r\n</div>\r\n\r\n</body>\r\n</html>\r\n',1),(431,94,1,5,'','','application/javascript','',0),(432,94,1,1,'resources/','crviva_v1.png','image/png','‰PNG\r\n\Z\n\0\0\0\rIHDR\0\0î\0\0\0\0\0Y×™z\0\0\0sRGB\0®Îé\0\0\0gAMA\0\0±üa\0\0\0	pHYs\0\0t\0\0tŞfx\0\0\0tEXtSoftware\0Adobe ImageReadyqÉe<\0\0ÿ€IDATx^ì½ÀG‘\'^Ò÷éÓ§œ“eI–-ÛrNlØ&,còÂ‚—½w{ìÿö\"»°ánawğ²áXL0Ñ6à€s²%ËY’•­œsÖ¿«»ª»z¦»gŞ{ó¾¤ùIßTuUuu˜î®×ófæ\r:ª\05jÔèX°`lÛ¶R\0cÇ…sÏ=—R\0÷ß¿şcœpÂ	ğÛ¿ıÛ”*Ö/_¾\\ÿ1²şkÔ¨Ñ€»F\ZÕbşüùGï»ï¾£Ë–-#‰Áç>÷¹£—^z©şÃé÷¥/}‰4W\\q…–óÚI }»õ³fÍÒrüÃúJ`{°][·n%I\Z5z\ZƒÕä­Q£FÀ1îjoºé&ow‹¸ì²Ë`Ğ ApŞyçÁå—_ßûŞ÷Hc€»İx@ÿ!²ùûÂîwÅŠ¶x@Ûƒí\Z7nœnç?øAÒ =¶)›¯F\ZÕ¡Ü5jD€H^VF``Æ …ÁëÊ+¯ÔÁ[/MK4\Z˜1¿ÚéÚ¿¬=–¯vÅöO^Gé³şÑ^\"pñRºD¶?²àÀ\\B={©¾F\ZM€vŞ5jÔPÀKÃcÆŒ±—’³—Š¯ºêªÂKÍ(G¨‹]j]Fï+àú…êˆí9çœslû±½ØfÖá_¶ıò«\0´Íæ¯Q£F1êwc\n¸£üò—¿¬w‚¸›ÍîHÛ·o\'.¿åµ\n^zÇšÍ¾Õ¼²—Ó¿ñoÆ\0óã.ÿ²»ó¾®_¨Øìl#ş}şóŸ\'ö)ö‹úà¢ÓÙ»¼ñ¿.ÀşÄr±ñjF½;¯Q#\0ŒŞ5jDğ®Q¢hÇüõ¯İêğ&-Ü!ÖhÙ›Ø²;òk®¹†4ØçRŸİ‘ãMõq5uôËÇÁî¾ûnxÇ;ŞA)5»ë\'Újp—‹»5ŞÍáîO~ÏŒ;Æ/|á”2ãw„¸Ëë7‰\rdğwİØÏrWß‹K¨^zÎ@[¼\"¢¼–ó½Fc	uà®Ñ/Á—¢‘ÊËÕE/ó¢\r_²Î\Z½<?ò/—óùÁ@?{ölÍ3²Ï-Ÿ×\Z5*êÀ]£_ƒ5~¯úì³Ï’$˜ñf~ÏŠ‹8ê\ZıxnñCZ}îkë¨oN«Ñg1.¼¸û’7B^\nÇÖ5×\\Ë–-Ó»qÜ±Õ÷À\0[¬q§ıõ¯4ràåô›o¾Ù;÷¸cÇñ o«Q–\\\r—\Z¤¿æHııÁíd_£eÔ»FŸ.®¸«ÂwOxÙk.Ş|Ç2ŞÙı¹Ï}.w©›ó×¸Àİtèö+®¸Â¼¿Aƒ6>{Ïáón¼FXü\"<Jl\nßz	à—\\½„$5šE¸kô*0PËÜïÿûúí]\\p%pgµuëV»#¯¿Ï¬À`Ì;êùóçë›%äo^½Õ®FkøıÛÌc‚Ù¿Åßx#Y\0<úù“aĞ%WC¾›G¸kô8pä€‹7ePÜ51Ïî1_}CYpŒ` —@ŞÎÈ¾Õ\r=+¼b“ı°X£5ÌùÜ#*€/¿ı<œ\\_;o\ZõÍi5z¸€Êï©18Ë…wF¸kÊ.¬5jTş®Ç—üPˆA[¾|¿†©/§—Àí\0ƒŞó-ÍâûßŞ­Ù–ÀÕ—œŸ§këÅö5B¨wÜ5ÚŞYg/YÊÇ·ÙK”¸Sªƒvvƒ5~?.ƒ¶¼‚‘§˜§Ş‰·Š9ğ¹/ş>ñ\0ßú›ú’y3¨wÊ;f¾xo.ËîZ0(ãCxW0ŞıZ4kÔèIàU ¼Êsã7ÂUW]¥o|DÇèÕW_­onãÀ_ßŞ$Şıgâ’ùÏáÖ:r7Œ:p×¨¸ É÷PãåG¹SÁ…ƒ{v×S£Fo?Tâ=Ù“ò>¼qƒxf1Şû1¹áÅÅÄÖ(:p×h\Zx‰›ƒ¯¼Ü‹Ÿ|dwÖr÷R£FiÜ‰ó¸F^Ş ‰mêKéå0ç”3‰x~Q½ånuà®ÑøR8î<p’½3Ó|¼ŞY×èïÀñc\Z¯&á~pLKà×AøÂ¼”½¾©­F;Qî\Z• »ÓÀİG¬kDàMkò\n^m’OIÈ;ÓkÔhêÀ]#	È¸ÛÈŞaËi¼Éw òå5jKÀ¨øÂy)=;_0ĞãÓÙ\'(jÔhuà®b\\ğÒŞh†o3“wÑâÂ„—ÂÑùú…(5e``ÆKé˜1ˆg¿ÿÆù_şå_ê¯—p¾Ô¼F+¨w(äkGÙËáõ¥ğ\Z5|`ÀÎŞˆ™½ÿƒ?ËX²èyâ\0Î<eq5Ê¢Ü5ôB‚ßIË]\0^Ç;ÂñÒ^Ä]Döò_\Z5Šxñë$~İjvñKŠçÂ—À­?çŸ%ù}ø`ıæ´Æ¯<ío¸ë®»ğ§ö¯FsP‹ÉÑK/½Ôö£\nĞ¤1X¶lÙÑ­[·RªF\Z­â¾ûîËÍ)õáXÏ?¤_úÒ—ô¼ëW¸í÷í\Zòû·‘,…Åß8úF²ÇwÖhõûîä‹Rğ{l¹ëÆËyõw×5jT¼’•ış›ïBGŠßƒì=—ÀÕW}~ôğ?«·ÛÍ ÜÇğ2\\vAÏ¢âåpµ¨¿·®Q£_Q©]¶½ŒT^JÇy;nd»ıÜŒ¼ñß‡ÏÕ_o7…:ppàÄÇïÏ0 _~ùå¹ï±ù}áøÉÓ5jÔè9àî›ÃïÁ³/nÁ4ß‰ŞŸßé¿äêK`Ğ A@?\"†?ÔQ»iˆŸõ|ûÛßN\\\Z_ùÊWà‚. ÔÀ.x‡«|!î¬³w¹Ö¨Q£ï?tãî>?ÅÏz–AıS­c@ì¸1—ùÛºu+å86€“^>š‚wˆ×—ÂkÔèÀÀ}´¬O^;ùtàŸ‰ãğÅGñNâ:hW€±ã.‹»îº«ôî¼??‰ã.[şş5?ê…ßgã_}³YÿÀuKàà¾]”ò±wÛ:Ø³m=¥ÂÒ=FO=‰RyL8¡şÑ—şœÃ|9]~Õ…ç4VãØA¿Ü5|`ÀÆÉË/LÁ›Ìêï«û¶­UAxï.ˆ·¯}UIªÀ«‚ïÖõ0h™~›—/„AÈ¨ô Ã)ùë	`Ç`èÔAß|ÿ8|ì6vªæë`ß»À@-?xãœÇ»Ğx	¿¯?˜¨w?Ş°rŞyçQÊàŠ+®È½å¬Fû°áÕ:(o]ƒ»äİ*8›Ş´t¡ÄŒ¿xsmŒUˆf½\Z¹	ÜlãlûFQÇ€>\\ı\rSÁ){ş5ÚÜyãMkøÂ¤ş|[ò¨÷\0\0ŞqŠÏ`#>÷¹ÏéOâõ\'ïj±{Ë:Øµu¬õYØ³e­æ·­yí7—³u|ÅàK9\r½ƒ&VGaÜFŠ[m+êû»hÁ˜pÂ9t©~ŞÉsP¯Q-ê+mÇ.êÀİÀßi!•;jş^ÿêïºZÃ½»`ËkKôîy«¢»U€Ş ‚µ^Íšˆª¯æXfs.p+!RŞa£…>zmYnşú\"š]0dÇàÎ;ö\Z­8~.ï6Ç5ïmÁËçu0x¨w?eœ„ühHıéº\Z¬[²\0Ö-^\0[l 67}qĞÔÔ°:;jÃ\Zi6ps`ÖX+Œ^ua«ó!×÷wÕ‹Eg÷£ù¹:°#­/··yzƒzı¡~à Üı\0¡ï³êç±Ç®-ë`-i ×.¯vÕK•”/OC4tàÔS£Ûˆd~˜µ7Ä½ÜÆˆ÷`j‘	ÜÖÑ¾„X,ğ;sæ¸3¯/³7¼\"7nÜ8JÔß,Ô»Ÿ€?Aã³Ø¸ó–¯E¬ÆæÕ&@s°Şµïâ&¥‚\r¦–wÁ©f-Å#Ûj¢&­¡„­~¿m¤(÷i_BO/ÜƒÀño\"ó\Zià‡}\\#ø·ê+tuàîcÀOË˜ñ;+ùnq–×ÏbÇ±só:X£õŠgÖôà¾=JŠK?Yc#ƒ¡	šjøkŠ @*l­9ÛjÖHeà6ùHÏRÖS^Ê¦ lu>äL=Ìüõ5ôÆBázØòis/©wä	ğ:‚_µ10¨óóßÙ¼Ôè¨wN0ü”Ìw‰Şxãú“\Zq,{ö!X³h,_ğì¤5=˜™ÏC-#)ëœ(BÛ„‚­hênË£å7Û8Û¾ƒ^(bA;‹!İ#`ü,âo‚	³Ï©ox+\0®)7ß|³æë§Pú\'êÀİGú»~;ÜU/UAzÍ+*X/|c ôl°$#Ó¬†Ó3ïôÚV3LÂíšEàÕ,Åè¸<»ÛFVgryõõ:Ÿ)Ê}Ú—ĞW·[Â”½âGO9Iğsaæyï„1Óêİ¸D}¿ÌÀ@¸ûğòÕÕW_­yü©¿ú²¸ÁÆU‹áåGo×;ëM«—¨å\')µ,ò”ÛÉE¸`JÁ“yakÍÙV³Fª¯æŒÌÛmk†ô¨ÓD<zmYnşú\"úCà>zÄğxD1îÆ§ö&õw	wú›´îX^ÙÃµåÙgÍcóçÏ¯/™÷3Ô»—€wxâ§\\üŞšÁÏi×Ïc›`ıÒ#·ÃÒg†]j—ĞAM8Ãèÿ†E. K™¡mKÒ¬Õ#´™&¥·åN‡ 6FÖë|È™ÀÍ6Î¶ï 7‰†·\"Èr]­XĞãN¿¦©¿é*ˆëáÚƒkNöûoşÊ®FßE¸{8QøÃõ÷Ø¬_Ä`½Àk\\»qù¶s4¬¯g™¢Ò–åçK\'(?&ÈV3LÂÿ~›x#Ğ:“ÏØÆ·Ñsşú1°8èì”‚YÂ”½¢Èr]yeËQ:˜\0NA|Xıì8ï<Ç;ÑñÙoìõN¼o¢Ü=œ|‰\nwá§Şc;6­ƒùwı^UÁ\Z¿¿¶±ŒAi¸m`#jôÄ+\Z²µydà6<çÓ¬q‹iMñÈ¶Z ¨+20cyFHz%DÊ\Z-ôõ¤3¶,×ÄÒ¾„^$\\§á–¯üer†Ü*´+NÙ²^1XÖ¬~W|úÇîåt¼øÙÏ~–RõÆ¢o¢Ü=¹Û5k–,ÇÚó•û÷ì‚¹\r^|øvµË^b‚˜ZvÉ¼‘›”\rlY=%\\`öı2LĞTÃ^SRakÍÙV³Fš\rÜ˜µ7­ =å¥l\nÂVçCÎÔÓÈÌ__Co,®‡Ó°Ë—\"‚u<Qò^à&%–eä\0]#`†\nŞ§¼ù#0î¸cëÆ6¾lÎ÷Ù êï¿û&êÀİfàwFÙï«1Ÿbq’K7Ÿ-yæ!xááÛôî\ZK³†š˜àeXÍ0oä&¥mIáéY†¼°e9Â”\'«Ók[ÍEh3Eü`«šú›y”ãQÙ\Zc<8[Ïó(7´/¡§êİR0Ë—²WY®+¯j9JCÍnÛˆŒÁÑ#˜6¾ºÇN†ÓŞò1È/ãGÌø;nü“ßc`¯o–í¨wÁ»ë¯ıëú¦³cx)üy¬_xè6ıœµ†ZyivÌ\0y›$Ş[aKÔè‰WTÚ:™f5œy§×¶šaŠG¶ÕEÍta=ï¨¹<sé›XÎoŒñ ó£œEFŠrŸö%ôôáz0\r·t©³Pâ2¹¦‚G†ËBîèä0m7¤XÎÄ“ß\0§_ò>˜qæ±{)wŞ¸ñ*aıŞóŞE¸Û\0ÜeË×\râ÷Øxù±4Øyw½ä³»6M-Š´&óÒ¬ƒËœÚ³³züÇŠZy¶ÑŒ)ËÉE˜ ©†¼¦\n¤ÂÖšk¡YÚ_¤¼Ô™·ÛÖéQ§	O/aK:Û\'Zfşú\"zzp=œFQà–+òœµ­0Â²Œ\\ñ´ÛÖ¼\"\\,Ç˜«³5l,œrÑ{à´7¾FC»pù®g˜>V7#}uànp@Ëï‰ğ»l|‘Ê@ÿ®¿»~æÎŸ«€};lß¼V¯8¸tpâ Ek251ÁË°šaŞÈMJÛ’ÂÓ³L1R.)BÛƒTÚ9Q„¶1ÓÃiä\\XÉnË¶ec´[ËMŸ°³í;05îY¸NÃ.]Š˜@KIg©6¤3ª…†OnÅh•OË1¥MAçÔÓáòı.L3ğ¿Î®iÇâf¤/¡Ümß=o%ÂÇ*òwCW.†§ïºN?Êe5^àÌn—<ÈÑÿ\rK2¸XÇv6\0’F\'\rëë	ÙjÁéu‚òc‚l5ÃÔ(üÀM¼hÉglÍ‡bu~£§:¿öcEh~‘G½¡}	=½8¸,†Yº”=WnF¬ù ¥ƒ¡<21­şe/“kNaJ`àF;“À´eá`Ç˜ûÖOÁë/?t\ràÇÊpóWñ§…å¯ÿúêÀ]ğ“\'^—M„d\r¯ÎHï°W¿²€—4³’!ÑÃŠa°4a©	†Ì;¹¥]6gË:Í²e:†.˜¢…Š¤-ËĞ,íF>MZ§X¯ˆõÆz%DÊ-ôÑÜhËró×ÑÓ‹ƒëá4Ü²¥j%—ÉñˆeSàV\'DçcÛDàfşàÑyò›à­üm˜rüÀÜ‰â\rjøw6h£¬~iKÏ¡Ü-wÓ_øÂ©KG¸³~üæk`ÇæunaÓGbP¬N¤hMFbRMLğ2¬f˜7r“bÛœÙ€,)BÛcÄH…-±dc\ZãêêÂŠÉGz”jé)/eS¶:rÔ\'Zfşú\ZèTö(\\§a—-Eëx¢ä‹7–K¼\"\\=µ˜l™G9²\nÆüo;‡Ÿ\0—}ì?Â9ç¿^Ûdğ÷ßø›ß¸+¯/Ÿ·uànøÉwÓ|\Zb ÿX=~=ÿns9ïGğĞ±ˆ³x™…—?|´z2«R”XÍ0oä&¥mI¡Y-Pe°LÑX0´¶&Aù1A¶šajØMÑ^‹d~Q.Jm7ö®^Æˆwı¶´8¨wKÁŒ=eT±\\W^Ír”†òÈÄ´úWâ2¹¦êŸşomˆ\Z±Ñ±€Èæ£cà„ß»ê´l ×»óÎ;Ræ»oÜ}×/mi/­ÑäÏøe*\r°¿å\Z¸æ¿}PßnV³n©¥/¿KIQ°âàÛRA\nÅ¶j‚ñí|…ÃŠlc‘_¯…Ö5b{\rÁz|j‡À\0ÒA;\0[E¤\r‹ÇÚÛŸú	üï?x/|óïÿZ}6€÷òàOƒ2ğûïÖÆ¾ˆzÇİğÓ&¾õ?]´Ğ0`/P;ìùwÿ\\ñ»Ij`×*bì\0òä´øéËËŠç¤!:ˆñúˆ”åÂÔéñŸúzçS–“ŠĞåa5E([ä…­5×B¨9Ø&/“k†ô¨Ó¾µTAØê|È¡­1À´³í[ ÓÙcp=œ†[²TO÷Ğc`Ú–yëƒíM‚ËA!™XÍ+ºöÀp4n¼å=PoLä×°MõO·uà.	Ü]ã\rø}ü?]¤ïttÀ¾ç:Xp—\nØ{MÀÎ·FY†Œù¯–0µˆ·†š˜àeXÍ0oä&¥mIáéY¦˜œ¡eÄ e½“EhÓ ?Øj¦^à¶<Êñ¨lµ1ó‡|1rCûL{,ËÀ.YŠ Ëuuã2Cµ!Q%ä²L U´ÁÇÀ°|c­Í¯)\'„œy<p¹Šß}¤Vš\0—¾ïæ²2®…¸y‘ş¡’cíµÎíF¸K\0wÖøiï\Z¨ßccÀ~6î°1`ÓÂ“œæacÕ,×Í—)Ò˜ N0äm’x\0I£“†%=ñŠ†lYpzæ^Ûj†©Qø›x#Ğ:“ÏØÚİ6²:¿ÑS_û±\"´G¿È£ŞĞ¾{^{®ÓpË•²W<&YâÆf†ÒÁP™˜VÿZº›f¤0¾\rñ¬\'å€…ëÂû>ô	ıèè@¾:õòË/×ü—¾ô%½é©Q\rêÀ]\0ùì\"ãšk®0>È€}@lnÁ1”áä†±jOn(r DKM0dŞÉ™Aâ²9[TX–õ(Ó‰x0tÁ-P$mYn„fiçºëÀ«9#óvÛš!=ê4á^ùIglYnşZA÷ğ‘0tÄ(Å™2·o,qB	pz\n®‡ÓpË•\n˜m¸L\'DçScîl‘-±<ÊµDù²ùò6çÛÙl:4\\ğÃğş|jÀp¼¹bÅ\nJ\\qÅõeôŠPîğ÷Ø¸Ò‹^~ôvxğçÿ¨¶^A4QÙÑabô‘e”“:8q¢5‰†š˜àeXÍ0oä&Å¶9=%²YR„¶%iÖÆêÚÆ4¨TàÖ\n£7öŠgc´`[9ê-3`Âô™0aÆ‰0rüd¡şø„Èótøà~Ø½elZõ*l^½B8kÂUÁõp\Zv¹RY®«g©¶Ûœ]#W4y™¥¸™\'ÂØ#ƒÿ9!äÌkG¦}vŞË+ºõÈ0¸çåípÙÛß¥oúêÏ÷ÍÈ+•ˆ:pW‡:p—\0¿p\0İ@ø®fÙ‚‡à¡Ÿvn^oZ¬ú¨<(äèpŒa¬Šå:£Yèp™âÀGk–\'³*E‰Õò6\0’F\'\rëëY¦h,:_:Aù1A¶šajfiÇ$[â@ëL>c‹N4Á?Ÿëeôœ¿•ÇÀ:»†ÂôSÏ„ãO?JRŸC$ÓG€ëVÁŠç‚%wã«\0R°APQd¹®Üş¥ƒ¡<21­şµğ¶4MQ¦¦FcåÌk9•µ!œ­=8n}f%\\ù¡öë\0÷ağÆ éŞŞD¸3ÀÁ…\ZoªhX³h<ù«k4õ\nZMÚ²–2œÜÙjxr³@¡Ğ2EXj‚!%·Iâ]°¶DxEC¶6‚Ó3Ïù4kÜbZS<²­(jÒ:ÅzE°<#ôõ¨ÑBQr@[–kbi³Îº@ì\nØ¶Ï|.<ÉôÑø¢Çï+ÜçÊh3\\¦á–*PKü\Zm«W—…\\oKÓöZ¢ü¨DØ†ôÄ‡m0-\nGT¥{†ÃM¿¤¿îÏ_ÏeoâÅu¿¯_›ÚêÀ-€	ïğÄËâø=Ó@y.Ÿ½~Jì—»C§İÂá/š¨%­Ã-2†±jON‹0)N\Zb‚ËœZ3Îy“bÛœ6˜â?+3a‚¦ª—¦e‹¼°µæl«Y#ÍnÌìÍnÊKÙ„­Î‡œ©§‘™¿ğ»ë3.{¹.`<\nğ¹ğ$ÓG‡ì‡¥ó„\rË“ÄG(O»áz8\r»T)\"XÇE ÏUËI‰eñ¸¯úmi:É”xoN(8ßÎFóh«%Êm´PÿüŒòüöapïÓ‹á/şâ/úıı5¸Ç >ĞÖÙD¸	8x>ûÙÏRÊ`Ù²eışQ¯y*`?{ïuæÆ3:Ó–šåÁ¬LÔ’ÖáòÛœÖXKÌ½Lqàã5KÊ¬JQb5Ã¼‘›”¶%…§g™bBr†–ƒ”õNN¡mLƒü`«šzÛò(Ç£²5Æxp¶/æQnh#Ç‡sŞùa»Ë–0è¤øçŠdú€2Şøê‹°èI÷Ö?F4O›ÀÁ²lÄñ§X®+·=GÑBïš1)S^ÜÎ|#¯òú@®|à&Öğxàr5²!^úÁ?æ‰‚x`Õx~ñ*øÚ×¾Öo#Ãßÿş÷)eŞ8‰›¦ú2zyÔoN#È· ákûn¼ñÆ~´—?ûüè}æİú=sóYfQaĞ\Za†[D2\n†û¾R\ZVîˆ­”q°ŒÁóE4\náËeËú&½ğVäWmæ­)h¿ë#Á ]%&x:œòúK)Õ÷w±áhÀÃò0—Éè¤K{¦ıò=^ÛP^‘9V¯t}Óè„ÃğÖãÂï\\z\"üÅŸÿOı¨¼şü\ZòÒKİØ«ß´Ö8ê·\0~Ä‰€7¡õ×ßÎÆËâ÷ıàoaíbù=6QN+j¥„„“Æª=9&µwÁ…’,ÕAŒeNíÙY=şcE-‹<Ûh÷I¾_†Õ+jÄÄ[kÎ¶š5ÒÆ.“{aK:ckò¡{*ÂÃ®¡ğú]e‚vörR>‚dú\0\Z“rÕsOÀÊ1	…h6Áõp\Zn™RÁ¸¼-MóZ	•×æËÛ0œï¼ñƒ	£cêçgj¬×ÿöËÇU\0«~Ú¥¿m4p½Åµ×ÜşºŞöÙÀ;lşN[åıõ’ÍÓjwıÜ}×é›ì$7DLz¢¬‘D(ií.¿aô‘e”“:8q2k¡&.jb‚—a5Ã¼‘›”¶%…§g™b¤\\R„¶%©´1r¢mc\Zd‚4r.¬ä·åNÛ²1ZÈÀ­å¦OØÆÙ:œû+`ôÔ™&‘=„œ”Ï‡§ ™>€ÆBùÜ=7ê;Î£öm„ëá4ì2…UÕ·â,Õ†tFµĞğ<î{ó10iÃÔóC¤lƒpö®.ˆWvvÃ·®¿[¿äoöêOëWö¦µØº\\ÃÇ1y©ïhÄOxW^yeîÆˆş´×¨İõÿüãğômßkğ™İ²‹&SÃÈEÃ}™\0Å(W‚	€qH=K	™½È—‡ ­ğ-Ê’mÃ×—­Åñ§å‚vã”‹Şm¾4BÙ íĞˆ½o+GŠ¼LîF¢˜W†F÷É˜rrâ’ˆå‹¹óÊGVı2b/|å·/…Ç¸SÁşt³Wö*l\\—ë·¬¥qÌí¸1hËªà÷Ùüİş†{wÁ£×=şk’¸‰Íg•O®M[¹b\nlNn«öä¼Pªå˜¡\",E™¹¥]6gË†^QÜÒÖæQ°zEYŒ\"kKi\r¶eVûtaÅùÒ\Z’^	‘ÊËäúˆzÒÙ+Znşc\'O‡)\'	“O:YÛ[dO!\'åsâ)H¦ ±TªrW-|VˆKæ=×Ãi¸%JÔã`ÜsŠ@ß1¯,Ae~„¶%¡>’^ûVÇØN\nß»‰şµBüìşôŞ	¼ZpõÕWS\nê;Îè×?•5úÉ?Ñİ|óÍ”ê¿¯/]¾ğaxà‡K;l·\0šÓ‰‘]ô„÷¨ñ‚¨%­Ãå7ŒU9²:8q¢*!á€Äq	)±šaŞÈMŠmszJd²¤mKŒS ¶Ä’iŒ««+&éQª¤§¼”MAØê|È™>éìê‚‰ÇÏi\'Ÿ£&M…!Jyô0•¬`…ìI ä¤|N<Éô1\04–JUI|ÛÚS7_‡í)¸NÃ.QXmÇ:(Â4\r&³Ëâqß®ÇÀˆ5¼väÚç|;Ë£­–àX r´ÌèÎŞÕÅØáÁÔWM¤ê|¾¸£®¿çI¸âŠê`Ø6&x™?hğ›Ö÷İw_C>øf½ğ¢¬úuàÆ“ƒ»‘“ÄƒwÙøi®¿}—‚»ì®ı[Xşì#:íOn“°“Ü1é‰²Fu dÆ\'SÃXËuF^8Ô€â&ˆ†šhJ¬f˜7r“Ò¶¤ğô,C^Ø²aÊ;\nC‡vÁØI`0Ú‘~Ï°g×n¶Y”=¶À°Š×\nZÎIgd˜3’-şiëîa#GÁ¬3_fÌî‘#”ü–gA])yrR>/‚dú\0\ZK%5nñcwÁúÈóİUƒz·ÌØSöŠÊªs›s”†òÈÄ´úWâmišªømQG¦:æ5å„3¯ı‘/Í‡lˆ—~ğy¢coúhmáùgÚ…ùĞ÷¯8?ó‚¾“»?lPp}Æ5ùhjSÕLLèè×M|¬€?eÅºeıíNÆ¸ËVA››\'-ÃNl:£|bmÚÊ‘QùØÿ26\'w¶\ZœsN4ôâA¬’±¼Mo şc%Q£\'^Ñ-Ò.µ£1g6Ì8å˜<kÚm”Ô+—Ãö`ùK/Á¶Í›EèÓ´EC	9p#gdNoë¢ÈqsÎ€)³çÂè)ÇÁĞaC”ø°1\"Ä¦Z¶O5Šl|^<Éô1\04–JÓpØ²j	¼øğšo7D\'áúL…—É5<2\\r­]&Ç#Ùk‰ò£¾\rñdË|Ø†(Jzò¶ö`dÈš±IBÅÚ±ª°ùP7üğW`öìÙz÷İÖ=¼Û¼ÑMÆ|Dn ıTı>p#R—Sø‘ün»¿=.ÁÀ]öƒ¸Ë^èï²Í©s”Ó|JùÄ:{”qÂ#„“Æª=9ÕA4½j˜¤!ú<Ñ©Ò”åÂÔéñŸúzçS²#G„s.¹fŸ£¤l³\rdnûúu°dşÓ°rÑ\"N^&×ÌQ>r$Ì8íıƒ£&Œ‡ÁÅA:$CX©TÙ2ÈÎ7\'™>€ÆRÉ«ğğOş…¸ö¢ªÀ-Ûmš…\\Y‰eñ¸oõ10Ò9•×æ3:ËE8ßyÏêÿÖáìÉ¡íğ`êkÆ¦Ñòºh¡’‡”İÂÍğ£_Ş§ß¾†ß÷\'àÕQÜI§ÕÅ€;õcá\'DûmàæOWˆØ®ƒ6¿¡§¿¾wÙ´Ã?¹‰Œ™¤|\Z­ÎaK”5’¨%­Ãå7Œ>²Œ2bR/ÀÍ‹¯%H‰ÕóFnRÚ–eŠA¶khœ~Á9pÖ¥âCÕM0>D³›W­€…ŞÛ·˜8ˆ÷ø©ÓaÖ™¯ƒqŠz—½³FM«ØT³R©.²eoN2}\0¥’;Vá¹»QÙOƒÆP6h#lŸa•Eµ­8Kµ!3LàÑğ<îÓ™zñ¸ÖyI‡0öÈH!gÔF®Ş†xéÿ˜\'Šp2WM+2[GœTê­‡‡Â-ÖÂ ÁCôåóşpIƒ6¿Õo&Æu<¼e<8~…¬ß>†;h~ÊÂKßx‡¢|­^î²ŸøÅ?ÁİßşbaĞnåòùeéy€[ä‚!Kq!ˆÜ!©6¶GaÂ¤ñğÎO~ÜÚ-bÂŒYpù§®‚“Î:æœ÷¸øıŸ€wıŞà}ô¸øÊÁq\'ŸÃF\rUuW=0rìâú\nßVÙÜc`4°<‘âqğxmCyEfÉW\rY¾¬°ÚH•âÇwî‡OŸ?.8i\"|ğƒWèu¿:ì/À§ğÃFv½—;l*DàFd/àn?!úÛn{ËkKà¦¯şxáşëIR\rì¢D‹\0ÏKÅ‚P\ndŸ\\8p´–^W°¤‰f1aâxÇ§?c§N%Iµ8óÒwÀé—\\“fNƒ!]$<FĞÑÕóÏsÇàNb˜ÏWßú(óÚñ…#*“‰õ•ÆB;„?rCuG¸z‘[JÆì%L^Y1LÍEÖtgŒŞ_øÀù0ÿÉGÕîÕ¬}¸–ã÷Öüî[~í‰uÇÍcÅŠıêÃH3è·—ÊñR‰|l\0‘ıQîx™¥?ıDçüÛ¿óïø¾±|vø$Ù´fÜ$å4Ò¼-QÖH¢”´v—ß0V­íËü7‹E•—É5ãë‡vwÁ9—¼?y.Œ0J	Õö)[a„t‘\'b‘w«1Û`BÓ*$CX©TÙ2ÈÎ7\'™>€ÆRi;`åÂÇ½W ¶úòt	ØşÂêŠ*[q–jœ˜0B,‹Ï^o¾-MSÉ+j¼»:à)Û œ½«‹±Ãƒ©¯™;*­H.p‹dF£qXù}i{7ÜpïSpÕU¿­¿ûî«\\Ëñ/ƒË:òwÛ>FÖßĞ/7~š\Z7n¥.¼ğBxòÉ\')Õ¿€—ÆïùÎaí¼’ ¦;q\rÑi¹8 B„¦œ¶rd„o:ÚÚ!\\^ÃXËuF^8”W^ü)¸ùÒ·¸\r«Éœ3N‡s/\'Œço}u5d…ÙŠf!òD,òn• f¬ƒBhZÅ¦š•Ju‘-ƒì|s’éc\0h,•|‚Ú¸Íh);Î•Uæ¶æ(å‘‰iõ¯ÁÇÀ<ŸHØèX@ÄpÄk9ùŠÚobåDÆŞôÑÚèÜª$S–V(ÖÜ‚EÈ¤¯\n‡…‡:áŞÅ»`ûığƒü _ÜyøÎw¾¿÷{¿G)‡~ƒZ¿¼T»¬óÔSOÁ»Şõ.Jõ¬SÁúº¿üm¨<I\r±é*Ñ´o²Ï}ÂWğbJ€mñùëKŞı>øìÿ¼åCïÏí\Z¬rlÓÒÃ800M(ÌÃ–©¨´)S¯˜M¬¬æPì+5\r;;ÁØ®Cğş¹Cáì&Âyç§‚Ş—HÛwñĞCÁıÑQÊG}sZDê¤üú×¿†¹sçêK*ıîøÜşO_Ğ7 4é<øùx‘°”\'7	ô‘D-ƒ‹NT×I«–¼ª¼KüŸüüÖû38íÂ3apæ«\Z52\"¼@(”NcLÈÃædbÆcNÌÈîÁìbˆrÈe¬^²DÓ¦L9*ú]ƒÕíRüœñà|ê­ğ‹ë®ŸÖÉŞÖ€uÂï½ñRø¡CáEñkÔü=÷€Úq3^yåıø\0~ßßo÷Åˆ—Æïø§Ï«ÀİÌïn‚ºËqDõ±ZXŸÄğbh¨¼òR\\ğûëw|ì£ğéÿşg0ãäÊ[°{»·n\"®z4r™Ü@ÙŒkÜ¤Q¬,ßÖËÁwçRO.ß·‘~,bÆ‰&Åæ&Ê»:Ã„!ûáãL‚I#éKæ7Şx#Yô.pİÇÓğE2øÄĞ‘#â1\0ò®»ßn¼áï\Z,´ûÂ¾ 8>öĞW>=â]ã7üÕ\'`İÿæ:	¯<Gm:4‘KÃŸ°YßŒÂ²´82ù‰\"Šbww÷Pxë•Tû¿À	gœ¤òÖ»·±{Ûâz±q—úx¿Eò10\r\Z˜Ò^îØ½ +ymCyEæX½Òõm²Lõ¯•6#4G‡¨à=¼ó(¼aò!¸êİªİíUú?zk„WOqwÏiËß™(B_¾S¾Uô»›Ó²¿ Ó(p\0òe–ŞÀK\\OŞôÏšÇ×¯)rjÑéà³BÄ¥5ãfŸ¾¸=Ê|eÈFÂÉ\rcÕœë œı”d)ÊxQjË¼ş²·Ày—¿YéäÃµDbÃSKC:+\nç“y\"y·J³\rÖA!Tïd[R]dË ;ßœdú\0\ZK%¨ı»¶ÃS¿ü‘æÛ²;n×O*÷äÛÒxÃ¥õaì5¯(—ƒ	+Ç?aÃp¾ó6®,£cêçgj­É¦¾&pmn-’g›Í†`ÖáÀ¡#°ÿè`øõ+{aÇŞz§Û7®á‡~\"¨ìF-|x ^.ïør?»õîÿğíOr–À‹.ºHltø(AO¿ş/?~İ×à¹{¢Ór’:fQ¹©¨ìÒMzCƒHéB`ŸÄàQ/ú¿¡$¼0ğ€”X8ã‚sáŠßım˜>g¦’7Z‰\Zm¨5//€í×j¾=àQPvÌ…áoé;Sİ1î Ò^fÒk‘á¥Ö+F$<íò\nß^^‰¨¢L9vÇ­ˆå\")5Ù\0ŸIzéÁŠïèP“\'tÀÑ¡#á~ùoaÚ´imŞëÖ­ƒ}ûöÁÔ©SíZ½~ızMËbÿşıºxÏÓ@C¿Úqãer¼ã±¨ñ»ÜUã_Oé,vmY÷ıûaëšWí|å^×DL@T3…RoyÍ¸™Å§NÚjjí‰f}ÓÔÖáò\ZÆªX®3ò\'~œèTE¸f¡À=}Ætxû\'>#Æt[ß9Ä1[-\ré¬(œOæ‰Xäİ*AÌ6X…P½“mAHu‘-ƒì|s’éc\0h,•t¢æİüØ§&¶z”İm#L?){EeU¹9JCydbZı+ñÚ™¦-K6¨7C¥¢¨#[“6\Z-×ÛobåDÆŞôÑÚ˜Úº@­RŠõ·`2ÙHà–ª‡Â¡ÃG`ãÁnøö­O©õõÊ^y3%^şÆ?üş:ûêoz÷«ÀºL?ÁšwÕ}ø}öÿŒw›‘;[OLÍà’2ñ“.­7ìÄÚÕ\Z•O	b6\'7ŒU{r®ƒZy¦+ÂR”±o<ûÀUŸ†É3§BtÈÄ1[-\ré¬(œOæ‰Xäİ*AÌ6X…P½“mAHu‘-ƒì|s’éc\0h,•êdmxõXô¤ÿ‹*Q6p»>R³Ä¯ñØ¶zÅèÀ¬å*™\rÜª­:eHnâQ®%ÊJÄlè;f#ËÒDË•Ğrê#éµoEM &¡bc[°\Z2pÖ‚eRe8xÀ`¸îéM0¨£KçÜ[#¼g‰ƒxê»ï­[·ö»ß¨(B¿\nÜØùò29ï¬1 ÷¥`Íxõ©;àÑŸ|ÕNJîhÓå¸``ÿ›4æí™’ÁúQ4oK”5’¨%­Ãå7ŒU{rİ¸D*“†èÅ€w|è\n8ùü3o½h°ïâ˜­–†tVÎ\'óD,òn• f¬ƒB¨ŞÉ¶ ¤ºÈ–Av¾9Éô1\04–Ju²Ú¹ÛF4¸±Šu<Q„i\nL0f¥¸±\\âáz`9Æœl™G9²\nÆüÏ	#×”xSg×>çÛÙhmµDÙ¢êÿÖáì]]ŒL}màVÄÚ‘ÌhôÜdÖ‚e•bİö<¬é¼CàîGèÀÙ[÷1ğ»l¬~\'İ‰ÄŸùì7/wğ/Äàó…x\"úòÉxê¦‚—¼Aóv\"\Zâ§ÕANf-’z¤œfŸ¶\"[;õ%QJz>˜¶¾õQáÀIîÏr–Í>y6¼óSŸ€Î!JB:‰èˆc¶Z\ZÒYQ8ŸÌ±È»U‚˜m°\n¡z\'Û‚ê\"[Ùùæ$ÓÇ\0ĞX(W>÷Ä1õ¶4c‡ÄÙjÒaùdªóh^SN9óxàr5²!^úÁ?æ‰\"Œ½è£µA¦ p!“2h#²[¦3ªœ`ßÃpX¿lÏ0øéOÂ—¿ü—ú	¾\0üJ8rÜèáoUdÛ¢¿£ßnş®º¯î®xIüÑŸ~V=ÿM8³ ¸£¹Ç5Q³T¨™¡)§5ãfõµ\'*|›tŞ†áäÎVÃ“‡7r£ÇŒ‚üáïéï±\rH‘ûÏ! ÙjiHgEá|2OÄ\"ïV	b¶Á:(„êl‹Æ`• »ìm	dç›“L@cRn_¿\Z»ï—&Ñ&”\rÜ®Ô+q™\\SÁ#“Üj¼\"årÊ~¿Í<\Zø6Ä³ø°\rQ”&ôämíÁÈµA¡Øfw6h#ÄtÎ#£ÃÒ÷:‡TôŞvh(üø¡%úq-ü*³¯\\––w¦ó#eı&pã÷½}“Y0hßõ/_€-k–îY\\,LãÑğfAÀOE=[QdˆÑ#å4åcXŸQ{”ùÊ„“Æª=9Ï`úÔ¯şã+J/{ß»áÔNwz\r£Ï‚ıçÇlµ4¤³¢p>™\'b‘w«1Û`BõÎÊÂØ·slY½6­x¶mx\r¦Î>NyÓ;ã~‰ZoN2}\0Õÿİ[7ÂÂ{nÃ‡¢=¨*pË6š& \0ç	`ZËßÄer½Ip9($k£y¢ç;oãùÑBıßÚ œ=Ù ´L}eàÎî¢µŠÑT\Z¸èoßÁÃpàğ8x´î|e7ìÜw¸W¿÷¡?ÄFĞ¯¾ãîËØúÚ¸ÿš?‡][×õªˆ†øiu“Y‹¤)§5c¦\rŸ²¸-QÖH¢”´v—ß0úÈ2ÊˆI°ÍröëÎ…7_ñèèP\Z]=ojûIBtÈÄ1[-\ré¬(œOæ‰Xäİ*AÌ6X…P½;7­ƒmk–ÃšEààı¤ñ¡ƒ÷%¿A)9¯T_Éô1\0e¼{KÏmDÃ[d¹şVœ¥Úƒ&ğhx>[é_3uâq­ó’aì‘‘6BÎ<¨}\\ÿ¼\rñÒ²amcÅh§™À­ˆáDRj²>¸e:£òRg|Õwœc\0G<òÚ`xxŞóú¦±¾|e´¿£Ü`«ÚaßùÏŸ‡ƒûöè‰¥¡‰Yl©T«ƒ±W\0\'ªÔ!å´fÜ”±>£öD…o“6R[;„Ëk«b¹ÎÈÀ˜±£áÊßı,Œ™0Â t]=5/“„èˆc¶Z\ZÒYQ8ŸÌ±È»U‚˜m°\nGÔdÿîİ°cÃ\ZXûÊ3°uık¤)‡)\'œsŞptñ;W\Z•ïWƒdú˜Çöµ«àÅ‡~İ§‚6ÂsìoÅrı¹m9JCydbZıkóerMcõ:m4Z®9¶!¥–r¢coúhmLm] V)Åz[°™,¸3bƒˆNú8¨‚7Ş´†X¶{|û†{äMa}uànKŸºûŞ9nF±\\p¨{“©b4¯)I™øI—ÖŒ›%ÖgÔ`â¤q0qÊD1z´`§N†Më6hİıûaãº°z%]Ppy\rCIËÈ:¼ó#WÀ©œ©R8QÅìÕ¬H#/“.#‡€8f«¥!…óÉ<‹¼[%ˆÙ²ñá#°gëØ¼z¬yåiØ_ÁÚ#Æ‡¹o|;Œ?™$:Sù~I¦‡Õ¶óµE/¤ı(¸İyVs¦’Ëäšhhµš:Û&7ñ(×Õ•ˆÙ0ĞwÌÆ+KP??SÃè£:è¼öC3ö\'êé%ú7Ìj´ã2¹­‡ÖãĞ‘#°‡î8ßx şı¶yú†5¼q­Fµ¨wà n;\r¡	‰øß¤Ù0oÏ”ìÖ¢Òö¸ã§Â©gŸ³O?:»Å\rb‚×ì XşÂË°ô¥%ğâÂW´˜‡ûEÆ,\0³O>Şóé™»Å-ò>/“.#‡€8f«¥!…óÉ<‹¼[%ğDGÃş½Õnú5X¿ì%X·ô%ª¦šÆâšZ›î¾g{1t¯3UÖ¯3ÉôÑ`ã’`ÅóO·õ‘¯\ZÜŠ Ëu·b(=\nL0f¥¸±\\âázè9£ÅdË<Ê‘U0öÈàN9óÚ‘ók¨&ÚÎòŠ\ZïÊV%´XËŒáì]]ŒL}màVÄÚ‘Ìh(Ğ\Z„Æ&Ë*+”ºPàFVuß½ÿÖl?Ü\r?~ĞÜ´Ö/kÈ¨w“xîÎïÃÂ;ÍyLºEÃ?é§ÕÁØ«OŠ¨=BìŞü˜6{Î(+7ğ¦QÍºô®­Ûá‰»ÔÜæ%nóÃ¿ûY˜4ï-çSó2Iˆ¹€8f«¥!…óÉ<‹¼[%@Ñ¾;à©_ıöìÚ¥ºÙáÏ!š6šEÕ.€v·Š‰ÓgÁø³aâÌ“¡£‹.¡Seı:›~½~é‹°yõ\n}À3é”\rÚs•=öµb¹®Ü®¥ƒ¡&¤‘úyÌÍg«ÿ[¢Flt, b8âµœ|Emˆ·Î±r¢coúhm1å¨´Jz[ªd²ìerDFeY¹ÜÙjÏ­‚7î¼ê›Ö®fîª¿÷h/Bé-Ô»	<®vÙKçıÚM²Àn‡³Õë#Ú¥ƒ7™¥©•#ã&†+“îæ~ï[aæÜS´Lƒf!û‘y=^³yİš¥ËáÎ_Ü;¶«™rrÑåo‚ßş&åÖylÈ§L¢C. ÙjiHgEá|2OÄ\"ïV	PôÊ#÷ÀòÓ\"ì\\¼¸ÉÜL^åbØàeô¡#FÂÈqIbpèÀõ!lìÙ¾UñşÍo±ö¶e·;ÇjÎôúc`Ä£\\K”•Ûø°\rQ”&ôämíÁÈ5£„Šm&p‡Æ¥³†øˆè¤Y–ã)Ø¥vŞø¸ØÁ£ƒaŞZ€UwÂ<Pï\nPîñøÏ¾¢‚ö8›x\n)ÖŒV+Q„{ÕÙ ‡&ğ¿I³aŞ)Ù8=~âXø¾F£Ó4sØ§óìì@¼\"÷îƒy÷?ç¼éÍ0|T§’I;D B³L¢C. ÙjiHgEá|2OÄ\"ïV	Ptï÷şªÀÈbtàÖíÃ°a\ZŠé\\wõÄÚÚNT¸åù@ç–“ËâùWéerÌkóå‰\"œï¼çGõkƒpödƒĞvx0õµ[/h#D2£Ñã”\Z›,¨¬Pêän\nÜˆ#Êfç¾Cp˜Îéck:ê;Î+B¿û=îŞíeO« -`\'d73C¿¸|¼ÀaĞ~ÿ§?BA»zÖ\r¿ûr´kh¬yiaôñ-FhQ<VQ6h;({\Zß±)ÄsMCğ¥Ê²™¬—(Ô+^Ê£6Ä \"6ÒEÌX\"Ñ$´CHªKtUî„\0~4º{tàÏŒ)\\|Üa¸â²óô›/Ú›Ìz\Zuà.|±ÊCßû\",Ó—Ç,=ŸJŒx¬O›Lä	Çé =d(ß|V£İÀKÎ/?ñ°âÜyÕ»mæ<ß5‚Áª¸\r#t7¹æõÑ@ìi½òı\0¬3^dU7&o\Z²Lõ¯İc,å=¯+ßXì~ŞƒM¨9eô>øØÛ/ĞÁ_IZ£9Ô»\0´ïıŸ‡Õ/<B’,ÊO(=ÜÕÁ.\n\rÎv¼Iìyß1´{÷4ÖWUbÉS\'vÛ~½’;˜\ZI„dvŠÈ +•N\' “‰P<İèäÚ!â\'Úk‡p¦9Jz6½ƒ]\',Œ6Äã\Z¥K)K\"µƒ©tğÖiƒ÷	#öêà}å•WÈŸÜì	Ô;ÚÛÖ¾j<2c+\0‰ù“;[ÅÌÅeï¹¼m—Çû\"é€—~üwÿ?ı$I{¯½ô,,a!¥pˆ“)ª*Åv¡¢á×^dæLñ9”îx/”Y‹L^©õ,E>ÏFÊ#6>*\r¸j÷eò$2ù19Fï¡:ÁûÏ>y|îsRï&PîLĞş‚Ú<7-5D¤ãS¶Q¸²q£æ‰3`æ©\'Sj`ã(tÀê%«àg_û˜wßİzyù©ÇHÛsÀ×“¾ô8^\"Gø+Qf]ª!ĞÔ÷Û¥¡lÅt“3/w™œàXw\"€\rZ;Ã;YÑ,¼ò™Uë›¼LŞZ5‘wïêÙÌåû‘C;lğÓ±~ÿ½ç×Á»	Ô;\0´éÇB¢\rÜğ`ÖÃ&¢MT¯D¢¸ø—7°±mã.øÅ?ı3Üó³ë;¸ähÏİ,‡Aû‰_Ş{¤\náv2íÿîq ÃœÄ(H^‚çNVıàÜĞe²U®üàNŒB´^›X½b~Ò(Î”jmª+ªÁøÕİ&ôŒéÜ_ï&Pîf/3xdÌ:^ŒØ*ÿIÑØT™¥vÛıùş½GáŸŞ\07}ëŸaçöm$õ±sËvâÚ‹×^Z]ÿ8¸ßÚ±ËäŒ†âD!=Zû\"s*9Õ¢óÊÉ¥‰g®ys²rbF´N(oäD‹r.½:E˜ Ÿ)G%{óƒbÑ¥÷2`cº;íİæ2x_uÕUZV#:pgğĞ¿¨‚öRJÅÁÎ~ª–³ÎC³ƒİå;å¬¹Ä\r<à÷ØÏ?ú4üø¾\n+—,V+×Š5KÌkYÛ…Cû÷Á¼[ÏŞwæ¬¥Ïa_Ø½…V.“Ç¦P>è\ZÄÊòí9ÑüIŠ×Ëi‚E\"\"6Á÷1c‰D“Úııvó—ïMÃ°ü±ÃñnscÌÁû¦›n¬ƒw	Ô[à‰ë¾^}–Rf€ñœ²ÔJŒx¬OW–_ÊÌ¹ó»íÕ‹VÁOşáïáÉ»ïÒé¢ÅæµÅ/W-îÛ‹îùáw`ıŠå$\rëÈµ¬/“7ğ•(7Â(÷˜%iï_ğÚ†òŠÌ±z¥ëÛd™êŸc­’šV©œ×5^”ŒÙãDğ]ïÒ¨7ƒöò§İÀØL\rI^ôQì¢ĞÀlŸ6İı2Ô@ÁŞİ‡à¦ıwøõO~û÷á›ÈH!’­í5ÕƒÕÙ#‡Ã½*`/zzûN\n—uğ.“køéÔâX#ĞtÈÊdĞ•J\'Ç äas2É,JK»(â\'Ú+SÖÅ26½ƒ]\'2H}PŒkªAêCu+cóÖÁ»qÔ¯<Uxòº¯Â²§ïĞ¼|Ï1B÷\Z]šªÒS`â\'ı´:Ø	IŠ¨½fÌ@>ÿâóà¼·\\lÓÄ[‘ĞÑ,bŸÁ|ÍtV$m¥\"¡ÙŒN$ñ§/Ÿ¾ónxöñÇ­]³{o7ke†\"ÿğÿ)tè4íã“°¢€!ò0÷«şºrnRXœY¤ÔnÇ–­êyÍ)Û8Û¾ƒH´e/•ÛeGd¹®V,è°#`Ü”©0|Ôh?õ8-ÇóÀódóÚ×`÷°iíZõ¡pùSõPZdTó`^Í*{d¤3j×?kÃÔóC¤lƒpö®.ÚN+Ìúbf„J+bx‘”šlÍM™Î¨<Ôñœ`Èºxş%¯ôáÙªó¸û\0¢×£î84¾uë3õÏ‚FpÌîù¿ügXüÈ\rz’ Ì{5ç&\r?9Yq ÙéÆiÖë#ÛQZŒ½ò%üÎŠÈ‡Ñ—¾ë-0çœ3\'G9ñV$t4Øo0B³I[i‡äCh6££äªWVÂ½¿¸ì7»ZóDFbyÊ`dšÕ`ıåù$wÒñ¦}ÜiVĞ!Dææßy¼¶äEÍc)²^F‚2LSíôÁÔ•ëÈ´/!ÒmöHYØq®(²\\W>=C`ÚI\'Ãñ§œ£ÇO2B\r2°E)Fóx;6m„•/¿\0+-²c-ı£\"xD½*ç>QÔ‘­I–kmˆ·Î±r¢coúhmx¥àFª”n&§‹I3~²cÓYC|DtÒ‡WÏ&£§’>²vJ€?H‚Á›{dû¡nø¶\nŞßøÆÕğÙÏ~VKkt|YøcËÕ.û¹;¾£†\r•ÌnÛ!3ÊriDHFÔA.šd‹ğà|yÁÙùaŞŠ„.;#Bùš\rè¬HÚJ;D B³¾nÏîƒğËo}{â	8|è°V³»EÊ‹M,²¾kHLŸs¢æ«Â k^}ÉÔK•ƒÔ•mL»Àÿ€ql£\\Gp°B{9ïTçwö™gÃ9—½¦Ì:º‡ m¶(<DÕ_÷ˆ‘:úèT¢k×.Ò©²9\\fáêèë²ugØ¹® 9JÆìó0å˜1F†Šå1§f5dàM–TV(uÒBÖ#ç_¤s*©Ë(±|±Zwç`Øw`è Cpæœğ¾y\rL:Î;ï<c\\ãØıƒö“×ı¥à–iJmôlå\'‰ìP¸Àg®¿ı^¸öïş6mØDÒ<¼Éœì³Ÿ[ñ²ùYÍ*1fòTâş¹+z¬/\"4úú2sdÔ¸ñğÆ|N:ï\rĞÙÕEÒæ0dèP˜{Ñ›àíû$Œ?ŞuqæÊ’½Zˆ:y6RœÛY”(^9~m”«ôÜèûÈ	©ëìF¡Àè}ğ»ï=>ÿùÏÁ5×\\CÒ\ZÇdàŞ¸t<uİW)%\\<xÎfwĞy4;Ñ\\¾rDßÃú•›àûûwú»lÉ.ñÛêt‘8pà`å/b:Òíêü*¦R~u4r™ÜÀÙã™Ÿ6{\\üA÷ÈQFXFOšoÿÔUpÂ)§êtzN5~B¥7ÏµHÄJôêÂlÌX\"QÍT€D$Õ¤K›¤\n\'\Z„hXÒÅ ıNó1İ.xãÖêàíã˜Üø6´G~ğEÅ™ÑÃØÍ!?íMÆ(’#6ëÛQV©Âú,öï·|ûpãw¾m¿_D„)“‹MÁº£{ºê±tº\nvx^<ß5ägvÚ	\'Áo~‡I´	¾ó}pÂ©&x3l]ñ.o;Öã%ÊØ4¬‹c­9NÍ¥ÆFp¸Íú/Söğ®;ÌŞŸ|çëàw~çwêŸU8¦÷Á}»àşû¼¢»óC±ô‰;vÁ‚>ªƒYT¾&føš«ˆë»8:¨^|âYøîÿş?°fÕk,%êCö^Q–Ğ¦”aëZ.£:L5‡ü«ESÔ+™ÜoW#m¨‘ÇTµÓ>ã-¿A©öâÂw½N˜+_fD7¥•B¹mçºæù ˆ(Èã‰\"d^‰ÔÅv¿¢|«pşeOŒÚ¡¸»º6uèø+/«Ï[á˜	Ü:hë:h‡ <¨8ÓØ²ŸÎ™ärëƒ}îÜ¶SÓ¾Š[öÀwÿæïá[o\'‰ƒ·àt‰´Í¯~ÿ®[†oX«ÓN:½¨ŠúrÀÎÆv£ñËä\nj|<¥í;í,^¯‚÷Ø	(•˜Ç²ı«1b›B„ŒèÚ*.“§¼Ò”R•ğÃ¸áĞ=Äü(	bæˆ½ğ‘·Ìïc&pã³Ú¹÷GÀóÎRC\"hlTf}º²ÉûZ»z-q}øLöİ?û%\\ûô.‹#\ZY@Œm¼‡¥/æ–¿lİªø]¨Q®ªƒ¨r–1Hß=~Æ%o§tÏâMW|ˆæ›·KCQòUC–/‡?Ö¥Ù\0Y)y]ãôŸlZX‰Á{ı(	ƒ÷[/>G¿ eÛ¶ğï\Ztû©ë¿\nk^|ÄÎDŞ!ğÎÙ½.±h¦†¤íIì¢Ğä*°sÇnØµ­g~\\£,V/İ\0ßı?ÿ\0‹^xÑõˆ×5®­^&\ZCjRg•G»ï¿ª\0ß –¬ƒjWúÊ@d°šqêĞ=j4¥zÃÇŒƒ3_ÿ“(5-ıíÅ\\Égš£dÌ^B~x00†© \Z~UŒÍÔğjÇ~¾S¤ÿÁ*1iäMçLÜÓ\'Ô;ïc1xøÀ½ü™;`¾Ê´Qğ ‰Ï4CHÏVŞ\'é–aêğÊ‚4ím<0nüÖàæk®Éí²r.íQåÄLÛúb9ß®Š\'+Ş æÎ¢AıX{€ÏfÏ>ï\"JõN½ğb\"oHóVö¡·3/5·Ë”Bo99ßrhµœDştğ/_ğàÁ¼I ğúi‡`x×àcòÕ¨:pãc_ó®ÿ»‹™\r<7-5D¤‹¼•Œ³ È:˜2˜.~a‘¦½»úSxmeúÆ°àd¢¼ŞïO©NMìmëğÅ\ZÕâ¸9§ç—›­EëÍ€Gãßo‚i\'B|ïaÈĞn8ñ´Ó(Õø	•£–×\r‘ğG¶ƒ÷€YEqmI~ˆM©*”y®EÄã>’M‹+9_Wç`ïNsÄÛN¯.~>ó™ÏäØÀ€\rÜ{¶®ƒG¯ÅÇ¾²0£€°›Cn€…\ZX‰‘¨`ƒ<ÂeqIrş¦°cÇnxş‰§)Õ;ØüÚZxuÑò†‚VØÖ5Z.6E~¥\Zm×.­şÃÌäYù_asu,XTk$!ƒÕ´“8`ö.æ^x‘›£\nr>ÆæfÌ&ö>æ\'âL©‘˜šKUŒàjı7ÖAx§ùÈ¡îNóN8ï=wÜ|óMÇÔ3Ş2pãä^ûçŠîqã‚fPn˜„Æ\rÌ‚YgwÆú˜IÛ¬ÍN?ß¼‡çÁÁıû)ÕóxèÖ»‰3À.²5”¼jx(ÀIIjâg¡MmÛ©°â•êoP3y\ZqX¤++Ğœ†ÚĞS5î³9f\\¯}·~×=jÔHÕqá3ó¹‘mlµ·€KYŒT› Ÿ)G%{óƒb%;ø„´˜ğf5ù˜Ø°Áà?¼ç<ı‚–ûï¿Ÿ¤2pÏ»ï _B©\"PpnmHÍv—Ï¦úˆ/79÷İÜÄwõ`áCÁê•MŞİ^Ğ%rqÊOX¿£½ºú;r¤ÚÔºGá[»Ò.ZT%4s™|lîõ²½‹ãOšCœAljó|DHŒe¢Œ‹˜±D¢«‹‚lR]â&?@$ó‹†%]Ä•±º1D_:gŒîÜ~ÛpÅW‰\r¸À½ä‘ÌäNÄˆ±â9e©!$GlYŸ®¬t)Ë–¬„ç›G©^\"à5_´¼À\Z°•2co{6H‡°wçâªAGÇaâ°\\voî~ú;ä?õxâúFŒ«©œ†±)ÙÀT-Y¦úWÅÍ;FÊ{^×xcóß\Zğ&µ	#ºôMkŒ™Ã÷À»Ş|.|àïğwš¨À½qÙxöÖ¦”:¡<öhÆÙ$qî1°\"”vÚ³:ØË_ÏöGî}Í¯ş‡6BÀ }ıwF)\\lx]n«4	-,©ÅÆ)o›Ttû†u”¨ã§MWedÛá§“õ­‘DG‹?R5ÆOI]ˆŸh/Ğ‹ñ¡9Jz6½ƒ]\',Œ6¹%Ú.¤vğUŒ}ç_ö„A#şqÇ=nø¯CN»Î<y¦Şyd˜À7£=öÃ?×¼œH\rƒGN&àZŸLHÏVó–À¾²¾™ŞsÛ}mŞ:hÿûÏôc_©‰ŒZoÁIgómsğ/Ä†và«½D\\u˜r‚|%¦‚¨D#‹JO£Âá×>¨ÜÙ5”}²½Kã’\'šC³\' ”¯qV87SêVÇs\"Q½Ê å‚ıÚ£ğf5ÑçN=\n›7®‡?ù“ÿL’‡¸ûŞŒæ¿Î´x.¹‘‘\rœWÌYæeÖ§Yd‚…qÏm÷Ã#·ßöí#IuxöÁÇáGÿúC8p ÿ¬vÅˆÓŞo«Ì^vÒ¯[^ö>†ò=y:qªDkäÑÌ÷Ûˆ‘ã\'iÚ—ĞÀ´óËsçÍo-¸L^Á@L¹Èë\\åš¿|/|$›Özã²ßww:ï>w\"|ÿûß°wšˆÀ½ğÖ†í…¯35„wÎí[\ZòTVQÍ@9]8ïyøù¿ıÖ,[AÂÖ°sËVøÅ¿]üú!’8ğäC\Zî×ÈğD\rwB2F+¥TgmñjÀÑŠâsÔ„‰šºş¢š¬oü+À¾]ÕŞ—P5\\uı-ç°Ç‹q­9JJ›ò(Î”\Z~í›)ÿokãõ7>0ÛäQ]0H|ß=lğAøô»Î‡Ï}îsòfµ~¸×¼ø0,yô;QÌDR\'Ç)8™œ‚YÇ‹‘+\"dßğ($˜|Îw†fZ‚ÏxßôÃ›àæk~Ë_jîÙæÍkÖÁİ?¿¾ûµo›»ÇEÕ“»_¥’ÚĞ§gO/éOÚÙı\\¦•’õöV{Å¡sˆWÉ~LïôMĞ\0î«[öa#W¾ÒEºóÊÑ©L^•¬bÚ,Ê^íJ!å£]ş;UĞ¨vŞ²ÇÙï¿ìüy³Ú 5H¥}ø½ö=ÿô{ú¹ØÔ‰UD‹HÁ¡€ßÑ#|ò)D\r¤60k‚?ıgÒ–øI?­®Fµg‚_fÜ6W:PF\Z\'z\"L?áx˜xÜ9ni¦Íxy}“\nÖ«—®„%/½\nÖoÖ\Z;!a™U)J¬f˜7r“Ò¶¤ğô,C^Ø²aÊ£³¥x¤¬×¶š!ªğæ}¦œp¥¸#ãCtzÄüÑ·aßî]TˆÙqË:ô5ÄÚÑ.d?V¥`Æµ²WÙ³ßò˜t‚ÿ#ô#›z<xbJØ*(FóxÀód¨9QQ”/]8½ã[ÖÑÖY§FË5Ç6Ä£ÔòBNaì@­\r2f}Á1¦X=Í‹IÓ.‡LÒKgTV•Ÿ¦‚^=<ÿ™Œ*cçë8Åmvğêë«<H\"Ùæ]`û>|}±Ã#+Áˆ±“á–[n!IÿG¿Ü´ù9·‚ƒ¦m•¬#ÑQ<Ñ\"”’œ¬&¯5P@ß¤×G¶£´:pPáérZ3¦<„_fÈ¨ğmÒy†“;[\rOÎ‡âxB(Â5C™œDÈÛ$ñ<Ùq\"Z[¢FO¼¢![›GÁé™wz¤šµtœqÑ[à´‹/Ä”A¶‘YˆNŠXÀ‹=\0«_zÆ•£ ëĞ×kG»Àó¤<î°1üì³Îƒ#ï)7³Ô‡˜¶\nŠÑ<pLjNTDFåOßu;¼4öêÏ´1¼•ë4ñV¦˜„¼7­\rÏf,‹„X=*[C°™äù¬Ë*+Ìê¤¯\n^ÏGFéêlÖ\0‰T>	ãÃô—5£x\\½mì?ä:tt0Ü2+|ø£ƒ¿üË¿\"iÿF¿½TşÒ½ß|¯­NÍ=œ´È	b°Ã\"W„(C²µ1ÄËCßÈÚL	!è	ÄE\'ª€sÃª%©‰t•šˆYhS›Áø¶IE¥«åÏWÿ*Ø	ÇÏ&ÎoW#m¨ÆÖõÕ¿c¾¬[µŠ8‰r\'ÚÎuÍóA1l<(Bæ•È3‰v?ùA ‹*Æ¾ÚYTâŸèÔÑC¡Ãú;ªoV{ûÙ“áê«¯0oVë—{Ó²ğÒ=ß§”›6°\"0JxäpPÌúd\"g¢Fë#Î¦úˆiŸ‘Ò…À>‰IõYj\"gá-8ÙR‹S¶A²¡\\{ví\"®:Œ7Ñ+¬ŠE¥]hôô·Š²»mb\\oİ°è½W÷JìÙ¾¶nÚìõ¡œßOáÍÇääL ”­®-š›Iu‰r’s4¥*á»)eÖ$ü¾{ÂHÿ}øfµ+/?>ğˆï»û]àÆ÷?}ÃW)F#S‰ç¥†DĞØ¨Ìúte!Óì/—Ï/ËÕÁûò/[5R³Fcë×$¯7H{U¶‡V{gù°Ñcˆ«Ñ:ògrÍâ¾ñ3µ+_©ö=\0á9ææ †Çæ/{(œÅH¹Èëb-hrng‘şğ^ÖC  Ñİ0¢«ƒR3FìK^w¦Şıı.pcĞŞ³m=¥ŠÁ;»Ãlûc`*Ÿœ¨ÁîŒ3ØÒF‹$û¢	Äs©µô²¸‚åüñLHMê¬Ò&õ5¦ìİÛ«şmîƒê˜ù0ã\\£\0şÎ•äW¾Ô7÷ËÏ¸¯Y\\3#,Sw†¼R¥9JÆì%ì:a1H\r¿*ÆfêxÊãEçÛÚxı‹û1et—Ú}û!îÜiGaË¦\rğ¥/ıIú\'úUà^ûÒÃêï‘àäpAÓ¤£³&9y²»Wï“tË0up¾}\ZD“Åó¢c8bî¤‰\"ÊDÚÖ¿[4¡Y½uM5Ï±KŒ\Z7¸¾‹&OÏ\"3g{wï‚µ‹«ÿu·F°lá|Øµc—W/ÿÃF™Ş- …Ş”«*v¡mG¢ŠéàßzÛ’ş‰\Z˜Ş¬ì1xKàÏ€â÷İõWİ¯Ÿïî7ı*ºD(nù“oƒ¤!\"QäĞì`tùì‡\n\n[ö­\n^ì«àr]Á‰$Dy½ßF©.šØ6c»quõ{Ê‰gjZP­c\nşÇª2ˆÛ¿üä£½ö]÷Á}ûàéî£T1ä¨õ¦©Hø#ÛÁ›×Ì*ŠkKrŞ¥TEs%¥&]ŞÄÕ³ù¢­	)ÿ\rÏ·@Ù?Ã†tÀ˜aæWùTŒêØŸ|ÿ[úõóİı&p?ı‹¯æ^iZsíÓ«l:‹Ğè)9¢È)ûæ\"l:^hÃÈú.\r²M )id…m]Åäd*ò[®Æ7êÛñêÓ1“Å³á5\Z‚ãrlJşàÁƒ°eıfJõ,»õØ¿Ï½Î76bu·è+Ak¾Rs©`š•B³ş«(;Ó_øÇ³tvø¡îÄQ{aú”‰ğ\'ò\'$é_èûÕGo€MË¥TêTò Y–›©9›½„ìîÕK«ƒ™ÌÍW?WÅRSŠè#‰Z¨:N^«–¼ªD¥Á_8C¦Jìù%ŠÜÁU×TıêÓÉÄ‰*õ!Tuú{<®\'NŸi˜Äóß«—-£Tœhc+ç\"·áñDÁuB%“»P¢íBÑ¾R>œNö„AsËwá—şñ§?§ŒÊÿ*İ¥\'wÃÍ7ß7Şx#Iúú|àŞ³m¼tï÷(•™Ä—ÿ%™‘“óuİìˆsùlğgªÕÂú$†Ûeh$ğ6;›\n²É²òEø­÷vèDc@Óûª½ìÚ9´+PÇcM]&OŒëqS¦«ÕÃU»±ì¹°ğ‰\')å×Ë¿J x¢!öR,!ıXÄŒ%]]47“ê§0õ\"¿LÃÒHÕ½é5‰0¼«ÆâO€\nàóİ{ÇùpÕUWõ»Kæ}>p?sCùKäşĞ‰hcÅsÊRC\"hlĞd}º²Ò¥¤á×!ë›QX–‡Û#¥Eó¤‘ÄØFê£ĞH–{Tÿ@J•¤&uÆwYñÜ‹ßF\\Ïà•yÃcwİ­yY—è4‰×æ ËTÿ’²¤¼çu76é?¡l­İ¦ÖC  Ôº4qd¿\"†˜2t¼õâsúİ#b}:p¯œlZ^t‰œÀcfœMç+Bù¥=«ƒ)Cå«|¶³od­ªo%šŒóÀª=;W9W¤Ih%æ•P\Zß6©¨ŸËvÒmë^#®:Lœqbº¾5’M–\Z7Ú0mÆÁıûàá›n€§z˜$1ÄO´l‡\nš£¤gãÙ;ØuÂÂhSÁ,5üª›©@W­Ùí[Yÿø6µ©™»Ìs\'‚¥K—Â×¿şu’ô}ôÙÀ/Zyî¶¦”Ahrä\'Cà3++¸`I„ôl•1o¦YßÉ2\Z-Ÿ}cÛè¶ÔDFHm#ŸÓ¶ş…Ø†ê@‰uK«}™büô‰ë[hôô÷\n2sFbÎy+Eû¯h,~!üò»ÿ«øgoÅ¤’õ’W	<héñÙ\ZpU8/RêV«œÈ_T¯V‘òïkâgŒ»dş7_şò—aùòå$íÛè³ûº‹<ÀŠÍÜ)fŸ–\ZRº¬FàÊBFÖÁ(äBG¹‰á—¥¨>fÁ¾üËuåJ0N$!’zÃû5‘Ù‹&½§\rÚ\Zß›Ö¬Ö´JŒ4¸cM}¿ÀŒÓ/ ®zÜ¿–¿ğüê»ß\'î¹à»ÇMJM·\0¼|\"sçÍkfÅÍÉ±vuƒÈ»wõläƒ¸á#Ù´¸²`È#¡l€Ÿ8rq/3×ÀŸ\0½ü¢³áÓŸş4Iú6údàÆw‘ã‹Vš‡9)v‡ÙÒÛÒÂƒA{R·;§²8iH¥`Ÿ–6ZÙMPÿHÓ–ÎÖG¸b‰y¥!Õq[ã[ê™=rÄÿ$İ*†©_}Úd°òâ–à»‡€!CªßmïÛsıÕ-pÓ·¾OŞ{ìŞI÷Å¨²íÍÀÕËl±ºçüPRÚ”Gq¦èPHÍ¥T¾²¨Ö¾­EkAÆGKm£Ìø.óI™»Ìqì:á ,[¶¬_\\2ïs/‘ÏW»í20I\r4ƒòÃ$\09³.»{õ>I[4;œL>ç;CY#ËlKà*—­º²s¦á]ƒ”421µ©Íi {~‰úRƒ};wW\r:»òß‡õ6ª:ımEpñio|\'¥ªÅs?k–¯ôúÇ«E´NayfÜÅrÅ¦ª]«$T²ù]në(ºÚUÉ]nşSğ½ûg¤¨h|—ù¨¡ş#¤øVµ÷¿ñDøÒ—¾Ôç/™÷¹ÀÏlï¦w‘{“ Â—Cñ\0bŸ.X\Z’G³ƒÑå³\ZoH!²4\\sáßŞf\'Z2[æ’¼°5åÙšjÈ:$İ*xÕU‰]Û¶P¢\ZÔw–›³×œ½f\r&7¸ê€Ïğ¯\\ü\n¥ŠªBÎGiãMÓˆ„7¯™K$ººhn&Õ%NaòD2¿hXÒE\\™ª{Ók’@ÌÃäÑ]âç?\rÆwîÕw™æ3Ÿ!IßDŸ\nÜøÌö+÷¹Ÿë,NøgÂÍ!ÃpÚRC\"hlĞd}º²Ò¥¤‘iÓŒËÂ\"zYBÑ<ñkÀVÊ\Z™t…–Ú—i„së7ªw–OšÁ¿Í]#/è‰Ó\"ùqSSç®úCk–¯Ê”/x=FÌ€‰ÕK¢ŒM³Àº˜\0ÖšãÔ´J¨ºÆëÑ˜ÿª`êiı: p­	¨»TÔ7bˆ7^§L8¨ï2ïË/féS{~‰w‘ûPgƒûœ:ß&™óÏI\'^O°>ªƒ]ªá\n®ş†VU‚^8¸©‰&ã<°jÉGj\"]…æPl^i±U\Zß6©h8›“\nSX³äy“¨cë›w–÷7à0>åõo¥TµXøà]Ä1ğÊ’B©IaYx\0ìÁ´‹áñD2¯DrJ´]Hº„ª4œÙUø÷á—‘òŸUM\Z5Ô¶[Q.ßõ†“úô‹YúLà^÷ÒÃÑg¶C“Ã¶fÀg–œå|2a½>\"ZqÖ§_”K»ÂòHéB°e&Õgí…mA¶Ôâ”m¬C(—”…ª»cKõï¾îKw–7zú{¹9ã0zÂXâªÃşı°g—¹-Ú?bRIog±ñœœ	„²¥¦EEs3©n œ ùY3bH¹Hùo½dò?}ÌPM%¦tï×s\Z|ñ‹_$IßBŸÜò™mãeçH±™;ÅìÓRC\"hnh°OW2Í³rùü²\\|°¯ÌwÎDË ‘ÄØú5Éë\rÒ^‚å\nß¢¬ÃG«¾³¼ú`Ó_ĞÊ÷ÛYÌ8õLå°úWœ.]8Ï{„ä\rLrâ’ˆå‹¹óÊ÷XŞåĞhWr‘×¹Ê¥?\\§ |$›Özã¬‡@A…¾ øáC;aTwş·Î=¾®½ö‡pÿı÷“¤ï Oî¥İ\0{è†´VÀİa¶ôXÚ“:¸İ9•UTDÈùÖGA-‹ì‹&¤aKW°œ+i¯¾m¥M*êkLÙ¡r¥İş];ˆ«}ñÎò¾?p£À<ÒÎy“IT‰AğâSQ‚A£A•»Âäê˜aÂÜã…ÍQ2fŸ‡,\'i¨á×ÊGr.•D2Ğ%ü7^t¾­×¿¸¿Ê\"Uô4µëîì,°ÔîÁàİo>§Oş‚X¯îFnHãÉa&’êd>§éYãƒGNAìî5ÿIÑğ($˜|Î·OƒHéàEÇ.>\\eQõäNZ©¤¶lğG¤m³û¹tmØ\'—»kkõï,ŸyÚÙ”ê=4yú{™9ÃÒ5ºGTûëmˆm›¶«£9ñ²L¯|1©<)ON<FxÜ…à•ã×Æ@¹ªbÚ›HÿÖÛV¸‹¶ğû·¹¢ê²Œ‘¿Z7{ô^8rhŸ{¶»×÷ó·ÿqîÈy”šS	!Ù_¶,;Á¢N›Œ.Ÿı0jTƒ°õgßú¨àÁu(¸\\×(„«üDóÛ(Õ¡I)e6hKB\'\\YC†T?¤ç\\ôV8ÿR(ÿ]Ø@E•—Égù:å°ú»É_|üá‚¹ÔhüQë¹‰X‰^]˜%šœw)U`üK$Õ¤K›¤\n\'\Z„hkÒE\\YĞ´<Êøùôd~·ñ¦3¦è×¡ö¥Õz5poZ¾\0Ö½üˆ?Aš†9v‡i}fÓY„Noò”;SöÍEØt¼Ğğëõ]\Zdš@RR4‰¼À\Z´u+¶u(PŒoç+V†tuÁ›>øQ7m*IªÅ˜ãfÂyïúŒ\Z7$5rŒË±)ùé§œC\\uP{$X»b)¥l]‘;İX½$ÊØ4W—Ö§æR¹yÄ×£Yÿ•İL=[ò_\"3›à•r|£Z¶wÆ\rÙŸ:üçÿüÇ$é}ôjà~å¾49KTs6ÊŸóÒŒ[/\0®‘V3›Ná|Ü\rnço¨>’¨epÑ‰ªãäµjÉG*!]i	mj3ß6©¨tåx)5@I×P´¯üŒŸ1ËÛ„¦Àyïù(tI’AU§¿7Ğ9dtuçÏ[«X¿j­:\Z¿®è1°R(W\'9×µo*€ç+Âã‰\"‚ë„J&w¡DÛ…¢|«pşeOTQ´ïÂ/#å?®ò}ŒÖ	#»Ä×:trÏšz~ùË_ö™Õz-p¯šl.øÉÎĞäpŸ^‹8U|fÉYÎgÔubD$áòÙàÏT1ML• ŸÜ.¦Á]w³ÉË_MÚæ‹ğííĞ‰Æàù¢ÄYoºFMnÏN;‹®n8ûmï‡Î|Ù¼ñËä\n™qÍ8õõo\'®Z<ÿè}Ä% &—¬—İ™+x<Q„7/#6ÒEÌX\"ÑÕEs3©.q\nS Òõ\"¦¤|Tñá\"é!áUøF5Ï…ÎA‡àío<şüÏÿ\\§{½¸_¾ßÜÆãÇxhü‡à›¥O´-#SVi_YÄêœÈ¥®CÖe¶¬p‰ìË×ÊŠæI#ˆ±\r×ÑHWÌ÷}ÒYgÁñgT)6ÜyŸ~ÉÛ(uìÂñø™œtÂIÄU‡ƒ‡ÃöÍ›¼9æñzŒ˜:	±ÇKÄäMC–©ş%dHyÏë\ZolÒBÙZ»M=­‡@A…¾©âÁˆ®×M8yì^ı#$×\\s\rIz½¸ññ¯½Û6´>c(?{±;Ì¶?¦òU>ÛÙ72†r	M—DËN œÖÒËâj çŠ4	Í¡ä¼Ê(mRQ_cÊü#GÂÜ7¾…R=‹	\'œgœ@©\Zr:0¿ÖÙYıMië‚?\0A£BÔ#„IxíÎ4GÉP[³°ë„…1LÍÅ¸FéRÊ’Hº*ü;ä;¥Zÿy¤üÇUñkKÇ\Z<¹ï|ÃIğ¥/ıE¯ß¨Öã_¶òÊıß£T¡Éá‚¦I7>³ñ™féÙ*fŞL²¾“e4Z>û$Æ.><BÅH-úÄ*µ|zNÛú“¥hB§Ô§½á\"èÚM©Ç)o¸œ¸ö¡ÑÓß+ÈÌÆÉ¶§æ?€¯85#C–é•/&•g#åT îƒPŞUñÜL©(\'ˆDştğoµàÿD\r\n{;Œdı‰QÀ»ËÇÏ¿ÃaòĞİpÜ”‰ğµ¯}$½ƒÜ¸Û>¸~+—À§ ÀŠÍÜ`Ÿ–\Z\"ÒÅŞ\Z…YdLr¡ˆ#>°$lıÙ·>fÁ¾š¿\\œHB”×û5‘ê¢‰íi¶ƒ9ß#FêñKäY5¦x\n¥â{âöÛp³à¾pğÀo.åçU£mğá¹“åÍÂ+ŸYEqmIÎ»ÖªYˆ¼{WÏf×ÏG²iqeÁ2Gp-Hø\'Ú*¦áÀ-Î¯ÂëNW_}u¯şôgnÜm/}üzJ©îğû£I˜Ódw˜-]&OœråÎyª8×ŸKª¦=Ö\'ÓF}“}hI‰ÿ‰Ök„çŠ«˜œL‰y¥!Õq[ã;TÇ9çG\\ïâø3Î\'îØ‚8‰Q`ï¼ïè°“±2,[ø4q4*TÙòƒx¨^YÄlbèc~Ò(Î\n©¹”ÊWÕúoªƒ20>ZjeNùÈëœûDÿzØğüKYFuìƒ‹Î?şâ/ş‚$=\rÜn·­z¥Á`&æ3iÎ_ÊÌ‚2³»×lÚÀÜÆ`ò9ßÊ\ZYGÁ¶®r¢êŞäU¼K†w\ry^…6µ2\rTbÏ/Q_j0ó¬s‰ë]Œœ0¥m‡UuúÛ\n9^æ\\p)qÕbñ³¸Íx%{µˆÔÉÌçüXŠC”p›ªv­’PÉæw¹­£èjW$w¹I1-ÀwáŸŒæü—ó1}l—÷*TÆéSÁøÃ^Ûu÷XàÎî¶Ü}Ş$ˆğåP|Ù§–†äÑÔˆPpùlğo¼!…È}° †C#·ÙÙ”Ìæ—%‹0åÙšjÈ:¤Üâ+3gr:\\òÁOÂ{ÿèÏàƒŸÿoĞÑ‡Çš4s`üfw+—Éı3‹—É«¿qoï¾£ú2y#ÈÖ‹!ç£´ñ¦iÄF\"8¯cÆ‰®.š›Iu‰S˜ü\0‘Ì/\Z–tW¦êŞôš$ôĞÓVÚ“Fæ¿ëÆ÷˜è]oêµ÷˜R¯Ì0kø>òWè0ìŞ£GL±\\¸¬Eˆ·ÁÈËà^¸€z-:Š\'ÇH]^sÂl Ó„›§Y¯lGiuà: ÂÓ!å´fÜ\0ñËÙ¾M:oÃprg«¡˜ISÆÃI§ÓgÏ„îaİ0aº{¾ùÀ¾ı°iÍ:õ·6®ÛK/ƒûji[kâ9ØâD´c¨Ñ¯¨´u2Íj8=óN¯m5cèˆQ#áäó/‚É³N†ãFCggş’«ns¶c²3By\"y·J³EİúÅÏÁ‹ÜK‚ê-³M(¸yÜé³…}£’(a1^xÓ‡?M\'U€b´›ÍÚ–ÄÏ=ö$,Z€¿fÒHx¾I\r|âYO¼´ÑT1N†	æ…œ(ÂØ>Z3^Ì\\ ¡b½€&X„LN6\rN:ó,˜tü,=a2Œ?Ş}:°glY½6ª¿MkVÃ«/¾¨æğ>Ò*£Œ{;×^=¼ÓáÙùğ|d”îœº5€‘Ê\'Ák„æõQ2ÈlY{0ğL…av¬É1iX§?¢–Ÿ×í‚Ã³vÀwnnºéf¸ì²ËHÚ3è‘À»í»¿ş›Şer.•—µñš¨ƒ¡FÈ™&Šêõe”6ÄÙq>ÜQn\rüÀmx:½êÀS‘:ßD9Mù®LMö(ó•!	\'7Ì¨Ñ#áŒsæÂiœ	£ÆÓ2—ÅÕÅã5;–¿ğ2,|üixmÕ:-f$<–q\"Úq­¨e‘gÍ˜Iëd†\"¬^Q#&^%fÍ=;é˜¤viÃFv+™ÔÜÆ,´4¤³¢p>™\'b‘w«1[Ôm[³æßy#	ªC´Ì6çIÜ9QóC|\0gñ™oy/L=a&ª}\\$%²‹)BÛ¢xPÜğ/ßDÆ–G.©œ£VÂ†>b6r>j¨ŸŸ©ÚØ3´P!×f‘DvÒÔ©pêy¯ƒÓŞx9?%ËØƒQîÊ…OÀ³Ş«ñ²-ù•¥™²ˆÜ©éœJê<¦Œ”ÿ\\y²ÖŒ2¸lfİ`äüÛƒÌC°Æù‘÷é×cí°~Ç~JàX¼mlØğĞC‘´gĞ#wÚîÀTWà £R¹p›µq6È`>ıß*¸ûy·:šªÚ<–øI?­®Fµ×Œ©\"»@hjm‰²Fu ¤µcp\Z/!Ÿÿú³àÜ7]]İôX\r@—ÅÕÅã5ëÒk—®€‡o¿6mÚb¥èŠ\'¡vK\nOÏ2ÅH¹¤m«(¾ôäsÎ‡sÕ‡Œ	ãı×afÚ‰ˆ\rO-\ré¬(œOæ‰Xäİ*AÌ–ïûŞÕšV…hymDÃ[d¹®,¾ìSÿ	:ñÆ´¬;2‹¤D*pïŞ}îøÁÿC‰._–©yM9!äÌë²M¹\\ÿ¬\rSÏ²\rÂÙ‹±vZáîIS§ÀÔ™\'Â¤éÇ«Ö“Ôßd6j$6RÍ|Ñ‡²Ëõ	`>d¹Ä­[ô<<|Ëu°qızj©éog\r¬™*$}¥;ŸFóï••AŞAÉılMnÏĞéFå$òé–Îìºùü„øö­/Â-·ü²GwİmÜ¸Û¾çŸ„{ÕÇ\r5¨+¹LrÓ­<„ánV›—l8&fbipÚú4pùÍëÀ\n$†³\"òÁuà´Ğ\"ì‰f}ÓÔÖÁüÄIãà}Ÿü\0Œ\Z7F¥\\™<@]¡óìì`ø§ï}\0zè)åÓ¼ø(-2×,ë	Ùj‘ÂÔã‡Ùg“gÎVz|XµA4H\" ÙjiHgEá|2OÄ\"ïV	b¶lÜß7Ï“2°ãûE±\\WäíerDÖ%õ•\\x%pVf¡m•¸è295uÒ¬!:më¬ÓF£åšcâ­3C¬œ(ÂØÁñ³fÂ˜‰Ó`ú‰jŒOœ®æäh:r,tá/Õq[õ¤0·™öÓólgÁ…ÚƒU¶“\n½’?sûõğä}÷Àw\rƒ^±™*x*é#kgn\r`¤òIH\"™Ì–õáù·ÏÔËèv£2Ã»ş”vr×íÆÂQµëŞã»î¶îFvÛˆo†h6p›	ËÃ·ÊËäš*Fóš’”‰ŸtiÍ¸SíÊÔ$`O56LŸvÖÉğö½[åÊäê²	ggâY»t9üúç·ÀşıTRıc3E-Ëæ(Ó‰£0tèP˜qÒ˜}Öy0éøé0t.\\ÆN\":äâ˜­–†tVÎ\'óD,òn• fËÆÇJàvçCÍ™ÔerDÖ%¹EÚ…`h{Tíj~ñ¯ßÔq9H,r-Q~U\"fÃÀ6Älì™Ö¼¡]j\\O›1¦0ÆM¦óD>vtuuª¢ªLİGMû¤Yä{&p#vnÚÏŞw¼0ï	jBÖ\\‘\"SI]FÉó_ó	ÿ¹ò|Ê ³¥|j–Ò3Ï0;ÎLÙ†•ıåpX‰Ÿ{m§æM7;»kZ×^{míºÛ\Z¸C»m=à¨D.XÖÀê¬\r2˜Oÿ·\n´ÔerD(p»²ˆšÌ&zÍ™ºk‘!Â)Ù¬Eó¶DY#‰:PÒÚ1æIAa‹reò\0uÙ„Î³³ñD¶¬]¿üşÏMğf3E-«˜ÑcFÁi¯{Ê\\9f$tva©l¢C. ÙjiHgEá|2OÄ\"ïV	b¶l\\eà–ÕF4¸¬åíerDÖ%É…R\"» \"ĞvÛfµüì˜Òå³ºÓ¼¦œræu¹¦L®?mÇü„IaæÜ³`òô0rìx>fíÆ`«òr5å´şX›—qÚÊE¾ç·á7¯Z/=~Ÿ\nâ«’\\9¹\"EZªL}_™ÏK£o&pç}”ÜÏ¢F©p’óoÂC”!uFì$&©C)WlÙ[wã€PàúdõáJ×s»î¶nÜm/ºÿª‘\\„ê\np*ÉYzˆ7Ã“0‚˜|àæn¦´Îfòù“—“¶ÄOúiuà:°\"jÏ…Ğ¡iÆ6W:PÒóyâœ™ğO^¡8j+7Ù1Š5¼Ë&t=ˆ·¢A°né2¸å‡7—êïä3NƒN;&ª…mÄ˜n%Â÷Pšiäe’rqÌVKC:+\nç“y\"y·J³E]Õ7§EËjÊm„9ÊûD±\\×±“¦Àéoz;9š$\nY·:¯ÓÍ\"¸<ğ¼úÂsœİZÙò-5\ZY/Ík¹)ù\'Sf¦ÍPõC‡\rS;gü°¡…~f—şxà[Y™ÆÀâx+ã´•!‹|ïnécÇ¦ÍğÒc÷ÀËO?ö‹›­2ÅË¤W5¬*±w.qIŸ/×<é¡S$ó³Å·e‰ñòy…n×Y˜>pè<¿†7¢Î¹õà®»­ûnµÛŞ³•îVÖPS³’ï·Íç¡«Eü1°Ñ£GÀ\'şğ“t\Z•c‹såò uY…Î³³ñVd˜]ÛöÀá£aèPùc|Íft2Iˆ¹€8f«¥!…óÉ<‹¼[%ˆÙ¢nóŠÅ°ğ¾ÛHĞ:¢eµ	e·;nw\'uÌ8#ğ&»¬[Ê/_	3«}\ZÜiî&W*.	Ï7$±ù9nÂx˜}Æ¹0^è1Æé¹ÓZ—O–xşèÛÀğ»¶n‡ÅO=\0{ĞâÙšÈªe«éÎe«ÛÔÉšQ™-ëÃóo©0Ì1W6sú¬N/ß²¶ìòß\'€¹^ëÁ]wÛ÷ª¿†7ı\ZGì^5%Y*Kñš¨ƒ¡Fh²‘†/“#e;Î—ø~›$dK§WŒÆÔ]‹öLÉ`ıp>}4ö6K}âô,PøĞo]ÇHßr9¶8W.R—Uè<;{ oEÒVÚ!ùšÍèd’À}’C@³ÕÒÎŠÂùdˆEŞ­ÄlQ·ä‰{aÕKÏ‘ uDËjš\rÜ]]pŞ;Ş#ÇMÎDVFùåb)‘]TûöÜvÍ¿*ÎŸKÈê”¦Gá„Sæê+ASfÎ†á£FÒ³ÿX¤ªå,£¿c)pƒøs?¤ß÷ !«æóœ0>t_²ÍÉ5OÀøa%ó³¨Q*œäüÛƒğÁ°Æù‘÷™©C)ì(ì=x^ZË»nÎpèh\'|û¶¹Ã¼mwÛ{·­·“Mw6J²Ô¦E-œ\r2˜Oÿ·Š|àæn¦4ÕÑšªÚ<–øI?­®Fµ×Õ«Ğ–(k$QJZ»ÓÎœoãïµ5¨½ÜlÇ(–ê ¡óìì@¼I[i‡äCh6£“IBtÈÄ1[-\ré¬(œOæ‰Xäİ*AÌuOİ|­Zø6“ 5DËiÊm„=ŠtqA‘\"ˆ¬ŒòËÅR\"¸ÑvŞ]wÂŠÅ¯êòÑbæÉ§ÂñsN…±“&« =BÙàK„Ğ§šLC2¢Z.ì´ì\rÜR´kë6X2ï!ÄåË]d5M;&³î‚oGL\0y%÷³5¸=C´•“D/“#l}°\0¯¬ß»ö\"‰Ã’ºÃ¼-{óògáÑïı©æ{5-ûùc`)§5Ãuà´Ğ\"ì‰\nß&mHÙqÕş4Œ\Z‡/e`PY¶HW6T—]è<;{ oEÒVÚ!ùšÍèd’àÆDqÌVKC:+\nç“y\"y·J³İ·c<vCñÏÔ–E¬œvÁ_ÊÒàqŞÙ9Î}ÇTĞd\n¹!‚ÈÊ¨cå,Ü(Ş½ë\09í­Åh\"h2\rÉˆj¹°Ó²:p+ĞÍ…\n»·íP;ñáù\'0ˆgwâ\\gE~ıesrM0>LáÖŒ2ÈlY{0ğL½Œşhwõg3×	Y.­|¨ÄÎ}‡aÑzó+—²ëp×ı­[_„_ş²½»î¶nÚ¼kÕRh”d©,9Äs`ÓiÚ€L^Úÿ˜©»âÙ\ZJvW¦&{”ùJ$ølöäé³`ÚÌã`ü”ã`Ø°µX\r‡Á¼£`oEBGƒ‘Ü*ò!4ĞY‘´•vˆ@>„f3:™$¸q‘A@³ÕÒÎŠÂùdˆEŞ­Äl—<~Ï1w™|îŞSçœîU67DYù¦D*p;PÂºPŒæñ ‚&ÓŒ¨–;-«·‚ÜjıÜòÚ*xEñ—yR‹L;LFİ„lSrMğ}(ƒÌ&}äüÛƒŸGCgÇ—)ÛÀ°NïùQJ“6A›ñÜk»`ÿ¡|_ásİÃÆÏ„ıèG$©•î=ÛÖÁ=ßø”æåd×’,µiQgƒæÓÿ­¢TàV½«©:)²\"	]YDMf“VWc‘·gJvëGÑ¬mW×˜6c:Ì8ùTœ§Âèq£¡{ØèĞ—ûhÌ9Î¿å­Hèhd¹Ü|ÍtV$m¥\"¡ÙŒN&	n\\dÇlµ4¤³¢p>™\'b‘w«!ÛÃöÁ£×]‡ø;‘f«O;ÑhàpÜL8ëò÷j^V87DYù¦D¸%¨šäûÅ“Bï\r^â5	È5¤\r#¸ìƒøšÕ°hâº=Ù¦äšF0ı€0~­™’ûY0`:IÎ¿=Q†Ô±“˜t¦¥42?poÚu–oŞK)|‡ù×ö,[¶N8¡úÛAT¸ÜôUXµàNÍ;×ªµ8ĞT’%²ÔÏAÓêˆÉnîIãßpdÃy4ÁeÁ\Zâ\'ı´:pX²7ep8mt³æàc\'³aÊŒ`Ì„±Ğİ\0\'ÚèÌÚÖç¤÷àÊ°¼	,—;¡Ù€ÎŠ¤­´Cò!4›ÑÉ$!:äâ˜­–†tVÎ\'óD,òn• d{¬ì¶<Î/ºâ“ĞÍ|‰\nç†\"+£•‹°D¸%¨šäûÅ“Bï\r^â5	È5¤\r£ pkp>ÄŸ¼ízX·z¥É¦äš%`úa|éÉd¶¬Ï?Qf<S/cQàvmËúpi?p£æ™U;r?>‚©g×u©uÿdøÁğıÕ£ÒÀÍ/\\Áñİª)Ù«QšìAß¤×G´#ªy‘@â\']Z3ƒà¤ÓO‡é\'›£ÆN}y¡ôÚ†şX^\'2<‚ôÄˆaŞŠ„F–ËÈ‡Ğl@gEÒVÚ!ùšÍèd’à\r€8f«¥!…óÉ<‹¼[%ÈŠvo^OŞòJUƒX}Ú…²›ÏÁ”æÀi—¼Có\Z¢Â¹!‚ÈÊÈ[°}Ô[‚Ú©I¾_ü1)ôŞà%^“€\\CÚ0\ZÜ’9t6¬\\\nî»Ö¯^¡e¹f	˜~0y­eÙ²>dZ³”Î˜y†Ù±eÊ60¬Ó{~”Ò¤©B‰š×¶ï‡5ÛÜ\r|ìeß‘.øæÏ‡­[·ÂØ±òş¤jPià^úø\rğÂÿ¢yçVµTñœd©,5Äk¢†\Z¡\rÈFšş~[%(©X?¯¤Z@§õš3~´È-Å÷oÏ8ù4óÆ0uR:;ğîB6@ÊE¥L‹™×‰ ½Óâ­Hèhd¹Ü|ÍtV$m¥\"¡ÙŒN&	Ñ!Çlµ4¤³¢p>™\'b‘w«R„—ÈŸ¼éZØ·Û=Ò*bui\'\Z\rÜ]ñ)·ÛFˆJç†\"+#?rÑ”¨·µS“|¿øcRè½ÁK¼&¹†´a4¸¥ìĞÁÃ°òùùğì·ÃÎ;HêÃôƒÉc[¯d~O¨Q*ú&ÛM:I²ŒJçGzŞg¦¥42¬‡f,P³ÿğX¸Ú¼!zZÕoºüğ×ı×$©•n~áÜªÖ*“Hd‰!ŞMıß*¸ûyÈöÔc`3æœ\'}L1†èTR|	g ê¥ù¡¨”i1ó:‘á¤÷ÀmEoEBG£ËåäCh6 ³\"i+í|Íft2Iˆ¹€8f«¥!…óÉ<‹¼[%`ígn»®²Ç¿±º´eƒ6ÏÁˆ1ãáuïû¸ŸKT:7DYu¬\\4%êÀ-AíÔ$ß/rLzzoğ¯I@®!m­n\r’ïÙ¹–<ı ¼øäÃöÎtÓcc[¯ä~OÄ·Ëã¯?ıÑnTNÒÈc`YËÅ÷À¶=æ\n«ì­‡ÃÏî|vD>¸´‚Ê÷º—§~úš÷]ªéXáerY¸‰\'¥\rî$0$¸Ñ7éõ‘íLzÜÄIpÆŞÓæÌ…îC”5jmƒ ^3DX\'äR¦ÅÌëD†GŞƒ5Ì[‘ĞÑèr¹ùš\rè¬HÚJ;D B³L¢C. ÙjiHgEá|2OÄ\"ïV	PÔ® ˆÕ¥](¸¹ÿO8ó|˜uÎü\\¢Ò¹!‚ÈÊÈ—\\ˆ%ÜwĞ¶˜Ö…b44™†dDµ\\ØiY¸ª\rÜ®¦ƒaû†\rğüCwÀ²—Wi#·-§>=‘í™Öl6Í†ÙqeúßÀ°NŸõáÒñÀ½cÿaxeİ®L)¿š¿şëÿŸğÛ¿ıÛ$©•nÚ¼Î¥jœâ9ÉRYbˆ×D5B\\hFŒc&Mƒ±“Õß”éĞ5l„R›A¶uí*8¸/¬_±6¬^©ä”¯ä÷Û§½î0ã´s`ÂñÓ¡Ä¥oMéO‹²	Q/-ô=ò$³r„ä¤÷ F\róV$t4º\\î@>„f:+’¶ÒÈ‡ĞlF\'“„èˆc¶Z\ZÒYQ8ŸÌ±È»U‚};·ÃÂ{niKĞFÄêÒ.4\Z¸Ï}ëûaÌ´ãı\\¢Ò¹!‚ÈÊÈ—\\8%êÀ-AíÔ$ß/Ø—N*ôŞà%^“€\\CÚ0Ú¸M«qLQ›®×^y{èNØºÑ\\¥å>à˜rüñ0~ò1fœ~<–÷í…-ë×ÀîíÛ`ãk+a×Î6…íÏüH7ıo`X¿~JiÒ~ĞF°FC±Ï®ÆGÃäk¡\rÖìÏ.İÏ=WİM¬ˆJ·|á\\ª)“,µiQ²³Aóéÿ0¤k(Ì:ó˜uöÅ0z\Z¾òdìñ\nš7k_šKŸ«–,V)²aBô´ß\'¿î-0rü(ÕÜéJiı ˜G9¥¥Ş–/ÓBïÙ#O2+GHAzräoEBG#ÌåäCh6 ³\"i+í|Íft2Iˆ¹€8d{ôh‡~1ÄæÕË`Íâçà¢+?A\Zk+ÃÉ#ş©PX÷ÊBXôÔÃ•=ö•E¬íD£ûÒOı‘¦^.QñÜAdeäK.œuà– vj’ïìK\'zoğ¯I@®!míÜÌ#öîÚ/=z\'¼8ïQ}ÿĞIgŸÇŸzéFáÛ«‡Š?Û·À²…ó`ÙÏÂnÄı¾ôGºQ9‰Iûõ±PJ#+\nÜGaİƒ°rKşÑ0Ä¿İ¶n¾ù–J_ÈRIàæ_c8—ªqŠÇ$Kdi!w§\nØ§\\ğf8ñ¢w@g÷p2 ?›Qò\nÒ¡Ò{·m‚§ï¸	V½ºH‹O8íl8ë²÷ÂÈq£U)Ù`-y‘æ?-BÊ2$D½´Ğ{öÈ“ÌÊ’GŞƒ9Ä[‘D†w¹ùš\rè¬HÚJ;D B³L¢C. F[Œ—»·nµ‹_€/>àï„+×º^Gá½ÿé¿h[\rë#V†“G,¬Éö5+àÕgƒmÖ\ZA›«G»P6h#Ì¹\Z¤÷ê´—ST<7DYu¬9oyÔ[‚Ú©I¾_°/TèÅø¶rMr\riÃèÙÀ­¡d8.Íã²éOğ^=|,_ø$Ì¿ÿ.8 Öƒxà6¼_7¥ti?pK†\nÜøHØÓ+İMjK¶\rƒaãgUúB–JwÙ›Ò4¥…x<}“?.øÀUĞ=f‚\"´ıÙŒ’W6‘Ş¾nŒrœªÕ!×ít™]Ûä|Š4ÿiR–!!ê¥…Ş³GdV<‚ôä`!ŞŠ„F˜ËÈ‡Ğl@gEÒVÚ!ùšÍèd’rJ|ôè`Ø·{?l\\¹Ö,Zk—¿ª‹·“EMÍÑÄÂKŞó«\rÜ[V¯†—¹öíªî®ñbõhÊn>OC‡„‹®ü´æ½œ¢â¹!‚ÈÊÈŸ	\\yÔ[‚Ú©I¾_°/Tè½¹E¼&¹†´aôNà&†(\"Â{õÈãĞ¾½ğÄ­×Áêejíğ|`7»R\rëô^}”Ò¤^Öh‹6ìµ7©I´ãÑ03’Z\0¾Ú”ƒv³àó€\'xÎùo‚7}æ¿À°±°\"Œ™:Uu~ş;ˆ\Z½‹Ã‡Ã–5›añSóáöoÿ+üâ_Qôë0ï×7ª ½Ô›0şÌBø“²*lY»fÀífĞ­w\ZıİÃà’.ú\rzÃÁ[K2H¨’ùä4rq>º€Ë.¹®¹æ\Z’´–wÜòMiçNµVñ˜d‰,)Ä_ğOÀŒsßl*—W5ÍÓŸ•K^AÚ ²i²·ç¡ŞqkÖ€x+’¶ÒÈ‡ĞlF\'’¸›Ş¿g?l]·V¼°\0V¼ò¢R›šâ\'aSŒÜQ»KTúS.=¶\"óÉÙè«Şq¯|~!,~âJµ±:´ewÛ3ÿ”½¢—şVı·Ëˆâ?)Ã%eÿ¾p`ÏØºaìÜºæ¾áb2´[éë7¶’×u¯ÅAŞ«G\Z+>	OÜù+Í›.v¥6û¶4ôMjùşÛ°o8ÜûôrX¹rIZCK[¾)\rá»ÂAlÒ,•ê,Î[¯€Ù¿S(êÀíCâ­Hèh”¹Ü|ÍtV$m¥\"¡Y—>r´vnŞk_}^[ò2l|mµV3<šsaÜ«)Á—ÁJÈÛN¡7‹ŸÑ¿ëÿæ7ÕÙ†gû ú9bë—,çø%¥Ú‹XÚÑÃI¸¹gæñeŸ®·†¢‡\r‚{÷Âîí;aëúÕ°fÙ2X·rlÜ°=;±¿ñ‘ÂÜ‹/Sé:pc+yly-úˆğ^=ŠÁÁÛô»a¯.JéÒfaxç‘	ÜË·ì‡õ;ò7±büä¡\rpíµ×Vr“ZK{Õ‚_«÷ßQ\nû“]©&(“,•%I~Ú‰§Ãë?ñÇ&auàö!ñV$t4Ê\\î@>„f:+’¶ÒÈ§°ßQµËØk¿¯>·@¿l\'gGj­µĞœP2p›|¦v²°ušı;ÿğAÇ`š,¶áÙş#ˆ~XÔ[AÎeÜ_ù):oè•§Sè#+#Ÿr•èKû^ÚwvmÛ[×­‚5ËWÀÊÅ¯Àí;T\rTbm±7Ñ>Ò.JÎ˜5®ü“ÿªÒuàÆVòØòZôá½z”Ã³wß‹}†RÜİÆO¶çQidêüf”¬Ñ>˜<pø(Ì_•¿I\rû`ÉÖá0|B57©µ¸ùç;r²cçr’¥6-J6j,¼õw¿Ã†Ub~a¨yú63iƒÈ¦ÉŞv}¸5k@¼I[i‡‡tÀ¾]ûôsó+^|V-5ßGkK\ZøœÍÉ‰\"´©%.dÆ6˜uÊò(Ç£›TUîËWÂÂ{n Tû+¿]#¿vî)‚ìY—şL˜y’ïA4€Ï…‡¬Œ|æ¡77^Ú¿wlİ¸6½¶Ö.{–-yUémuu_Ø*(ÆôM&p£[ÍˆäGÿà?Á´SÏÔ¼­Î$©n>d¤+­A¼&¹†´a¼À¸ëûß„m›6i×D¶çñ\\™[cùóöñÜšİ°ç€?ÕUçıGºàŸ®{¢’›ÔšÜÙg·Î•\ZÔ%/“_ğîOÀñç½…R\nVYnrhoEBG#ÍåäCh6 ³\"i;ì€-ë7ÂÆU+àåyOÀ®»üA­¦o\r¯³YªYKÂÜÄÖ™|ÆÖî¶‘ÕùyR\r‚·ÿÎç¡«»¢áÙş#ˆ~XÀÍ»à©›¾M©ö!V~» F~!ÌÜSöŠ\";ıÔÓáä×_ê{\r0ç\"ƒ¬ŒúÇGíÜG¡öî9Û6o-kWë\0½âÕ¥Jo<ò°`Š@× }´6&Ù±‰),Ò¦‹˜yÂ	ğÁ?ùoš·uÔ™$•àÂìÁÕÁ@èe„õK^€Û¶Ã¬³.€!CåMTÎÆa`îM+Ã}×]K]í|xõPJ—æ5ÆÀ;¿ˆHà^»ã\0¬Üâ~xıP8„§WwÂ>ü›ğ…/|ÁšDÓ[ş Â¹QMP<\'Y*Kaß‚vÙïı¹I0¬!úÈf¢?aãxiƒÈ¦ÉŞvr¸5k@¼æĞşıpã·®Q\ZïcÀ¾SÿØTd7‹t7¼Q$mYn„æ<˜|Hİyq¾0IY¯„Hİ\'æAğ¶«ş†j’¶áÙş#ˆ~Xó[Îeş\0>tÄH¸øCŸö=ˆĞiô‘•‘_>çYT¸{ví-ëÖÁŠW^‚U¯¾\nû÷›çz±\n6hŞQ9™ç¾ĞGuĞy—É‘u#_!À¾ÿªÏÂ	ç¼ÚOÌçú„ürÁY¨z9©ĞËFüàİpÃ?şo¸±¨ÑcÆÀo{¯~±Õn\nâ^3p#øé·aãšÕŠs>¼z¨ó`Òfı‘ÈŸß€•	w×O-wï\'Çös•×î—µş&µ¦Ãï·›ìó9¯»”¸\Z}ß~ìÜaòn~XÈ­C¨ıü‚7ló·ëï9Û‹ö¶ \"ĞdÅ#şÚæ•ær_ÂQ;¶î‡å/-ƒGo»~øÿ®ı¿ÿ\0¿ø·ûnú,}é%ñ2‰òç¸ğ\\)Wé¹apçÏ~»6o¤TÏá±›bƒ6bÇöípß/~ßÿ«ÿ~öÕ?‡%ó‡ƒôãg¼Ñ¿1¬ù™îFEÖG‡Z¼Æ\rwW5dÌ›6|7¬\\¹,X@’æĞñeâK/“¿|÷w(•…k×WVœG\\ğ¡ß§TÏ\"_Ãş\09<ˆ·\"¡ËEÌ@>„f:+\Z¯Î_\0Ï<ú¤I)9/Nš·vÈ“Ü$4e½¶ÕS£0GL*{J°÷3N¦Ú]£È–eŒ5?óŒ ‹w\0ÇëÊçŸ¢ÔÀ@Ùİ¶CŞ~¿Ú¹M›s\Z¥|ğùò)’ÏaAÛC‡ÂúÕ›àùÇ‡\'î¾}äxeÁ3°rñ\"Øº)ÿy9Ã½uHğR,á_ñsY\ZŠÍ¦%8yøĞaX³ø%8ùü×Cç.%ÁŒ¨eZ=–<ù\0Ì»ŸmÌI¼tùKÏÁÂï‚%O?\nC»‡Ã¨ñ“ £“¾zª²\níiq\ZÃÇL€Ï=\réõÅ^Ô9ğê\'¾FÁÓ	¼f±U¿ŒE^o02j*¬Z³Şıîw“¤q4µãÎî¶½®\nÔYL;étâj„ ß v 6oÜËm€Çï›¿¼ö¸ş;?ƒûä÷\'ííûo½[órñ,Z_\nÔ3@œ¯pX‘“Eê³uÀßş­Q\rä\\öâ–âñ¹ämkñ2cïáîŸÿî¿é:XşÊ+*èˆ®5Ùº3òËh+hÜ×ÆõëáÆú;ı!¨İÀ }ß/~N)¡ù¶SíÄ¸ñÇğÃÿı_áæo~–?÷,ÊÜd5pÜI\'CÁy\ru‚‚6bÂóÁ\'äé¤IpÓM7Qª94µãÆGÀÑ³Û>Tµc3)ƒYg¾ÆÍ˜C©…ë÷*\'qs8td(ìÜ¶Ö­ÚK_^ózî¼ñNxâşÇáé‡ƒ…O=\r¯<÷¼¶|%lİ²\rvlßË-ƒ¹gŸ\nC:É‹I¹È*ÓÒÎÄ¹ñßd]Ù].ş³2C¨×I¦ª_µLØZskcòêô^>–²^çu»qm¡vã3NtówÜà°ú ĞÎwïŒ:Ûi%¡ìİºî58nÎ\\ÜÁcÏÀH‘|Ş³º¶‹y\Z–½²„RYD\nÂØêæQãŞÁ}“×›™²E2£ÑíÙ³k7¬|ñY8Eí¼;¼wuxáÛà¡_ŞH)B¤^ÙóÉ½»wÁ²ÀÂ‡î‚õK^†‘j§:|ôXz\\®yxåíitvvÀòæËW\rgYötxç8§#ˆüØM»Éİ]è\Z|[±N<ñD˜;w.ICÃ7§íX·ø@)çBÕVñœd©M‹’Şü›ãgvİÖıˆš§?aã9•6ˆlšìmG÷àÍi‡¨ôı°qÍzØ°ú5XşÒó°qã—Àil»U±Lû2Éî¡]ğ®+ß³Ï8E¥l‹ôàAØ¼RçÙÙx\"×şı7íwƒ:˜jyó\'¡eÄ e½“EhS;íW+èœhÒc*w™<¸/úàgaÜ4z¯½m¸ë¢Ã#ê\\\r…û¯ù\n¥ªG¬ÜvAŒøB˜9§ìqü)–ëÊİ†tÚì9pÆ[Şá”\nîœdeä$(©›Ó¶mÜ\0÷Şx³İe³¥æµ_ã“×Œ¼\rñ(µ¼E{#°b+ËÜ˜¦ˆá	‚EÈd¶İC»‡Â;>ş[0ûÜ‹PIR•¬	ñª.N*ôJşø?„…?æ»LÖ‹‚L»:›2f©mg½å]0iæ,¥¤r©¯¼z l:9zã¾õŠ\rúˆğÖ¶9à»Ìoú—¿Ív‰n¸‘É5ë™±äv+x\Z›q6î:‹7„¯¬¼¼yŒŸvüàîÇ¹\ZAÃ—Ê7‰ç¶|œdi¬ƒA{€\0ŸqŞ¾e,}q)Üsı¯à»_ıGøÖ_~ğ¿·ıä\'ğÔƒí8ÌĞÀ»doùÙíğ«ko‚[·iY•˜0ÙB–1ÈÅÈÄ!H[Ëf}›´œa¿Nºoçâj´‚Ø¸ËŠ×.[k½@©ö¿|øÖÛr—ÆcÓ$9}š,SıË-äM¿_¾õÿN©ê°yİ\ZâÂHÕ^LÑ°İ+—¼·~÷jøŞ—ÿ¿ù§°}=Şl×ô=Î½|—yªá­U—ß˜	#ü«R\'Œ;ÜÒåò†{<~7¹ªvå3¦ïã¨êÂ=»ÂÊÅ+á¾nï}õkğ¿ù?ğ“oşüúºë`Ñ/Âş}æFˆ–{‡È!öêâpıw¯§Tu5fq©Ií”¦’6©¨Ÿ{ÁI…i¼R$ëP£2„¦²”á˜ï	àİÎ÷^ìÚµ‡$!Ä…¬snJIÏÆ³w0ye9F›ZîSCUã]›7W\r¦Í>©’y’İmK ê•ùOÁMÿúøÉWş,¼ïvØ»«ı÷ŞT…±&—…¿ÛÎ!¦dêPÑuüˆø?}jÓÁ»¡Àw“ïX×Ü#!±ÉÑß€7íÚ±/x	~õİïÃwşêoàÚÿû÷pÇO~‹Aï„“ík´ídÏ‹]|Ä8ÙAkU‰‘cG‡E¥F²!6{90ß–˜r—¤üÎãKê‡UD\rj_Pò[ĞGA8VWTSÍÏ¦°mãF¸ó\'?­[¶Ú:!d½äU\'šGÑ k\0\r¸JÍ‹][ª\rÜ9$êY4_Ë\0¯,xè¸îk7~ã¯aé‚y}ş†Ñ®¡ÍŞãFVªç¸[\'ŒÀ{Â8ó¤Épİu?£Tch(p¯{ùâÒà¦‰yÔ¯q`ÿXõÊr¸õ»×Àwÿú¯à§ßø{xà–_ÀÚUeî°-71¸¯xñ	wûÊ_®[óê\nâªƒ™Ô~Mä<o$H{-„oQVñE+_¿w‡{ÙAğÌ¿ÃÿXUåì»G\'®=X2ÿ¸ÿ¦›a×NÜi7ÚŞ:T\"¸{_0«háeòÖªÙKpmMMçä•¡Ú©æâÃ·ü~ü·ÿîüŞ?Ã¦UøkX}üRºj@¬uÅkQ\Z©Ëå“‡‚_ıê6J5†–·?ÀÕ°Éş=»ÁËO=×~õoá‡_ùk¸ó§?„u«›FÌCí+²\r¤Ö†V§N!Î 5©R·5zfcY´œ2„üV±c¨ãÑ\rÈÌ´¢ùK\Z›V¯‚~ñ˜ÿèêóA5bŠêåŸÿXİ¥\rJÆÚ—Fq¦Ô¨l÷MY¢å‘okÙú¯[µnÿş?Áó÷õÌö4óö´,\nÎk¬İªCœÊ÷—ËG\ro¼\\>ı¸)M]./¸ñ\'<åŠøh|8ì\\[ı±UØ^yêiøÑßıøÙ×ÿ½ı%½u	aÚÌ§‰\0KYã¯Õ€»[tûêeÕüÎ+Cÿ~p	è*Ø™œi ‹*\n^J¼!gâûv¯<í?è5D²¬¸cHµ/è8°ï°Ø÷ßò+Ø°v½ßWÑ:5Ú£fPÅrÅ¦ª™Ë™©’­îÆz©½U~ Ş²~q}éf—oY“GÅ/—Ÿq\"^.¿RåQ:p·r™<ÄïÙÖó¯şKá¡~\n?şê_Âc·ã#\'Ù×ÿ¹3a/eËFUë[ˆá…ÃĞğåº\nç™€_–,#|]ØÁ«o°òÎ·¯ÍÛn[¿Œ¸\Z­\\&÷Ï¬û®nwDØ³{?l\\·RqÄëå4ÒÆ›¦	o^33–HtuQÄ×ÉV	|ÎŞ\"Y´hXªş	eªiÜîİÛ«ê¥àHÄšl7Ñ2ˆ].Çõ|òˆƒğË_6~E¢tàŞ¼Ü·j6pe’…Ø¸üâúV½j^ì`ç*1­hÿôf}3\n‹Hè@íBaô6p=Û(ÒoE~qa(,»F!¼ \'NKz\\\"Z\rvn6»2?\0#oÎp™z•¯{ãÀº˜ÑÖšãP ÛüÚJâÚ‹Ô\\iß<:\n›7nĞÏN÷lß°–8…Ğ	iÎChl‚¡ƒõ_x¹|ôèÑ\r_.¯`Ç­ªİÄ,ymqÏ=Z|ãzd«\n˜C[›êzáàQÒúx+ØØÖb«4­´IEÃÙœT˜Æç)¤>™¼ªvè9’¸\ZÙém‚XµwŞ:Èè5,¥NilĞø°óQAúzÁRŞ|9UíÆú\"ÜÙÑyZ€Õ/·ö£\ZUbù‹¡¯|Õ˜Nµ-¦+Ù!ãw—Ÿ3w&Ü}·y½tY”\nÜø¶´ƒÁWœ#49p2ìÙ¹\r¶,{Ñz/<ş0qåàÚA”Ó¢­9¤t!Ø2#Ÿ,Š.Å5‹ô~Ö¯¬C(—”V·à10Ê`ç–üK´ŠîáÕ^\nN´ ï€p¬®Éñİ\"vÇi…Êâı«aQEBùŠÆ¯@ÑÜlÓÔ5Hø®bÍH¹ÈúõÙgˆë]ìÙ¾¶mjækZ7R=ë“±Ããw—ÏpË-7SªJîµßoó¼á¦•àË<J\\ïáà¾=°r‘ùÎ#[³ ¸3!ˆb¤N¯ƒ_–¢ú˜ûÊ|çL´=ğk\"dQöÉÂ·Ö›tqÛ„^åãÿÒO\r‡V¾ß.F£¾‹±cóÚÀü2å44íbùbî¼ò=ÖŸw9Tß=\0×Àà%¤?¼—zX·j%ìİVıìF±â¹yÄ)ˆ5$‹ÆÛ\ZUÎÇøLà–±{aûöí\rıÔg©ÀLU¬ÙY¥°ü…gzıîò}À¾Ù¬\nØBıÂ½ci£İEöUL fšÔY¥M*êkL#¤¹0ƒ2$ë |·£o:KŞUßß!ƒ•›ÌgÇkêÊO+8t\0ßºEçQ+ÇÕÇ?ç¡º#¤ÍQ2fŸ‡,\'i¨‘\Z‰éqÜ^4^t¾­×ß÷1ï×­ı\"V«ÀïÙ—<úñ æ/“7Ò%£‡Åwİ¯?ït¸á†(UŒÂÀ5û¶4	f\"©æRzÁ¯›{sLØ½u3,x¸±Ëä|yHÚv± „”.^tìâÃ£DŒŞıâô²û¹t­Ÿ‹áMšœ‰ïÛû~;ì®Œwq­#İ;}éèå¡sHu¿}…WQ\')÷?l”©wùâ•:sÊUÕ·WüUÏ”9gFê2yJW1+—,†\rËzï¦äy·_xb¨ÊŒ1l71àº•z‹Ú´q\rİ V¸ãÏnûà¦Éy”šS¬Ú¸j¼úè”êYÜû³ƒ;¼@”[(Ê]Yßú¨àÁuHï,\'N›L\\5Ø½};qş€MJ)ó´A[b:‘íO—ös§R5$²«Šáì³gƒá†ı 5®ú·¦íÙ•ı»ñ3,ëîMS‘ˆ·Oh˜%šÔ)U`üK°zçÖ6üHN²hÑÖdÓâÊ‚¦åAûÕõ½r‡ùÚEÏÁkËÄc`ª>±&$ÛM´ŒÆ¿Ñ…ãºöÃóÏ?Û¶•{t®Dà®ö1°½çØ±f9¥züâÇ°eÃF[n†M·Ô0ÿôf}—Ù‡’”4<‰J`ç¶…~Ëk\Zá|…ÃŠlc‘_ÿƒB‘uä—c³pœé›À®¸•o¹°•©WCuo®.­9NÍ¥¢\0ß*RŞÛW²é¯¬ÿ];vÂc·ü„R=ƒVÃSwÆnş*8¯©óF4ì#ŸqÄĞÁĞÙ‘—ã˜í€Cpáùg—ŞuîìÏx:¨\n45K0±”÷ÿğêŞ/?z,yî9J5‚|§#¸ì$í²mm\\t¸\n0ñ8ÿ¥í„®‚]lLmRQYEÇK©J¢k–Vøß=å/“‹ôÑø÷GÍ »Êş†ìô^:®¡_ã!6h|˜ú\Z[í›\níòx¢™×B%Ûµëp dODçi`«–,†\'nş¥ÚÚ÷ÿü{pğ@ì\r˜M¶­LÒ4õ=÷¬©£à®»î¢T\ZÉÀİÊ÷Û¡É‘šøxgğ}*xo^öIÚƒGÕNû‰»ËuÃ^Êfª®]•‚|r_1\rîºÅˆèê®öfª]t©<?>ıFû»ß4<_yÇJæ|ù’@WGVû\nÎªà÷VûÑøer…Ì¸ÎÂçmjĞˆ‘#ˆ#ˆB½â¥<jC\"b#!ıXÄŒ%]]´‹.P·\rU”›òQöêÁ«/<OÜÒŞàÍAû@\"hg‘_gİ@Hµ,İlçcL\"p~zèAJ¥‘ÜÙï·³œ“,\rÿ|3×âƒöÁ}?ú&,y4ö›ßÍ¿WyàÇß…%Ï»v¬ş¦å`á|Ù¾ñËRT³`_¾V–€fúŒêwÛ»¶ï$Î¡‘ ÉÙVštñer¡W~9•ÚıÔHÃÍåFúĞìŠÛñìğQæ…7Ş.Y—ìüaÄäMC–©şµ{Œµ{§ü§‚Mkí6h=\nÂyüêÏÃíßù\ZìÙ¶‰¤ÕaåsOÅƒ¶XCš…Ë\Z€qïc3[ßƒË?V¸cTÅZ1”Ÿ½Øæ€ùwß÷_ó°£¢GÅ–?óÜğ¿…‹©Tu€ëŸoW“ Œe†ØĞ6üRÓîÔOef&¢M*êkL#BiÆ)¢z\r¿g©öœÃÆM%nàCNæ³SÄo…ÔeÇf1bÔ¨ì) >(¼vgš£d¨­Y˜¼²c˜š‹©¡šÇíÁè1cˆkùNigı·nÜ·÷›ğüƒÍı¼eø‚•Gñxò®_•Øiû_ÅåÓµĞ!#‡v@çàxØ=ï¬¹pß}÷Q*dà¿FhrØÉAàİæw~çïáÑÿl^ÚøÖíİËç?\n7}ãoà¡_á‡´ºØ˜“ÅÕ·íJµ§d[-Ø\'1vñáq\"Æ‹†“¦M\"®:ìÜzS!¶hü¨}È¶é£ßy©ÇÀ:»†ÂÑCøpu:¬Kûm~ú(h\0Çêšßâuïø\rxÃ[ß]]]^¡²xyÅ/{õ/Œò#°Ğ[ƒYÎÍ²ê\rkÅ»³+Â¨±c‰sHÕ«¨ÎeôOÔÀïm°Ï=ö0üò_¾‹¸íoü®óíëWÃ¼[·~çjxm™ÿõnó-sõLùHu]şõÌéËåÇï‚{î)~ıé 5‚c¿ß¾ã+WPÊÀ»¼¦xL²Dz	ñ¸­6Xá^0ş\r7FŒ“?¦Î>†O<MkØOö¶×–ÃÖµ«`íòWõ\r.¿9plÙRm´Ğ	nsÈÖ£Yßt µµC¸¼†±*–ëŒæ×À°&vBÂ2$ïıè»aöé§è4\"ëS´Åã5Ğ)²gÛ6¸î_¿Ë®4Lyt¶”õHœ©QğíF˜—0ëQgò[ş~S¶,cŒ›°É¤€uÃG‚óŞyŒ˜H_Ø†[Æ‡8k‚/yF-»¶6÷œmÌ»@g§ì8WY®+·=Gé€tÔØqğÆ+?ABs®2ÈÊÈ™Ïà˜À+=ÿêVØ¶yk®^rnÊyéÛRË9Q„±7}´6<›¹*¥X—VÈ4A&³íË6W¦™ı_ûq®Œ=ø :\Z=µç¶ÿ÷UxmÅŠL½ˆQÈ×‰f^I¤òIH\"™Ì–õáù\'züIs`ìä©0uÖ‰j½Ÿ\0ÃÇŠ›EU1PïÙ¾6¬\\\n«_]{váW{Î‘˜^qª0—æ5Æ Ûîè=7	K¿d¸zÛ~XºqæétYì?Ú?¼ã%Ø‘ºâ©\rÜøıö£ßûSJaÒLM±#&ÍR©ñ<¬N3fiç!ˆ—ÉQ†„Ëk\Zl\'™\njš’!è›ôúˆvú¶Bgˆ°EÆu¾+S“ oMµFåc{üËØ0œÜÙjxr®âa)ÊXü›¿ÿ	˜0	­OÑ×l@§ÈúeËáŸşÂúG˜:˜3ÁõAÂ6š`ZS<²­(Êge¤WÄNÖ+!R7à^ç\'±£ÇO€?ğ›Ğ!¿*ÈvfâdD,rçëÅûo…uKñk–Æóß.¸NƒÇö­œÇ²İÌ#•swô¸qpá{®4W#„½9Ïdeä”ÇOf50—âï½îØŠÁ[¥]]1y‘·r&^ÑÜ\\Ç?”SšadF¨¤×¾5£„Šµcf5dûBMe™Tµ#p¯Q[BÖ%[/“šÏ´(•OÂ÷A 2[Ö‡çßü<\ZÂÇ\n#ßçNïùQJ“¦z\neşü|Øüˆ¼a©\nÜÛö‚…«wò©ò€¢ëÙ¿úÕ¯àÜsÏ5Â\0¢—Ê7Uşı6æ#–ò—òÂ½RP¦7‘Ëğ;µ<ü|\\K¹Y&‰Z¨º\rÚaëú\rÄùĞU°£4Ó@%–Ut¼”:xƒ=gâû–ƒŸmƒA»M8ıÒ÷ÀÄãO T9TuúÛ\nÀDÄ~Ğn#†tuÁ[?úa7aI°NX©ğX\nÃØê¦Ú#Û(Õ²=¨d6˜õ7ÈÀ–EZGLğ]ø\'£9ÿå}¤ÜWÒ¶TÙrİ—¸T8mÎñ…ßsGwÙ7¦!¼IàågÃ4Š{2ç3êºÙ³âòÙàÏT«AÎ\'1¼pjv–YÈ‰6y²[ÜªÂÎíÛ½iÊ³5ÕuÈ×Ğ‡7¸½ÃùöµaÏCTà8ëòw÷HĞfœ~é»`ä¸	”ê{(»Ûvpöş™uà¹†À×œ¾®‚6ƒƒ÷ÈQ™ÇÄxî dİe}eBŠ%¤‹˜±D¢«SAQ n#DÃRõO(Su/jw$=4ä¿ÌIô‘o·óÑzËòı3fXàµÁd2qtGá÷ÜÑÀ?åÉÈpN6Ú=¾½ßW„alL\r‰ ±®Íúte¥KI#Ó¦—…E$ô²£ÆŒ6L…Ø²!şxFaOëŠ™F¸±šmé…·\"¿8ğÙæìË~FLêÙ»¾;ººá´7ı¥ú/bc<=.Á™—\\ÖcA›Áû¢·¿R>Zšª!ø¡9ÀÊ\"³V{hİ{â%´¯l×„@ø•x%\Z,ÒA¬!ÍÂå\rÀbïl1¢+şŞ‰Q]GáÁ¢TÁÀÿımUlS3óKùm’¹Òn‹;‡\'}TŞÅV?ÛÙ72†VU‚bÜÔD“\'NH\\uØ²1r3–¦•6)ªêÃI…i|r‘Bê³—›&L=&8—R=‹‘§Àìs.¤TÿGh:de8¾\'?&0‡$=‹É3gÀ‰§bÙ±Aã×ÙÎGÍQÒ³ñìì:aa´©å>®épTö„At6\r¿Œ”ÿ¸*_ÏR>’m‹é\Zè\"ÿãFä/—ó¸ÄŸùÄ¶|yüM¢ÁÀ½½‡Ş–Vn=9ËùdÂz}D”ïà\"¸2‰Ú2\r\r\"¥Á–a˜TŸe?±NŸ}<qÕàà¾}Gçü±²¡öm‰‰AŞ¼¡‰ÎS§]òVJôfœyAáÎ3Ñ‚¾ƒÜœñ!Ç÷©ox3q½ƒ×½õ2è\Zj~YI^1ˆösTQ€P¾¢ñ+P´›,œmBá.·R.Rş+irÊ%dáBÊ}ºìô 54³ãÎø:ïìSáşûï§TÑw6p’`Åf®æ¶ŒLYa4wæØ§+Y‡t©>ÊÕÁ/KQ}Ì‚}ù—ëb%„×l[Ö®ódC“>h+Z©õ&]|ÑÊé±˜ÂİöÈ¾D^2ŸqÚÙ”êhåûí\"7ûdèUı×1\0ïi˜1{&¥ÂˆM×ˆØŸß[p™¼Ñ® …˜8Mş,­k`j:ÏÉ(¨İŞ¸œqZCB¨¦İ‰¶Q»¥ÅĞ!ƒ ³#úM5Œ9æÍ{’Ryî¸İ\0WÅÆfGÃ0M°;Lı¢È¼s²ĞÔÁíÎ©¬¢\"šûÖGA-‹ì‹¤£Æ5û†¤0Ö­XI\\™Ïu@øµ5é};-§2_\'œ}>q½‹i\'ŸI\\ÿ‚Vrl2Ÿ¯8w¦Ÿ‚ïKè}Ì=ÿ<âÂuGÈ+Uš£d¶]åPœ)1T“ã8„u‹šùÑ£8ºº‡Wù¶6ZöÑp6	ÊœìW¢–Øüer§jj@ÿø5FvŒ	jÇoy0p7rGy\\	3‘TM¹R¤ÈÔ1îİ‚Y—İ½zŸ¤-bg£&Ÿó¡¡–„Šo\0Ö\'WYT=û‰õøÕï>ñg÷|d÷s™úJ‘Ì(^r&¾ïìc`½õİvCG‰ŞaŞâéïÌ)Fç.;­Ú¯bšÅ¸É“ƒw˜çwÙtÙv­’PÉjvc½‡ä.7¡+‹ò»hÌ5WtyÍ·Ì/#†dÙ‘ÇÀ²;<şXØ˜Î=ğÂ/P*\\àN]&gpµ¼I¨kq3â½-Ë¶¨ÓfO™Ëg?¤\ZÕ lıÙ·>*°\\3\\‡‚ËuşŞ¯JÈw”‡&¥”ÕĞË®¶Õ—ö}åSx™¼/aÒÌ‰ë]´r™<{6<V\'?Ë0}Óg»úÈº{ÓT$âí\ZfcÆ‰®.\n‚Iu£§°!ˆ†¥êŸP4-3$­ò9‰ÊGÌK²İD[Ax\\˜zÚw¤ Óæı;¸÷l[OœrïÍLÓL-9\0;Ÿ~º\\Yu­õmˆ(«TaøuÈú.„½,Aƒ‰S«GùºÕá÷&ö´®˜i„«c8¬ÈÉRä—şøãúÆÎ1j|õ}ßNÈ1.ÇfjœÃşèC?ibéº7\\“ÌØlÍqp­&÷v¢}e›şJù/ú`S¦ry\')r_\n	N\ZÅ…‡,†u™ğÇÓ§Œ‡ùóçSÊG.poî¸U±MÍÌG,åÏy)í6Ş9®Q†:Ø]l³uOÀíü\rm¦„ôÂÁE\'ª€µêÙ³}qº\nvV˜VÚ¤¢ÌúÈKQ\\¤úìå¦a½|ƒTCGV{oAo#;Ep|ï#—É#¿xeçºæùà·Ëã‰\"d^‰vïÆz.Ê0ˆÎÓà»ğËHù«òõŒ!å£©¶5)išÑL<Ë3¼æÍ›G)¹ÀİÌ÷Û¡Éa[!-åÖ“³œO&²`òƒ\rşLõÓ>\r\"¥}“ê³Ğ\'Ö®îj_ˆ±sk6pûõ‘uõ´”yÕ\ræ6ºú7Äµ|¦;‹DÚ‚Æ/“+dÆur|ççWß€¬•WE‘h¨æ!ãº¶h7™T7q\nË¢ Z¥òQ¸‹n	ÿyUCg\\#ÿÁÌùHµ,İìrõà²Ç¼A0zØÑèos.•¯#ÎÏ	®VÙ9]ÒLÃ–‘)+Œdïå«¿Yœ\ZóåÎÇ¾~YŠêcì‹/×È²fbÅï(_¿ÒİQ^¤=Gr¶•&k›ƒĞ+¿…e×h\0ôfßëù)3Ó„•÷aÄcıy—CİÑ›=š\n6­Í2×„@A©\0¯5Mï2¥Ú†Ê¦Ü‘]ÓqïÜnßÂ÷Ñ=$‚-Ætî†_ÿ¤u.×^úÛ\rpUl65\n°Lì³íUP÷\0ìÎØ¶Ë é’(cÙ!†ã-»º» \"ìß·Ÿ8Ì¬°IªƒƒiD(à#Í¸q ET¯ÑtÏÖPÁJNæ³S$uå§7q`¿ûÍu¯¢¾š£d¨­YØuÂÂ¦æbj¨¦Çq_C¾SÚ]ÿ”ÿd¿m—Éc:•©õ²\"Nº;cÛœ›¹§†oPórU{™\\Õ4?.ŠÁ½Ÿi†­¼OÒ-ÃÔÁùöiÏ>‰±‹Ÿ`q¢CŸXGI\\uğßQî_ˆMz…µÙ6}ô;/ûX_Äá.ˆ üôQdæL•N¡6 ö«uåJa3ûè˜«\n©pYî¢-ªT¾Tõ›o™+#å#YvÉÇÀ$Æ^}*1iÂèàår/pÇ.“3¸Ze\'x±™ë…lpÌ–%?U‡Ñø)3Á^ÖÁ”QîC@¹òlıÙ·>fÁ¾\n.×	ŒS}à>¸ßì¸‹&¶§\rØúõÙV‡{!ãÙKíÜ”›=›RA¤ığ?V•A#öÊV¢CW`zräxÓT$b£Ë›×Ì*ŠkKrŞ¥TEs%¥&]ÚCHÕ?¡,hZÁµ áŸh\r9ãÊGÌKEûè(¸İ~)¦²ìøÛ`ÜÈ.X¼èeJ9w6pe’MÂTÖî0­Ï\"ç¡Él§B¸,.©šöøhÚ7Ù‡’”44›Ä–M[ˆs(WÓ©™Ê6ùuŞ,ª{wºçËûöïÊßß!ç²›±qjç§úÛ¹9ş+q½õ«Vkêµƒê[\rŠ}…Æ5#5GSùÚpÙUô›ñÑRÛ(sÊG^ç$©>w(hkÌ‡rîT!¥\nO‚	óáÊš0b,x6ÿV½‚Kåªb\rG\"æ#–òç¼¤Ü”™İ½zi›µÙNõóqU,å‚e¶.:Qu¨¨5¦½ÏØê*ˆàéêÀp¼”\Z $:¹´Â÷»L¾eY´û\n¶¬uõ©êô÷x\\‡°yİ\Zâú6GnÖİjl—ÇE˜¹œœ*ú=PÜWĞlß…ìífıû>RH¹¯¤m	ÉËäeì_.ï\Z|{® pÜ·‹¸8¢‚øòŸ€­ÉôLÎgÔu³gÅå³ÁŸ©>Vë“n—¡áËu±‰VuàöŸáö[/ëPÔÓ^uCuÜ×¦=ïÜºöïì;»Ümë{/¨5u™¼`\\ó\\Ó ~ëúu}êrùº×ÜËüúºD¼}MÌX\"ÑÕ© ˆHª=…=ŒTİ‹Ú]I	ÿyU™“è#¿Î:­·,Ğ\Z»³k5tğØ¹s\'lÛæ¯}^ë^Í\rpN6Ú=¾}¬;Œ•-£TYumÖ§++]J\Z~²¾…eiq¸=R\Z\ZÇÌüw#AZVÂ±Ù¶š´°E~±l#ómXú\nq½‹mkVÂ¾İÅr{±q—úƒ¼3¸aYñ+{«/†RªEˆâ‡æĞbÚ(Ró1å½õ’ÓH×«•Òy^øÅ¼\ré ”%Ü\'áò‡&LÜ;·Û·ˆOºÜO|fpáùçänP³;cš*6=Ã#À|ÄR~›$Î=V„xçd¡=«ƒ)£Ùº§ÁõÏ¶«UxC,Ñdå{¤EØYaZi“¹:p/8©0uù²àÁÓkø=¼ü…ğËz\Zk?O\\ÿAh:dev|#H¹zIßø°ôâÓæÜË:Ëúj’gï`×	£M-÷É¡Úà©ì	ƒô<l)ÿqU¾C}0Kµ-¦k Cšò¯Àù:;¤Q¾Í£Gn~~»,B“Ã›ø‚[!+¸`I„ôl•1o¦YßÉ2\Z-Ÿ}cÛ8Á…ŸXÛÿB¬¬C¨6¾-11ä.“ûû~›ıîÛµÖ½ÜÚ/×µŠı;·Ãº¥‹(•mAEfÎdßƒ`ëúõ°uÍ*J÷ğÅ@ëÖDÖ§fO@(_Ñø(š›Iuåô5¤Úíkš<1)ÿ‰~k¾K]=S>Ò§»ÙAhÛqó¼Ñİ›2O±$vÜ\\­d\0(6s½À>-5¤tYÀ•…Œ¬ƒQD/i{(7Dü²ÕÇ,Ø—¹®\\	Õ£¡\nA[ÑJ­7éâ‹V¾>e½ä™ÇsÏP÷$^|ğâzM}¿]\ZÊVœBf_|üâz}‚8ƒØ4ˆıyí±—Éíê\0R.*pŸD:ĞÅ•,\Zå|s0î#g\\)ce¯EehµÛ·0õŒ•ú[¶lô°A¹ßæö·àª\0ÅÇ&Hc0•µ;Ì–Ş–n¸ö¤v÷Jçú©ìÓÒF!û¢ÄãiÚ²ZÈ²¸y˜FH=³±,ZÎƒ;`ä&|æÃ±{Õ®{éS™Dcı¢…°mCø×Óú\Zd°’c36NíüÔG”ïÜ¶–Ì{œ$=‹—šëi·íµ#[SJ6<5Š3†ªEh÷]äÛÚxı–šM™“ıJÔ¡ÑÎkÌê§jj@$ª+û|˜\rÜá²:…­[·RÊ@\\*oíf\"©ÚpÙ4ƒJ5›[Q0ë²»Wï“´E¢·’0ùœïe,S°ÍÀúä*‹ª\'w¿Í6±´Ÿ³eg\Z¨Ä²hÇK©ƒ×„œ‰ï;v™<„å/<Ûã—ÌwmZ‹òw-şApDÅåâóaËk={É|Û†ğÔƒ©f Äš›ªv­’PÉjvcÍ¡¡«]M íş‰\Zøg¤¹¢ËûH¹O—í—C²ìÔc`\r »ë–cwtçÜ;ËÅ;üç÷&A„/‡x/dËrÁÒ<’g%—Ï~h¼!QØú³o}T`¹f¸—ëz¡Á)\'{Q\r½ü:a[MpißW*•ñ+ğüƒwÁnL{»6¯‡ù¿şE¯?\ZÕÊeòìÙ`¸a¯l…‘,‹¯’=sÏ¯aÇÆycí;¯»Ió²îŞ4	)–ğæ5³1c‰DWÁ¤štiíEj½IÕ=Øî‚¾È\"iİ¯ÈIT>b^’í&Ú\nÂãÂÔ³¨ÏeàÎµLéG	Ë—/\'Ü»·ú—\0½	Ò\0ül¦²€O?]®¬xÃC°¾\re•*,¿Yß¥‘°—%48\'*Ca±ºb¦®á°\"l‘_ÿƒB‘5À¼[¯ƒÍËÚ{×ó®Íëà™;z?h79ÆåØ,\Z§j8xà\0<~Û-mŞ´÷ï?@’âº7\n\\“ÌkÍqjàö¡}k‡é¯”û¢6e:&oâ$ík›s\ZÅ…Y„êïßYÇi§œÜî®rå ©Y‚ùˆ¥ü9/¥İÆáŠe¨ƒİÅV=ÃÜÎßĞªJĞ75Şd}¢­Zòbò¬Œ_;ªL+m2Zn^Š’èä\"…Ôç/7ùé˜¯ƒ*˜Î¿ûW°l^{¾óŞ¼|<s{ÿ\nÚe\"v|#„ÒÉñƒ÷ƒ7İ\0Ë}F§«ÆÒçŸ‡»®¿	¨rb°s]ó|P„««àñD2¯DrGD´](t-Âù—=aP}Ñ~)ÿqU¾1¤|$ÛÓ5Ğ!Mù`ÔĞôtww†wY„&‡7ñ“´†[OÎr>™È‚5\Zì™\0lğ÷‹rél‘)]¶Ã¤ú¬ÌD^³²½oîòw¿yHYauó |•èWç?	Oßò“Ê.:°Şy#<{ï­Ñ hAßo}ÌÃßQqÇ¿ğÄãğè-7ÀŞÛIÒ\ZölßŞü+xìîı6Q„_ßX«\nÊVrœ!ŠæfRİ@9½TİSí®¤Y)ÿ9Uãç>ÿÁÌùHÕ?y>KÖ#ù¡0 ò†6éñÇF^}õU“PĞ;ûrÎÈùËÎ‘’f\Z¶ŒLYa${/‡XıM nÌ—C¹|~Y®>Ø_®3h¤fÍ¶\"…‘£Gû\rdÑJ­7éâ¶	½Ê¶)‡­ë×Àc7^/Ş+ìŞÜ\\\0ß§‚Ğ²yÃ£?ÿ.lZí>İö„¿ˆH¡{ßVYù²$3}Œ-²›×¯‡»~òcxæŞ;aÏæ8ì\'îø5ÜtÍaÕ²•$m²¾Ş‡}õç]vu\0)y]¬Õ£µYf`=Ö‚Â\0ßTñ.SÂ½V6å>ˆĞ9‰{çvûåÏë¨nó,w,^J_ºt)¥(p»İŸ*VöÀİa¶ôXÚ“:˜2ª«»„í›L ¶´Ñ\"É¾hˆñ\0Ej-E–ıôœUbähÿıçv’È:h˜FÈI*LãàÁ4Ê|˜IÚæ±fÉË:€?qÃ÷uŞ¶fiÂÀ»ÅW-|Jï°Q{é³OõëKã2XÉ±É|v¼Úù©NéÖD&S«–,;ò#¸ïç?W<›\nî>ß¸j%,zzüúÚÃÍß»–¾‚¯UõOt¨îY/ÍQ2f/a×	‹ˆ¡@jø5:6CHºj‘okãE÷WY$û•hóPkH3¨L­—­p«WÑwÜ£»z—Ê©‰~tÕü;`şM‡IÕf5¼éüği\nM\ngƒæÓÿ­\"¸QFi$ªšªƒ‘\"ëçCâÊ\"j2›4ê5gê®E†{¦dG°~ÍÛe$ê@IkÇpù\rcÕŠÑ¾ÌUªªÇ \nRT%$ö“ËœZ3Ì£ü¿ø\'œ\"ª@m¹RçÙÙa<}×]ğò‚ç½²™ZK•à·Y»ºòÙ62şÎÚµÍè½œTÂVçCúDËÌ_èì\Z\n£ÆM ÀŞİ;`ß®æŞ7îú¶çàz8\rwXId¹®n\\\ZŠ0z¸y¨å˜¦œG`¹Ä+¢ë¡gN¶Ì“Ñ9¤ÆŒ§8#Ùºi«şÜø1Ğ¼vdÚgç\r ±¼¢\\_Lh±–ÃÙ»º;<˜úš1¦ÒŠğx³ÉŒFSFhl², ²B©ã9qå|¦œ|¦jp#ìÁ‡l›ÔSãŸ½óxú{D}\\¶5[ÿP{y%÷³¨~NrşíAø`ˆ2¤ÎˆÄ¤3õ`(¥‘a=4cáÕ4÷ÕÁæGä}Hëì}9Ün}´fé>—üÎı‡á‰¥ÛáˆïÖúÚqp8<ùÊvxá…tZï¸C‚qşĞ„!¡\"ˆZØ_¶,;$£Nó¾ÊÁåsD´råÙú³o}TğŠ`_¼x499ªÄø)“‰sğJ\n”ë‰t\"ÛŸÙ4Ã÷•õ\\uq—Óù¯Ù İğ—²2(¶wÃ^ÙŠS$ËÊ]&\'8Ö/\';—0Ho\\·6®İ\0Ô¦ôæ¹	¿D¯.ÌMÎ»”ª`P&Õ¤Ë›ÄZĞ\ZÖ.wß‡2Rínx¾2¤ú\'é¾¡Â#ı¥|Ä¼4»Î–…´-L=Ë–¯=ÍµŒ³*EöYn¸%2s¯I˜9\0;ŸÙt¡F–k8;eß\\„MÇmYß¥Aö¡“)%eÇñÚ&¿ŒaÄ˜1Ä¥`\Záê+²Em“¾İ“l Cq96‹ÆiÚ!pòä¾OÂ–©¨·7æ±zÅlbe5ç£5_©9ÚÌ9>ÿ¡¹oÁôWK³³Dæ¼‰“¤úÜ¡à¼Æ|(çNòQªğ$ÊÕ¿hÇoMS^c3)	ÌG,åÏyI¹-(3»{õÒê`&b³=ÎÇU²“<Sf%à¢UÇmÕ’§JìÜVÍ½|$Œ}ÛAæ•+y)5@Itpj…ßyŞå&/«\'¦Á¯aÿBvªyP(Ü?g2¿çKóædåÄŒlá\Z9Ñ¢r«—,1¸N¨dêƒb#µjòëˆ	Õnç_ö„AsËwá—‘òWåëCªú•´-UÿÌer-”İ98ù¸ã³¿&w\Z¡ÉáMü$ÊôLÎgÔu³=ãòÙàÏT1ML°®ˆáv1\rîºq˜ç¶”ªã\'\'®¸§½ê†êû.©\0\rtÃ€GS—É3ã:oœ>V–oÏ‰æO’ïÎ¥<(\"\\¾o#!ıXÄŒ%M*š›Iuó]Õ#HÕ½‘5)†¤‡„ÿ¼ªÌIô‘_gÖ[–FòCa@5ª[<ËÍzÑäéS\'Á¶mÛ4ï]*çñÎ¶¡ñ‚o«¬±²e05$‚Æº6VÿàD.p².Ë•8\n²„¢y\"\'ÒÚ•¯WÆOšD\\¢\\ÇfÛjÒrÀ†›#}9ëÔ@¯‘FlÜ¥‡>Ş¨†ü~[ƒNº´—Ü½ +ymCyEæX½Òõm²Lõ¯İc,å=¯«º±q´ÖnSOëA¬ŒÂ\0ßTñ.SÒ½XCš…Ë:\'qïÜnß¢=çõÈ‘ÃÄÙÀ­ŠmuÆP~öbw˜Ù Šxçd¡=«ƒ]*ŸíìC¹„¦K¢ŒŞK4ÇƒU{vM× ÆMè&‰¬ƒ—í¤Â4>¹xpÇô\Z~»Ò¶5RM‡¬Ìo„P:9€€#…âéF\'¯Ğ?Ñ²Y_ÍQÒ³ñìì:aa´©å>®Qº”²$xÁŸ4e*|ğ÷?§ù*±e=_E•=aĞî¹•òW5~m)å#å$¦k Cšò¯PEŸO0\nî¿ÿ~ÍëÀ}K¡Éa\'C~\\ƒ[!+ØÉÉ„ôl•1o¦YßÉ2\Z-Ÿ}cÛ8‰EŸX¥œSÏ˜ïüø$©ÇŸr*tuuQÊGº†ä.“û—ÿ~Û ŠŞ.ø-è£ÈÌ™,âã;İñ:_(³åÏ°g)òy6R±ñQáàhÀUáÜL©º³/º>ü_ş\n¦zõ¤Úíkâg,‰”ÿD¿%TpõLùHŸî&Û*óŸû]îLQC:\06»îŒ¥³\rÍÑŠÍ\\-Ù§¥†”.«¸²‘u0\n¹PÄ‘<ƒ~YŠêcì«ùËu<‘.ÏepÙß\rCº‡êt•>v,|à÷ÆOtÏ<‡FšxQoÒÅmóõEÖÇ2\Zßƒ4b¯lÅ)”c¶Ìc`öC¨‚tsóªµ3ì¹“åÍÂ+ŸYE±¾É±ÙZ5‘uÿ¶Şø¡ÏPªz\\ñŸş;Lœ<EóÉ+¶;¸$üm‘3®Ê•Ñì:ë#Ñ6j·oaêÙLÙÃ02#\"Yqh>d©4[I¼	Ò4L‰v‡i€\"ç¡š†k¯=©ƒ]8¨â\\\"•‚}ZÚh!d:™RÂãi¸õ\0oUAû”óÎ¢T{0¤{¼í7?ã&¸Õ¸r2««–óà¹	ßü‡™\Z8İ€”c36NíüÔG;§²¼(ÈV¹’şÂõòıÆê«W¬}igJµ6Õe{éíù8œü†Ë(ÕŒ?Şõ{jƒ7£¡S©aú«ál”9å#¯s’ru.8¯1Ê¹S55 ul¼ÏÃÖ°ğ9ñ–Fa&’ª\r·“fP©fs+\nf]v÷šÿ$h¶GL>ç;CY#ËlKà*—­º²cÓßx^Ûƒ6£sh7¼ùÊB×PsÙÜU7\\qopæLüÎ‹]&gT5Ğ«DU§¿­Î‘¨Ø ¨ÄàäŞ4æš7\'+\'fDë–Ç!Ê	dõêHa×*	•ì­Š¯¿ümmÚŒ!ÃFÀ[ëÔ®öÊœßsşÉhnî–÷‘rŸ.Û/#†dÙrİêt9\n;v˜\'‰ÜçŞ ÅÕŠMÔ†çZ‰ÉÁ>]°4$b_a¸|öÃ@ã\r)Döƒ†k2|i1¼³L]jbLŸ1.¸üJõ†o~ÿû(åàU7XwÛ™Ö¦ÛY¢´r™Üõ¾7ì•­0’eÅ.“»Dó\')^/§	‰ˆØHxóšÙ˜±D¢IEs3©Îè¦Ï:Î÷‡)Õ31~¼ı7ÿ¥|¤ê^fM*BÒCCşã\'1æ%õÁ¬õ–aõSşº¢ÂYŸi2ÇÇƒÍ¥òA—-8úÈ¿A\'ìX™B¼\rF^÷h	êµH¿wÜH]^S3Dñ(¾3ã4ëõ‘í(­\\Tx:¤œÖŒë)¿Ì=QáÛ¤ó6\'w¶\ZÜ´kbO¸\"\\3”ÉŠ¼M*¦[íz?ö{Ÿ€‘cùÍf¤•Frdë!u=ˆ·\"i+í&½yå2Å†ƒûöÁ¶ëaú4¸gçØ´vÍmÚ«Ú®FŠŸ\\u›Id¤(÷i_‚ëÏ¦)ğ¸Ã^<J/:Æ£§nŒ<2vNâ?¸1­x´Q\'©›;ş\\e?HÜXw<\Zø6Ä³ø°\rQ”&ôämíÁÈ5£„ŠõWÁ\"dR.ĞÙq9iÊ$5v,Lšv6&NŸ¡¤ƒ`”\n–#õUT9¨Õ\\1,Êèù¬sÛ\0{ğAí2zÙ)ÂÇ£×}-\\à“+R€ç­æõQ2ÈlY{0ğL…¡1ù>wú¬—æ5ÆÀ;¿±[–\ZWµÕËæû;nÎg-4C>D>ß_>-ñÚöğÂ\ZÚH»¢4ğlo?8­;\n=ö¸\nÜKç}ä»JJyîC¼&ê`¨ÊÉ¯©X\0./Ùq¾ÀŠ`>9	\rO§Wx*²Sç›(§)Ã•©IÀe¾2d#áä†±jONuÀ€…<\'\rÑƒ€O(R–3óúKÎ‡×y»m66D0Š5¼­‡Ôyvö@ ŞŠ¤­´Cò!4kÒ{·o…Í«WÀ¦Õ«`ÓšÕ°w×N­ãÁ¯Û¬ê-3}®?{<OŠÀãû6¸­Zy;ZNJ,ËÍ[,—xEä|5ædË¼õÁö&Áå L¬æ‰\"œï¼ñƒ	£cêçgj­É¦¾fŒ­\Z\"™ÑXÛ®î.˜1k&Lœ6¦Ÿt2L3µÆ¯¶qÔä‘2d‘ï½À}pßn¸şÿş¿*˜+RÀÔÑä·f”ÁeSı*œdıé$É2*aœéyŸ™z0”ÒÈ°š±`†ğ°\Z›Aex~\\BÖÁuÔGkÆõÌæsÈ¦%¶î9O­ —j¹¢4ğl:Úÿzı|=Î“[+ÓVªtE´ˆÜı<œ‚[ÕZSu ‚B›Ç?é§ÕÁÕÁ(¢öšq=•] 4µ¶DY#‰:PÒÚ1\\~Ãè#Ë(#&õÉn;\0XæÔšÁİöoıñg K}¢w`cC£XÃS„Î³³ñV$m¥\"¡ÙŒ’û(¯{u¬]±L·Û¸5}ÂEäŠêp}ÙsàùTwXId¹®n\\f¨6Ä9‡	<\ZÇ}ú×ÀLx\\ë¼¤C{d¤3jŸ7¦: e„³wuÑvZaÖ=ïP¨ˆáDRjpG=ı„YpâgÂ´9§\Z¡ èÄPí++ã´•!‹|ïn<ÌûÕá…\'Ó¢\\q¼&q~kªä~6Õ¯ÂQÖ§N’ÌSy†şH7*\'ñv¹D-l}°š±ğj\Zóaó#ò>¤uöûmn·>Z3gÒgŞ¿¸ı¢4ølóº…z\\Û›ÓØÖ;ï	›¹Z²OK\r‰  u°OW2²éR}”«ƒ_–¢ú˜ûòOjÙVÎ>y–\nÚİ”ê¿è3¦Ÿq.\\ğÁ»~ïspîåï€)³f“¶†„¿”…1÷â-0fÂ!JåíO8m\'œş&ózD¾­³±ï·=‘’s*?¿L99qIÄòÅÜyå{l~1õQ\Z3\ZŞüÎ·Ágşôóğ±?ù\\ò+aÚI§¶ãôKŞA\\yØî	D´³Ğš¸º’N)cêäù.¸/h[49ĞK@Î9FSw•çašÀ¸ ¨1å;X{RÛš¨Í.I°o}´Ñ²È¾h ñ\0Ešµ<û\rç7pĞ1t(wú¹pş{?¿ñ>ç\\ö=~Bz¢Ö°8ó²0aöF¸èÃó`,o96gÍİ	ç½{L:qœó¶Í$ÅáhŒôQd-\Z\r²U®bş\\‘¾_Yw~4GÉ˜}²œ¸áĞ®.8ıìÓáø»ğ™?ûÿàì7_\n£Ôxh>nLÈ<G²cBjåu)ëB;e˜NerªÚš(»ëY©ÀÍ“ÃL$Un\')J5›[‘iJíûÌ’G4Û#&Ÿó¡¡–„Š/öe}r•EÕSŸXÑ/“O˜Ö×î¯5`Ÿ¦‚øÅÿxã‡?\rÇÍ™Cºª±L³hòô·\r´;Æßİ_ù…‹>ò4ŒÏ;oµÓ¦ ıWß¸JÛßéï4p<ºË©çMCÍ›±›3DÏFÊ=§1$æH^9~m”+¹\\?s:¼ıï†ßıâ‡Ë?òQ˜pÜñ¤¸˜9÷âÂ(ÜE[øıÛ\\*ï£)÷\ZeÆXAÙ™ËäÍ ¹ş‰Cn®Vt¢fPÜŒ|-Ù_¶,;Á¢N›m±Ëg?¤\ZÕ lıÙ·>*xEp\n.×E0q²|ÊÀÇÈ‰SáÌ·½ŞüÉß‡Ó.z9Š4ÇÊ\\&g|é¯¿¯ƒ÷Åc&Ò;ís)h£î¼sO…É““5BùãS–½Ln~½Òs©ñ±.½y®E\"V¢WfcÆ\nsÏšÿƒß†+~÷³pêë^GÒcSgŸÚx	d(à3h¨ğÈIT>b^Rël#%Çn·©g3k|™&?€*Tp©ÜTÖî0m9Ùt”l89eß\\„M7Vh~²¾KƒìC\'SJRãø¸™Çwl_ş2ãœ7À›?õ‡pÖ[Şã§›ıÂó÷O‚ÃÛÂ}7ŒƒOœmƒ÷?ú´´?ü¡wÁµÿø¼öÊlXp·»ì[zfl±óMi#çLlş”±iX3ÿê	½şÍo€Oîá­ùÚ]O7FÇÆMÇßÜ/‚9‰¥©%2çMœ¤\\|/0	NòQ\\x‘E¹ú7¹sOÑ?4Ò`àVµávÒ,Ë5» /ò-ãÀ!Òê`…f{$œ»àdÊ¬\\t¢êx¢­ZòÇ8¦Î=.øÀ\'áÂ÷}¤à„Xğígï1AÛº<èœGœ‡ÍÉÄŒN\'¦»ÔK¡ÜÈ–s]û¦bõ¬—×ì×ÃU_øpáÛŞ\n£ÆÓòcCº‡×ü³&{[é§4®ò}¤pß\\€l SÒ´™²[Ä¨‘#4\rîĞäğ&~ÖpëÉYÎgÔuë=cƒ?S}Ä41U‚|r»R}–ü~›0jìhâjŒ=î„àí\")4r™ü¹û&æ‚w(h{ã\\ğ¥Ê²™œ‡¢P¯x)ÚƒˆØHH?JÔ5t¼şM¯‡Ï|şTÀ¾ººûÿ“íF™5©%$üçU±3Gşê¦ó‘jYºÙåê‘¼DŸôßlàÿ|³tØ§¥†DĞXë²>]YÈ4ÛSá|ì›á—¥¨>fÁ¾ør,¡è„v€ÇÀªğ×½÷#0nÊ±¹çq·}M7Ìœù|ğë4bÖÌÿŸ½÷\0°ã6îÆ‡åîØ{§DR,Õ©^¬nKVoî-±å8ùÇ‰ËÎ÷¥9ùÒãÄN×8î²ä&õbuQT£(‰{ç±İ‘WxıøÇ\0`°‹Åî¾·WH½y‹ÁÌ`Ğ;Ûß8á7°mùâh$ŸÇîo“cr}~ê]NK*Ë\nsš#‰_2„=°Ïƒßû³?ûòJÀÎ\r5)f×äÙI¥ŞßN`÷‹BX’y[Şç€ÉÖu¿]¢Ø\"tâWÚ=nZqÚ¬9Ãìñ×ÀD¹ÂW»¶„Ju\r%×D³ºúƒÑdEöïŞKTQŒ™üCoÛ\0>ó¤FXpíkòòøı÷ÏàW]\"Ï¼‘FŞÅï[c&¨ßîuv\0lıX>:ßÛÓ—9lª‚9w¼Ş^IQÖÑa4_é:ïçÀÇ>ûpîU—ß>8\Z\n²ÙÈ²BØI’å@ÀLQU„Ü¾Åaƒ¦Êç‚îEt¥iè:H®µ’ÔKƒjCÔv°¼õk›D˜D6™i—¤ÂÒ\n8ÆL›iøÈ±Å½{›wú{´Ï¼Ö}íáŸ,s.›ÿûÿ¾Şñ~¼\'ªàí\"ìar]ø‡d©²\\êh²rçF¶U€÷°Ï½øøègî€s®¼´r†]\"RÏ¢\r²Ì]>„v‡Ù¼ÀÛÎ`İığ50\r¸3­#t5ÛJmÓ¤*aùtky¡v¼\rª\"w¦ıÚ¶ÜF¡m¹—Éó\0Òş½Yß¿­\0øïı8œvéÕGåkdYÏAfÔÚxO{×º ³¾3¼/Áà=¡ÛqTî³é_KSŸÕ¯¥ü¾î´%!“Tã‰§Ì…şÉ\'ä¯æU\ré?ïş÷gìİ¸š¨ğDì>‚\\,aÆ…$+å_@GúFíw5T;‹©ÛEZ|,íR¹„j¬9Ã4õ„+ôN ãÂœéU¢ëÒ59¾ ”l›ô}“É9Ü“z ¸scÊIgÀ;>ø‡\"€¿÷£¹…gn…•kŞÚø \ZşuÔ¹Á{ı–KáôË·\ZNE¬Y\"uƒ;Ië\'I\'i‡ÅuN<e|ø?WÜrm%`çDÓÁıDù 9»x@…C6â2ËÉæ~~1H²áş%\"Çò)·hî\'­ X·}ã {‘´z	Ñ³WÿÙl©#â–ÓM1©®…×I¬²¡«4İ™hAÛìhlhíå+Èà—|ğ“0{Áù¹xQÓßxù¾Saê˜åğÒïŞc‚öògì-¼÷ÛÀÔÑ+à•‡é›ğÚél€Dc|ÖyN+å1¶†SÀB­gîèi`õ0“Ó¦O†?p3\\~Ó»ÙOÜVÛ×® *ÜYsç·´ å÷Bæ‹!ÁËäÔ].œÀí[´IGÀq¤÷&f3Ñt©#cË™à¯S¹-Æ&º_*õ_&O»¿Åæ5ˆª /WÙç^—|à“pü)g·ÿ!Ï£:í`ñıóaşôE± ­¡ƒ÷¹\'>\r‹~s\"t´²u‘P_û6“ÏW9¸9½Ş*	ÆÉ€}ÃGßSgÍP‚\nr££õ°üe¾(òî“|ZØ‹¸#dC|?km”ß3lc ı\ZJÖ,17ó¥r×TR‹”–^w&UIòõ.jÓÖ®%·\rQÛ\Z©uI¶¿?œ›6¡ÜQV¾ï¹‚8ğKl\']ü.Àï€©sèçBh¿ÃàıÊ}§À\n\nÚ>w\\úÔxXôëùĞÑ–í50	ò;®Ïw\"NĞå´Ô¡²¬°¯]ˆ$~#G€Ëß}ÜzÇGDÀIÜ\nJÅöUKœßãv¡&Åìy<;©Ô\0Ÿ\"Fx¬Rê­ÒB3˜Â–÷9`ºuW#£÷2nÑ\\İFZq&KTlˆôÁÑ;¹³SÈºÚsÀì”\"ı*ÒÅtW]FG5bGÏ¶/—¯{s%å*(CFS¯¸Î¹î=Gı+díıot‰8:Lhƒ1:ã³ò-IG™ò\\/Ñ²NdŸ¿àò‹à}ÿßÇaŞ‚Ó%¯‚ò±ìù\'ˆ*îD‡‚l`¶)-GR<¥Q¹(É¾@*Ê†	Ü¾Ekx	Ğ½ c1›:Ñr¹E×{[\'¥¦N•z’ù`êPDhÌÒX¹”_¾ñÒ¢*(c§Í€snü€7€çş>AlÍ¸püÛQÊ°¶La¿n¢iV©£Ãù	:\Z5ÕUpÖçÀûşè÷á”óÏ!nE`í¢Ç¡ñPüy™ğeà²¨ ôº­g…l„wÅ>ïŒ£èËä‡Û3ŸÃ€ƒ»Öyæ[è,vM« 4ÀÊˆĞ÷ÉL°êÖ­S–tt™°WKtŞØT°åÕF·A0Q”a‘\r;Rn>}J£¶iCb£‡°eaDš/ªşaKÌ‚‰n™æ“i=¥ƒ6”DfÅß¹Ÿ\rg_~±ä)M›0‚\n°öq™£g6¢\rKm­ğÒ÷“Y<ÚUü‰Ç©Ÿ@=q=FNœâ·É³=†1xØIº’ë“–¿/£©ı›×Á[¯>­ÍMI¥zzdñs‘\"©Ûª»Ki£Rí™˜ÿä>óÊåví¸k•ÛÔí,”É”Û¡e¤«òJ\"ù’Ò:\0.8[ë³ÅÙ¶û ¡ô7­,AeR@’ÆX5zÁèÔÇ£Tò™ä\rdy.“4’<«TÑ­-p`ç68°{´µ´@cıAh<X/‹ °®Ù§§\\~¤¥\rfG¥ÔO™8  Ír™œÆXAÑ‡ëöÁƒÿó%ïerÕ„Ò•9âñE›Çó†$ÂQu\nºŞ®DŠ£hÛv®‡B›Ç}‘\\\"Á*Ëj#¢)dÌ)\Z\rIè±Š–#BÀµŸ\röµÂÆ}Í”óã•Íƒà?¾ü_¢›÷}ñ*g¾5­\\³Ê+B-Xí6|€°eUËíb¥<é©„í(äõˆ–)quâfm^v¤l2ñèSŠ’\rËW„;|İt¢E¢¹È3lÆ— ¼-fuµâÍº¦È‡sŒÁ‚T´i—9zfC Ú°±ğŞŸÃ¾]»…YÌ+‡7+\\R‚‰é„iSaâôãaÊœaä¤©(Ğfè1ŒÁÃNÒ•\\ŸÌ°üåx™¨Fí[ËaÃ›¯Ê\0Ş[Ğë$\rvÄšéV4nùh\ZSßÚÅºôšŠn1‡²n¢‘/9ÂÈ$éh í¨ÎÜ“çÁ™_ÃÇŒ–­‹BúÃ¦Œ6AH\Z7¸fT*5‰G©ä3=ÉË¸;Z[aËÊ7a×æM°kë6hg³¤a ‹ Ô\nxßgşŒ;ŸòWvL\\Y‚ú)“ø¸ààY.“ó\'şßû2Ônß*é(ôº–´Ü\nP[x‹¢ÍãyIR>¢æ(FçWÕ­ H+wì¡ÊS;™PK$’l˜òˆ¸\r¦)‘¸\ZÙ`å\\{ñ|d	Ü¿yq?<òÈ#ñÀm¢v‘H	ôF»7p‹VËTlI·&¶.JUa•G¹¤°\rJ#®¯SÒ#;\"ëRª%<Ê\Z=\r[^FÌøHÊÉ”\rS%ÃÄ8€æY±$4­ø*§uµ¼fH5Üø¡[aÜ”É†¯`SÈ´Ë=³!mX`ÉcÃÖ·Ö©œ°«ÚönA³²ÃG€ñÓƒ©³çÁ¤¹\'_Aav’®äúd†å/ÇË$hÀnÀ7öR\0×ë)\rfD2¨ª\ZÆLš#ÆN€ªê\Z1n¢ìKKc´65Àa‘6Ög|²•Åº´ß««dD‹D·Cú±d“®¦‘¤€ÒGÿëãkZ\Z²ı³¶fÏŸg¾ã\">Ú¾Ö…5F!×Ã¦Œ1+Iã}T¥Êx”J>Ó“¼@àn®¯ƒÍ+—Á[K—Âş½ûŸ€*6‘PuÚ†ã\nAÔ©›ÿğÏ`Üq¼u2å ²2q@Ç’HG®Xâ¼ô«ïÃ†K)ïBµ¡Ê˜¾Û\Z\\Û–mªÌ/\"bÊ®§+¶å¨|¤\ZB¨xØI8-ea$¦<\"nƒi\nYÄ)Ë­QÓíäåˆˆÛÏ†,û¿Z.×‘Ü¿ı›«ˆ-šDíVnVå5¡‡_»\r¿L.·²˜*§.ñĞé˜ÄÍºy±ÑmĞ‚D}ÍpëLÖµ…6”ØÔ©\"ŒHóeAÕ?\rãä,1 y\"%RšV|•“º$Ğò!\"xßğáÛ`ÜäI–i	*ÄÚÈeÙˆ¦dÉãÂ–µo‘\Z¶È:¼lŸ	â(Æ­–+%½\0\næ°‘#aÊ¬ÙpÂYçCÍ¨±fcğ°“t%×\'3,9^&AÃ¨Ô®ëÙ\0®×RÁzò	ó`ÊœS`Äx1÷\ZÔXw(T¦³½\rön^[W¯€†zuÙ}4Ëer™ŠøuQFª²Œ¤eª3Œ¯iil	ººº\Z¦Ÿ0#°5ĞÇ¢¾å°)c†N’ÆğLé„È£ÔÇ£Tò™äy÷º%¯Âæ5k`óú\rRâ€Q¾^’Hk†Šàı)Ş³QQpÄŸL9¨Ÿ2q@AŒ§å2¹s…½WÁãw}›rq¨6\"T™#Û\Z\\Û–Ã›jH\"œrNŸ\\oW\"ËqÎr)•Š6¯÷1\nÑqå;«\rËğm#$%7z¬\\#N»\\Qfô`àVKK»ŒdÉEÎò˜R§ÔÂÕ|,kÔÎÀd1åb±Ñm@#ÃTç%aGÊ­Ó§O)³­òq\rË·º_õ[b&\\$ºeÈ‹N®É­Ê¡\r¦K©’+úô³O…®s¦u,a”L¹ÌÑ3‚¢ñöâÇƒ][¶X©°‰½CÓÆa…ƒk¹i·d(..\0Ùgb).^NŸ³Î8&ÌOÛh=æQH®OfXşr¼L‚FÌìÁ[aÓ›/CıŞİÄ)v“û¸“NƒãO=[œi×ÄÛLuÛL<¹U¨ßµ6¼¹êöÔ–y™·¤/9ÂÈ¸:D“nuuœtæipÒ9gCUM\rùKXkR×aSÆ˜„¤qƒëF¥Ø§D¥’Ïô$w“8ĞYşâ°vùJso%13*“f	´\nPV-Î¼¯ıè§`Ê‰øÔ¼`ğzÍÆ9‘\\¾@¶À­ôMíÔŞšhÓx^’Ñ¼SŒÎ­ª[A‘Vµaóz£×¤Àmë¢¾:Å\\¾Àm4$A6X9×^<ŸËw6ÃîC­”óÃ	ÜùCpøà)0‹6*UL½£Ñ.SÄımâ.M¯Ø(‰(glÈ„éë”ôÆ.\'·\\y:ã$‡å+Âˆ>µA4Aë¬J¤è	ÅTó™ª•ã?ÃtåøwùµWÀÜ3Å‚×K(ÓF.sôÌ†0\0öoÛ‹Ÿ|š›…=‹B\"lj‡–}“ÉQ&]#Ó%™ÉSCFŒ„N?¦Í_\0ƒôI¶ÑzÌ£\\ŸÌ°üåx™¸YÁ@VÓş=°}Õë°{“º}P.ìû1fâ˜ÿ«ÅXÙßeµ™\Zë¶™xrëbÛò×aıÒ7 £½]æ±œnµ²ƒëP\n­ëÀ?Í–)R¢¬)§dš>b8œvÁ¹pü¼y0ç˜vGê‚V¿©ë°)cLBÒ¸AßS©t²$¥’Ïôğ¯vóFXûÆ°v…ı¦·TÁT%.<2UŸm´ö}„¶¥qŞUWÃi—_UÃFGƒÊËÄ\0s\"¹|‰#ğ“¿ûS¢ãàí4Í<·‰Â;X££í—YâEDL9îéq›‘vh¡âa;$aà´”Ù@‰) :;6ÃÛĞm”[£¦Û-gÍgÅâ­Pß¬ÖeœÀ½ğûwÂşÍËÌœÛIÍ$YàŠ¼LJiÊ˜ÄÍºy±±mP‚D}IP»Ru)Õˆ\re†-¯¹Õ<*ˆY9™:HÑĞ`b@ó¬XšV|•“º$päâï¶ ğKå¯=ö(l^»N-lšmÌËDYÔ}T4òqË–\'¹cKÓÈW)ïÑÎ<mÌ<ó|Tÿe\'=æQH®OfXşr¼L‚FÜ¬`pVW{+l[!øÆ5%_F×k)	\'œ~¶û;Û\Z±6Scİ6OnãhÜ¿ŞxòQhin–åd[¨E\\&?áÄ¹pÂ)\'ÃÄ‘¯œ¡’€^Qôeà®İ¼	?óìÚ¾Sä-¤˜ÀH…™ªú\Z)ÅíiÑ¨ÑcàÜw]s/¸R1$¨Ÿ2q@Í‰#§1VHÜª¥oš%øn‹qm[Ó~™%#r]oW\"Ë±ıÓl‡$$¢­Ôû$„#1å®\rËàí@è~Ë­QÃ¾¸Fœv¹¢\\(,p B¿v™Şz\rÌ‘aªó’°#åÖéÓ§”ÙVyµ!±ÑCØ²Š0\"Í—Uÿ°%ÆÉE¢[†¼èäš,Ñªœu\n™U$É‰é\'ÿâ3”Q	#Œ¢i\'—9zf#Î´·Â3¿¹OÒª­ª´RÁ‰v‰ŒqX!\'JêËv+eÜÈòÒa©~)”«”Cğ3aÆÈ/ièqBr}2Ãò—ãe4âf#I·~çV¨İ°\nömß\nI_¥ŠÃ`\'_tLs*å\\ÄÚAuÛL<¹õ@(w¶µÁ+ÿ\Z”eíÚq×ª¶‹‰^oœF$ÇŒ³N\'œzš¼.í\"S>‡²ìBê:lÊ‚4nĞÇTªœ,G)ò×½ñ:,{ù5Ø¿Oı 1è|„­ ã6Ğï9û‘‚³çŸïºãNÊQ?e9îD:r\Zc…lÛ4ƒxN#mtû¦7\nªSĞõv[·V³mÚ°yÜ§)×ôÀ­äÜFDSÈ˜\rR4\Z’ ±rD¸öó!-p·u×ÀÏŸX\r\r\ry>yªZ¤İE]&GØÎú‘½\'Ò’Ø¨:D9Ç	‹İ)©T×`Ò¼U’~Ì‘€k4\"¶bÇ(Õ˜0q,QÅaÏöm2uK‘‰r	ô«¤ÛÑŞŞX/üì»°éµçå½ö£ø1—“/».ûÈÿg\\y=L}\"®Ê÷£&2hÏ=r=üá•o¼]´µŠ8Y|Ÿ&ô&N™,_åºá÷?\n×|ä#pâÙçØ İÏ±eõ*¸û¿¾O?øxbĞ.|\rE²¢ı»w©L˜r|èS±ùvviíOBH–\rnĞ!I&\n•_·@ÀH°]9ÑØÒI”­]ƒàÔSO‘´ÜOX`­\rš*Ÿ+’é^$•ÑuÜV‘£T¨6XÛnêEŞêµM\"ÌÁ€D6™¡…ŒàÒ47CS#FÙûEaß;Ş7¹uÏ¹Üî:€/¤\0—¥L˜9Ïñóoü\0Ì;ç0aúL»éÇ”æõJĞÖÁûú[Äºs(!YîOzØq\\ôîkà–Oş\\~û{`ŞYçÀ°‘GÏ/uíŞ¼üáá±{ï‡ÆCÄíxÖFã¡ƒDõ,‚”*xü\"7\\¡İa@”[GÈF°n¾ß*)»úTtv›³áD˜+\"hYóô]°Zü!tà6k™ˆø·n¥à®ÑÑedâ^z“‰›uób£Û >}U‡nƒÎûu4j›6$6z[VF¤ù² ê¶Ä,–˜Ö<‘)	¤•=3•YEºr‘œ}ÑÙpÖeï2­ÃT–‰i+—9zf÷ûÛĞŞÖ.ëIºL.³ÈerŞ.ÅA’ãk`Š¥úelPš\\fzfì¸¬…O–†aydV&A#nV0’t½mĞ>£¯fáÃm-M‡ ­©¸\nZó¸SÏ‘OK$Ù¥Ô€ô\\uâÉ­¨Ì„{¶l€†ıø^²šİv<{3q¢œƒQÕ+hÎô1ŞyòÈ®^Qôä¥ò]›¶ÀkÏ½\0»vØ7¢íˆd|DdQ¾[Æ•:ö#uöSÿñ=¢¨Ÿ2‰¥å2¹ãG¼_±ıVº2G<Ş,§½nßD8ªNA\\ÿJd9ÎåiJ%„¢ÍÛ}\":®é—É®\rËpÚAŠF*	=V®§]®(7~·Z]ùIÂ¡a°ù@,\\¸0kàVKJ»ŠdÉ‡XXSê”	tüAE m’Ë-êQ*i–ÁÄÍÚ¼$ìHÙ:eâÑ§TJD9­\rË·º_·ƒh‘h.ò¢“k²D«r8zL—R%\'Z¤æ‰rÉP	#Œ²i+—9zjƒ—¤ûíïP1¬_Ï¢€`êÀ”âY¹ê›®IqeyY3ªOŠ/“æù^SçŸ)ó²Öè„!Ë#C°2	\Zq³‚‘¤ëmƒ€ñca¸\\œ¦«Az®:ñäÖTæBï¤¨yÂa1^Q5Ò¬“z\"pãïÙ?sÿ#°sû.¥ÆÀÛák’æyD†•q;fÍÄì;zEî—ı}X¿Üı\0‹ê·Ò3uSy[¢mvû¦7n	¦Óø˜[¹cGUÚÉ„|\\é±aÊ#â6˜¦D)ÛµÏçAc[¼´1|ÅegÓ2vüô§?U—Ê\'ÌV;CQ»î9í!Æ`p\'htò¦h©#à–ÓM1©®À[g™ĞUškÄœpœ‘À9Ú)FŒ)ö²äÁ=ê5@·6ä$:£¸ƒÇßc.ÙVàëÊ…OÂ¢Ÿı/ì^»Œ¸Tà~+ü™ß>wã{2h÷xP*{ÖûK€ÃÇÄ¯=	në£k›ˆ\\È¾s\r™/`Xƒ6œıVÔ]écÕÑyfÎP¿¡N£2óŠ<½‰ŒL<Xª$RGÆ–3ÁŸä‚al¡û¥Ò„À[ªÇŠSì=îú½:pG¦Ğ×v~TJ©B¸Ÿ¥ƒ-M2€¿şàÏàà.ÿ÷—+xû¢½µ–<³îùÆà­Uo7´µgğgßşÀ ÀõE\\-ìÇEv’ñqMÚ\'Ğœ0¬™€oß dà>vŠÌh¸Ã™Ô\"¥e´NU’€|½‹Ú´u…k	ÃmCÔ¶Fj]’íïç¦M(_H>]ÎCİOE–ƒ¶6VG´¯*ÏÖÓDØF­Üy•‰úÚ]°ä‘_‹\0şshkŒÿ\\ao/´·ˆ€ıìp÷×¿¯½˜ïgp}ëN#äÁqYÂ¾\"€[!!èuMğ@j€ÏĞpUJ½UZ°}H©°å}s’l]÷ÛÕÈ?¯yQ×~¢q¸­Æ\'i¸‡ñÀ­ÛHËd‰²¯¥!ûĞKËb£êåÊ\nÌ~Ø3•Uƒãb.£?±£ço	WI[Cå`¯|¢ÜV )LëÕÎ$—pûÕS}¨ß³^øÅ÷aõ³TøÛo½±îıî=°äÅ×¡½­ƒ¸.zÈıB®§|¿·j²¨ˆ=¬ÿ9ƒ$Y/É¾@_Ìiİ¡fX°`¤Õ¥r4KîE$àÚ`IIô`ÀU/ª\rQÛÁ:òÖ¯maúç¶´#V.Íz|9uº{e¤H¤:bì2¹;xI÷·{ËÁwmX+ø¦%/@çQô\nY¥cËšõpÏ×Ï<ò,46fÿ‚]êÚ‰Ëõç@ùÔ³Ü2<¸ TÁ]Û™²ê7¥ùİ\'ùÖûÊPÄ´5´¦ŸqW±o.˜À=ñö´n¶•Ñà¨Ël]Hğ6(A¶ËçÙFØ­K¤r…¶åŞßÎVƒ‚w!1—+:Kóáàı\n³ÍêJ?¨påiÚ=MKÃ\"ÀUø1Š][¶Á?¾ûÍãĞØ°pÄ‰¸Ì®ŸÒ/ô¦º½DƒñSÕÃL‰ğìƒ²øÒ Ì\'ìË„0©ÒÇ•#Ğ7ê·«‘u?X:é7öCX½vÌš5KÒ&pû¡\ZkÎ0ËúZš¿ãÒ’ØØ³sªKgUR(´M“æ­„ôÓ&Sû?¦aM«ë¢\'zïBÿØB7!©­’¯Û£d|ä`Æ£Û“À\'ĞU\0ÿl[¾˜¸Ç\Z÷†­KÃÆWÃ¦Åêoß–Á¢ÿ)Ëú(ìr/<ğÓûaçZâ¦¯‘ûõ´o†ìûDuû‰*UC†¥¡Æ«¬nSá¸,o)óšdN¸•±ÿ4·\'|¦¥½‹¨d455Å÷ÄÙgÙ~Ï4#Ğ½H‰~ñËä>ıRGD•³¶#©–ğ:Yt“³6]èYÕì¯!¦?¨\"¯á8gLÅ¼´×Àú\nÀ×-^‹~ş]ØıÖ±ñ\nYgÛ\0ØøÊ Xô¿m°ø‡`Ã\r°åyû·âW\r°ğkÍ°ê‰Ğ$û±€Æƒ‡àÙƒ¦vÄÉD¶§ÏˆB¡fE6J…[stm‘Ùm„Ì‡ëÎ¶Öz\r¬—ÑÚÜG¥óĞ<}ãÁR%q¤ÛòÃ–Ëw™<b—É‰PıÂÏ\n`Ú{¯±–üq„Ó\\™‰ÖeónC¹ˆİ>ş‚×ªV|İrâ}hø•·Ê\0İv¨S¬^á}ƒÊ¿U*0HºàïYŞ¯ı¨6‹³ñ£Mà9°ú?wÁ[«Ö+f–eğ»´µ“,¬ªœR/Š_ßŞ~ç\\ Aí\\¶ú*l$Y	k¾^øá÷ÕÎ`İTŞÒ‘şÄwsg\r\\xá”ãgÜ\'œN·E66*Âhª$ùzµië\n×F¤?:˜L­\" ç5¤M(wŸ.ç•| x\0wØ´8ıIÕî˜\0ş‹ï‰3ğ£+€cĞ~ı§ĞvPìƒÁ šÁ0xHV\rƒ†VKz`õ`$d‰¥-ô¶,l„Õâìûhìç|~Æ64++g€>K„ù<8;úf…¨v†êNİ×dhx\\ÅrzzWfÍûæ$½ò4h–À4È„ÇW4E.İíô3ç(’{flò:ÄFŸÅ¦GÍü°íWiQ5È‡îj`2q¢˜Ó	-á¦zÚÉ}íFVb½$àòøå&7ßã}(ÀW.R\\=Ä–ıç8û:hwµvË³j°‡×@õ¨¡P3z(Átä¨\ZQU\"ˆ2Xœ‚ìì{İóî¥¶şˆÚ-Ûà‘{~?ÿÎO`İê\r’Ç½Éì\'\"QÚSºşèûad_»É¢èş !Á±K’åğ’ì÷ZÚÓw}ó\08óûDöŒ{¶z?,ŞèŞë Hs\röñ3åòGÆ·*›VÉ’ù`êP„éŸyÎNJ1Ô?y\"åŠCjsS^sÀ»“f·¡{€|Ó²×`Ñ/ xk?}|õ#­6h‹3êj ‡ŒÃ&Œ„aGÁP‘;jF\rƒjĞ‹³oÔX%şğÌ[LÆÎÅMP¿³^6ß°l<vÏ½ğğ/„İ;í—übğ¹^?K[›Aq†zBAQ/–àÁ¥e!d?&\nì?×è>Éğ°fkGğ 0h?;²qO úA8gÜñ\'ıˆÇğäë]r F¢Ô‘ÊVÎ­Ë¶Á…¶åŞßÎÓ²<;¥«ZR=¤Øß:>¸_=a½du¥÷ÉE9¿ÎÑù:ğ{«Ÿ{´_}JuçšÁĞTÛ&Ïœñò8Q×ŒVA{Ä”Ñ0rÚ.ÒaDàgßU#Ån¼l.Îºå}oQ\'hóKş“ôğÓ¤«/_ıÏaáïƒ]‘€íì;¤ÿ¹ƒ1d\".c+Ö†œ«„±îÙ¥ø’šfÌKaIæ½ğÍI²uİoW£ˆyÍ†,ïpïØÛ\0gu6å\"{ÌÔ¹2Õw<ÍfY¯ù!-‰ªC”ãµ ˜3ãH 6iŞ*I?ÍÅ´ƒbê×´sg[-¸óDèzƒõkç*Ef‚ºı»6¾¯?ş[XüÛŸ@íºå\"¨÷í»àûÖ©E—½ñy•8£ÆÀ=bÊ(;s<Œ™1FMÃÆã·Ú\"°ËûŞòŒ/—„Uğ>´µµÏŸ4ß»u¼øÈãğÓo|^}îehllvÖaÒš4û	ƒE†ûá›Á@°_@Õ% }¼²\"8®”–Ò/“2®#EøŒYŞáÆ¯Œ3†r‘À=|ìd¢2@÷\"%úEÏ^#é²¡Ú`m»©%Vob´=‰l2Cõ¸4kğGy,š§Nîàõ××ÀBÈ:ıÀªEOÃó÷ü¬~şQØ¿eIzû×6Ë±0hª$/ƒc€>qŒŸ=ÆÍÃÆ\rƒêC \ZƒvM•ğøÚ@ù”¹XâòŒ[MĞ¾2éU4<kÅÙõo¿û#xì×ÁúÕñÎ|H+ìÖÑàx&÷ õ,Ú º¶‰È…ì6Jïµ­#d#Xw¯9mõÍö[\ZIX¼d©ùÜ)Â	ÜÎ7ËÄ[i‚¤JX>\"ˆ¡ÔÛræ` ¡5²ÕgÚ¯mË­€S…¶•r¹.\0ïBb¬¸<KKƒS—¤£u%Õí¶1Úâ\"º?`÷¦u°üÙGa¡âkz1ˆĞ÷¤EàÅ\0,ƒ·8‹–§Õ¢KàäYõ ¤ñR:¾¦Î²E!“’vÄ¦qoú‡Š@ó¡CğÖ’×á‘»~\n¿ùş=°xá+òìÚ,4$ïrÖµ&)=Q„!‘€dÅ$«„í\'ƒõµTyáélh|‚ÍJW	3.l$Y)}\\³A÷Û­Eµ³§ëFd¹¿­ßáN<ã$PS5g˜f¬£ù(|ÌØq,É¶®Âä“+Í¨íÌ }ßdrN?öëÚ†ñÅ”ÇnøÌò>¦Uë´1UûèFgG[,ˆ×®_Ñãµá¨â0ë¡>Òİ\r-Ğ¼¿šttutAw—ÊÜ¯e!Jin:[³=S\nönÛ¯?ó,<v÷Ïà¾Ş\r‹Ÿêö×“´|˜“§“ùÁ\\6†€È;JµŸ¯î<Pí,Ë~†ÂqË	‰EÊ¼&ÙÆ­Èg#SåAdk~”ò7\"vÆëvh,S¢_ôìÕÉ‹Zˆ¥ˆ¿œn’=óW©Ü«lèªMÇ‰6bN\'4‚›ê)\'	«L¬W\nÜ{OñËän¿ú¢i(jú:ˆ¯~ñxé7?†—îı¬Yø˜äõ»¶‘VGWîîê†N¨[»	ht´n‡Îv¼e\0ïVkÍ,†\"{®Ğ|¨vm\\«^~	ùõ¯áç_û<õÛaí²U\"X×‘–_ë²5¦94¥ï~BdCŠ=í~igğYP„RáÖÌGÛE„É\"×F¡^1$Áö+§´ÑĞš~¬µc\0Œ?r\nÄwFüŞ¿¼J¦:ğéÖ½¡<&¢÷2JiÊ˜ÄÍºy±1’‰úš!`‚Šn¬-´¡¬caË+Bn5\nbwfò)ÅÄ\\rÑ<‘)	M+¾ÊI]8rÍç_÷ş›`òÌ˜#¦J¡¨éLæè¬yéEXıÚY%:Ëœ¡‘[¸qHe%_İ>Ğ:V·ÿÀIï`Ä˜ñ0¸º\ZÆNVŸª1n¢È‘4‡n×è)Ç% ü/•¿yÏ!À¯¡\rª©‚ªáê‰rù7\nïi×ÈĞ`0A»³¥:D\0ïÀ´¹M¦]­âl¼½tb@?ãO\ngÜ(òÙ`´45@Kƒ½j ×‚Ã½ÛwÈ´¹±š\Zaïî=RG­¥Ä×%\'¢‘khÆ§¡ôÃ°\rOí_¤o\"S$Š&0Á³Ñ\0õMˆ—é5!éH)Ç¾+ŠØ ‚€ùs¯¼Î|÷ûDF@&Dsˆ1±\\&ç*øû6­Çïú–Ì™êDEnÕ¸¶-‡·Ë–q§87Jd9ü@ß±0íáûÔ‹h&Ù0å®\rËˆŞßÖı–[£¦ıÌÂi—+*Ëw6ÃîCá`·g^ğNø§ú\'âˆ6ˆEáôäÙïŞ)&{™hºbóÀ­5õñÅŠ½6®¤óZ.·Zòb£ô…-!pd˜ê¼$ìH¹uúô)e¶U^m0Õ:\Z¶¬\"ŒXóeA½ãVõÌ‰D·yÑÉ5Y¢õb×N!³Š$9Ñ\"õéölàu	qXáàZÛ´E2€ì3±ùnÚŸ`Ç¤w`G0íwg\\~-ŒŸ9OÒÚ)Ÿú÷fy[ŞÛZ\rÕ\"xWã+_Ãk jH•|İ;Ö-sg[\'t‰¿N¬;[ÚT^ín<rğ³.	\'œßa_…{ñßÂ¡ºzÉÒëÓØjñ‰Ör¢¹Lay˜Ñ4ãSŠPúŠ!·FG–5éñ9AÚ¼\0#<«ü×\"ê›ÆgUâ\"AÆm8ípì;z.D¸W‹Àım[7UÄÛâ´WÀi—Ù(8ªNA×Ûù˜+Ò¶+jÃæõ>F!:®IÛÖ¥äÜ†«‰2fƒ†$ÈF¬®ıò°xkcêÃiKwVÁŸúSøøÇ?NœÈ¥rÄpy¹\\5şX}\r,7¨`hGÁkÄmã”\"|NQ¤£ø€æë A¸\rîÈöt{U¬~éYh:àş¬ã„ùÃÅğ\nîî–gÍ˜;·A{c«¼DŞ†\r-ĞŞ$µ8ÃîlgÙmtÏ»S”gÙ€¯›ĞZ˜8G&+_|^mš<wJ<Ñ|YÇBeGßÂì\'”4¶Sg¹_¾=à(×şøi3‰ê„ÚŸ,Êzˆ\Z‚´cH’åğ’ì”;§!dy¢|ßó«`\Z±À­ßåN„î_i6XRBr­Q/ª\rQÛÁ:òÖ¯maúç™ÄĞBFpih‡EİB;²uÏ¹ÜÄšØ“^.ÜôOàÙïòggÉöÒÙÄËÆw‹à‹÷¯;Åt\'^onÁZÿ‰@—ÆÅŸŞ\"pãY6zy‰ƒ¾°1zæ1Á~ìaé³OÀöõêı0>>ÎX±Eåèp~‚‹#‡©Ôµ—Ûä@ù¤vU\rFTÏÁ­9yÆ‚\\hL¢Øv†l„§»Ä¾2„íçCÖ/¦­}k=\\qÅ”SˆîiüÜ¶R¯M“ª„¯ëÂ`ëB‚·A	ø\"ÙFØ­K¤r…¶…G–¥Íœw¡2V\\î¶¤H‡q \r«ºÒûæÊ{ªIÇòŸƒ(}üë¢_ßtæ=ıäN}ÂPyÖŒa@ÆKàò^6ySğ–÷´ñ9ŞÓr¼4.Ï¸eĞó+şN¸¸JÚD¨ ½ÁYKñuUŞ;æx=”FáÔ¯I‘âAsĞ7{Øãæm;K?¸f6z°ıu»·%à©(t`S\\³Ø¼rˆº“ê(}\\9}£~»\ZªÅÔ,¦5w\r…ã?r±À=V=­¬ËäşKKbcÏÎUª×+%…BÛ4iŞJHß7™œÃıßß{ÿZ±\rã‹É¯[’ÌK¾vn’mcé3 ?Úy×dg{;¼ş»ûaßVõC§_‡U(ïQË€,Îºí½l¬eÀÆ?ıd¹ø;Ò%şğ2¹ø›~Ş;]”ik…—ø\rlß l» yEÌ\Zàk&iı$ép;IvÂH/òÄĞZ*Âƒ{Ú~)ho9\\^İT8d#.³œĞ˜X¤Ìk’\raÜŠJr(…@³µ¿44fy¢¼s Ì˜¿}ÜUCG$AM÷\"eÕé‘ÖŠÉ#JUÎÚ¤ZÂëddYĞM4İ™hAÛ¬?À9êqq¯ Úfîà%]&×è«>„PÔô÷(\"kƒ÷²g‡¥O=(µÎùÈH7xcpÆ‡ÏäeÓ™6>Œ†2Ô÷ä3†Ã‰—wÁ5+á™Ÿİ\rû÷ì¡AQ“ÅkvZá]·ÈF~‰fõxL&-Uµ–#õˆl_(†ÎP³¢¥Â­ÙŒÒš•İFÈ|¸n·$ëæû­~‚ºÃé¿ĞØpÅ—QÎ\"¸ê>wú,êgƒ¥JâH·å‡-gv&å z a»ƒ„~Z>!ğ–ºƒÅÜºJ­\"\r~»f\"M7¢§Úx4g/¬¾}…}Û·Á¿º¶­zN¿m\0Ÿ\\-ƒ±Ìòr8»—2`ã%raIüÍ|Ç0=c9<óÓÃÒ…¡½½´\Z‰¶Kƒ¯G®ã,ÓïºNRæuÚÚŠ3Lağ\0\"Xu,C=}`³r-öäIL²\Z×\"†+äÁº‹¨œ¡±%Û‹Ì{\"å,¡]¯)“ª$ùzµië\n×†Û†¨mÔ*r^CÚ„rGñér^ï«N:\n”&Û¨u‚;¯\n‚p‚ó5Ÿ_âÇNŞxêûpdÔ¯Äô^¨!ôğŒZpñ×¥hüÃ€=fV;Œ>åUØ¸î»\"`?-ÍÍÒ9Èpëg´ÔQóšÖ.D¿dğ:Å?åcåUZV!fåW1\0\0¿”IDATËò·#Ÿı‚g\0R÷5\Zç±J©·J‹´º3ÀZğÍIº}W#n£€&&LëØiØ³¯ŞùF¹†7p«OŸfAzÏôAnÅÆì\n_íÚ6*-ª¹ãĞ]\rt\'Úˆ=K¸ŠÏIzÒq4ë —Ç/7¹ùŞhïÛ	Ñ%‚şİX_;w>‡«~\0Æ?\nƒÆ-†Á£WÃàQ«`HaìSĞ6æ‡P[w7Ôî\\\rt†íØ’tt²(b/’\'š×cÖ£€¤(ëè8úf?Aè@1YR‚gjTöGŒ³¿¹Ü³à£n²ÈµBÈFpì’d9¼$û=Œ,¦á7ÊwíÚ•=p™æy%L÷Vš^p6XR¢år‹(ndl”š:UêEHæƒ©C|çEÚ+—:;œ”!é­³ØÑì‡Ù%R^sÀ»Ó;Í-	ôÄÖŒÇ¿İqd´Â*8<èõ7àUh;ùÜª)ìŸ¤ÓN¥ç\'è8H¤ÀW.‡Ÿ¥®Í¸\\”Ok×ğñ=¸Ëí–D ıqQ©“Ïam„ÚÖlííçG–Óğå]t!å\\xwõĞ0fªz-L¯M“ª$¥õNÛ´u!amñD:²µÁ­K¤r…¶¹çLi¤ï@˜]I»-áÅëöî#ªT×ÔÈ4½onı: Ê¹¿W—{Š}DĞLàè°\\R\0VPõÄØ‘T.ÉœS¿Cºë.†¼CíAÈD\\fWú*`6\nh\Zê÷ìôVÚ/II™mö-°)fï’lC÷ÛÕHòÌC–Óê›ÀYÎ¤œoàFŒuŞçö!û\0Ëa{v®ÒRwAhÛrËÒ¼u‘~š#iÅÔ¯i+æÎlIÃ¸®FG[úWv\nvn‡‘ƒ™ nQ¸“MGıÕ^Â&^Ê5!¤+L%Ù³Uºv}mGp;’¢l’~¼ ¢D¨·Eøf0ĞìPuYho\r;\rÁq¥Ô\"ooK¿LnEé¾‘ˆ@İEøLY¾˜vPèœw~3nÄ¤9ìººîEx¥	±’k­ø‘<¢ÔQå¬íHê›@_õ9`lê&³¦‡2êqiÖà(æˆ³Äªu/í5°şˆ2§¿w²¦²\'ÅÚâf*$­&0ÆÖ`ÎÏÔîìâÔã¶FA˜ê³µQÂÁ¿gûæZwÇ·´ª³Û(½gY|,¥î^+zj\ZÛÒ/“#6m­õŞßF$nß}n=zÍš–86¥öØ–3™vÙ`Ú¯mË­€æKB·!år]^0SñÅjZ\"ÁÅ=½°yİnM¡œÛÆ·;Ê¹LîÎ¼…u{¡Ë”x]‰—ÉMÆmWx-åí¶ÅÂ1Í2I5:mÑd’2G ™ik%(&YX%T9¥^°yôFMTqÈ»>ƒê¹Œ%L¢°‘d%4®9»á…ß/T;{ó ğ@súk`ø`ÚÎ;óî±\"p®.éà:7ÈØq2¦mjÓ&Ÿ­²¸mˆÚÎÒ÷M&ç¤ù1w¿®mXºnñ¨\Z2ÄécZµNSµ+H÷qî›i~š\"¶ğ8÷,VÀ´E$\\\'K»ò´=/°-ÊÇÊ3ZKù<ØßRíûd#G%ªg‘v`“e`â*–“f>6¬È7\'é•§iÒş\0\Z2¼¿}¨}\\|ñÅ”‹#1p#&óËåâ=Ó;\0=”N^lÜ³Ø¼ğ—Ó;³Ã‰ÔYtÕ¦ãD1§\ZÁMåq’ú}û‰*£&z¾\'äŞ{Š_&wûÕÓşvC4:A—	-_Í™/ïØ’tt²ÔOxfC¶‰æk]Ú¦\n’ÚÅH§¬È†³µªt¤º2Ñ“öwoÛ\Z>ÚX7$‹\\!„l”Ôí…‚ª¥Ô]ê3~1-élÜò>·î=­4½àl°TIåŒ	ş:•[ÌQ$È¦î—İ)Æ‘g¡9;œ”bÎÙoL÷´÷ÔÃi±×À²!Ç0ô:zÂEBÈ™\\ â×Q8~ÎèLu™Â~İ¤:y¥NõœŸ¨C\"A\'¹”ãH[›Aq†a\r^i\n‰2Øî×t .Ê?‰ñqµ6BC×lííç~x¥µ#ı÷Î}põÕWS.ÔÀ­×_xòõ.jÓä%QêHùË±ı‡„[—Hå6\nmK_®Sà5¤MhˆÒõ·Ñ“Gä\Zş\Z,ÛĞó­8öaƒ^ÑLÖİß&_áŞÄB“°,¬hV˜ÓIü<àõóc[J\rY2—åïlĞ~‚pÄØqDõBû)	5<¶PpWUÀ>Ä–÷ÍI²uİoW£\0\'Î‰º÷·o,]Yú7Şç®\Z¢îs[dz9,bcv\nE¬öÌN‰lë\ZJ®‰\nfu1ô£é±-àÎœf5èø=€a#Ùüjç¶!r0ÓËíÍ‹±“§ÁœçË¿s¯{ù;éüK`ö™çÁ¤ãgÁàjõ>{oÃ‰[DG—ˆöo¹eBã÷r.\"…Q[qĞä¥ê!’\'Úé3&)Ê::Œæ0û	¥Z‹É!	3\"è\n°oqFOtï Ôşà¸RZ:Ä>¤”\nŠ\Zğ€™bç4Íé—Éu“?å9kÖ,âÄÜyŸ;y¥©„äZË9’.j$­m7õ\"oõÚ&fç£\'‘MfÚÙ/—¦n*¬«.Öí¯SÙ1läH¢tÛİÁ;\Z_› ‚ñ‚wŞ\0WÿÁçáÜ›>³ÏAZü>SŒÎ3N?OòÎ¸æ6¸âcŸ†où0L›s®ê¥ Y3Q$ûwxd9_aÉŠÏ°£ÉÊ9:œŸÜ0†ì’j­@Ÿ+)XdE |8øØÁí\nßß.\r®PóKï™­#d#Xw?|\r‘åşvSÛ@¸ôÒø/‚q¤ny¹œh½fùQµù{¬v¶œ9(pGaÚ¯mËmÚVÊåº\0¼‹‘±âr·%\\ÌuKıe§0’Æ×mc´Å=áÔåbâŒà’~¼û=0ñ„“ˆ›\r#&L†S®¸^–Ç3ñ<P‡UyG_è²)â³•şµ4ıËv\náµ”B¶$d’jtÚ¢I‘b{ƒë.$*À)ãl;Kİ86Êobf´·ª–ÑO°Y¹\ZÍæ•CØH²Rú¸rúFíw5T;‹©;²ŞßŞw¨-x‘áŒ›rÍ×É@Çi!*Z¥z½Râ.ø‚P²mÒ÷M&çäñc¿®m_LivsT›UÕ5©}³m,ı`¦\'—ºÏ½á½pæ»o‡!#Æ·4 ­Î¹.¸åC0bL±—.y°â¾™ä§zí$ˆãHs S§HİàN„@b»t¸$;a¤\nõ64Exp±öU_ÇO›)Ó>5<Ôş¸Ìr²¹_Ê¼&ÙÆ­¨$‡JEåS²Şß~sù[pÅWPÎÔÀ÷¹‡õ¼6Dˆ½úÏfK·œŞ˜T×Âë$VÙĞUšmÄœ(4øË*Ğ|èL‹Â˜‰!í»ƒ—v™¼§=FŒ—~ğS0¦àŞˆñSà‚Û¦ÎÿnÙĞA[	m€tçŒ—wlIZMVŒ­‘Ø&äç™hVÇ¤ÓFJªO‘zD¶/9ƒØˆÊª‡#ªt´&\náNFi]óLhBæ‹Øo„l/“Pw©ØÓ˜şVPs×P;vLğş6\"5p#ğ>·^p6Xª$RGÆ–3Á_§r[,ŒM\"t¿TšxKõ¸”b¼®xnï›5U,ÜjÃ\r.báisçÃy7}Ñ¥ôN¹â†`ğ.ç2¹;³<¸q¥¤º\\})}’’Ûe%Ş*	:ÜA’2G Kik3(Î0TÁˆ`yÖ± ‰È‰ºÚíD…¬90piûª,ˆ÷ÛÚ(bD‚N\ZRÜ©$Ôgx0í`Ë ÔûÛˆÌÛ|½ÓëUOÉûrf¸mˆÚÖH­K²ııáÜ´	åâÓå<¥›ĞÇ¥ECÿBX°\rºîØ¹”ŠãÆÃ)WŞĞ£A[ã”Ë¯/ûÌ;ÉïÂ®Ÿüq~[‚|…ëÛ3s·~‡–:T–NjW¸½%€×)şác|E²—åïl>û.zò·¸CL\"­qqË	šgûRaËûæ$İº«Q´§¿OŞÙ]´qd¹¿È¸;í±M½C[±1;…ÂW»¶„J‹ªÁq±@—ÑQØÑó·„«øœ<ÍñÀá†b/•Æ¯§‘}Ş†øå&7locèˆ‘òL»7q²Şc&M¥\\yğ-‡(].´|œ\0Æ÷«“Jt²(Ïõ‘<ÑN¼-fÑqô-Ì~Â@IC»ûdI1º\"|ßÚ·#1¬Ç7ípû“E®Ò ÌBc—$Ë1à%ÙÈQEIØÓíÁâ^z=õş6\"SàÆßçÆŸù´Á’Z‰vJ‹ë½^äÚ¶ÉÛÊâÉ|0u(ÂôÏÓ´#V.Í\ZüácQ÷â(¶¡\'.•«:ƒÇ»“ÒŸŞÀiW¼[œi¡\\ïáÔË®-ÿu±Øšqáø·£”aàƒ‹Ã5çh²rç\'è8H¤ÀW.‡Ÿ¥®Í¸\\”OkWOcÏÖD•ˆ@ûC]+½×ÖB6ÂÃšÍ	ƒ…¥w {ÛˆJF–÷·52nÄœó®%J£´ŞéaÕûµC°¶ø\"ÙÚàÖ%R¹BÛr/×åéeú„Ù•´Û^¼·ı¨‰Ñ£|·ŞŞiEvà}í1ÓÒ»\'P3r4Ì>ó\\Ê)OÉ‡<ú®.÷”r^‹¯/UOŒIå’Ì9õ;dÊeò¼CíAÈD\\f>¸Ùvm@ê-«rÚ—”Ú3e>aÆ…0©ÒÇ•#Ğ7ê·«‘ĞÎ¾ÖØšşDy}ó\0¸é¦›)FæÀí¾–9,bcÏÎUZê!m[nYš·.ÒOs$íÿ˜ú5mÅZ×…¿a~]‚rqışDƒÁtæêkƒ]ğ‘ƒ™P{{sÏ»”¨¾Áq§ŸC† \\6¸“$?µW€\\ğ`ì ×„®0•dÏ¶Ëµ›ÔvnGR”Mê_é…B½íißÙÏ_µíëø)ÅÜ†)	Ôğà¸Rj‘··)óšdN¸•äP\næö´Ïd}\rlİÖ½™îo#2î±Óİ×Â¢g¯ñ#yD©#¢ÊYÛ‘Ô7¾êsÀØÔMfMı\n—ú‚¿#g™ğBô|Nµ¯£~h¤ªºŠ(…şúµ4<ÛÆ³Ş¾ÆŒS²ÄÆÉØ\n‰ëÊò¹Š£.i51¶+àèåCØQœ6RŠPë.RVdÃk£gQÄÕ®àYnOG\nBİŞZ±uç±´ª³Û™×íÖ‘„`İıôkiY^Ãßß~kİÆL÷·™7âx|H-qlJí±-grï4’¡ME44áî8R.×åEĞ”i‰wßÂÖ¼æÆ&™‰Ñãõ‡FÜz£­è	§ÎƒI³æÕ·˜zÒéÒSòÁê»3oaİ^è2%^Wâer“)~’øzdU:õógs8ëZ“IÊ.¥Á ˜da•På”zÁ:4¡„=ñòöÖğ}Õ`ós-ö„I6’¬„Æ5OÍIğû…jg¡ûøØ—áşöõûÛcÆdû€T®À=e®~-,_ÇõzÕÓkòÎÊÏ·\rQÛ™Ğç5¤ù1wŸ.ç¥érDÅMîg{\nNsÎwO\0¿h6qö|Êõ-U±“¦P.\'è1_KóÓÌnìq çÒµS?Ñ\"á¬YÚ•E§T`[”•g8´–òypşv„ìg©{Ä˜ùe°´›,‹«XNšùraÍûæ$½ò4nÿÆlO“hì‚÷¼ç=”KGî3nşkaz(õAnÅÆìJZáá‘4;%^g;]u 	8ÑFÌé„–pSyœDªšÊvO9ÙÄéÓ‰Â:¢ıpó=íèI;e\ZQıc§GTyˆ.t¹Ğòqß¯N*ÑÉJ~/<lmÖº¤õÆm‹CSŠàe9zúl,„P +Â÷­}>Åcß¦ÕbëÖj²({;C6‚c—$Ë1à%ÙïìiÈvkóÕ7VÃí·ßN¹tä\nÜˆ§_\"bt2Ëüu*·˜wS/B2´M\"œe©G¬Î\'¥Xø,Öm{ö°wÛ6•)SfÏó?Ã»“ÒŸÆ¨ñôiÖ~‚±S\'*#\"~…ãßR†7…ıºIuòJê9?Q‡D‚N*|Ê9ü,mm–»3®Ñ(ƒm|¢|æiöm…>G qQ®—ˆ«µ\Zºğ¸fkGğ 0h¿4ìËp_Ëò™Sbaæ\Zùí+Á³?ü[Ië‚Ú‚LÄÆI#ÃTç%aGJ7#YŸRf[åÕ†ÄFaË*Âˆ4_T¯Î`KÌ@$ºeÈãŠ´É­ÊéË}JG+)9Ñ\"õéj9ÂÊ5måRW¤ï¼ı&˜4c†ÊHÂ(›¾r™£g6„P·c+,}öIhinbbÕVŞ†¾À‚wİè\\*—ıã“­aX‚•IĞˆ›Œ(«iÿxõ¡_P.ÆÏÑ† µ]G,¥Jµgb^ü“÷·1¯lád`j×{\rLò\rI:êŒ;Ú&„â­å†V2+š2²>C3>¥¥¯rktTkõZAÚ¼\0#<«×‡FÔ7ÏªÄE‚ŒÛpÚ!àØtDÜFTÏ0Ôº:í‚‹aÁ5ï…ªØ›\nzÌÆ“Ó8ïZµûõ%­áöMoœf:Ö¨ÀÇ\\‘¶î¨\r›?ÃG†ñÓfÁˆ±“`ø˜±0|ìT¨ª®†ªšj¡;×•šİİĞİÖm­­°ë\ZØ¾æuh8°WÊœf¹µ	k)\Z\rI(yhN]ûå/“/İşİõ†Á¼SÏƒ¯ıëÄIGîÀøÅ_İ(2ND’–)RbÈ¬¶N‰ÍKÂ”YØ‰úÈs…>ËW„;|İá zæD¢¹È3lÆ×&¶˜ÕE!µy2“\\¤š,®{ÆùgÁ©],2ŠÇ£húÊeÙİÙŞ\nËzölÛ*XªŞ†¾Ày7¾×y[ö/:áÃòÈ¬L‚FÜ¬`øtŸşÑ×ˆòÃ.-0»[Íæõ ­×ä“g@×~¤\'€h©ªt±¥nu1!’chäK°eÊÅu4¬í¸SKİò:U„ÜŠ,kšm¿Ì\ZÔ`ÙˆÄÑõù¦æyD†ÉezíiØˆ2\"4X>&â²ˆP×gÙ—ßş8şôWÔí‰m“OËer\Zçu/>KzXÒˆX;ÌÆ$Lgˆ#>æJ^]]›Ÿ#\'L…á£ÇAÍğ‘\" ×=ûD%Ñ¾àÔ«Å©OÑ-‡ê`åóAí–õ2¯à”uØrºrkÔt¶\\lL\"ùr±|g3ì>ÔJ¹düzÑ>xôÑGaÁ‚¤O‹ÇQRà~ñg_‚\r¯ıNÒª8M¯Ø(w#@fµuJlÊi;\"ëRª%<Ê\Z=\rÌW‹#ºIS&ÃÈ1£aÔ¸±F°w×nhmi…í[¶‹ZE;t¢&ab@ó¬XšV|•3“•Smr>OR—L£:55UğÎ÷Ü\nc&M\"E„!Œ¢\n&sôÌ†@4%ËŸ~v¬_+²Š!ÛÅÕ{Guà	’Ú†aGS©k\03Š\nÜ(CÂª“®¦I†PúHàa|MKCj¢uû)‘z†©²nÛ€LµÂêÛ¶(=Ü¨ö*y‘ =í¸)rİN˜2ÁÈö×î‡öövØµ_qRˆšç&—){¦•T·‚cŸÓAL¨Û‹}»á?ƒ±ÇÍ&ñçT€ 2±öøxr9üWû}Ø¸b©¤£æe–xÑš­²ô0ƒ\Z„18Ošq\"Œ?EèÉP=l„8sD\Z‘vR[xKÑö+§^ÓnnÃ¥÷m^k·CsÃAhi<‡ìƒ¶6Ñ\\®‡ÍW–åÖT¢ë´µò1‰\rxzm}ê÷Éñ×À~õäjhhÈ÷EÌ’7^.F_.§Ò25Ibô¤q9¦¨#™v¤t|ºN\ZµM½Q£GÁ‚w\\Óçã›%ÊÌéİš]ëß‚\r+VÀê7—C½\':Æ¨\0¦¦,Ñz¡j‡YEºrÍ)×Õ|„µ%3T3*­şï¹YmzŸdŒ0t™£g6¢\rk€ŞÀÎõëœ6ôŞÀ-\rËRÛĞöc)mTŠuªG*v™\\R*8KZA™Šò¿Ñ¡T±•L3(QÑ’O¶uˆ6ÆTbø”\"”¾bÈ­Ñ‘¥EM`ä¨0kŞL˜¿à4?Åı’Ÿ\\TFá¨İë–¯†-¶@cƒzË\"ê›<F”ï–q¥ıHAG$2#ÅşgähõZŞ‡ –\"À7¼Oí$­˜:åĞe6.hü˜œ¾à¿úÛÈàÍÍ’§f¡8Yì3\'Î8Iş>ø°1ãa¨8{\\5(ÒD_¼n3ï–&´?¸æ|6hÖÇ–†°gãjØ¾v™ä{E•Uc[J?4§nßÊGËä¦Í…»ï¾›8ÙPRàFü\\_.§Ò˜S:q³6/	;Rº\\²>¥R\"Êi}üc:ÇÍšç_s-LG÷B¥Pÿ!D*x¦fóR¬â#Ö¾ú2¼òÌóĞp°A:AtrM–hl™.¥JN´H}º¦Œ€•kZ—“$¼ëöÕ½m^„!Œ²î±#sôÌ†@´a)âÅ{ï‚Æú:Iëvôú[àîjo…ç~ú¿”‹Ã.+\\=—Éš6)£‘ĞŠTy÷·‰F¾ä;\"ã×!9Ñ~Ì3%\\®!u‰!·FçŒ9Î½ä<8éì3${…\\›2ª‰°~éJXòâk±×$µ¯Râ\"AÆı×èÈÑ#aìÄI0qúL5nœ8»)ß·®Rƒªj` ø«®…dA›ªµËyH\"­ËuÊ¡Êl\\ˆñ³\\&çƒOüÇ¿ıÏP¿¤55C`âñ3Å¾dŒš8\r†™CFŒ„*Ñ/Õ¶„³Dm	Ãçrâó–¢uíN½6h§ûvÂºWŸÚ­¬mI(}œSèpÇ†¿Lä¹Lşíon½õVâdCÉ{^._ü¸ h¹‰š 1zÂÈ2%6/	;R:¯›‚[«K©¶Â±Á/á\\ğÎwÂiW\\C­¤iÊc*x¦fOàFº½å0,}î9xõù—Ì„bjÊ1ZñUÎL¾H§?\rFO˜£Å‚9v9N´s¼¬T5d˜XÃƒ` ´Ã ø9<^?iGhã¢\r‹É¨¶´§B’™a)¢­ñ,úõ=ĞÙQüÛò`ÎYçÃìóìïÔÊş9cF0,ÁÊ$hÄÍ\nF”up×6xıw÷Q.»¬„_÷ÀımÔEF©“®¦‘¤€ÒGÿëŒâË”Ó”\"¬í¸².Ú€:’)ÿ„Õ·mQzGàÜ‹Ïs®À_´ÀD‘¸%!ş¿ùÜ‹°äå7ˆ‡å(U‰&9j$?÷$˜\"ˆGOš#D¾zØP±.E=Òıƒ<+ßÒ†§ó†‡$Ò}¸»;;Å>­ª‡‡ƒ°¸Ã:J·Fı\r°ôé ¥YŸñ*ıŞÜ=y™Qrà®Û¹üò§$-\rˆš 1zÂÈ2%6¯ºú4]3ù<›	“\'ÁõŸøC¯Ieı‡I$©à™9JÜºÜ®ëáá{~	ímírbM9ALš4¦Ï“›.Æ\'ŠÀ<j†…Áñ…{U^ÁÚS4ñÁiÉ˜Úˆæ\rÒ ´¥=å’ôÈËÊ¶.{\rÖ¾ºˆr}üÜé©WİH9êŸ3fÃòÈ¬L‚FÜ¬`DY;V¼o-y‰rq(¿cˆe©ËkÛ±5äY3f0§Æ_×¬·Õ\'ÛHG.“c½X?©Ê2’–©Î0¾¦q£ë•´O‡hnÿ4M)Bé+†f1®}ï0nªı|²F97u»÷À¿}Ø9û6j3çœ\03NœSN˜ÃFÒÂ–\\/öoÀ@–ç2ZW†GéÑ¸ã6’t4îÀèlmeOı\ZölÛ r¸ZÜñåÃú2ÑÓ—É%nÄ¯ÿñƒĞT·G\r©Ø¨	£ Lj«Ú¸ÉKÂ”YØ‰ú”2Û*/‚ö¤IpëŸÜ	UC‡I’é?L\"yLÏÔ¸vî€më·Â¤ãgÀ˜‰Tp¤ƒ3&¬œLtYÆç<ÉÖ´ÌDhÉpï\"Ú°˜Œ¼Ğ–ö”CHÒ#3,®;\0ÿéw¡µ©øÏ­fş÷%ş#ÊQÿœ1#–G†`e4âf#ÊZıü£°{ÊÕÂ.)1†XVd‘ÃíjÚ¤ŒF‚îò.“ãV…D³öDêê­åDs™\nÂò0£iÆ§¡ô·ã\'Œƒ›>ú^qæçÿIÖr7şuŠƒì‡îş%´µµÁœ“O…Y§ãÅ~bğ`1ˆrm ¾J¥mÍ£¿JàFı[cù“¿‚ëWˆºÜñåÃú2ñÆö¦LŸ9-õ29¢¬À½ôñÃ›ß%ÇTM=YdU7yIØ‘2;Qy®“‰“\'Ã-ŸÆ ­Şÿ“…ô&‘<¦‚gjÏ¸UJ’…©æaB©“grGiâ>‚Ó’;àŞE´a1y¡-í)‡¤GfX\\w\0ì^³–/|š}ƒË>ô)ó##²Î˜Ë#C°2	\Zq³‚e=Ïÿ$Ş>°KJ„¢Ş¼L@¹%-|ÉeM¹¸†µ×qêb©[^§J{‚Ú7Š mï£ÆQDà6AQ§>¥’Ïô$¯¸ÀÀà½sıJÊÅ‡:6ôe S¬÷§×ªg‚B(ç29ByR‰˜{~ô7ºK…\Z93uD$ÍÏ¨Ñ£á–?ù<T\r£3í\nz“æœDTßaçÚeDõ-öoY—í?9pÒn&yÿ“aOâ+,YîZB8š¬œ£Ãù	:qÔTWÃÕï»Ií\n*èmœqõû`üÿ—‹Úˆ=\rÙ¾M¾ëà\0¸å–[(—eîã¦À”¹é?q¨÷j‡`GJï ø\"¶Üõÿ”½<^A¯\0XcòŒìŸäë	l]Õ?÷¶UoB=‚ĞeK€¯sQH€/K²³m¤\0¬ Ú”i¹yT.Éœ®ÿò®‚cúşçX+xûâì>UÕ=à¸µ®…¨0–­Ù\nŸüä\')—enÄÜó®µ;Z¨z\'-èrpæEÁØãfR®‚ŞÄ¸i9¿Ï]0:ÛÛ`Ók)×7À§ÉëåïûáN\"8Í¡×NTÌƒ±ƒ\\§¤+L%Ù³írí&µ=f‡²Iı›5g&Ìœ\"å*¨ o€ŸT=å×~†ÍÑÒÑ\r­ø–PømòÁƒeşímÊÜ3Ï¸D¾f]øÙ¡Êéu¯w\0&e{†š!CàÜënSù\nz£&¸ÇèàY7¾CİWX÷êóD¥ !’%8	¯×‡åsG]ÒîZBp:¹M~~2âõpps^SúÎ©‚\nŠÄ´“Ï…¡ÃGQ®xl9m¿´³®n½µ¼8Vvà®:f~)åÒ`ƒ»ŞYäÙiÌ?ë¬Ê}í>Ä˜é}¥Ïºß|ü·”ë]l~ıEh<˜şà‰ãç”Faİ^è2%öèdâer›±ºy‘Ü.+ñV‰HĞá@;\':¯r‰¼‚~…yç]N”X=¥//vL’?áùùÏr¥¡ìÀ8õŠ÷e×´^Ğ&ï¬ü¼P#|†üÀJowÔÕî‚Í½|ÉHÛ´|	åüp‚s÷4×Ï¼2hOÃõù¥k·~FK*Ë\n\'µ+‹NÌ:q.QTĞ?€gİUÕş×ËÁÎƒí©\\Aì9<\\ş|gŸğô¡À=nú\\7m6åŠ¿L>aÊd>¾ï/Õ¾İqÍ§şÌ¿ğjÊõ6¼¹j×.§\\Ï¢éÀXµ¨üWá¢AĞ¹_Ì„–Á–ñıê¤=} —«¸^\"¢eıp\0ÌF$¬MãiÌ˜?Oe*¨ aÒÌâ(wÊv¶½ag#Üyç”+…nÄ©W¼¨tè³½Èõº7yÍ`˜~BñäÇ€]0óÌ3àš?ü¿2€÷Æ“šÜ5V¼ğ$l_¾˜r=ƒƒ»¶Â’Ç~›ï“¯Ú¿å6Ç¿¥Ôöë&ÕÉ+uªçüD\"N&øPZôGL™}r¡—Éñ¡´úæôıC[w\r¼±t%Ü~ûíÄ)…n|H­j>¤f½^ãj‡PêH©røyÑ\núPüÊ;>ç\\ÿá^à\Zk_}Aø—şYÁb±ùõE°äñûr~§=Ÿ»ºN|ŒŞß.ø2yH2‡õİsUPA99q\ZQÅ ëCi»Ã‡?üa3Fır\\9(,pË‡ÔÎÈúZ:ÌN‰ö6Õüiô8ÒŸW}â3pé?\rã¦G’ŞD‰¦ºğêo›–½Fœt¸“MsBû·Üò²Úï%\"…2ƒÅm•‘ƒVÆ¡™1IQ6IêÌ¾}u°‚\n’0dä8¢ŠAÖ‡Ò–¬ÜŸú”ú}rQXàFœ}ıÇ‰Ê÷B/z¾ø9¦œx\ZQôW3Î»õCpÕÿæSÜAœF‚k=›6BÓÁ”Ë	ràòÛš- ªŠÜµ„pêgÎwŒ&ÁmS­2¢˜+BYJ;Ğ6¼ìw·9\n\rÜÉ_R³^ï ²í(*8\ZQU\r0ç¼áš?úK8ç†Èé)ô„íƒµ›dÊ_ÍÊ†t}ëöB—-,¯Ù5ãÖ^Kyû€m±pL³LR•u]ÁÑ€a#ŠyM1ë—Ò¶ïo‡Ï}®ü‡Ò4\n\rÜˆÓ®T©éõ[ŞBÎ¿Ó© ÿ`À€n˜0c:\\ö±?†K?ô§0mî©$)C†¸[›óı\n\Z÷qîîi®Ÿyex¤q/©[˜:Eê\\ŞfêIíÊÓö\n*¡« ­¹êwï†Æ½»‰{l¡îpg¦/¥áCi/¼ô:ÜqÇÄ)…n|HmÄ¸øoíºğd½³0;bTö!G?ğ2úéWß\0WÿÑ_À©—İƒs>Ì–ä£§ÿ¶Aks#QÅ \Z Ë„–ëƒñıê¤¢ÖRŒ	ÙŒU»X=TAR»YÁ1Œnœ[\Z\ZaßÖÍ°åÍ—aÉC?…\'ş÷_à¾¯ü_xğ«ÿûÎ?Àó?û\Zì^¿”Jô4Öí%ªtì¨Ïvo»È‡Ò4ÊúYÏ$¬{õqxşî/IÚ]Ü*£yZdò†ï*`rÛ~\Z¦œˆgl\"gŒrZ@Òú“HôÍîªò³’T Ú°¸.×CxÊ!$‘ñ,AùÁ h:Pk^xêkw(A\0ÑÑĞ˜{ÎpÂÙçPNÀ(&”`ãœdó©|UÈ<\rO€êĞ)’Ú®®*–¢†ü\rmÌ`NÕ¥ıŞû3R¦+U„’!”>\\‡ñ5]¯¤}:Ds;ø§iJJ_1p{ão…©\'Ìy’«ŸµŒ£ò³ÔO™ÄÇÇÒr™œOJ¢$\r{¯¦»ët´†–Æ¨ßµê÷ì„½›×Bsã!¥ Ú­Z.¼”uAs3æŸgİğaI#Wû‰ÓcÓnOÛ$íô±4üî;ÿ¨Ò€¯€-\\_O¹0îúİfxşù…°`Áâ”	Üí-Mğó¿û\0´ÆKvzøB¦*±yÃGB”Óúâï]ï}?Ì»?W\'rZÑ¡$­ÿ0‰äIß´¨¸%©@´aq]®‡ğ”CH2\"ãYBÔå:Äëöå¯Â†×“¿†\r3®¼&Ïeú0Š	%Xİ>#GÂÓ?üO!ó4ÜÛ¡/hÌjÅRF#Á·rIÌ+[8ö˜Úµƒá\nK¾!IG…?M£‚«C´–Íud*ËÃŒ¦ŸR„ÒWÜsÑÙpö—È¼ÉUàŠ£¿îîîÂWÛ¡«³Zš[D0;(÷u]ĞPW‡ëï*¯“/»NÒ¦=¼X!ê§Lâã‚ci¹LÎ\'%Ñ†Kwwıh†æƒõp¨vÜ»êvm†ú}{©YVßi¥Ú|rà0ıxxÇ?-iäj?ql™v\'·ÓÀéc~4íÛ/şæ{”+\rkjÃ¶÷·ñKi«·6ÂŠ+ˆSz$p#^ôÇğú#?›ZªJ×¨+6y‘òKàÌ/‚‹ßûQA¡’ærZ@Òú“HôM‹z)pãC‡]İUâÈµÚ[» ££\Zì–íh<Ôí‚>\"Î<·È±5,pá»ßÃFé*HÁè±TX×îÈ=³!mX\\—ë!<å’ŒÈx–ärGÄ±nÇvX÷ÊS±KYş\0çŞøq;u<åŒbB	V·O£«»ıÑ—„ÌÓpl_Äv+\Z·šÍ»Š´òo¡Ë”°.í÷Ñ³m{YNl”ºÕÅ„LH¡‘/9Â–)×Ñ°¶ã:N],uËëÔhÃÌÙ3àšÜJ9)ªÀö,\n©ë°)cLBÒ¸ñiRÉgzø×Ñ9\0š‚Cûjeà:°sìŞ±MlYŒÀi„ªú*íâ—äjà}şP5t8ÉéOÓQ#ºŸ2q@µ#çÃl´77Ê~>¸Wæ]P¿{+ìß¹ÚÚZ©…ª}\nŠ´6]!Ty7h#´DB·|şß4)ıDÓ¦İ¶®DÚéc~ìZó\Z¬xşaÊåG§XçÏ¯;˜éiò\'–5Ã_şÕáãÏóÆU:z,pã‘èÿüAÙéQUáÈ:®İ¤ZÂ±9z4|ôïşUeL“9- iı‡I$Oú¦Eî.y$ŞM‡š ©~/Ôï~÷vØ³c§ÊjÁsÇFZfÉñµŒ§D’Î˜4m2\\ùŞ÷h¦“0Bê#¨uLæè™\rhÃâº\\á)‡dDÆ³„D—cìÖÃ°î¥\'¡vã*Îá‚ÛşFMA9£œT‡åû4Ú[»aáO¿&d†{`ú\"$µMÃ¦RCcµQáJû}ø29rQ_\nM2„ÒGÿëãkZ\ZRıÓíêèTY·mÀ\r¦Zaõm[ª««à÷¿ğÇ”#\"j$\\H]‡McB’ÆX+Ò6ò(õñDŠWV7µÁÁ}{`÷¦\r°yíJhj`%¢*Ï*{¶Q2K°}£¾²’³NšW|ìOI‡ş4ÍH}™ØºØX;r>1Äß¿i5<ıÓÿ‘´„S—ëéJd9*¯ìp=	!T¼´À}.¼ñC0ùÄ3%WûœSÄ´;Ş~F;}Ì•Oÿ\nv®_I¹üØ°¯6îk¦\\2ğç;ï{z444§8ôXàF<w÷—ÄÙÓã’æ;™ªÄæ\r	1¥ZŸ6˜~èsÿÆ?ÓÈ”@Ó’Ö˜Dò¤o¦ÄÀİXß›W­‚Ú-aë†MÂi¥;\ZçÅT;®¤‰0º*#S-—º’Ğ©èÚÙ—^óÎ:[r$(a„)£J ˜ÌÑ3Ñ†Åu¹ÂS!ÉˆŒg	‰.çawu\r€í+ß„o,”¿ÅåùT«¦œ€±‘T‡åû4Ú·ÃÂŸ›réP})’Ú¦®&–ÒF¥èíj€Š]&—”\nÎ’Îx™\\Êd*·2QÑ¤«òI:Dc*1|JJ_1ä–d×Üv-Ì<™ı7éØàæBû9‡ÔuØ”1&!iÜˆõ$m#Râuu\r„ƒêa÷æÍ°zÉ+ĞØĞˆ!·pšåŠœ,×sÊØ¾áÌ¹B]pÍtÉeâOêë”ƒú)“ø¸àXZ.“ó‰üÎÖÃğà×ÿNœX°µãÔ¥=PA‰,g€º\ZN…¢ÍLí7î™óÏ€×XJ´¯8Z¦İnû-íô1:Û[`á=_\'TÙ,óáùõ¡µ#ı£OKwVÁåW]ÿôOÿDœâPøSåçäú KÑ©\\úÜ“Dõ-şÑ÷á•§„-\"h+XGâ;%g}xÀÅÉºÊ6Êß\\ô*lo\'Ø\r3Ï8®úÄpöu†‘ãzö‡fÚZ:ˆJ‡Ş!ø¾$i¿¢wµQ1ß;Hs ¤+L9»tf:±]	:IíJ²ÅŠÅoÕ·xô\'÷Àşıßá¾ï^}æI´£\ruYPH WŸx6¾–ñ7İËíg~ü_nĞ Ş7ËÉæ~)Î@6vmzK´\'Û;Ï=‰½W–´ñƒ+Y‚¶~ì_øqŠEî‘ã§À‰^K9„šE=Õz`R-q÷«ß\\\nÍöQ®o°şõ%ĞxH]Rã~g+UMÖA„`;v)ÕÔâgŸÁ»ôË<G-tÊO«^ôŞßƒw|àO`âñê´ÁCŠ}»»³„EÉ‚Î+Ä9¶|gpuI+ˆ±5Û„|îai`õxL:m¤ky×=âw+qúµ[¶ˆv¨÷ˆùAu©ÙËˆxá{aÓ’\rŞm*h×íÛCÜ	\r\rOhäÂÃªêÀ`¹iÉs’îK¬<\0›ö&*ŒûÀG?úÑB_ãèÑÀÀ³n{9Îu”RğÂo~ATï£C1.y~QØ‹…£òKEÜ©ÕÂ.¦Ki´êk\"x/[Ø÷‹ ¯0|ôPXpİ-påïAŒI±ß)om¬#*+ì¬%y·ãöŒv/RZ¸ú:“æÉHn—•x«D$èpx×5±–,|U}„7_x‘(±Ë¹Á¡f}\ršHâ:~á_Â’‡î&N±8´{<øßçÚ|‡”Š¤OF¨ß—¾-‡Jü”pØøê“ĞÚTúıæ¬gÛGÁ«o¬î‘Kä\Z=¸ãgİip\'^»Ş7l\\ûlÍñãEâõ§’Osğuçˆ>USÚR¶fíBZ¿b5<õ³ŸÁÛ‰óöÃàj›ô/åAWg¶KåI¡	l‚ï.®‚yÜBƒ&ë»—Àh©CeYá¤v…Û[xâßîµ°òå¾Y¯«^yÕœm+äïlh†dY°jñKğĞ×ÿîTo“”‹ÖfXõÌ}ğØ÷¾ííé¿Xo¿åweBXJßñ¬ûÇI¹Ş¾¶uUy~˜õl{Ç¡!pùå—Ã¬Y³ˆS<z<p#Î½áD%#z™<´Äøå/¡n{1Î[W®„å¯Ù{vÜq}Näø’m„ª—&+R1ËeªĞP_Ï?ğ ¼şäïàĞ¾Ò¾Ô%Ó®µ«¡««g~\ZóhÃáÆü_Mó¿(].´|œQÆ÷«“JÔK(Ïõ-káÔÉÛb6GßB•µõ¼ôÌKPWºd[<êjkáÍ—ìoµg½Œ]*¬}>\n!ûu{káÿù7xùŞÿ-9€cÀ^ÿÒãâ,ûoaù¢§‰«\\u¼IÙG¶ç6ÙÖŞ>¶ü™û{åŞ6m?ÿêJøó?ÿsâôzô©rgïú7xë•Ç»èZMª%<Ê:;	Ä„É“àö?ı<TñŸû”Jú“HSÁ3ş”ñ©òº];àÁıÚñ]N*¬m ãjçÅÅËù<EH]\"0å:ŠO)Bê¨6H»R`Û®x$—À˜qã`ÚìäÆ§VÑXPt[ã!ù~êİ;aç†u’‡öç_øN˜qúA£ƒ²rªr†¸M	IFd<KHt9;IWr}2Ãò—ãe|\Zë_[[–¿D¹d˜v‰ImË°£©TÔO}ãVÑÚïûË×ÒtêØ¡\r¦Zaõm[¤`ÿ°ª_Õ5ÕpóGn‡qS&IßõAû;‡ÔuØ”1&!iÜàš ‚ö^xäç¿Vë• ê´†T»œæpZÀEm0¡í“’\'ÙwêŠ\0mŒŸ4E~¬eÊœù0qÎ©dÎÖ©q¸n/ìÙ´\nölY;Ö¯}µAIVAõ8Õ9•³ı €YNâÓä¡¬xÂFDÈûû$\rGM:ç]·Àq§]@ãX¼¯	4wÂxíşïŸ(ïÊdÖ\'É·šÀ‹/úoÑ…^Üjá§_ü€~]«I¥DL/1äVlHìÌ•¦1xßôÉ?‚áã\'(†è?L\"yLÏ8Q†À]·k»Úm­íÊI©°$%C9¯¡IAñ$)aå2Cå1Cº’Ğ©è–µAZ2¤L•Sºz‘`N×5lÄ>J=¼%m\r(x·R’mA»RlRÄ¼s.™gœƒªˆÁ…<ÏhIFd<KHt9;IWr}2Ãò—ãe|\Z¯?üK¨Û“ş£:8¡=$µ-m>–ÒF¥*¤)–ø×¯q™¢ŒtU^I$_RZ‡hcL%†O)Bé+†Ü\ZÕZã›˜dŞ7}øv?Õÿ[ÔÒ—6e´i$$›P¿ƒöoœ à.lÛ¥à¸·+r²¨a¨uÅ*ÇÁm 07bôh9Æııè=‘«}³Q`¤«(Ûi¡DŠ£h;è\\…6/l0a´ß¡Àù³yğ6eË$ÒÜ	À3íOı\ZönÛ@œÒ€gÛ+we»÷ëEûàg?ûYa?ß™„^Ü<ë^kŞë–‰MqbMiDGÃò@Í\Z¸ùãŸ€)\'Bı‡I$©à\'J	Üë–,†gxX:¤qP‘\Z’Lu°äº¦Œ€‘‹T³‘et)/¡u5)mÚv[[RBL’&¦öˆYÉey’)]ÍW>L›{\nÌ¿äZ¨Šı/ÀhIFd<KHt9;IWr}2Ãò—ãe|\Z«{vmTW!’`Û$BM!_KÃ-”àHU¥«ë	n¢‘/9ÂÈ$éh í$§.–ºåuª¹5<$µSºÂ\0qæ]WŞğN˜9Ÿ½ßMÀ^F!}İa[{\nÒ°L·­]\ZÚDĞ6b½^4´ï#b¾Ïò1—E„¼ıX}®\ràÅB6%Iùˆš£kU·‚\"ùx1¡ÊãşD¼ßŠôØ0åG`Î™çÃ©WŞ&H­ËÛ•@sGL\0>dúÆ£?ƒ†º}±væEÖ³mü¼éú?ÛFôjàÆ³î{ğ¬›j4©ˆ\recódË+·g_t!\\pÃÍP5tq0ÁTÿ!D*xfwSİ~xñ¡‡aóú\rBWi›É©!‘¦:>çó!u‰Plt|A3]\"IGµG/¨hà¶gàº É©,`º²R¨«0ouı7e:œzùÍ0lŒ¾-Á0Z’Ï]ÎÃNÒ•\\ŸÌ°üåx™\r¨ß¹Şzåyh<èÂÜ´I$Œ´4¥¤•‹YaJ8Úï½—É%-4$›t5|$”>ø_g_ÓÒµ«R™H=C‹TYº\"#Ù’§d\ZVß¶EéáFµWù˜È‹Dû›ÆI§Îƒ‹Ş}%TBÙ3¢,¤ÿ;lÊsä{Êo.|	V¼±Òğymj\rY#¼-1ßgù \r®g2J²«·A|·®mË‰Ù7fCƒÕÁeŠm9*i‡†*¶CNKiŸ£a$¦<BÙ5~2œ}Íí0r\"ŞŞãåhîˆl}óØğÆ\"èhoµ1/úãÙ6¢W7â<ë~9rÖ­\'…\'bCÙÄ†LåV@xö}ö;.‚W]­¸ÔÑ‘\n™ËHànª;\0k—¼\nË_]m­mrÒµ›I ‚º¼”kÒLWózÑK– 1Õr©+	*Ş‰aYÅâåí¢‘ÖLWúRW)ãFĞJ>™’…¶´]”«4\rCGŒ„S.»Æwœ(£Ç–$7&híD—ó°“t%×\'3,9^&AÃ¨l~}l\\¶DeT›DÇDŠ¤¶£ËÅRÚ¨T…4Åÿ¢gÛ’RÁYÒ‘ûÛML[É4ƒE-ùd+Q‡hcL%†O)Bé+†Ü\Z$R7‘5ÕÕpú¹§Áiœ+xŞÀİ!ÖèÊÅ¯ÃÊ7V@{[‡±Ëj’ĞkBÒ©ãû‘‚(¢çÊtN÷Ù‚—slDÀm dxn1Q3äØ§TN9§rí\nJd9zˆÚ°yl‘Ñ~óÀÕÆñ\'sÎ~‡àÇÇÚphîˆ»Ö,õ¯=-Íö•/n¿ôÇ³mD¯n<ë¾ûo> i]³ÜQàt²‘QªaùVW‚ñkÄN`î)óáø¹s`ú¼“`Äxı#BIÈÍ\\Š½&]ïÜ°6¯^\r›ŞÚ ›r½ØÑÍÌäSªäD‹Ô§kÊX¹¦­SIš·ZW2DÊÚ,˜:p#¥xVnê’Å•åe9ÅR\\ä»iœtáÕ0ıä3 ªš–$7&híD—ó°“t%×\'3,9^&AÃ1[»n9¬}utv¨{¦¶=b<—Éš6)£‘Ğ³…Ty—ÉqKú’#ìˆŒ«C4éjÚ¯C)rrÒ¦f£xH*o#¦ ¯\"‰Àì¬Ù3`ÖI³aÚ¬™0bÌ(%şLfBíÖí°uı&Øºiq	d7bŞñoŞ˜ß;z.¡^ÓØP§Ÿ¡rzİJZn¨\0/µáØ7G•)¢GqØök5+Ú°y½QˆÏ¯ß+·¡5GŸ3N^ NfÃÈI N~×ÙÖu;6@İÎ-°cİ\nùÔ¸k/j?úëÙ6¢×7bÑ½ß€eOÿZÒj™KÂ&b£mÎ;;\r„Ã§Ù’m€<Ÿ4e²˜D­-¸Be‡Ø`jæ–ÑzÂ±¼™üˆÜèHBÕey*E \\.™\"Ğé]]£.™hK•S,•W4–SıĞÖLàF™´-¹LW–C\nu•æ­ni7å88õŠ›aè˜‘Âjäit¤=ö]ÎÃNÒ•\\ŸÌ°üåx™˜Ù¦ıµ°ä±ßÊàmÛ#Fº~\rLÏ4Ö£ÔIWÓÆ†ÖW]2‹3Ùé\"\0¬c&M‚1\'Á`vIúĞ=ĞÖÚ\nûvì?„S»S½ª¥ìY;Ö¶’ihZ¶Q‘¤‡Õ^åcJªıØ€e#£;í8õ\0—ïíÔ¦¢å$<2eÏ´RÈ¬4æû,q™Cëõ5`?Vo§Q<·®mË‰Ù7fCÃ(k³ˆÛŒ´CCÛ!	§¥ÌÂHLyÕáØ±ŞÑã\'Auõ_äã½k¼(uÌCÀ_\0{qã¡~y¶è“À¿Óı“¿~¿ü\rX³ôy\"6ºQÑÖñ†LÍA¨ÿj2e@ÃTÉ1ÑNª\'S\"%¡iÅW9©KG®y‚ğñ5$LµÜò)EHÕ!iW\nh±I&$Çœ¡‘[¾¨°¼Ï–¦‘¯ÒrQU]\'_rL™w’°É.£{ì\'ºœ‡¤+¹>™aùËñ2	\Zq³‚±[œy¯zñYÛ‘ ©U\r;šJEšQÉT´öû\"_›8e\nÌ[°\0¦Î™«ärë)¨€?Ş²vÉë°qõ[ĞØØdd˜ ª¤™¾åÙ¶ ¡Æ&¸E¢h–å½65¢¾Éó‘Ãà2½&$)åØwEDœv˜L¼Wâ6‚ïÃµm9Q›2K<Gä(J3P\"ËÑû„caÚƒí„D|~l˜ò×†‚eğv t¿åÖ¨i?³pÚåŠr!ë/€á{Û÷¿XÛ«gÛˆ>	ÜˆÅı^{øÇbè±z1ÂÔ¹L£-Óyİd#Ö|YPï8pâhæD¢çyÑÉ5Y¢U9ë2«H’-RŸ®–#¬\\ÓV.u%¡S% İ¼Ô·AZ2¤L•Sºêà„HY^É©„,/íê£]¤Q®Ò\"1mî©pâEWCÍpü´1]ÎÃNÒ•\\ŸÌ°üåx™¸YÁ@Öæ×_„ò«}¢SÈL­ªËÄRÚ¨T{&æÅ¿\".“‹íè±c`Á¥—Áøãf X@)’z²¢Ì	V,Zk–®”¯S¡Š©“éËâÄ[££Zk|s‚´yF\"xV¯¨oê|„­ ã6œv8ö=ˆĞ¶Y­+P9½n%-·T€‹Úpì›‚£êÔ¨ÀÇ\\‘4™Q6û\"¢ıN\nÜ|¬Ü†«‰2fƒ†$ôxEË!àÚÏ<¿·İ[ïmGÑgÏºñÏwÈ{ŞÚWtCt‹¢-³|E±Ã×³…ÎE´H4y†ÍøšÀÄ³º(0¤–#OfÔ¢å|\r#©f#‹ëj¾bª…¥Û.¯¤Ïrâj9Êd¢G…•\'™ÒÕ|õ×“³]~3Œ?şxQ—]‰.ça\'éJ®OfXşr¼L‚FÜ¬`hÖ«÷İ\rõu=r™\'D–¥\nÜŠ>ùœ³àäßaò\n*ã°8P™#pøĞAxö¾‡¡n¿è§ÈsÛ¦\rDÈ­ØÈvt™áóMÍóˆ“Ë”=Õ„Y31û,qYDÈëÙÕÇàÚ P^ŒÛˆÙ7·ŒSÆâˆ9/!TyÜŸHÂ€÷[‘¦<‚úêØq2BÆl¢Ü\Z5²ÁÊÅÚÉgÅšÚÃ°­.ı—Ìğlûß­‡|¨WÏ¶}¸k^z¾ëßÌ<ËDltƒ¢-KÚi¨Dê¿šL¤hò01 yV,	M+¾Ê™ÉÊ)ƒ69Ÿ§©K¦Q#GHÕ!ÛVì‡‚¬‹ZZ“%Wú|Q1]Y)\ZÉS½…¹ç^3Î¸\0ªj08©vÅàa\'éJ®OfXşr¼L‚FÜ¬`hÖÁ]ÛäınÔÑ<­K¥ö3Š‰3 ­…/“#—t5M2Äàªj¸øºëÄY¶úB™\'¨ŒÃâP•Yxá¼üÈã°~ÍzÇ¶¦y[PíTíU>&ò\"ÑşfÀ²ÑZµÏ#¢Mâùh¹$›zMhğ¶8ö9-´Á„¶½Jh_ š×ˆÛ ¾[×¶åÄì›\r³¡Áêà2Å¶•´CCÛ!	§¥<àR*aÊ#â6¸6Úİo¹5já1ÛÏ†Önx~}=åÂÀ³íƒ­ƒaáÂò~q¬ôÊ·Ê“pòÅ×ÁôÏ¢\\|‡!S¹BÏ–Şyä_CDåQ\'#BÀk‹Á‘zt–r•·}óBÄr$G¦z–,„g~øexé—?†¦‡çèü6ú˜i3`ìäi”Kƒh6E|·iŞDp#¥X–…Fã÷ˆªê*¸ìÖ[aüñúÒxÏàâ¯…¹\'«ŸOåp¦4)R´à”q¶¥îÁ®%swÍS 4>Aó¹*góÊ!l$Y)}\\9}£ö»\ZªÅÔíÏ¶³\0Ï¶Ÿ}y|ıë_\'Nï¢O7âü›Ü Ñ®Ã÷\r™@ú¾Éäœ<~ì×µ\rã‹)Ín¶6C2yŠÙT»¶¥Ì‰Æº½ğÒ¯¾+‚øWaë²eĞİİç.˜3O]@T²Ÿê › #Í.½å6=ÉÿÙĞ¢ñ„àFz¯C½\r\rE\\¬ıÌ3€²QVß¨pÈF\\f9ÙÜ/¥¯I6„q+*b¼âÈ±|Q¸ö6fû!’u{«àæ›o†ì¾ 7Ñç{Íé\'.€ù]«¦³¨9Õ“˜Lœh#æ´hD¡Á_ntHÛ±K©ËU@Nb½RàÚvÏÖ)eÈÓ‡\0>ÉüÖËOÀSßıwXşÔ£ĞÑRìÏsö$&œp¢|åŠ#x É„ö,Ú3ç$–Û’´š,$Ï¸ø¢^Ú\Z\\}%Œ›0Öm#¥Õ§ˆC‰l_(r°–Q\\|´KµïÚ!d¾¾lD/“;( îÖÔ¦?Ehë®§.†ù—!Nï£_œîœóP=t8åÒa¦–{vƒiBà-ÕãRŠñºâU¸NÈÛÖ\ZÇ–¯íI÷’R,—:=‰Ú\r«àÙ»¾*ÎÄï‚Æ‰Û¿1i†ÿ·vãAW_&çpõuÆ¯;qê˜sÖ¹”ë=T\r©Ko¸FÒÎer\r+†€ß¥­Í 8\\T\"x\0,Ï:4‘,µ½ä}CĞBÀ~\\”e]Äûmm”ß3lc ı\ZJÖ­umĞÔšşÎ6âµ\r‡á‹_übşŞv\ZúEà5~\n,x×ûÍ´G÷\r:ïİi $Û?[œ›6¡N`õèrÒMh€c‹ÒD0[¶XÔ6É™µ4»Ø­rôşyı×ßƒ§ôuØ¿m§èqÿ½>rÜÄ˜ŸºÀ{Ô~ğûÛ4é\\ß™š*:ç]*xöÆNóNVï‡°c{‹ğ1¶lbYË’F?ùìÕNcß3\0¡\0&‘¡q«”z«´Âæƒ°å}s’nİÕÈ?¯iÀ×¿6î;,,§Û>Ô16lÚ_øÂˆÓ7è77/¸é0Rğrà¸XÀĞQØÑóOWñ9yšã+ĞÕY‘ú‹Y.SM®ƒ\\¿Üäæmõàeô×û<ó£¯ÂÎ5«Eàê|äøID‰Ñ·³`BËÇ	`|¿:AMÖÌçÁ°Q£%İW8ë²‹eÊ›¨úÄJIC»ûv¿P +Â÷­ıØdõÀÚrëÙOÅÛ™âÀ,Ô·$Y)É¾@¹c¾aotve£\'_İ\nÿıßÿ\rcÆŒ!Nß _=tõ\'şŠ¨ qÖ;C³SôLbÚ+—f\rşˆğ±¨{q”·ÁWÊÕ%\"	±Ëä§c¶Êuğ„¯ÀW½ğ(<ù½‡Ö|½ÿ`ÔÄø}æxĞÕÈ0ğ¾ÂŒ5gA¶·/zÃÇŒ†O‰<¨æës?K]›!q¹ş(ŸÖ®,™Ù/¿fıP»(Íë!áaM\\@‚…9;ĞØÖÛêÔ§SÓ°³iŒ?î¸ãâôúUà>î¤³`ö‚K(§ ÷gúr¡jõl¹—ëòÌaú„Ù•´Û^<×¢÷ê2Û¬®ğÂ•çhE¿GkS¶w+{ƒªù·“£#Ï¦{J)¯\r1F{ú3Oœ£§í)—ÉpÄ‰¸Œf©•3Á®Ğ9\rOE=à•y6™B˜TG1ıôúíj$´³¬ØÙ$S¾æ|À×¿zq|ãß Nß¢_nÄeø,ÔäxPMwš#iÿÇÔ¯™¶Pıë×%!\'ë*Û\\®É¤\"’O|ví‚Ìxt+(ö\n‹ÄC†	™vÂ	Dõ=fÌ?‘(úÈêmOûfÈ~şªã}Íß~e£¬nSá¸,o)óšdNˆ¥ûF\"Í-Çgò<¶¹®.½ô²^ÿBZú]à5a\n\\ps¾Kf§¨\'‘MfğìWˆ¸Ôü9Ë„ÜËä1§BÇ.¥.×ÂéBLÅµö\ZXDKºÏá»Âmàâ¤X¾sÖÍÕ%­&pÂtıÓ†ıÓ¦«gQÔº‹8™È†×FÏ\"×Õ®Ïr{Ú>¥\nÜ!°¹İFÈ|¸n·$ë½–yÆG?–Í]CaÑâ•ğÍo~“8}~¸g]ı>˜pü\\³#‹]&×|IèÙJ¹\\—9•;ŒoQr^Zâ2ãÖÅó®­P.b÷(DGk¶ûP½…¶F÷»\rºb Ù”ñC¸ÄËä&ãŸ¤ÑíƒpıSgLWëC\"~—ƒb’…UB•SêëXĞD²0÷zËY ¨ËVÂ$\nIV‚ı¦´øıBµ³¨}üŠ]Íæ´Ä«a„¥›šáóŸ¿³O_ÿŠ¢_nÄ5wdxP-0Ş|zÓüØ	¬]ÎKÓåH“rH£=[Wà›f×=PHÓ>:Ğx`/Qı‡’ß7ï<Äw\": ÷õÓä!`{•eîµ¡µ”Ïƒó·#d?_İy Ú¬;4(ˆ‹«XNšùraÍûæ$½ò4RÛ¿·©ö5´S.| mßƒğÿğÄéè·{âñóàÂ›İÏ¡&Aî8ô$&\'Úˆ9°Ø¹©<N\"UMZ :+R¿©89‰õ’€Ëö×ÀBhØ¿¨şúİÛ³f„säÎ„–Àø~uRé¿“5~ò$êS¼¡ÅîQ(ĞáûÖ>Ÿ,…BìSªàÖ²Ÿ,Š·3	!Á¾%ÉrHIöK^\"+ãÒôi?ùÉİÄé?è·qá-ŸÜÿÑ½3tv–¤±28;œ”bá³Øè‚³º¾Rœç4××ö·Ék`>ÔíÙETÿÀ!v º\ZŞöëfŸŞ~IÍÛ°~–¶6ƒâõ×hH”Áv\ZB6òì“JBÀ~\\”ß»âãjm„zîv¶v\nƒö-6ìk–öèüX¹k`¿z £_nÄåüŒLıS«gË½¿q%òì@”®Û’¸\\!lUÀ[o´—*ŸŞ7&vSë>\nïtïÛ´–r}‹®öVØ»}+å8Ü‘ç³»¿Móïè°œ½ïİÿĞT¯n`{ƒŞV€#†LÄeÅ™w‰ŠXeÆ‚§¢Ğ~IJJªŞ\nõ\r…%™÷Â7\'ÉÖu¿]bæDdÛ÷Y™¤?üBÚÒëà{î!NÿB¿ÜÇÍ?K>¬wš‹iÅÔh:EìÄqgvT<àº1D„&+RW¢êö|W/Ò¶AØæcÖ=:°gË¢ú;×®pÏ²ì ÜX¡İ1àD\n¥h<Ô ¶Ü¡Òûr¿\"|3èöóWïkşöç¡ªó÷-ŠÒ/“—_·@ÀHŞ1ÇKä+we¿DŞ_¾–„~¸İr‡sÉÜî$ièId“ZÈ.Í\Züa]–iÎ•\"vË3Z‘îâ;¼¶kÃÚØÓÜ}-«–%ú·Y\n;6$íÎğ¡}{ˆêhoóüô¡hrA»ëE ‰áà_~ß‚ö)UàåˆÈ…ì6Jï™­#d#Xw/½¶a_+´tdg{öìÙıâiI8*wÍ°pí\'ÿ:â‹z¶R.×à]HŒ—\'/†´…íH=ºnàEyÔ¡“ÜµµœÒ¬£ë_{¨¾Á¶å¯AK“úÚ’1ĞlŠø!\\–¯¥qD/“Ü×¿¨?°g¿h{Êº‰ÒÖJHL²¸\nÍ°ıd°q˜ÙÏ½Ş<²ørUîú˜°‘d¥ôqÍİo·ÕÎrê–—ÈëZb]¶WÃ,ğù‹¯­ê·—È5ŠÀ˜8c8ó¦§Ìi¼}“É9yüØ¯k\'–/¦4»ÙÚ@Éä>UŞÇ4»¶¥ÌôwàY÷Á][(×»À{Ûëß|rqÄw	ğLo\'‚À¾oÇNÊõ=Ú[Û`×ZÊ!2÷Ú‹äõáú{©(Õ~uûAë^nKD†ÂqË	‰EÊ¼&ÙÆ­Èg#SåAdk¿^\"s{#åÒñêê}ğ÷ÿ÷ıêmšÀ¸èV÷’¹„ÄÀdâD1§…c\ZüåFˆ8­`;v)u¹\nÈI¬W\n\\Ûi—Éóô¡·²[bÅsO@W[ïåÇï‡Îöv÷Ò¶€t™Ğòİ9sÎº­TÔdqöş]ıç‰ú­kŞÛˆC‰lè@1YRÒÎà³ x–kd|VŠX[®	·ıdQ¼I5¿¾…ÚºL^@İˆ;›eğÎ‚-‡Ã„‰SàóŸÿ<qú/ªÀx÷ü5Ô!\\\'#!ğ–êq)Åx]ñ*¢éRšÇ–¯íÌÁÓlq”:ı-M\rğÚƒ?§\\ï`ÕsAİ~¦)fœO9£ùerW_gÒ\'©©©vmXG¹¾Åºkˆ\n Ğ¥´µ§•P	UN©|rJC¨í%ï“‚öã¢ü}«µQ~ÏÂ*ßy¨ö5Ñ‡VRºŒŸ5}î••ış¹ÆQ¸\'á%óÛü\rğ9L[\'yv J7yæóinØ’QÛ*ï(Pê‚Û²ÚÁ×1‚Æú°êÙG(×³XùÜ£°c=i&ÑË~[‚&ëó3v~›Óë–.%ªïP»y›¼LííiYË’F?AûayıVí4<¥ø’ª·…‚æ…°$ó¶¼oN’­ë~»\ZùçU£µ£Ö>´Â×>EşØËÛŠKä\ZG]àFœsÍûaŞÙ—RN àmèFìèÙ‰ãÎÌU|Nîã!-P©[L×m¹L5¹ÛÀú…ëİÀûİ¯üúÇĞİÑAœâ±òÙGa\';ÛuÎšø€-\' RˆµMĞÛ·»öoß¦ò}„×_xYl¹C©„v÷!÷+Â7C®XûñÉêéµ²Ÿ,JºŞ“ÂFÈH’,Ç€”d_ kono‚úy\ZôSäGÃ%r£2p#®ıƒ¿‘O›G‘vÄÊ¥y/ÃºîbÉÕ†´&Ä.“»Î˜t;«ƒ÷²-§lÀ3ï}[‹X­­ñ ¼ü›Ÿˆ í?ÓNºá—å|…%+>Ãœ^üÔS}öc+;Öo‚İ;İ[9ü,u]„Ä9êñ\"P>­]å\"dß•xü\"BöCı¦4?l;C6ÂÃZb_’ìoÜ×\n­¶qª–§È£8j7í[>ûo”Ëç„Ş…ÄX\\®hwæyñ´EïH½ºÌ6«+ı Â•§iË<$~\0WºTÁÂ_ş\Zë\'1òl\n¹§dy\r,Ëer…ĞÜØ«^~‰ò½‹v¼U(š”z™¼‡1nf©•3Á®%Svqx\ndğå êWQwR¥+G oÔoWCµ3oİøêWÚÏuê5‡—Èï{z¥üĞÊÑr‰\\ã¨\rÜˆãçŸe_cĞşiÚ´û×Šß¹ıº\\œ¬KÉäšL*\"ùTÀg×.xw§šÜ†cƒ‡Œ$ªt¶·ºÖïfó`ì ×„®0Åí­_¾¶®\\A¹ŞÃ´9‘·9’úÈêmh(ŠpÛbíÇûšm)eõ\n‡lÄe–“­Í)óšdC·¢tßHD iíÇ§Ç—æxõ¿E~ÅWöë­$á¨Ü|Eì¸“P.\01éÜ±|Grœ“gaJUS â´‚íØ¥ÔåZ8õÆT\\Ûi¯õG”±¤1hP±n|¤Ëÿ…¥¤\0.áâ¤X~âÁ€¤ÕÆØ\Z¬Àâ§Ÿíõà=dqÄÉD¶˜³±Òvµ+‚g¹ØÁµîÌ¶»ÈŒì6BæÃu»u$!Xwè5°2°4Ç}mü¹Î-Û÷ÀO~òâ]8ê7â–ÏüÔ.¢$o{±pÔ¤³XU_t±0]J“à4×c‹ç][aËİ·ªkUº:UàNÚØ*š)ñ\'’.“ÛLé“„^Á{ı’äÁN˜zÜ4¢èRÚÚŠ3Uğ\0\"XMNĞD²0Ôö\"‚ĞB.ûÜ]$Y	ö›ÒràÕÎ<c¾q+Ô5³‡Tµ<Òe¼z…¯~=ñÂrùsıõ[äi8&7Şï¾YoDš;Õ£Ëyy]ª¦´Ei”ıÉ9P 4	ØF­rôc\ZQ:Ù7 ëAŠØ‚&ëóKàI÷·••e…‘~cÑË°è Ã÷íğÀü³Ï&c\r)¡eòà¸,;òÙ/\nªÆ¾g\0R÷5\Zç±J©·J‹´º3ÀZğÍIºı4Pñ¾ö¦”ûÚ\Zx_ûÅ•ûásŸû\\¿ü¹Î¬8&7ELÿ(\'ÚÌ5§;÷Ÿ“$9d!-P©¿˜å2ÕÄ:´€Ëã—›Ü|¢­cƒk†Uº:â0\ZÀûØ±@‹À	`|¿:©D\'‹Şçz	Ø±y<ôƒÁº×{şì{ê¬™D)Ïˆ(í)„]¾oíÇ\'¡øµåÖ²Ÿ,Êà,„`ß’d9¤$û´ttÃ²í¾ßğcİŞ*ùu´ú§\"ÎÑ‰c&p#ğç?g/¸„rÉpv8)Î>‹.8«ë+Åy©¾ò\Z˜f+Ç\ZêudßµäÃÀÅq¶5×\'¶5t52¼)ì×MçÀÀBŸ™··wÀ/¼}ÿ°ê¥áğ¡ùµ¡#ª‰Èágig“EïÌÊ§åf@ÈDğà‚Ò²²%zWX¡ö‡‡5[;‚…L´lGtvw»ëRË#UÕ‹ß\\?ü0q^‹¿ˆí7h;Ü¿şògáÀ\rvê´ZHöµÌ*’äD‹Ô§«å+×´•K]IèT	ô÷µP_Ÿ1k9ÊT9¥‹›(©/ëRÊ¸‘å¥bŸ<&L›£ÆO„ª!C`ä„I0¨ººÚÛ a¿úu©úİ;áÀ®±OwözÊÑ®şÔˆ0•$Ô–9ŞzõUØ¼L½v¥Õc)mTŠçÙj^R÷·1/hTó„©^jG°×À$ß¤cÏ¸UJvT‰Ìk]•WÉéØñcáÊ÷jäCeh%\råXhsñ‹oüš\ZeµÆW]ÕëC#jWç#l…·á´CÀ±)èˆ¸¨aàÌºÂP9×x¼XÔ†cßlU§ «C@‰GÑvÂ¹\nmŞóh¿?½ll(9·Ñ2fƒ†$ÈF¬šÆß×®=Ô&Kû+h]Ækî\Z¿zj5<ğÀƒGõ%rc.p#öm_¿Á»½…>y\'&çRO8:…q’IRË‘\'3jÑr¾†‘‹T³‘Åu5_1ÕÂRr´išµ%%Ä$¹`bj^É1?|äH˜}ÚipÜüÓ`°Ò$‰T²\'¡hæ{6¯‡\ro¼-ÍÙ_Ÿ(=áh#Ç‡ßûqÊ	˜JjcîÔåÏüvmXmTù\nAZ]ŒµgKãØƒibNd9­ÜD#_rÄœ‰L’Úê¼ãºaæÉ\'(&\nYYí3.”?F±tÑ›°dáBÙ,ëù~RBï >›šç&—éõ¢ÁÛ³Ïò1—E„¼ıX}®\ràÅB6%Iùˆš£H‡zñ1çãÅ „*Ÿïøüzl˜òê«cÇÉ³AŠrkÔÈ+k—ÈãwÈ×ìR—È±_¦(ñº`<³¢ŞóŞõ—È5©Kå\ZŸWâ¯UFL\"ŸwÇ=àNÖ¥ÀjÀ=\'«ë·é8\'£éÚ®®©‚³.¿®úğïÁ¬3Î¶A;#ğL|šö—}ø8ıÒ« ªš]í!„G§tŒŸq2QÅ¡¾¶ÜO‹ºsÌw*ÎFÒñvÆŠpt8ß1j±aÙëD‡ésfË&§­£şØ¢É²\"hŸRwîJ«:»Ò{æ÷±(‚u³ ]*Ğ~c[—	Úˆ÷7X»g0L˜8õ˜	Úˆc2p#fŸu)\\úû°šÌÉâ-y1ø%ç9R¯.™‰z^’\'€©3‡w~øcpÜI§¯<L›:\\ş¡;`òŒ£ëËA\Zc&M!ª8´4ùv±;1glŠø!\\â×ÒLÆõ‡¤ «àêf·V»s7QÅaô¸±D1š™ƒb’…UB•Sê© ‰daJ×âğÈà#ÈUy‚	IV‚ı¦´è~»¶T;CuãÃh¯o±W	c=ÓEI°£i8¬Û¼|ğAÅ8FpÌnÄ‚w½N¾èZI;ÕëÖÒu-RÄrH£=[Wàë“ŸtöYpŞµ7Š3ä!Ä)x¾àİ·ÂÉ¤?Ø×ß0|Ì$¢ŠA÷õNxÚQ|ŠØÂã@æ2y&ˆ‹„ë¸\0DD¤ÓÑîó¤ÒQ]Sº½ĞZÊgÕ?¥Ú/½GiPí,Ë~†ÂqËIÛ)$8•F’\raÜŠ|62Uo?~mÙü}mvtÀ¡ÎağÛÇ^Aû¡£ö}í$Óñ®Oü5L8?×˜°Ø)Edsr©j\nĞÕY‘rS–æ\\ä$Ö+êŞÓÙ—_\'w¡â÷fœq.œ~ÙU”+)»…²0tô(¢Š‡\r”NĞeBËWs¦‘P•ŠšxËŞ©!Éi\\ÜWGT1\0]0rdò\'f³µªt¤Á—k?>ETíšpëÙOã1=<¬aûë^µ»šğÇC¢ëS£íHµüù~ğX° Ã—52óqÛŸFŸ\"üƒyHŠ³8g¿1İè‚cº”&Á±åófşğ¥sN=›_Ì¥ñ4L›F¿=ó\\U“?æœu>œwÃ{á¼ëß+†°ØŸôlK½L.Àhÿµ“Láº¬R§zÎOÔQémÅÿrÚŒ¹ì»å.¥Ù 8ÃP….©†ÛEDÙ(âà\"h!`?.â^‘\rñqµ6Bí\nw;[;’ætİØßè®õ˜E*Úud,\\Y7ß|ËQùò,x[nü²Úõü/P=t8q\\p‡S‹.ÙÉòi¿\'Gm«¼s @)bÂÔ)pê%—Q®w0ãÌsûÕ=ïqS¦Áé—]\rW}â3°àº÷Àœó.ƒ1Óg‰?÷ƒ EàPêƒiÉgÅ¾§É%-·\nî%ğZêPYV˜ÓI|ÄÆoU&ŸòéÓœğ­¸,ĞÙí„ÁƒT¨v\ZŠR|IÕÛBAóBX’y[Ş7\'ÉÖu¿]äyİİĞÛë³ÿœ->Œ6nüd¸ûî»‰sìám¸Ÿ×}ú_gæãsò4Çç0Y‘ºZÀLŸ©&×!UÕUpşµ×£wqúU×õÊÓæ!à«^çßø^8÷æÃÔùg·gQ\'·„Ñ€˜÷29G(¸*#¤ê!’œÆ­ÛÕØØ,Ô‹ı$ìØIşÀÜ*!	3\"èŠ°oŸ„bíÇ²Ÿ,Êt½\'êV\\\"’dE\rHÀVŸ3]Í ÷Í\rÇ–ƒÃäÃhÇÂGVBxÛnÄôÀ•¿ÿ—”KFøXÔ],iş›\"v¹L>ÿì³ ª&ß«^EaPõ˜á¥”+™âsÏº\0.~ÿ0fZïùãûÛQ$İğìÊr¾Â’¥Êr©£ÉÊ9:œŸ ãb\0tväòÂT‘şpdÚÙdIÁ\"+åÃÁ¿ÜŠSìSª<cAÛO„¥÷Ì¶3d#Xw‰¯ák_Ëwúo]!¢K«öğpxî•UÇäÃhQ¼­7bşE×Á¹7ÚvÄšë\r\\œº3¢TÂ£ë8°”«¼ï@aØˆá0{ÁÙ”ëàıî¡Ã‹ı­ë4à;éçßø>˜s~ïŞ@tu¥™ŠybSÈ=%ñ50J±l–Ëä\nqÈÇœÈ4j L1¨2Tå53qó|4K­œÙ˜ÙOÙ\rÄáİìSZ>¢~Eu\'ÕQú¸rúFıv5T;yİøùÛ\Z¡3ág:£ÜÃİCáñ…+à®»î:&F‹âm¸çİø	8éBõš˜»­ãÖ•\'ë’C2¹&“ŠH¾(0ãÄy2ß×˜uZï\\¢F`Ğ¾à¦÷ÃØé}sı°p±JĞA7*v.Ÿs¤9Ò¦ÜàN„@b»t¸ÆúDƒAâß†õ64yF)	ÅÚOè\\P6ÊêÙˆË,\'›û¥ô5É†0nEEŒ—´·7y‚¶¿®¶îj¸÷ÉUğÕ¯ş7Üzë­Ä=¶ñ¶Üˆ«~ÿ¯LğÎ³•ª¦@Ä‘››²4çZ8õFTŸ\nQ}‹é\'ŸNT~ä]Ò´GL(şƒ*Y±wË:¢DÛC÷\nq-?) *5Ù1¶FBåêÌÜïK~(İú½ûdz4#íjWÏrƒ2\"Ê€kÂßÒìg·2_HßBu‡.“{Êé }í+\n½Dğs¦WÛOûğ¶\rÜˆ‹ßÿ/ßñÖÀû×Ö›¸Cª…],L—Ò$8Îíõtk¿N5lT±ï\'—\n¼×=vòTÊ|J|Æ)çÂ¼s¯„3®ºÎ¿ùpÙ‡?Ó§A±yùËDYÄƒ®BÒcA®¾Î¤yG2¸9¤ûÛ¾úêöË´HŒ5‚¨8Ò‚lPœa¨‚—sƒåÙàM$CmOëw-ä²Ï!âı¶6ÊïYx|tİ«k§mJø\ròsÎ½ğ˜~‚Ü‡còGFò ½¥	úêŸAİ®\"g7ú÷3¸q«PË¥®$tŠ[­+\"UÃ¬åxÇS•“AØP0÷´Sá´K£÷xµ¡Ë¨Ä‘©\n™s{Ê!$é‘–•92XŒStuuCG¾K9\0ZÆalğP5TİÇï©4Õ…ƒÃ í’Ht9;IWr}2Ãò—ãe¸Fgç`xò_¦œU3)£‘Ğ³…TQ¿¦iTpuˆÖr¢¹Lay˜Qôğ‘Ãá¶?ú¤Ê ¤\"ÑòÊ?£Ğ¬Gï¾ví´>ÀUùÚkƒx‘aFeÜY3§GÏ…c#\"´mÆ™u…¡rz!i¹ ¼XÔ†cßlU¦¨<Æ\">æVµaóîGûíû¦‚‚Ûp5QÆl¢ÑÙÿVï>{\ZÛŒÇ¡¸EU{j`Oİaxá…ù‡Ñ¢x[Ÿq#ª‡€›îü\ZŒŸ>‡8è`Døä´\"õ³\\¦š\\‡Œ02ıvAÍğj6jŒ8RşM™7şN4fL²Qòoè¨¡¢L\r®êv‚vÅ[‰R;tLhù8™ŒïW\'•èÄSë%\"Éi\"uò¶ˆ¿¦ú•¼1|”İQ&·ªğ E@”Ñ@ÄQ„}n!ûÉ¢x;“²ì[’,Ç€ä±¿FœiïiHÚ\Zoç xÛnï?÷5¨i2ô9–‚s„K)‡«KD\"G¶ÃFöËäo\'lXòQñ «‘6¡¦°_7Ñ4«ÔÑáü$7~œwùE*S †öüØˆ@(È\"òìÌs#P>­]Y2<¸ ´,„ìÇD‰^‘ÖF¨ıáaÍÖµµ-òwµ³ÔîÃÃañ›kà¡‡ı×¾’P	ÜŞ7üÙ×Ì×Õ¸CæZô^]æÀR®ò±KSôªªB¯‚¹óÄwGé¯!msIXAÕcg/wüì™pãÇ>7|â£0ÿüóˆÛòü¸Ìv¬ô5ÃlLº&=¥ø2«õ\r…IâbúlC÷ÛÕ8µ\r*hgíÇ®„…Â¬YGç/\ZJàfÀÕxğ!âø|‘Dá“»z’ÏTĞ«8î$õ4hê +·<è?†\\sHºÂT’=[¥k—·“ÓãÆ…w¿ïV¸âö[`Ìäb9Í‡Po‹pç` ØÏ_u|üó·_Ù( Ûáq¥Ô\"o¥_&·¢øxeÁ ½vw–ßÕVüÀÊc\"h?ÿüóo‹wµC¨î0x_ÿÙhğv/“Çœ6âè6œES)cATP2&p\"Qyhç,) *5Ù1¶+àèp~òŞ\ræœ<®şĞû`ÒŒÄé9Œº­Ô¿şÉ²¬H=‹6pç®´ª³Û(½gÉ>Æ¬›İşó¡¶¡Ã	Úihî\Z\n¿xø%øÚ×¾ö¶ÚˆJàö€oß¢ä<GêÕ%!3Q‡¶ùxé\nzƒk†À¨±ã)\'fÅL‹˜6eü.ñ2¹É¸3\Z\nº¥Ì>·vÑÕWÀE×_U¢½ÁÕUDY¤Á ˜da•€4X5© ‰daJ×âÈY ¨ËV‚	IV‚ı¦´DıÂ´aĞşå“«à‡?ü!|üãö«—ogTwÆMŸygsbµp¬¯FÏÖøb‰Ê(ş½Û\nÒ1ã4ÿ½àP¸uàÙÁ&_\'¾HÜ{àD$Åù¨ÎÅ×\\	³O?ƒ8½ƒú}õDùŠ5‘şA(Õ~¾ºó@µ3Xw¨Ñˆ‹«XNšùLØ°\"ßœ¤W\Zµ\ríŞ3í$_oî\Z\"ƒöÿ÷×àŸøq+¨î\00x_÷™ÿ†\ZŞfUĞÕY‘ú]6ÎENââ’uï©¥±ØoKW\rÇŸr2¼ëãwÂø©êçB Ëö,–¯æL#\ZP\r$øè›¸!$9\rÀœùóDĞ.ıëvå ¹UÅ 5Ğ•	k?>ETíšpëÙOá1)÷·“£P’*í·öd5QŸiW‚v•ÀŞ×~FœyÑO›[¯ôù\'ç9ìóæ„ìÛµ›¨\nzÕC\0Î¿ùvxçïfrNd_é›ñLÄöë&îz‹¤ûÛHáƒhİpbô6x#Ò‚lPœaXK½LÒ¬LÙèéƒ‹PåqQdR2 >®ÖF¨gánÇÛÚ[*h¯¬íTw¨àıß&x{áõä¨«|è29¢¡¾7TÎºû5CÀi—]×úÿÂy×¾FŸäÌfìş6Í¿£ÃrÉXV4+Ìé$\\tİ»‰ê}L>n\"Qùàów¸,Ã D´R¡Úi,x*\nx))©z[(Ô7–dÁ–÷ÍI²uì÷ƒm°‚v¿®ít¼í?yšu;7À³?ø\">¸Gæq±—•+GİÏÖ‹Ÿ¬ÔräÙÏWËQ&=`Î©§À©—ğÏjK]^%Œê¶“ê)‡¤GfX\\—ë!<å’ŒÈx–èrv’®äúd†å/ÇË$hÄÍ\n²ğÓ¯‡öíƒ]ÖÀ†7#G‹E?ígNUùĞgN‰F¾äˆA2åâ:\ZÖ6ÀìùóàÂ®7\n\\OäØÖTæÂØü\"ü—T9ëÑ{î…İ;ÔgOy`ò–#Gd˜\\¦ìÙFòĞ³Ïò1—E„¼ıX}®\ràÅ¸˜}³qËH0åò?s\ZŸSŞoEzl˜òê«cÇÉ™µñÖØÛhßÓvıT³*A;*;\'ğÛæO|ësP¿k£t^×¹µS+n0pK’ëÅOÅ@uu¼óÃ…ªš\ZÃ³ šé;©rIzd†Åu¹ÂS!ÉˆŒg	‰.ça\'éJnp/à/ÇË$hÄÍ\n†O¿»aÿ¨Ûµ\r¶­Y\n‡zª<nM3(—´Lu†ñ5-\r©Ôã@	Üö‡wÀĞ‘#\rCóˆ\'· 2Ææ‘¸·­]OŞÿ¸¤ãAÄ‚ç=&\r“ËôšĞà¡Ã±Ïi \r&´íUòDûÑ¼FÜAğİ\"8––³o6Ì†«ƒËÛrT>Ò\r!T¼øœ:-e×Q3å>¿°ŒPĞF¸~ª Y• •À]0x?‰Á{·ŞÈ OæÛiÉ2íğr0¹ŞÁ(¹RÂò\'uœxŞ…2¯ù\nD“Q%vR=å’ôÈ‹ër=„§B’Ï]ÎÃNÒ•ÜĞ^ÀgÁÊ$hÄÍ\nF’nT¹£³JúÇÁ½µp¸áìÛ¾íßÍMÆ‘´I•Äğ5-ùj\0gÍ?¦Íc§Lƒ‘cF	a‹äó²Ä“[xEˆØü\"|;èÈt\n÷şÏ¡©Ñ½w-Çó1“Äˆòİ2®Ô±)èˆ\"z®LçD?#Fœº]‘oà&/µáØ§TªSÛi¡D–ÃfÔ†Í»s\ZíwiÛµ¡ÛáÚ×ODqäU‚v>Tw‰ÁûÛŸƒƒø«bÒ“ÕÂRN-]8°qiéøÊáÍ`rèQCnE¾Zœm_vû{Å™~»ÜXĞ6TâÈTDm\ZrIzd†Åu¹ÂS!ÉˆŒg	ÇràÖğµyİGªÅ™úèj?L\\€Ö–8ÒÕ\r€š!Õ’WEßÍ4°S´?s³Jõ¸ÕOn=@e.ŒÍ/\"ºƒVpXÂÆ+O<\r«—®&†ß”æùjÑÌ¨ŒÛáa#fßÑsáØˆõÁ²¤#%Cå8\\*À‹Em8öÍÆ-#ÁõI†=hĞjVîØB•§v2¡Óï$¦<\"nƒiJtßZµ»\ZZ:…¶Ûf×GUyå+?*§•ùmó/|fŸ§²îë:29®³3HëÑ:ˆw´·ÃëO<&é\n\rĞUƒ;`È°*ó7zü03i„H‡Ãá‚\'ş\rh•<h÷GÌ:iQÅ¥R²–Q\\ÑµMD.x\"^Bæé[Àíå;UĞÎŠJĞ.\r•À]&.úà_Âìsİ§{çöyº9»$¥\nqİCõõ°ìÙ\')WAıã¦„¿‡!!z6ì X»õøj{!”z°eì\ZñqMÚ\'eÃáö.´›ÛTĞ\\£2¨mßûÍ+• ]*»\0\\ôÁ¿€³où¶ ¢N«ò|±¤-Ü1h7Âòç*Á»‚ş‡êš!0b¤şÆL¼ù{\\VJ JFX’¦A¯k‚g\0R|†ê=V)õViÁö!¥Â–÷Í‰’bĞ^±«Ém¢—É1h?òü\n¸ï¾û*A»TwA˜é{á‚üå¬Ãcš¸¸HÀåö^·†ÊïØ°¡¼+è—9ª¸éñËØÆH<a?„ıd‘/`æ…ÿyƒ$Y†ÙÛØ+v6AgWövê ¿òuë­··‚<¨î1ûÜkáÚ;¿UÁµXWË\"àğlİà\ZÚ¹q¼xß/¡¥ñq‹AWGttà+K¡ß¤î9t÷Q½ô,J\nY(_Äeì‚”*”tCöCı¦4?¢û$?¢ucĞ^¿·:»³÷sÅ\Zxø¹å•Ÿæ,•§Ê{\0õ»6Àâ_~	Ön!ş4¹LğO®}4¬äúŒ{ *$€OŸ‹J,Óªêj˜uÊi0óô³`p5¾çMB)ú—\"×»½¶._[V-—ÂiŒ;ÆL™	ÃFƒšaCaØØ)0pà@¨¢~jàà\ZX¥ß/·èîj‡îk§õ°¢TŸpÅw»:Z¡©nÔÕî’<Ä¨qà¢÷Â»Ÿ;Ö*÷Áp¹8MWƒô\\uâÉ­¨Ì…Ú¹d{ªñØOï…İ;÷ÄôuŞg]3£2n#z¡×±)èˆ¸¨a¨uÅ*Ç=k—9âñbQ}J5á¨:±J¤8Š¶ÉõPhóî\\FûøÌMÀÆú½øº—]ëIO“cĞ®=Ğ=ôÌš5K1+(	•ÀİCèhi‚E?ù[Ø·i©tx³Ä\"‘-\nßk`¸cP:¨«ùêøô9ód\0:r´b’’)*ºUœ±ïZ·*°KE4÷¬`ÎùüKq\n•Àí\"Æ%=Wxrë*saÔ±$Üµ†Ã\"¸kw©¯	rèò>ëš•ñ:yØˆµÅÑsáØˆõÁ²¤öcõ1¸6T€Ù”$å#jb{\r¬«`Mm3\n<9]-GÃ“ËÁ qÀÿÂ/À˜1cHRA©¨îÆk¿úlyıwj±Ğ\"‘‰\\|ç(òÄeà6ºJóV7¡ÃGÀø©Sa¤8{5a’»#å\Z÷ïƒ–¦Fy¦ÛPw€å£Hç9ı²k`ÚÉgRN¡¸]Ä¸¤çªOn=@e.ô:VöÀ}ïw~Í‘° tyŸuÍä2Ú÷±¶°|Ğ×3%ÙÕÇÀë0j‚çÁñ³œ˜}³a64Œ2í+Šm9*i‡†*^|–š#1åÊFs{7¬ßsX¤]Ä÷ƒ¯–ÖîjxvE=œsîğo|£´B%p÷¶¼ş8,ùÕ˜E‚B/~µ¨ÔÉr™¼¿¡Hç\\Ug¿ûf;İ^F«n1.é¹êÄ“[P™½ßá#Ùøá|#¦Ëó13Äˆòİ€èJû‘‚(¢çÊtN­+§½®È·9â¹Åpü,Ç±O©&œrNåØN%²{µ.nÃæİyŒö›îºÃ°aïáÔûÙ|¥à×Ğ~şÄJøØÇ~¾ùÍo·‚\"Py8­0ëœká]ŸU­E–MÎbOÕ>¶ĞÙÑ‹şìZ³Œ8ôwÔnİæ†(òyp8(ø²ßs«Gµ3XwhP\ZW±œ4óåÂš?»:äOræym÷ááğÓÇWÈw´+A»xTw/aÌ´¹pı_üFOcV_|üèYÁÍ÷ôBíOX±ğ	X»è	èlk%Nı[×m ª<„]¾=Sæ(~me_»É¢ìA2d#Ø·$ê:rD~s|ëú.~Fl:8L¾î…¡UŞÑîTw/¢jÈqæı}˜u6~i-°0Ù‚*~§R²ïZòcëªeğÒ¯ï‚İkË?ûnm<¯?úØ½q+\Z¾‚Ò±uã¢,J\nÁ+M!Qk%d#xpAiYÙ‰ò¯¾ø¸ZQ	ŞÇ^µ«êwÈ|Â0VÔÖÀú‡äë^W\\qI*(\Z•{Ü}„­o<+ù&t´ª›pŸ&Ç\rŞßÿhEÖtŸ¡·gèˆQ0÷ì`Òì“`PõÉ“uû\\×°ÀŞMoÁ-`çú·‹,xçí0uŞ<‘Ix%jV0<5)$,Ÿ·Ã=îÚ-ÛàÑ_>Ó3>«	2n#\Z`û‘‚ˆÛˆê†ZW¡r®\rñx±¨\rÇ¾Ù(8ªNAV‡\0?hP¤À¨\r›wç0Úï¤ûÛõ-]°qßaè2—ÆñÇqˆL\0>„öÌŠ:˜0q\n<øàƒ•‡Ğz•Àİ‡8´{¼ş›)ş¶7.2ZZHÓRÂ…Ç_Bo;Ê¸)SaÜÔãD0m_cÀßÆn8°êjwËWİĞ·ÚÓu:ïÜË`æiç\0ÄV„`DY	Ëçí¸»§˜×ÀTP²\râ&Ö–‰¸,\"äu„ìÇêcpm¨\0/²)IÊGÔÅ\"^ãõ\"x¿·±¥®\rö4D~Cÿ¹Íqp°cüê©å•‡Ğz•ÀİÇèhm‚7~ó%Ø½æE¹8õ¢Ô‹óÑØĞNƒ£’Æ¥EÂc”ak†\0Ò#ÇO„“Î»&Ì˜ƒu9r	Áˆ²bÊ\nÇzàŞ¶v<õÀïü:ÄóYÕL.Ë¸9-´Á„6è)y¢}h^#nƒ øn7Ë‰Ù7fCƒÕÁeŠm9*i‡†*^|şœ–FÎ¶Û»ğ~öaùİñ(ğW¿’°­i8<¾p|ík•\néMTw?Á¶7‡U}:Úğ}X\\¸â­³èìèm§qwea(—ú\"å1J{z,¥\r¦£ÆM„Ï¿&Ê Ş©Hªqh#Ë»½µ\rîÿÑO¡©¡9X>VœQ¾[Æ•:ö#QDÏ•éœZWNİ®È7p‹ÚpìSª	GÕ)èz»YNÑ¯<Ü	÷·°KãşËä]0ŞÜ1\06mÛ\r>øPåó¥½ŒJàîGÀKçoŞ÷%h¬İ$ózá9kºŸ ·&kà¶î<À{™¡i“2\Z	]×àª*8ñ¼KaòÌy0lôH1¯EqÃÇrà~úWÀÖMş×ÀŒÏªÄE‚ŒÛá&fßÑsáØˆ‹ÜjĞŒ\ZàÅ¢6ûf£à¨2ÅŞúZ\Zêõm°\'áÓ¥\\\rQWÄ÷³Ÿ_¹¯r?»Q	Üıxé|İ³wÁ¦—#_|ı}á0EnîíH«si¡Ë”°.}}¤ëU4~nÆ)çÀ¤™³a¸ØYÉÏÄsƒ½\Z¸íäJËoA\0Ëp¡×Éü{ÑƒÁú5ê0Ÿ\\ó|5“Ëx@D”¸c6¸É(yÈ~¬>†¤ÀíÁ1³œ˜}³a64ŒrÜÓã6#íĞBÅ‹Ï]4pã%ñMâ,Ûwiœ#z™ßÏ~øùeğ¹Ï}şáş‘¸ô6*»Ÿ¢ví\"Xzß¿C—¼tŞ¿ĞÛß•%C¹³Ğ)OÚËc)j¡s,CuE·Õ\'ÛH‹rÃF‡)³N„ñÓ¦ÂÈñÓDp\nUCª…–z†£ˆÀİu¤\Zººº¡áÀAØ»m+l[·vïØ—\\s%Ì9óÒReıĞ6F÷òñışÃpÿ~@¹x1YL¹Ñ-åØwEDœv˜L¼Wâ6‚ïÃ1³Ç>¥špÊ9•»Ş®D–“x™aÚãÎ]´•µâ{{]õ&¸ñÒøªÚAğÊ«åYvåU¯¾E%p÷càÙ÷²ûÿö¬}‘8ı½í0î®,Ö•…¾ u|â®i“2\Z	]RGä-nÌ+[¸7ÄT×ƒõTó†”:Uâ”|Ìøq0jü2|$=Rê`ƒŠIHwv´ÃáC µ¹Z[Z¡¹á lß¸ÚÛ:„\\hPLL\"=ëÂsàÌË.ÁœâÉ­¨Ì…NàĞpwşˆuo®…Ÿ°¿	•ë¼ÏšfFeÜFÖÀ´ò ²-Çá\\¨\0/µáØ7GÕ)èz{ü@ÀN\\Ô†Í»s§%mâ€o³8ËnlídVBP÷·å¥ñû`üÄÉò£*•Kã}Jà>\n°ù•ßÀºç~­ıãì»·Æİ•%ƒî¢/“K±ØÊrb£ÔC›häK°eÊÅu4¬í¸SKyù)Ó&Ã¥7]+Fkí8”1¾—7pwşˆx6¬}KÒ¾\"šç³¦™\\Æ\"‚‡˜}–‰¸Ì¡uFÕ²«¡”À³o6n	£÷ôü;>o(©oéAÛ¾›m­$ımkÃpxláRøüçï¬\\\ZïG¨î£-káÍßüÔo_Eœ¾A_8KîÀ-›;šJ\r¸1k¾H#[¶CRG²)pkšd¥ş×Æ×´4D»\\IÇutª¬Û6àS­ƒĞôşäaèõûé1(cÑ=½D<\0ÜóÕï@G»º,³– Ë¸9-´Á„Eî¸\r‚à»Ep¼,\'fßl˜\r„£èzºYÊGÚ¡!„ŠçÎşçæ-p¾€¦aGÌ#ƒ`é€ÛvÃO~rwåÒx?Cå“§G	†™{[ÇÃ[ëvCW\'½¦ô6€»+Ë‚<úB—íÁøÎL]&Wp#¥XÖ†iÔñÓ\nyûàÂ1Çë¡4\n¬Èğ¡”+İG› ]*â£`{\rƒÙÁlL„ì‡Êyá)ÀƒvyÍ\'#aÆEİ¾:êwÂŠ± †úağƒG×ÀÈqS`ùò• İQ	ÜG	vmXóØQÛ//ÙõuM$©\0áN\"œ Ç ƒnTÌƒ±ƒ\\{wÒ¦ÜàN„€¥]»Imµ‹²¾şUWWÁ@ß«ke ¥Q}š\ZŠ<£”„bíÇ(×TJ(eõ\n‡lÄe–“­ÍªmG`Ã¾Øä|¶ÔÂã2x–½fÿøåËà®»îª¼êÕQ	ÜG	~ñŸ\'\n µ­–¬Ø\r+Wï„Î^<ûNZğı\n¾H&ÀVğ\nqOiùNåê’V{Õ[#±M~~2âõphsóœ¥ˆq 6şiÓr:CÍŠàYnöCp­»3RZÕÙm„Ìïmê€5»›àşq¹MeÿjÑ.8Ø:Pœe/‡Ûn»$ôGT÷Q€~ó}Øµq5å,vím…¯l†={ˆsl¡œËäiÁMê2%^WÒer›ÉÛ.‹ävY‰·JD‚Ú™yòÉ”+[×¬!*` Ê0TÁËäÁòl‚&’…Á\0Y@ğZÈe?iÆUíâ\0~İŞÃ°£®5áhÉØpp¨<ËşÂ¾\0/¼ğÌš5‹$ôWTw?G}íxâ®ÿ¢\\bÁ¾¹z¼ºd+´´$éXFŞËä\Z™wo´ƒåúYîo+*Ë\n\'µ+‹NŒ4¨â°u“û5?Ba(.ËßÁ|ö‹‚j§±ï€Ô\0Ÿ¡q«”z«4èÍÛu¨\rV‰³ì¦Vü˜Jx\\¹Ï²öB-Ôê’gÙwŞy\'I*èï¨î~¾ıÿ µ¹‘rÉ¨kl‡g_Ù\nomØKœ\n4¢AĞ¹_Ì„–{JÆ÷«“Jt¯ªLgÅì‘œƒ³	«CÓÕÕÕ0xP±÷·;;Ë0#|‰›ˆ2`í³\"aß…[GÈ~²(ŞÎ$pMm]ğÖæØ¯yi$Yí4÷²—Â%ó§ÂÓ;+gÙG*»cÕ‹Ãª— \\6¬ßv^´	ö(öáµì»–>E¯¤¶Æƒ®F†½¹)ì×Mª“WêTÏù	:.æ÷À=4Ö×G0fÖ å¹Œ]¢ıòkÙ‰ÜÉÇ_òÚt 6ì;,/‘#ß\0‚óŞE;aÏøØÙ“à¸¶òªŞ“?ü\niTp4 ¸û)Zš\ZàŞ/—véª¥½^^º-Ş\nÍ-Å}õzü50¾Ï‹İß¦½¨£ÃrIXÊFÙ‘T.ÉÖ?çôÓ(WvoŞBT2B£—Ùôåk`Ya,x*J\rğeVÏÍã½ëÚ†vy–İĞ’ï\nHç‘Á°xû ø…8Ë¾ü¤ÉpÉ°ı0¤Ó¾)ğä¾»Ö¯¤\\ı•ÀİOñÔOş+Ó%òêÄ\"êÅÍ°fı>qdNÌcnà$B@ÓÑà§ƒ®Üò²,”ÚË\nSIöl•îİ×vDËäˆÑÆUV-yM¦¡\0™¥^&Ï_5BşöÇm”ŠPÕqYœSw¸S>|VÛĞxøÌÏßÚ8¾÷èj€î.øØ™caRën’¸xèKTı•Àİ±iÙË°è>ûcåâ­-áw7@{ÍtâäCq»¯^ewšÖVR€T*jck°çgjwh·o1~âÄÂßßÆ¯45ö¯º	ÿlcBöËäîÜ•VuØŞÇŞ¸¯¶×µšËâY€V›º†Âsë:aÑÒğsfÀi°u%Ÿ©oZ*ö;¿ú.å*èÏ¨î~ˆ‡¾ıÿˆ*SO8nû«»áªÏıª\'ÿºP‘èo¯Ùàê¶+tóöÛbá˜f™¤\Z±-§_xåŠCS}òUŸ` \"YX% \r… ‰daî ë)=ÀG¡ò®nØQß*‚öa¼“gŞq‰k…»_SFVÃ-Çá­ÉÏ)p<õÃ¯@kÓ!ÊUĞ_Q	ÜıOİı_°{SüírqÇÕ+eøéÔ«?ı-¸ğãÿ#î\'Iİ3W\"¢;²(RÄlò%pâ‹Ä¹¼ÍÔ“Ú•§í!L›3—¨â°yµú6~(Ö¤‡!KµŸ¯î<Pí,Ë~†ÂQ¼\n¾§±\rÖîi†ú\\÷±U{·àeñGVCCc¼ÿÌI0½m—ägEksüúßşŒrôWTw?Bıíğâo¿G¹âğÎ÷Ÿw*åÆÏZ\0·|á‡pÒõŸ‡Á£ˆ{l!\Z Ë„–»QÆ÷«“ŠÚåZ6½–	ÙÂj«‡*ğµ_2DÑEbÅkKˆ*E\\ÆÁÚgD(¢j×„[GiÖì½í°¶¶Y¦Ó…Qß9xã¼,~óY3`ş‘Z¨êl%i>¬^ô8l^úå*è¨î~„_ùÎ²H‹bü”ãàæOÚÏ¥F1÷üáÖ/Ş“/ùÿà0Œ ®Eö]G1È™\\€vpIm]…Lu™Â9ÛÅ*uªçüD\"	:h§\'^½¿„†ªÔËä…à ıò+ZğØÇŸÜ\\··ö5µC—3ßZ7iæZº«añAğóß-…ùSFÃuÓ†µ$iéøõ¿~¶rÉ¼£¸û	Şxâ^Ø¼üÊ‡üÙßÃ°égÔç¾ëığ¾¿jÎø(4vûËR=ôòìh“ÏŠ‹z\rÌ9Kf…9Í‘ÄÏ‹x\rìÀnÿÓÇ¡ÑËòw6h? ,ï50ÕNcÁSQj€ÏPıAzR|×ÁüŸ)ÅYµ|í—/Ã©gœ·Ÿ:Æµ÷=ùƒ{vÀÓ?ş2å*èo¨î~€Ö¦xø;Å?væ¥×À‚KßM¹lx×íwÀÿñèšw4t#nÿ†/@FbŞËäéÁ•öÒ©zˆä=ºÓfLR”ut=fÒX¢ŠÃº7Ş”iZŒÊ‚àƒ\\Ø·`ƒB(Ö~!û>şÌæzq†BÓpZàtøÕ³õ‡Â÷[£\'Ï‚Í›7Ã7¾õm¸íÏ’Fqxù×ßƒİ*ïv÷GTw?À#ÿûw…_\":|$|à³ÿ@¹ü¸ù#Ÿë>eÿà´ƒóïæ÷á½¹,ç+,Yª,—:š¬œ£ÃùÉ\rcÈqfÎ™à“ÇbÀ Ø°ö-Ê¸ÂlMNF |8ø—[qŠ}J²Ì][:aƒØ)¯vùnãì<<ş÷‘Õ°Gì*î¿ÿ¸ûî{Ì§JoùÔçaüÔã$]$~ûoÅTP>*»±yùËğæ“¿¢\\q¸ñò2şïïæoázÀw¸uöl\0Ï;¾Ğeû[\' &½F)–MºLGŞ>DÚ’IªÛræ¥—R®8´4•÷ƒ5ñQ°=(ı26³0ÑŸ^ÃÁ{×ëö4ÃîCmâ;i&“pDì»ÖÂ›ëáÁ’¿àuÅWÜâ“÷U¢ŠCíÆUâÌ»ònwC%p÷!ğùo¿ò9Ê‡y.„w¾ÿ(W>0€ÿáŸÿ3¼ã¾	+œ[÷íë»g®D8AAİÌ»Ì{wS§HİàN„@b»t¸$;ã§ÿk`›W©WÃ²|k?a€rAÙ(«o¢0èı\"`ogØû›:d\0G$ôù¸;•û¹76Ã?ÿó?ÃŠ+¼[ã¤s.‚w~ ¸u¯ñì¿k·S®‚ş€JàîC¼tÿ÷ààŞ”+ïÿÌßU,ğ²Ü_ıÃÀ\rŸş/XÖµ\0–ÕÿyÍ\\HÚ	úÙ\nLh$î¦Ÿ•wlIZíÒclÄ6!?O8`õxLêj¦7­ğ¯¥!V¿¡>sZzü2vPFDpM¸“µßÑ}DYoÚw°€íEBÛv4cÀŞmö¶mÛáãÿ8IÃ¸ùS_€¡#FR®à»İ÷}©rÉ¼?¡¸ûµ›VÁ³÷$ÿÎv©¸áwÂq‘w¶‹ğ¿ù§ÿ‚Üùx¹åLxvÇhùĞL9(ç2yÒ¾1t’êrõu&o»,’Ûe%Ş*	:hçìË“ÏÀJEgÇ\0hjğæ43U©¯9£4‘,µ½Üƒ‹Ãí]°½¾UìúaŸ¤yK^ÿÉó¥la#GÁ\'şî¿)W¶,{	Ö.zŒrô5*»ğX<E>nòqğÎ÷©,	Àÿåß¿\nŸùâWáÅ¦Óà7k‡ACWÏ¾J–x©1¸—Ìö\Z˜íÀ¹~Òım7\0#MeYá¤v…Û››JTqØ½U]\r:J}ˆËòw6Ÿı¢ Úiì{€øn1‰õ‡;`óşùyRüU¾|¾‹¯umj*öêJØ.¿N<ë\"Ê‡ûÿı3•w»û	*»ğÊıßƒ-+^¦\\qø½¿ş/šáí¢üËÿùUøêwîÍC.‚»Ş¬‚‡{ş2º/øEyÎıb&,ç2¹å¹^\"âA@Ã©“·Ål\":DO=n:\ZXğÓä«^)Î7{ü2¶1ÂˆP„}ª¶ÎnØÓĞ[´ÈûØİá\'Ä}è€AğVıPù”øƒGà{î‘÷°Ë	Ø¿ÿw_í‘KæÏßUy·»? ¸{èüÏıô?)WÎ¸ä\Z˜· ø£ì<À‡Øşæo¾ß»ë—0ğøËá_o‚çw…ö#ƒI£@PôŠï®âAW#ÃŞÜöë&šf•::œŸ ã Qàâì+.\'ª8tw„Ú]ş¯a¹A2P¾ÜËØˆ‰àÁ¥ˆÆ¶.Øy°¶×·ºCq#Ø”\Z$Maë‘jx£¶\n¾üóWaèøğÀ&>%^ÆO=®úÀ§(W^ıíwaë²)WA_¡¸{÷ÿçŸõÈ;Ûû«â_)À?ó™ÏÀË¯,†S/¾	¾ôØAøñƒaOÛ(±C‹ï${ü50¾CM\ri›K\nÀ\nªßN<’Ê%™Ãú\'_ÚÏ´†°oW-QÉ~\\f{Ğ—¯åUÔŞÕ-¿¾åÀa™¶tä?»FìiO½Õßt¥˜·yòÃ)øvÑ›ãÆ?ø7ïÊ‡ß}ë‹DUĞW¨î^ÄÚ—‡·^ùåŠÃ{>ó}r‰<ğÒßâÅ‹áO?ÿ×ğZİ$øä·WÀ›uã ­»Š4²Ã\rœDh:\ZütĞ°\r?†\\gv¤+L%Ù³íqíúÚÈr™\\?ºÒO“¿ùÜó2Í5% €ó\">@ùÛ¯l`1üúhCK‡üP\n>pÖØÖ~:<øÀææÆ¡ğãçwÁïo„~ôã°uëV¸ë®»Ì‡Sz\Z¿÷·Å?¨¶gã*x®rÉ¼OQ	Ü½¼Dş»ïşåŠÃÜ3/„®}åú/ğÌâ;ÿû]ÄN^\0ø­×àG¯†]­£I#|‘,\rŞ2¸›¶ü¤€ªTT$ˆ±5XG\'w[ÃG›;ûÊâÏÔ¨N¼L^\nŠ¹Äl£HûxÙ÷\ZÏª·Õµ@]s‡¼—Gú|6v\r×w†ï<º\Z¶ÕwÃ7¿ùMùÀÙwŞ)¯Fõ&ğ\r“+{àİn¼×]y·»ïP	Ü½„çú8Ôïl´]\"Ïù*Ùß|¨ƒ›ŞóaøíÒføÄ7—Âs;FË_:J‡İY\'íBm¬ºL‰_’O¼Ln2å…(œ+”\"xı<ÃÙhgìÄâ¿M~`÷^¢âÆH’…UÒàP³QšH†Ú¯qáf;¶Áæv™Ï=]øtøöÃCá¾7à‡.…O?–.]&ï_ßzë­J©pÃü9Œ›RüçPñ)ó\nú•ÀİØ³i,~ øßÙ¾öãwöÈ‚ì-àeôÇ–,y›ü­Wá/îİ	+…®#®k¦]&OBŠØÂ³wO½¿-¥£ÊfiW4œ²àÑÜâŸ&_ñâ\"™†]@äAş†ìç«;‡;ºDî€[a_c4·ušÍ8²´¾®s(,¡³ëû»áÏÿï_BCC|ík_ëµËáiÀÛhï½ó)Wğİî¥ÿ‚rô&*»ğàWÿŒ¨â€ïl_\'÷±\0ÜÁıÇ|Y…ÿë¿~	Vì·ıãSp÷›ƒ`}S¶3Ëè~×¹ïÌ„–a€ñıê¤\rÉï…Ç‘-Ü8\0fã¶EÓ§¿ã2E¼L¾uã&Ê•ğ%n\"Ê€µÏˆµßİ}D>T†—¿ñ©ğıí*X~JÓ/Q\\¼2´¶~üxa-<ôò&çìº¨×¹ŠÆ—]gäü¥À,xü›[y·»P	Ü=<ÓŞ³yåŠÃ‡ÿ²ø¯®õàeÅŸıü—P__—¾ë&øÅÂmpÇ·–Ã}o\rƒÍ‡1ˆ‘;æ¤]n<èjdˆ¦°_7©N^©S=ç\'êHĞá¨ª®‚£ó?Ø—†r/“‡Pêeòr<ş¾us›:³Şy¨M^onï’%\" ÃÍ¶O­ï‚¯üüE¨7¾şõ¯Ë{×ıéì:„÷|îˆŸİyLï\nz•Àİƒ8´w;,üùW(W.{Ï\'an¿³İÓĞ¯”áÃl¯½ö\ZLœq2|ëğ—¿Ú\ro	u]£`àÀ ş\'À8ñ1z›\"„£ÃrÉXV4+Ìé¢qö%—U,–<õ$QÉÅÑ¸¬ØAq}`€“jé”˜Õ6´ÁÁ–hípo)ğùµT°\n/m\0ÿö³—aÇpøÃ?şŒ<¨ÄW¹úúŞu^Œ›z<\\÷É?§\\qXú»_Âæ¥/Q®‚ŞÀ\0áÈ=¸›y{ã¿º¶®|YîÈåŸØÁğTıcÒ}Dì|¤LüÉwFG>ê>şöç¯ôÛ×¿z\ZK—.…Ÿıì§ò÷ˆWœ{\"œ=}\0LªnÇÏ¶pwã¨6j<u0>Ò­ÆVÒR•æEl”ºÕÅ„LH¡‘/98?º\\\\GÃÚë8u±Ô-¯ÒÜù9¨¢h	p]UZo=P•\Zt‹\0õ“¯¨×†|Ró<\"Ãä2uÛVÀÏ¸cöY>&â²ˆëèêîÁú´‹€ï[«ywåxwwÚ¶áÍv®†íû[áé^…3Î8C^ş¾í¶ÛŠ³ê,øæŸŞ›–¾,»ã*SÑyMãÁ°ä\rP{!£#òZ†C-GRìŸ0=é8øô!#JxK¤‚Ü¨œq÷Ö½òlA»h|è/ğS†oÏ X°`¼¾nİ:À#¦œÿñ›ÕòığûÖ\r…‡ÇBuÕ@1	ïÁÃå¾Ü·C—,ÜMIp4Y9G‡ó}¶cPõ„0nâ7h„Ú­;‰êeºì»G.b³8ƒî††Ö.Ø\'Îª÷5uºZ;ñx–1öïYok‹Ä™õ¿şôexcc=ÜpÛäGR–-[&_ã:V‚6â¶?û\'¢ŠÃÁ=;à¥Êïv÷\Z*gÜ=€ÖæCğ­OmÍrg#,ÿÄŠ§ú“,gÜ\'œq!üÉW%¨\n¢À3ñGyzè!xõÕÅğŞ›Ş§Ï³F¶ÂÈ-RÏÈğ³ÒGğ,A23BÍ‡Ê L¦4èV‡RÅV2Í DQDK>ÙJÔ!ÚS‰áSŠ@úİx?LŸ=8Râº\"Ç¶ 2>øãŸCİ¾ı’ÆKˆ#ÊwË¸RÇ~¤ #™Î®#Ğ!&ÛºSÌ>£÷ËÎeQ¶‹†®!°³`Õ¦=°jÍ[pÓM7Âí·¿G^şîíw­û¿ûáWà‰ş§gw<oÖt)gÜÚ¥>ıı§aêÜÓPRA¢¸{\0O~ïoáµñõ/æÔÒ±1@Ø4Oà®>>ÿİ\'ê×¿z[¶l‘üÅ_€_şòWpÙ;.€“gM‚“\'‚ã‡¢ñÿº\0Şî>\"ƒ‚*+ƒ:¸Ì`Ş–F¾äàÜØ áêœh¿æ™€.×@úùçbçùZ\Z)q]‘c[P™„à§_ıº¤ JĞ<È0£2n\'ëerlşXgÔzB¢ıpó*çö_³ğ~5^ß}¨^\\²F\rW\\q¥Ö·u÷ª‹@KSüçÇß)Ï”q\ZĞëu€.\'pÏ:óbøä×îCI=ˆJà.ÛV¼÷üõí”cN-[ìR÷ÍŸşpé{zï\';%ÜÿığÒK‹àÙgŸ‡%K–À{n|Ì:fŒê‚‰UMJIº\nâ\"˜‹ñÆW…Ì™¹Ò yAÿëŒâË”Ó”\"Ò7Î1Õ#yJ¦ôÜSæÃå·\\«t8H‘ë+zë*“póšMğüÃH:X4Ï#2L.ËrÏ±	GºåYµ¼âvÀÀÇuy*ç+¾¿c(l?Øë·ï…U«ß‚K.¹Dê+¯¼RŞry»cã›/Áÿ|ö=r†pO¥t9ÿ®ÿ“‚‹ß÷‡(­ ‡P	ÜãŸ}\'{ı‹95şa¥èüLB{ÚìSàÎïÿó·#ğlü¹ç“ü™gƒƒëáòÏ‚9ÈGŠ@^­9€\rOşä\\‰¹À\0#/·£L‰i¾9šöéÍíàŸ¦)E ı?ú#3n¨±a@Š\\_äØÖT&áO¿öèhï´¬\Z<9.ã«ÁñRã‡¾¬Îª5²Ü—öi¸<u€8 umS7ìØ×/-~N?ıtqV}9\\uÕ;å\'wß—Àóâÿúgğúc÷Š9,.p×ÿçŞ%•Õz•À] ^øÙW`ÑÏ¿¢Z¢˜À}çw‡isOEÕ\n\nF4oÜ¸®¿úr˜=eÌ3\0&Õ´@5t¨ù£æçFÌ™˜@>êòºàË<Ê1§t–Y¤U\"ó–‡M3>¥ˆÁUUğ{_øI3¶)r}­ÓÕ@eñ¿åp7üò[ß’¬hĞFhGd˜dŠÆrºUŠ›\0”ï‡uQ\roé®‚ƒíƒ¡¶±ÖmÛ#Ï¨+:?ğ’ù¿¾ŸÇ9dt¹é“ßq-|ô_ïB\nz\0•À]íÙßşäyÒ«í€–¸ßqÛÀÍŸş{T« €t{ñÅE°|ù2xâ‰§à‚óÏ9ÓÇÃ”Ñ50yÀ4qV®B¸\0Î•%[œ_uf°÷ÏUpC\rsÖ.Š§Smô7ßsN£òrË@Ê¼ŒÖŠéjP#–¿¸ŞxI½ùàÜ|×€fõY²Ìê¦_ä9Ûî82uÖÀq6½¿±\r^[ºZpÈ@—½¯ºê*yé»¨KÃ’Ç~	÷Š3ï\"7ş}ô_~§\\zjUP0*» Üó—·Áv|ıKxµĞò÷ØÉÓáÏ¾óÄÛúõ¯ş\0<#_¾|9¬?m¹äõ×á¼sÏ–Á|ìğj8~ô\0YÕ#¶É¹C¨9ÄÎ«\nØ’L!ï§GòÍûØŸR!*¤Ë*On=Êƒá_Â¯ïY]dÛe#\\‰(/KĞF$îC]Càpç@8p¸¶ïm„íµûaÛ¶mpÉ%ï€³Î:Î>û¤+÷¨‹Åw>sl^¦Şí.*pr|ö‡ÏˆıWå’yÑ¨î°ü©_ÀÃÿı9éĞ¸±Z^àş½¿ÿœúk¥NıÌñÌ|×mğæ²åğÔSOÃØ±càü³Nƒ1#†À˜aU\" „êİ0~ğašSIãEæ•$ªƒ8~öl¸âö›TF@Ë\rXYâÉ­B¹n_üæû?\"×õ”Bºg‚ˆ#ÛÙ6Şíİd€ŞßĞ-mğâ«KäÓŞgy&\\qùepÂì9• İK¨¯İ_zÿyÒ#‹\nÜH_üŞOÁMŸıgAUP$*»LÈw¶?q.´n”; ¥î“/~7üş?ü@Ê+8:€—Ùõ=ó¦ÆCğæ›Ëàõ7Ş€C‡Ál€çÌ˜SÆıÿíİ`Eğ—F\n	E¤— M¥	\"Hø@Q¤ƒ(½*RBoD	)HP@z¯Ò¥—(*H	Ò¥I½¥|3³s— d/3$w÷ÿéŞÎ›İ\\\n·÷æfgvıÉÇÓ²úó¤N”Åëy‘1ÅËxmD™-ïµ¦™}emâv+¾SâJ’uâñ	ØÎ›–¬IrS‘Ä}ŸğU¼Š¿<Ùô¤ç·$î;ñéèvœ;İzàF·îÇÓ»éúí{tşÒ5ñ	:00P,<Ag~.‹5A£»;õl9–¶°EeâæK÷¨-”«0æv«„ÄBkÂ»Óá-‹Å«›¿ ùCâÔ¾Äíí@ıæ}.r\'Â“¹eíÉŞ\0·íÜÍş±ãië6£_™«pş<KÙŒw_o\Z5¤Û/qî¶|É$’‡¯\\I²N<>.%ÔŸ\'Ş¤&é~|•ùêN‚İõñ}öiù/öiY”cèÊŸ7ÈÍÃ‹=Æ\Z*7Ä\'ç%Š“»»G’äÌ3>A§]_´©BWOÇˆ÷2U‰;G¡bÔsÆVVU¸SàÜá½4ÿ“÷@aâ®İqU¬9Û®„w»ÿóÏ?báeşÊ)SªÕ¨şÅßç×a öã¯›¸»ÆUÎÆ‹(öÎ5±6uÆãã~:t•fÎY.Ê×nŞ£»÷Œçæøy7~½XæĞ‘_D¶àÉ¸$KÆn,s¥^)A™2ga/}71Š›ã\rgº<¨«9s`/MïYŸ¿)KÜ|©Óu8UjŒ¹İª qÛ‰w‘Gu}›®ÿ~Ñ¨P”¸ó—,OÁc—\0{ğà9RFÿh‘„]Ó7Rô²iJw:¿Œ2keÎ‘—ERHÜvÚ9í^`sËNE‰»Ûä”³ sÏÙ>ûóÚ¿a1ıqé<M±ñD/”ª@™ØAızí&ôâ«ä\0ğ,İ»uö­šE›£ÂèAl,ÅÅ»Qœ|Ÿòr\'òóŒ7ï1›¸ùû[RAÔi.‡ª·®9BÓ»V-Q+‰»JËªÒ*Ä¨tB—O¡M_\r÷îåo<aÇ²ß›¯ãäšÇ…JQÓa”¯.:ğ¬l›5†¾_Iwoİ”Ç\"¿;.Ù:V¬Ëû³äÑ;ŞxŸcu|m¼¯É…—mc¶ˆ&Ì‡#gRqÌíN1$n;Ìë÷¾8¿­2qgÈš—ºOŞD>N: mÿúÅ´~Ò\0Š»{]üŞÿ•¸yßË/µ2^«Œép\0:İeŸ²„¶¦ó‡ö’»›qµÆKÜ–z¢~±ìÍË\\âöNŸB—ı€¹İ)”Œ»ƒ­}_GŠ‰¨Ö°o„Ó&íK\'chÙètïvâ@§§¹ÃZı‘ƒ{ÒÙã–ë¾€üªi¿4÷vë¡]¹í)£äãï£lN1‚]¸MàÒø¹mÕJWmDJÉÈ¹ğk!Oîf¹[š9<yíÕFF\0 \Z¿/÷ÑİddÎu–¼o²Å¬]K§Ñ©ê?ü¸$nÖŒëF÷M|jLŸôT»Ã09Ÿ¨OZ›ú¤ı¨k—/Ò¶ÕKd\0ªÚ¹6Í\'#û\\¾cL\r4ëëñe	ìÄLÇ£×Ó‰hûZ¦ÿ¥VÇaNÛE¾lü :}À¸‰EJìÛŠ[š¨ôçå4ÿ³2²ßÃx¢{±æ?u_:CĞen7$îdà]ä›§„ÊHü%‚¨tÕÆ2r.Ñk—ĞöÅÓe”2û¶#q¨rçæ\rŠì×FœÆRáúó‰›ãİô±˜‡Ä;çI¼ĞŠB\rúDÈ’s9\"†–D’\0¤%‹Ù±yñ$¿5jê[0¢»,HÜOqõôÚ÷õT©S¹EeÊî|Wâ­ù‰}ÛŠ¹ \0¶lZ8ö®]*£Ôwê@4}¿v±Œ ¹¸Ÿbõ¸n²¤NEé­–½eä\\¦íE^Vß;\0)óËOÑ´ bˆŒÒ•_RÖmï*¸ÿÃ÷+#éêõóˆk;ç(òe‘á´Ç&©“5gY\0{Ü¾yƒÂ{·•‘Z¾ü+öãI{9F™›‚Äı/ş¹zvÌ“‘:¯×kGùpÎö¾miùT=çìË½]]–\0ÀCƒ‹ë\"èŞ+e‰›Û·n	Ü¹İÉ…Äı/Víª|Î6¿Ü_å–}dä<øÕÍ&Öwõ:-p‹S\0{MBçNèŒ–Å;<ìTş˜¹Ã{ Ë<™¸ŸàøŞutîúÖ_½^ãÉ‡%ogÂ»à&\rê¥­5ß°CeË…[Øcûê%´}ÁhüŸY}ãd”r]¹HÛ©ìŒ¸Áok·j¬úi%‚è¥ ç»aÆ¬°AtVSk¾LåêÔ¨£sâĞ÷„M\ZÜKFêÕoÖBÙ§m‹uQãèâIÜŸài¸±cn˜–.òw{}!#ç±nşTÚ±FÏåHó)J‡Œ—\0˜qçæu\ZÛ³µŒÔAµ;†R¦ìê.‹À@µ§Aâ¶qöàú~¥ú®š7›÷qº9ÛGÜC³Çè¹ÈŠ¯öÆ0üœóR°\0ºñ¤Í¯ó¯CÅ:éºÉÇ?#½÷ÉY«ÎÉÑ´uÑ4Á“ qÛØ0YıeM³¿PŒÊÕk/#çpíÒy\Z×ã©×,d(ûÄ]LF\0`Æœ°PúåG=#´ó.JÍC§³æ/UJUo\"#u¾™>V\\O‰[Ú>\'LËœíº=¯‹<¼G+º£iôg•&íèuÔ¿\0¸‚«Ğ†ù‘2R‹÷„u;ó±°š]‡+tËG—ã²Éÿ‰›ùçÊÚ1Wı}¶Ë¾Û²p®O‘:Ó¹ãGd¤VáÒAÔÄ¦5\0ÉwîØašûy©×)l=ŸóñS~¼Ë¼f·á2RçàÎôóõwdtHÜÌ×a]eIŒÙòP¥æÎ5g{çªù´kõB©Å[óÃfÉ\0ÌàƒÑ\"tÒÖÖ ç0*òj=®t¦”ÿ•ßn¯%áƒÄı )—OÜ?o\\Hg5ÌÙ®Ú^}÷Qj:wìMeoºtŸ´‚|1\rÀ.‘¡è¼¦°•jĞ[M>N§Á§_Ê’:^¹Hk¦á¾İréÄÍçloøJı€´\"¯× \"åkÊÈññÖüÈôÍAoúå.ŒÁh\0öXñÕúiÛZ©•«P1j> yãt2åÈKo·VßË¸eñtºps»m¹tâ^Ö•îi˜³]ÇÉælGtã×9ÖÓ]õZÍÆT®£Øã§-khåW#e¤ï1lÊ\ZÕ¾şeÍÓ½İº/ådÉ^µ™C{Èp.›¸ùœíc{×ËHJÍú°|ò_èiİ¼Ñ}éØ»d¤?À›ôWß½à\nşøíM\rÕ7Õ´1;6s..£ä«İí3YRçÂÉ£´zÚ8K&nŞE¾òsõÒò¢²õ‚eäøv}=‡6Î›(#µxk¾ÕÈÙ2\03îÜü‡\"º5§±tà]ŞÅ*Ùwºï…R¨BCõ\rŠÍ§Ñ˜Û-¸dâ^)nÛ©Ú;Áê§D¤–sÇÒüÑúFÅ71›2çÀÍC\0ì1oTo:üŒÔâ£Ã«|ÔWFöy§M_-s»gí)#×ær‰ûò©#´múûló©_Ù˜ïVJ‹xk~|·ÚZó5º­r\00oÃœ/i×ª¹2R+cö<Ôì³”OËäs»i8\rv|4íß¹İ.—¸×MR>g»¬]Ö4òÓ¶ôÇ¥ó2Rë•jM¨|ƒ2\03~Ù·ƒæ®§\'LF>G$]ŠVªI44Ğ£Ø§nWŸÛíR‰{ïò)tö ú9ÛuB&8Í€´“†Ñş­«e¤V‚Å¨zõW\0\\¥\'L—\Z]‡SBj{\rù§n]æ_Ouí¹İ.“¸ÿ¾r¶Îú\\Fê”¨Ò„K8G·ïO[VÑÊIzÎÓóƒ·ş\'ì VÔšp5#>¨¢íôUPÃöâêgªñq,UÛ¤ì|ù“l^4ı-#×ã2‰{İÄşZælWíàÒø`´©ıÛÊH½†Ÿ~A9·æ\\?6u\rFãÓ2kwÕ×V±Q°¸‹jÓ\\x šK$î£»×Ñ/{ÔÏÙ®\ZÌ/kêøŸ yÜÔOÛhkÍWı¨·8ß\0æíZ9[LÍÔÁÇ?uør…ŒôiÒ_ıE©ş¼|‘VNuÍ¹İNŸ¸ùœíµÔHËW¢•|G}×Rj˜;*D[k¾x¥\ZT­sİlàYá=aóF‡ÈH½ÎV˜º2š½ø…\\*5R?€÷ë©áôÇ%×›Ûíô‰ûÛ™Ÿk™³ınˆs\\ñkÃœ/´µæŸË‘\'Ù×9€¤Ä`´®õµõ„µÿLïP•5à3³÷Õ\"‡ô’%×áÔ‰ûÒ©Ã´gÙ©S©EÊ˜İñ/\"¦–Œî-#µ|ı(8l¦¸]\'\0˜Á’ö—ÎÉH­òµ\ZÑëµŸí=ø\'ûzİÕ	âƒÔv®Y\"#×àÔ‰{é¨.²¤NöÅXâV?JòYûã·³âA—Æ½†QÜñÀ.óF…Ğ±vÊH­¼…‹R#v|¦†â•jŠÓgªÍëZ÷ívÚÄÍ»ÈùUÒT«\ZìóyÒÖÕ÷NÓ¶T»±Œ\0À>-sã\\=§âxOX—13Rµ\'ŒßqŒŠSéÎ­›9ÄuF™;eâæs¶w/™,#uÊ½L%ÿ\'#ÇùéGÚ£½ôjyj2TF\0`Æ¹c?ÓÔşmd¤^–´³äLİÓ|¼Ë¼††«?mßH¿¸ÈÜn§LÜKFvÖ2g»RKÇï\"×9µÄµæ{’\0˜Á£Ejœ–Ù*d0½T&HF©ë&ÁT°´úŸeÊ`×¸ªÓ%î˜]kéÌÏ{d¤NİŞYSİ­ùAS—’_\0£ØCô„;(#µ^«\\j4o\'£´áıêªıqù\"­[0MFÎË©÷İ[×iñˆÎ2R§HP\rz1È±/ Â[ó]ô\rFë2d¾ˆÁh\0öX1q(íß¢çù‹¥ÎCÂe”vä.\\\\K—ùòÈp:{<FFÎÉ©÷æ¨ÑZºÈ«u!#ÇÅ“¶®©%•ë6¢·Şm$#\00ƒOËä7÷ÑŸ¾ê:,œÒ§Ñ°\Zmûˆë=¨6gì`YrNN“¸OØM»–ªŸ³ıfË¾”ÉÁçlÏB¿ü°CFj²Ö|—a2\03xcú‹n\Z{Â†§ÒxOX\ri:úS4­›ï¼]æN“¸iè\"çs¶Ë½ïØ÷Ş³jmš;AFjùùg ÇÏ”\0˜ÁO_}Ù]ß´ÌZ-ÚS¹·ÔÏ™V­Ğ«¨\\-õÓG—NG×œôr¨N‘¸7F¦¿¯h¸¬iï‰²ä˜.?HÃô\\ë;~eÍåøWH\r‹Ãú°cTÏ´Ì—_«@öM‹¬Ø£AÏáÊç–ó¹İ³Æ8g—¹Ã\'î¿.Ÿ§M3Ôßg»ÜûÁ”£ ãŞ†ò.kÅÏÔ^ØÓáƒ¾ŸQQöæ\0\0æmY0‘ö®™+#µÏ™—ú°Fµ#áI»AOõ\r¶o¤}Û6ÈÈy8|â^øY\'YR\'c¶¼ôfËeä˜fiOOèiÍ¿ñnSªÙÒ±O!\0¤~\\.«çšüôUï/æ’_€ãM]-_»	Ö0·›ê¾íds»:qï[»€NP?g»^ß	äónu§ËºiŸÑÁkd¤V¾‹ÓıFÊ\0Ìà=aã;T“‘z­Ø±ÈQGÕràÊ»Ì¯]¾HK¦8×}»İYv(¼xXıtÿÖ\rrsscûeX½X‹²QÁëÜåv#NÜ×ˆBâv¢ü¯$v[ÇJ„nÄÿhâklˆ=$şAıø_\'ğXTëxQ6Äó¹Ÿ±æÏ–ÀöIü&–ı-ÿb	l[‚øOÆl¹÷÷úíØË0..ââã)6ÖXsÆ³²5ûáùóğßAÄb‹\r¶Aün¼mÇ¶±µ»‡7å,ú\Z¥ó_Ë¿/üøóYş.ü{ˆ¯¶Æro5²ïÀY\'Yp—uü‘×ñ˜Wğ•mÙò|bmY‰EëÔ&fÿõ¢ Ërñ}y=ãniÖòßUü¢ò¯-q~èÈ¢¬ã•¶õFlYäWeñ„¢RÔ‰/å.É×³G#u¢Ö6û\ZuFl©³…$_Ã‹rQgSÏñ|›µÂˆÅ~Æÿ?É×›&ÿ¾IXçIÛ“¬YşAóh½q?Še›\\‹Õ#u6Ûø±˜¸?nxùñúNï¥û·o°c“ŸüØŒ‹Ç)ÿó=ø÷æÇÍãlê¬ÛM~œfÎ–›ò).ö´¾æÅÊxn#N°[bŒz^¶Ô‰µØb»%îc}ïïAü÷4~vîI±í{e›u»ÍspNÆˆOÈü§¶îkY\')Ûùsó˜ãkKüè×ŒY¼)Í°O.‡MÜQıšÓ‘]ëäÊxs7Êrá‘¬3›¸E™±Qi©²Ôñ?šu?\"d‰P›5_xl³¶&b¶ˆ-¶±E¬ù³ÉÄ-ë­ûËØ6qó:·„8òxøx#Ğ‘¸zøS¬›§õû%®ùOËşã»±E$DF$nYÇ«,Û-‹%q‹å‘íÖ7Xc¹<úœ‰Ûø¾òÉZÏöóÙìc‰-ÛòêÜùoÈğßQş²â?Qæ¡Qæu–ø©õÖçãeK½ŒÅÆÄ²±]–å>¢ÖXñÿE]âş²>!Ş\Z‹}ñÚ‘uÆ>ìµe-ÛÖó}å÷`–Xl“±±ˆHî÷8öç³ztş÷}”åy°Éúõ‰›°ÓyÒ“\n–z¹æÿîl%~ë×ğ5[ØÿÆ1É=a?NEµQ— ¿Ş¶>£÷}JçşĞ8.\'nr÷¢t>şÆë˜oáÕ|{uFœ@¶Û,k¾,‹¯Ûl¿Îˆ-Û¬ÉR¼ñßÓˆ­eÛ˜-– \"æÛøbçHú~È×¬^¬ù>r¤ll·ş,¢.1~ôk‹£qK6±Èñ‰†™£9¹7ŞµVFÀñ—~ºø›âEªC¼‡/Å¹{Ê\0ÌHïK¾e¤Ë¬^>ée\0ÿæì‰£´xJÚ»‚œ=.qósDó‡w”XøĞ]ÖªdÍxXkş¡»·\0ÀŒt	”ÑçŒÔóô`Æ\'ZøokæM£ß`n·Ã%îm‹¿¢¿4ÌÙvd>n÷‰Ø¢ï\"÷ò—\0˜ÁÇI<ŸşèÓÁ#%¸{È†Ïíşr`/9.‡JÜüÓöúé£eœ—[,y$Ü•‘Zü<]¬Wö–ƒÖ<€=²Ä’§»1¾D5wt”àé+#H®˜£é[™C%îïÖÎ—%àÜÜâÉÇ]OÒØ\'í87´æì‘%=;>½ôœ¾rwó$JÇ»ÈÁ[W-–%ÇäP‰ûäO»d	¸\0Ï»ÚºàÜYKş¡‡Œ\0Ào¢Œ~z>ió±ï	Ş™äŒ°Çáğ‰û™ÑuùNGäïuŸ}âÖÔšw÷¤^hÍØ#QöŒz’6—.#KÚè	K	~QG†&›òñäçÍbe¤ŒëûœŒ\0Àww7Ê™™¯e…bn^é)Ş3<\\·ƒñtO ¿tšæƒ2	¾™)/\0»äzÎ¼Ù\'nø`´XOô„ƒ%îÜ…KÈ’kâW-Ê q>¨‡OŠw×ô®àä²eò¤€ôzÆœ¸¹{ÒÃtì£<(Qì5õ73y–*q)SI–\\S&¿‡ì\0ÖóÆàéåÃZó˜Z`ô¾î”-³¦i“üô•WFLËT¨ü[ÕeÉ19Tâ.ùfz.G^¹–¾qäé¡)i{xQœ·Ú;ò\0¸Štî”?§¾ªxÏŒè	SÈÏ?€Ş®×DFÉáNf¶4E–\\‡ŸOùxkê‚ss£ßLóÚ\0¦yx¸QşÜŞl-+TóğÃ´LÅšvêMéûƒŠÃ½[~µ\"µğ•ŒœŸû”­ë¼çé—™âùÅ\0À´<ÙÓ±†µ¦.lö)ûW&€\noÕmDu[¶—‘ãrÈY¯×nAÍC?yóÁh™YÃßVOoß\0ŠÅÔ\0»dËâMY2ëiôº¹yĞ}¯,2j·hKİ†GÈÈ±9lÿh9–¼.?Dek5“5Î\'KÚš>§óò¦Øt¸y€=ü|<)_n]^7–´ŸÃé+EÊV®NC§/£6}‡Ê\ZÇç–ÀïˆïNØM—N¦{üêjìªqK|ƒåFğ–ëK½Åã$5Ö}ø-é¾ì\'Yş¸Æ_9ñ¥–›¼[ˆîóµ|¸v:š-ßS\\\\<ÅÇ\'P\\,[ó›îÇó5¿?¯7Êâfü|±&£­Å\rûùÍúc5Ç¿Kæl¹èÆÉÃÛEnû\n°|KÕn“	ì?ñw2şOò§°şíe9Éšÿg-¶ë$ekÛzQ´Öñgd?‹Ü`ÔóïaüÄF½óbbÌÙ>bÍëÅ±Ÿ•,òßÕZ~BQ4bK•eÇ$K›À(²¯J²]<Ú”ùÚvëÖÄí6IêøÚRàX™ÿŒrW!IYl%Ëÿr-k•Ë²)òï›„åy°)åö¤r;[ñ’øı’üŒI¿>>ö]90bÜÇ¤õxÇ[Øñ&Y^Çc^/E¾Èã2­ù±)·Å³o*¾7[ÊTmL¹Š–e±ñ‰×´øÎò\'1ªëd,Êr_ËŸXo<<}»Må¸<N,[ÿÙYÁR¶®eÁ¶ŞòşÆ‰zö`»]¬e¯Œ\"ûimê¬kö`[öáDl©h™\nøb1‡?Ÿı$N“¸É©7Òú	Á”`yCP˜¸Ód¤şs¶RàK¥D\0æÌï_“şºxÔ8Å\"Gqü±%‰»â{P‡Q3oğ/Ğ“Æ\\¿v‘6Né-#õ‚Ù›’6€}¶ÎJ×Îÿ\"#µò½ô\n’6$w\Zrïö\rZ1¦=İ¿sSÖ¨U¿Ë *S¥Œ\0ÀŒCÛ—Òşõ3d¤–_@F\n³UF\0ÿ\r‰;\rÙ4c(ı~NOkşå²oRı®ƒe\0f\\ùõ(};Sßà&´ı0õ’‰;ˆ^ÅZôËd¤Öó¹©×¤2\03xOØ¢Qí´õ„µødN_)HÜiÀå3GiCÔ0©åëŸ‘zLXÖ<€æhO×¯ı&#µşWïªşA$w*»ËZóÓ>m,#õš}<Nz\0ó¾Ag|\'#µò)IÍû“@ò!q§²)7¦{·õtÁUiŞU´èÀ¼#{7²Ä=^Fjñ°.ã—¡\'ì‚ÄŠŒéM—ÏèŒ–‡µæ›ô+#\00ã·ÓGiáX}Ó2;…/¡,¹e`w*ùnÃRúa“Áh¼5¹IF\0`Æİ[7h^Xˆ¶°ZíC©ÈkoÈÀ<$îTpáT-Ÿ¤ojI÷)›È7 £Œ\0ÀŒÙ£{³OÜzzÂJ¼Q‡j€}¸Ÿ±;¬5?¹;º«©5ß|@¤è&\0ó¾]\ZE‡öèé­ÊU¨µ8MF\0öCâ~Æ&~Òş¼ªgjIÙš-éõÚ­d\0f;M‹\'èé	óñÏ@ÍYÒFO¨€ÄıÍ?„ÿ¬gj	oÍ¿×sŒŒ\0ÀŒ?._¤/Y£Z—zİÇPîÂè	5¸Ÿ‘wl¤MKô\\çØ\'}j=r‘”\0æÜ¹yƒ\">nKwoé9}U±ag*[«¥Œ\0R‰û8{\"†\"‡õ’‘zŒXD™s`j	€=f‡¡ó\'ÊH­^©Hu»…É@\r$nÍn³Öü¤!!tGSk¾VçQT T%€Û×,¥ß,•‘Z™²ç¥VÃÊ@$nÍ&êEçNèiÍ¿T¡UhĞYF\0`Æ¯ÇcD£Z—ÃN_HÜ\Z-šNû¶o”‘Z9\n§ú}&Ë\0Ìà=a¡m\ZÊH½÷zO¤œKÈ@-$nMb~Œ¦ESÂe¤–wúìaZó\0v\ZĞ¶¡¶ÓW¯¼Ó”JWk.#\0õ¸5¸véîÕFFêÕë5‘r 5`—™cÓYM§¯²¿PL4ªtBâVŒO-	ëİV[k¾\\İ`z1¨–Œ\0ÀŒík–ĞÚQ2RËÛ/µ\ZµZF\0ú q+6{Ü`mƒÑò«@UÛ\0˜qîDŒ8>ui:›|Òãôè‡Ä­Ğ†…ÓµM-É5Õï?KF\0`ï	ïÛN[OX•6Ã(_ñÿÉ@/$nEÎ³Öü¼=×9öö úıf¡5`§ñ·—5Õ¡XåÆôZ`è‡Ä­\0¿ã×¨Îd¤Ş[£l/“\0˜±jz8Û¯çY‹ÒÛ­‡ÉàÙ@âV Œ%m]×9.úF#Ñ¢\0óìÜH«¢\"d¤ï	«×g†˜	ğ,!q§Ğ¬!tá”ÁhÏç+JÕ;éyÓpvNÆĞÌúîP­CeÈšWF\0Ïw\n|·~)E³E‡t¾Ô`À€woİ Ù#C´õ„•{¿\'|­ºŒ\0-$n;ıv*†–~©ojIışKÄ¼P\00oî¨^tQSOXÁ2Uéõ÷õ}’x\Z$n;ğÖü´Ğvt÷¶Ö|åVƒ(k¾¢2\03v,›N‡vo’‘ZY_¦jÆÉ u qÛaÆÀ¶ô×U=SKŠ¿Ù€^­ÙVF\0`ÆéƒÑ´r’¾i™5;…£\'R·I«\'\rfoz¦–dÏÿ2½ó¡¾îw\0gö÷Õ¢Q­Ë;\r¦lè	ƒÔ‡ÄmBÌ\r´k…ëû°Ö|£~Ó1µÀ÷ø`´Amé¦ÓW¯×iC%+ë»V€HÜÉtùt-£o@J³şÓ)S¶<2\03¾™<˜.ŸÑ3-ñòT£-zÂ í@âN†{·oĞò±=µµæ«4ï)Ş\0À¼›—ĞşÍz¦efÎ–›Z„N“@Ú€Ä+ÇõÔÖš/T%nL-°Ç•31´bœ¾ã§Õ éäƒÓWÆ q?ÅùãèØwe¤V®/SãŞ˜Z`Ş6«_©×´÷XvŒb0\Z¤=HÜÿáÜá½´sÄê›>€šÎÖhÍØcéğÖtŸ%oÊUkHe«a0\Z¤MHÜÿâúÕ´lÄG2R¯U¿q”» Zó\0öØ<u ;-#µò|™Z~Œ0H»¸ŸàŞíë´ì3}­ù*\rÛPÉŠ¸Î1€=}»ˆ~X­gÀï	ë5÷€´\r‰û	6G¤ß‘‘Z/–*O»\r‘\0˜qõÌñi[—.#§“¯?N_AÚ†ÄıˆC›Ñá-‹e¤Öó9rS×ÑÓe\0fğ°¥Ã>ĞÖÖ¬û`z±tŒ\0Ò.$nWO¡5İe¤–Ÿ\0õø|:[£5`5ãºÑõßõÜ# RíFT­	î\0‰[ºwë:Íù¸ŒÔkÕk(å+\\LF\0`Æ¹at\"z½ŒÔ\n,\\”ZöÄé+pHÜÒì>õ´uÁ½Y§½Á\00ïØu´sŞ©Å{Âz‹\"¿\0ô„ã@âf6|JWÏèŒ–¿HQê2$\\F\0`Æ•ÓGèë1]e¤^—¡”5\'î\0Åå÷é»‘2R‹·æ‡M_&#\00ƒŸ¾ZÖE[OXÓ!T®2¦e‚ãqéÄ}ùÔaZ?)TFê˜±ŒÒ£À.k\'õgŸ¸õô„ñ„İ´SˆŒ\0‹Ë&î»¬5?/´•¸Ş±õB/¼ˆÁh\0öØ³t2Ø¸HFjñ®ñîÃ#dàx\\6qÏéß’ş¹zAFjñÁhuZ´“\0˜qúÀnúf¢0~úª_xzÂÀ¡¹dâŞ4c4ùyŒÔ\n,R”Z÷*#\00ã¯Ëçiö§-d¤Ş‡½‡R~ô„ƒs¹Ä}xç7,q.#µÄÔ’±hÍØkF¿æÚN_ÕhÚ–*×m,#\0Çår‰{åøOdI½ƒ#(k®¼2\03¾_;Ÿ.:\"#µ^zµ<µ\nÁEVÀ9¸Tâşî›ùô×=çµßk×‹Ê¼‰©%\0öZ?}”,©åë@=Ã¢dàø\\*qÚñ,©UºR5–¸1µÀ^OÒÖ¨î÷ÕR\\\rœŠK%nşæ ZBE©Í@L-H‰“ûwË’Z…†ãàt\\*q«nÑó›î·fo¸ã@ÊÜ½y]–Ô	ªÙˆ*ÔÂ=Àù¸Üà4•\ZuJyÑšHsr*JöÇ=À9¹TâÎ]¸„,¥\\å†m©<kÑ@Êå)¢îØôI@Á#0\rœ—K%nUo_)Oõ»bj	€*¹‹””¥”k÷YeÉ;~ór©Ä]¾NÊ¯È”9{j3­y\0•²äÌG…JW”‘ıêuL…JÉÀ9¹Tâ.üj¥¿9´E¾Œ \\ÍvŸÊ’}ÊTkDo4À=Àù¹Üà´æ&“‰·QßpÊUƒÑ\0t(üjEz£qG™“³@QªÛ	÷\0×àr‰û¹œù¨ó„oÈ\'½¹äİ wkÑã:Ç\0:½×s4•©ÙLFÉ“ƒ%íöc—¡\'\\†[#Ë.åï+çiù¨®tşÈ^rwc-öàÎš1nlíæf,	lñ>/UF/Õ_	\0ºñûqo›FïŞLr|²S›|OnTüí&TƒŸöö¢8\"—MÜ¿ÜC7.¤«gĞµ³1\"qgÊ—²,AE‚jRÉ*Mä\0ğ,İ»u°cóøŞuôû¯1,‰ß	;°äÿ({âT¶^°8V\\Ñÿ¥‡Z¯‘Å\0\0\0\0IEND®B`‚',0),(1170,260,1,1,'','index.html','text/html','<!DOCTYPE html>\n<html>\n<head>\n    <title>Popravljanje jeza</title>\n        <meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">\n    <script src=\"https://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js\"></script>\n    <script type=\"text/javascript\">\n        /* <![CDATA[ */\n        var task = {\n            load: function (randomSeed, mode) { task.randomizeAnswers(randomSeed);  },\n            unload: function () { return true; },\n            getAnswer: function () {\n                var answer = jQuery(\"input[name=\'answer\']:checked\");\n                if (answer.length > 0) { return jQuery(answer[0]).val(); }\n                else { return \'\'; }\n            },\n            reloadAnswer: function (answer) {\n                if (answer) {\n                    jQuery(\"input[name=\'answer\']\").each(function () {\n                        if (jQuery(this).val() === answer) {\n                            jQuery(this).prop(\'checked\', true);\n                        }}); }\n                else { jQuery(\"input[name=\'answer\']\").prop(\'checked\', false); }\n            },\n            displayMessage: function (type, html, isOptional) {\n                if (type === \'validate\') {\n                } else if (type === \'cancel\') {\n                    if (confirm(\'Ali Å¾elite poenostaviti odgovore?\')) {\n                        taskReloadAnswer(\'\');\n                    }\n                } else if (type === \'saved\') {}\n                else if (type === \'changed\') {}\n                else if (type === \'deleted\') {}\n            },\n            randomizeAnswers: function (seed) { task.shuffle(\"answers\", seed); },\n            shuffle: function (tblName, seed) {\n                var list = jQuery(\"#\" + tblName + \" > .answer\");\n                jQuery(\"#\" + tblName + \" > .answer\").remove();\n                var rand = new task.RandomNumberGenerator(seed);\n                for (var j, x, i = list.length; i>0; i--) {\n                    j = parseInt(rand.next() * i);\n                    if (j < 0) j = 0;\n                    if (j >= i) j =i-1;\n                    x = list[i-1]; list[i-1] = list[j]; list[j] = x\n                }\n                var answers = $(\"#\" + tblName);\n                for (i = 0; i < list.length; i++) {\n                    answers.append(list[i]);\n                }\n            },\n            nextRandomNumber: function () {\n                var hi = this.seed / this.Q;\n                var lo = this.seed % this.Q;\n                var test = this.A * lo - this.R * hi;\n                if (test > 0) {\n                    this.seed = test;\n                } else {\n                    this.seed = test + this.M;\n                }\n                return (this.seed * this.oneOverM);\n            },\n            RandomNumberGenerator: function (s) {\n                var d = new Date();\n                this.seed = s;\n                this.A = 48271;\n                this.M = 2147483647;\n                this.Q = this.M / this.A;\n                this.R = this.M % this.A;\n                this.oneOverM = 1.0 / this.M;\n                this.next = task.nextRandomNumber;\n                return this;\n            }\n        };\n        /* ]]> */\n    </script>\n    <style type=\"text/css\">\n        @import url(https://fonts.googleapis.com/css?family=Lato);\n\n        body {\n            font-size: 15px;\n            line-height: 21px;\n            font-family: Lato, Helvetica;\n        }\n\n        ul {\n            list-style-type: disc;\n        }\n\n        label {\n            padding-left: 10px;\n        }\n\n        .answer{\n            background: whitesmoke;\n            border-radius: 10px;\n            margin-bottom: 20px;\n            padding: 20px;\n            border: grey 1px solid;\n        }\n\n        img.centered-image {\n            display: block;\n            margin-left: auto;\n            margin-right: auto;\n            }\n\n        div.answer, div.answer input, div.answer img {\n            vertical-align: middle;\n        }\n\n        div.answer {\n            margin-right: 15px;\n        }\n    </style>\n\n</head>\n<body>\n<div>\n<p>Poplave so odplavile enega od hlodov jeza nad Bobrovim logom in bober Miha\n   ga mora popraviti. Bomo zmogli? (Bomo, da!)</p>\n\n<p>ManjkajoÄi hlod je dolg 387 cm. Miha ima na razpolago hlode in odrezke\n   naslednjih dolÅ¾in:</p>\n\n<p style=\"text-align: center\">1 cm, 2 cm, 5 cm, 10 cm, 11 cm, 20 cm, 27 cm,\n                              30 cm, 37 cm, 50 cm, 51 cm, 100 cm, 117 cm, 200 cm.</p>\n<p>ManjkajoÄi hlod Å¾eli sestaviti iz Äim manj kosov, da bo tako trdnejÅ¡i.\n   Koliko kosov mora uporabiti?</p>\n\n</div>\n<form action=\"get\" onsubmit=\"return false;\" style=\"margin-top: 20px\">\n    <div id=\"answers\">\n            <center><table><tr><td>\n            <div class=\"answer\">\n                <input type=\"radio\" name=\"answer\" value=\"13161\" id=\"answer1\">\n                <label for=\"answer1\">\n                    Tri\n                </label>\n            </div>\n        </td>\n        <td>\n            <div class=\"answer\">\n                <input type=\"radio\" name=\"answer\" value=\"13162\" id=\"answer2\">\n                <label for=\"answer2\">\n                    Å tiri\n                </label>\n            </div>\n        </td>\n        <td>\n            <div class=\"answer\">\n                <input type=\"radio\" name=\"answer\" value=\"13163\" id=\"answer3\">\n                <label for=\"answer3\">\n                    Pet\n                </label>\n            </div>\n        </td>\n        <td>\n            <div class=\"answer\">\n                <input type=\"radio\" name=\"answer\" value=\"13164\" id=\"answer4\">\n                <label for=\"answer4\">\n                    Sedem\n                </label>\n            </div>\n        </td></tr></table></center>\n\n    </div>\n\n</form>\n</body>\n</html>\n',1),(1171,260,1,5,'','','application/javascript','',0);
/*!40000 ALTER TABLE `question_resource` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question_translation`
--

DROP TABLE IF EXISTS `question_translation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `question_translation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question_id` int(11) NOT NULL,
  `language_id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `text` text,
  `data` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `question_id_2` (`question_id`,`language_id`),
  KEY `language_id` (`language_id`),
  KEY `question_id` (`question_id`),
  CONSTRAINT `question_translation_ibfk_2` FOREIGN KEY (`language_id`) REFERENCES `language` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `question_translation_ibfk_3` FOREIGN KEY (`question_id`) REFERENCES `question` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question_translation`
--

LOCK TABLES `question_translation` WRITE;
/*!40000 ALTER TABLE `question_translation` DISABLE KEYS */;
/*!40000 ALTER TABLE `question_translation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `region`
--

DROP TABLE IF EXISTS `region`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `region` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `country_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`,`country_id`),
  KEY `country_id` (`country_id`),
  CONSTRAINT `region_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `region`
--

LOCK TABLES `region` WRITE;
/*!40000 ALTER TABLE `region` DISABLE KEYS */;
INSERT INTO `region` VALUES (16,'Dol',4),(15,'Klanec',4);
/*!40000 ALTER TABLE `region` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `school`
--

DROP TABLE IF EXISTS `school`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `school` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `school_category_id` int(11) NOT NULL,
  `level_of_education` int(1) NOT NULL DEFAULT '0' COMMENT '0 == Osnovna Å¡ola, 1 == srednja Å¡ola',
  `address` varchar(255) DEFAULT NULL,
  `post` varchar(255) DEFAULT NULL,
  `postal_code` int(10) DEFAULT NULL,
  `municipality_id` int(11) DEFAULT NULL,
  `region_id` int(11) DEFAULT NULL,
  `country_id` int(11) NOT NULL DEFAULT '1',
  `tax_number` varchar(12) DEFAULT NULL,
  `identifier` varchar(20) DEFAULT NULL,
  `headmaster` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `school_category_id` (`school_category_id`),
  KEY `country_id` (`country_id`),
  KEY `municipality_id` (`municipality_id`),
  KEY `region_id` (`region_id`),
  CONSTRAINT `school_ibfk_1` FOREIGN KEY (`school_category_id`) REFERENCES `school_category` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `school_ibfk_2` FOREIGN KEY (`municipality_id`) REFERENCES `municipality` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `school_ibfk_3` FOREIGN KEY (`region_id`) REFERENCES `region` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `school_ibfk_4` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) AUTO_INCREMENT=1059 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `school`
--

LOCK TABLES `school` WRITE;
/*!40000 ALTER TABLE `school` DISABLE KEYS */;
INSERT INTO `school` VALUES (1058,'Butale elementary',4,1,'Pri cerkvi 1','Butale',1,261,16,4,'','','');
/*!40000 ALTER TABLE `school` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `school_category`
--

DROP TABLE IF EXISTS `school_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `school_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `active` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `school_category`
--

LOCK TABLES `school_category` WRITE;
/*!40000 ALTER TABLE `school_category` DISABLE KEYS */;
INSERT INTO `school_category` VALUES (1,'osnovna Å¡ola',1),(2,'druge organizacija za izobraÅ¾evanje odraslih',0),(3,'viÅ¡ja strokovna Å¡ola',0),(4,'vrtec',0),(5,'ljudska univerza',0),(6,'srednja Å¡ola',1),(7,'Å¡olske in obÅ¡olske dejavnosti',0),(8,'Zavod za otroke s posebnimi potrebami',0),(9,'osnovna Å¡ola za otroke s posebnimi potrebami',0),(10,'Center za usposabljanje, delo in varstvo',0),(11,'dijaÅ¡ki dom',0),(12,'osnovno Å¡olstvo (strokovne sluÅ¾be)',0),(13,'glasbena Å¡ola',0),(14,'svetovalni centri',0);
/*!40000 ALTER TABLE `school_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `school_mentor`
--

DROP TABLE IF EXISTS `school_mentor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `school_mentor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `school_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `active` tinyint(1) NOT NULL DEFAULT '0',
  `activated_by` int(11) DEFAULT NULL,
  `activated_timestamp` timestamp NULL DEFAULT NULL,
  `coordinator` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `school_id_user_id` (`school_id`,`user_id`),
  KEY `school_id` (`school_id`),
  KEY `activated_by` (`activated_by`),
  CONSTRAINT `school_mentor_ibfk_1` FOREIGN KEY (`school_id`) REFERENCES `school` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `school_mentor_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `school_mentor_ibfk_3` FOREIGN KEY (`activated_by`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `school_mentor`
--

LOCK TABLES `school_mentor` WRITE;
/*!40000 ALTER TABLE `school_mentor` DISABLE KEYS */;
INSERT INTO `school_mentor` VALUES (1,1058,2,1,1,'2013-06-30 22:00:00',1);
/*!40000 ALTER TABLE `school_mentor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL DEFAULT '',
  `password` varchar(128) NOT NULL DEFAULT '',
  `email` varchar(128) NOT NULL DEFAULT '',
  `activkey` varchar(128) NOT NULL DEFAULT '',
  `createtime` int(10) NOT NULL DEFAULT '0',
  `lastvisit` int(10) NOT NULL DEFAULT '0',
  `superuser` int(1) NOT NULL DEFAULT '0',
  `status` int(1) NOT NULL DEFAULT '0',
  `create_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `lastvisit_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_username` (`username`),
  UNIQUE KEY `user_email` (`email`)
) AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'admin','c7ad44cbad762a5da0a452f9e854fdc1e0e7a52a38015f23f3eab1d80b931dd472634dfac71cd34ebc35d16ab7fb8a90c81f975113d6c7538dc69dd8de9077ec','admin@example.net','901f2be1b43413de5e74977ce1a56055a9b12e11631bf1964600948a99cf35572b823ec503b2db247d962c0ba745d780ce644826ee98a6681598ab0aafbc1b10',1384021190,0,1,1,'2013-11-09 18:19:50','0000-00-00 00:00:00'),(2,'kozmijanbuta','286dfa10ae9354691469223f6bd820bd762aa257bb26cf561d4eedd9266e82be277900a3d319e9e83aa83f94cba6a7933cb3c918b326fc43f0333b407435824f','kozmijan@example.com','f9e9a7773df4a9accabc459043f6a0fc0aa9401cf55cf4b2cf987ec1c3dfaf0d342abf3d9f77f5a7f17379d259879f4eae4a6bbd921ce80e510f920f5d911a10',0,0,0,0,'2014-08-11 13:44:48','0000-00-00 00:00:00');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-08-20 13:50:41
