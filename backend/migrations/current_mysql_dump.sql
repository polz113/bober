-- phpMyAdmin SQL Dump
-- version 3.5.2
-- http://www.phpmyadmin.net
--
-- Gostitelj: localhost
-- Čas nastanka: 17. jul 2013 ob 12.46
-- Različica strežnika: 5.5.25a
-- Različica PHP: 5.4.4

SET FOREIGN_KEY_CHECKS=0;
SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Zbirka podatkov: `bober`
--

-- --------------------------------------------------------

--
-- Struktura tabele `award`
--

DROP TABLE IF EXISTS `award`;
CREATE TABLE IF NOT EXISTS `award` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `competition_user_id` int(11) NOT NULL,
  `type` int(11) NOT NULL COMMENT '1 == Priznanje za udeležbo, 5 == Bronasto, 10 == Srebrno, 15 == Zlato',
  `serial` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `serial` (`serial`),
  UNIQUE KEY `competition_user_id_type` (`competition_user_id`,`type`),
  KEY `competition_user_id` (`competition_user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Struktura tabele `competition`
--

DROP TABLE IF EXISTS `competition`;
CREATE TABLE IF NOT EXISTS `competition` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `active` tinyint(1) NOT NULL DEFAULT '0',
  `timestamp_start` datetime NOT NULL,
  `timestamp_stop` datetime NOT NULL,
  `type` int(2) NOT NULL DEFAULT '1' COMMENT '1==šolsko tekmovanje;2 == državno tekmovanje',
  `public_access` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Struktura tabele `competition_category`
--

DROP TABLE IF EXISTS `competition_category`;
CREATE TABLE IF NOT EXISTS `competition_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `active` tinyint(1) NOT NULL DEFAULT '1',
  `country_id` int(11) NOT NULL DEFAULT '1',
  `name` varchar(255) NOT NULL,
  `level_of_education` int(1) NOT NULL DEFAULT '0' COMMENT '0 == Osnovna šola, 1 == srednja šola',
  `class_from` int(3) NOT NULL,
  `class_to` int(3) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `country_id` (`country_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Struktura tabele `competition_category_active`
--

DROP TABLE IF EXISTS `competition_category_active`;
CREATE TABLE IF NOT EXISTS `competition_category_active` (
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
  KEY `competition_category_id` (`competition_category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Struktura tabele `competition_category_school`
--

DROP TABLE IF EXISTS `competition_category_school`;
CREATE TABLE IF NOT EXISTS `competition_category_school` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `competition_id` int(11) NOT NULL,
  `competition_category_id` int(11) NOT NULL,
  `school_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `competition_id_2` (`competition_id`,`competition_category_id`,`school_id`),
  KEY `competition_id` (`competition_id`),
  KEY `competition_category_id` (`competition_category_id`),
  KEY `school_id` (`school_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Struktura tabele `competition_category_school_mentor`
--

DROP TABLE IF EXISTS `competition_category_school_mentor`;
CREATE TABLE IF NOT EXISTS `competition_category_school_mentor` (
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
  KEY `disqualified_by` (`disqualified_by`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Struktura tabele `competition_category_translation`
--

DROP TABLE IF EXISTS `competition_category_translation`;
CREATE TABLE IF NOT EXISTS `competition_category_translation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `competition_category_id` int(11) NOT NULL,
  `language_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `competition_category_id_language_id` (`competition_category_id`,`language_id`),
  KEY `competition_category_id` (`competition_category_id`),
  KEY `language_id` (`language_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Struktura tabele `competition_committee`
--

DROP TABLE IF EXISTS `competition_committee`;
CREATE TABLE IF NOT EXISTS `competition_committee` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `competition_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `president` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `competition_id_2` (`competition_id`,`user_id`),
  KEY `competition_id` (`competition_id`),
  KEY `user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Struktura tabele `competition_country`
--

DROP TABLE IF EXISTS `competition_country`;
CREATE TABLE IF NOT EXISTS `competition_country` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `competition_id` int(11) NOT NULL,
  `country_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `competition_id_2` (`competition_id`,`country_id`),
  KEY `competition_id` (`competition_id`),
  KEY `country_id` (`country_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Struktura tabele `competition_question`
--

DROP TABLE IF EXISTS `competition_question`;
CREATE TABLE IF NOT EXISTS `competition_question` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `competition_id` int(11) NOT NULL,
  `question_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `competition_id` (`competition_id`),
  KEY `question_id` (`question_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Struktura tabele `competition_question_category`
--

DROP TABLE IF EXISTS `competition_question_category`;
CREATE TABLE IF NOT EXISTS `competition_question_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `competition_question_id` int(11) NOT NULL,
  `competition_category_id` int(11) NOT NULL,
  `competiton_question_difficulty_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `competition_question_id_2` (`competition_question_id`,`competition_category_id`),
  KEY `competition_question_id` (`competition_question_id`),
  KEY `competition_category_id` (`competition_category_id`),
  KEY `competiton_question_difficulty` (`competiton_question_difficulty_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Struktura tabele `competition_question_difficulty`
--

DROP TABLE IF EXISTS `competition_question_difficulty`;
CREATE TABLE IF NOT EXISTS `competition_question_difficulty` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `country_id` int(11) NOT NULL DEFAULT '1',
  `active` tinyint(1) NOT NULL DEFAULT '1',
  `name` varchar(255) NOT NULL,
  `correct_answer_points` decimal(10,4) NOT NULL DEFAULT '0.0000',
  `wrong_answer_points` decimal(10,4) NOT NULL DEFAULT '0.0000',
  PRIMARY KEY (`id`),
  KEY `country_id` (`country_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- Odloži podatke za tabelo `competition_question_difficulty`
--

INSERT INTO `competition_question_difficulty` (`id`, `country_id`, `active`, `name`, `correct_answer_points`, `wrong_answer_points`) VALUES
(1, 1, 1, 'Srednja stopnja 2', 3.5000, -1.0000),
(2, 1, 1, 'Nižja stopnja', 1.0000, -5.0000);

-- --------------------------------------------------------

--
-- Struktura tabele `competition_question_difficulty_translation`
--

DROP TABLE IF EXISTS `competition_question_difficulty_translation`;
CREATE TABLE IF NOT EXISTS `competition_question_difficulty_translation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `competition_question_difficulty_id` int(11) NOT NULL,
  `language_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `competition_question_difficult_2` (`competition_question_difficulty_id`,`language_id`),
  KEY `competition_question_difficulty_id` (`competition_question_difficulty_id`),
  KEY `language_id` (`language_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Struktura tabele `competition_translation`
--

DROP TABLE IF EXISTS `competition_translation`;
CREATE TABLE IF NOT EXISTS `competition_translation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `competition_id` int(11) NOT NULL,
  `language_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `competition_id_2` (`competition_id`,`language_id`),
  KEY `competition_id` (`competition_id`),
  KEY `language_id` (`language_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Struktura tabele `competition_user`
--

DROP TABLE IF EXISTS `competition_user`;
CREATE TABLE IF NOT EXISTS `competition_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `competition_id` int(11) NOT NULL,
  `competition_category_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `competition_category_school_mentor_id` int(11) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `first_name` varchar(255) DEFAULT NULL,
  `class` varchar(20) DEFAULT NULL,
  `school_id` int(11) NOT NULL,
  `disqualified_request` tinyint(1) NOT NULL DEFAULT '0',
  `disqualified_request_by` int(11) DEFAULT NULL,
  `disqualified` tinyint(1) NOT NULL DEFAULT '0',
  `disqualified_by` int(11) DEFAULT NULL,
  `disqualified_reason` text,
  `advancing_to_next_level` tinyint(1) NOT NULL DEFAULT '0',
  `award` int(2) DEFAULT NULL COMMENT '1 == Priznanje za udeležbo, 5 == Bronasto, 10 == Srebrno, 15 == Zlato',
  `start_time` datetime DEFAULT NULL,
  `finish_time` datetime DEFAULT NULL,
  `finished` tinyint(1) NOT NULL DEFAULT '0',
  `total_points_via_answers` decimal(10,4) NOT NULL DEFAULT '0.0000',
  `total_points_via_time` decimal(10,4) NOT NULL DEFAULT '0.0000',
  `total_points_manual` decimal(10,4) NOT NULL DEFAULT '0.0000',
  `total_points` decimal(10,4) NOT NULL DEFAULT '0.0000',
  PRIMARY KEY (`id`),
  UNIQUE KEY `competition_id_2` (`competition_id`,`competition_category_id`,`user_id`,`competition_category_school_mentor_id`,`last_name`,`first_name`,`class`,`school_id`),
  KEY `user_id` (`user_id`),
  KEY `competition_id` (`competition_id`),
  KEY `competition_category_id` (`competition_category_id`),
  KEY `competition_category_school_mentor_id` (`competition_category_school_mentor_id`),
  KEY `school_id` (`school_id`),
  KEY `disqualified_request_by` (`disqualified_request_by`),
  KEY `disqualified_by` (`disqualified_by`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Struktura tabele `competition_user_question`
--

DROP TABLE IF EXISTS `competition_user_question`;
CREATE TABLE IF NOT EXISTS `competition_user_question` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `competition_user_id` int(11) NOT NULL,
  `competition_question_id` int(11) NOT NULL,
  `ordering` int(11) NOT NULL,
  `question_answer_id` int(11) DEFAULT NULL,
  `last_change` datetime DEFAULT NULL,
  `custom_answer` text COMMENT 'For future usage',
  PRIMARY KEY (`id`),
  KEY `competition_user_id` (`competition_user_id`),
  KEY `competition_question_id` (`competition_question_id`),
  KEY `question_answer_id` (`question_answer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Struktura tabele `competition_user_question_answer`
--

DROP TABLE IF EXISTS `competition_user_question_answer`;
CREATE TABLE IF NOT EXISTS `competition_user_question_answer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `competition_user_question_id` int(11) NOT NULL,
  `question_answer_id` int(11) NOT NULL,
  `ordering` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `competition_user_question_id_2` (`competition_user_question_id`,`question_answer_id`),
  KEY `competition_user_question_id` (`competition_user_question_id`),
  KEY `question_answer_id` (`question_answer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Struktura tabele `country`
--

DROP TABLE IF EXISTS `country`;
CREATE TABLE IF NOT EXISTS `country` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `country` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `country` (`country`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

--
-- Odloži podatke za tabelo `country`
--

INSERT INTO `country` (`id`, `country`) VALUES
(1, 'Slovenija');

-- --------------------------------------------------------

--
-- Struktura tabele `country_administrator`
--

DROP TABLE IF EXISTS `country_administrator`;
CREATE TABLE IF NOT EXISTS `country_administrator` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `country_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `country_id_2` (`country_id`,`user_id`),
  KEY `country_id` (`country_id`),
  KEY `user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Struktura tabele `country_language`
--

DROP TABLE IF EXISTS `country_language`;
CREATE TABLE IF NOT EXISTS `country_language` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `country_id` int(11) NOT NULL,
  `language_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `country_id_2` (`country_id`,`language_id`),
  KEY `country_id` (`country_id`),
  KEY `language_id` (`language_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Struktura tabele `language`
--

DROP TABLE IF EXISTS `language`;
CREATE TABLE IF NOT EXISTS `language` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `short` varchar(5) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`,`short`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- Odloži podatke za tabelo `language`
--

INSERT INTO `language` (`id`, `name`, `short`) VALUES
(2, 'Angleščina', 'en'),
(1, 'Slovenščina', 'sl');

-- --------------------------------------------------------

--
-- Struktura tabele `municipality`
--

DROP TABLE IF EXISTS `municipality`;
CREATE TABLE IF NOT EXISTS `municipality` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `country_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`,`country_id`),
  KEY `country_id` (`country_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=212 ;

--
-- Odloži podatke za tabelo `municipality`
--

INSERT INTO `municipality` (`id`, `name`, `country_id`) VALUES
(67, 'Ajdovščina', 1),
(197, 'Apače', 1),
(46, 'Beltinci', 1),
(48, 'Benedikt', 1),
(49, 'Bistrica ob Sotli', 1),
(199, 'Bled', 1),
(174, 'Bloke', 1),
(194, 'Bohinj', 1),
(192, 'Borovnica', 1),
(56, 'Bovec', 1),
(57, 'Braslovče', 1),
(78, 'Brda', 1),
(14, 'Brežice', 1),
(59, 'Brezovica', 1),
(61, 'Cankova', 1),
(15, 'Celje', 1),
(69, 'Cerklje na Gorenjskem', 1),
(111, 'Cerknica', 1),
(62, 'Cerkno', 1),
(63, 'Cerkvenjak', 1),
(65, 'Cirkulane', 1),
(91, 'Črenšovci', 1),
(211, 'Črna na Koroškem', 1),
(117, 'Črnomelj', 1),
(71, 'Destrnik', 1),
(189, 'Divača', 1),
(74, 'Dobje', 1),
(75, 'Dobrepolje', 1),
(76, 'Dobrna', 1),
(77, 'Dobrova-Polhov Gradec', 1),
(9, 'Dobrovnik', 1),
(108, 'Dol pri Ljubljani', 1),
(79, 'Dolenjske Toplice', 1),
(73, 'Domžale', 1),
(191, 'Dornava', 1),
(147, 'Dravograd', 1),
(82, 'Duplek', 1),
(105, 'Gorenja vas-Poljane', 1),
(94, 'Gorišnica', 1),
(95, 'Gorje', 1),
(96, 'Gornja Radgona', 1),
(89, 'Gornji Grad', 1),
(97, 'Gornji Petrovci', 1),
(98, 'Grad', 1),
(60, 'Grosuplje', 1),
(99, 'Hajdina', 1),
(84, 'Hoče-Slivnica', 1),
(12, 'Hodoš', 1),
(100, 'Horjul', 1),
(145, 'Hrastnik', 1),
(81, 'Hrpelje-Kozina', 1),
(22, 'Idrija', 1),
(101, 'Ig', 1),
(45, 'Ilirska Bistrica', 1),
(87, 'Ivančna Gorica', 1),
(68, 'Izola', 1),
(21, 'Jesenice', 1),
(132, 'Jezersko', 1),
(113, 'Juršinci', 1),
(6, 'Kamnik', 1),
(70, 'Kanal', 1),
(55, 'Kidričevo', 1),
(165, 'Kobarid', 1),
(116, 'Kobilje', 1),
(30, 'Kočevje', 1),
(44, 'Komen', 1),
(118, 'Komenda', 1),
(20, 'Koper', 1),
(109, 'Kostanjevica na Krki', 1),
(85, 'Kostel', 1),
(119, 'Kozje', 1),
(19, 'Kranj', 1),
(36, 'Kranjska Gora', 1),
(121, 'Križevci', 1),
(38, 'Krško', 1),
(122, 'Kungota', 1),
(123, 'Kuzma', 1),
(40, 'Laško', 1),
(124, 'Lenart', 1),
(8, 'Lendava', 1),
(23, 'Litija', 1),
(5, 'Ljubljana', 1),
(125, 'Ljubno', 1),
(18, 'Ljutomer', 1),
(126, 'Log-Dragomer', 1),
(37, 'Logatec', 1),
(196, 'Loška dolina', 1),
(188, 'Loški Potok', 1),
(127, 'Lovrenc na Pohorju', 1),
(52, 'Luče', 1),
(107, 'Lukovica', 1),
(129, 'Majšperk', 1),
(39, 'Makole', 1),
(2, 'Maribor', 1),
(130, 'Markovci', 1),
(133, 'Medvode', 1),
(134, 'Mengeš', 1),
(135, 'Metlika', 1),
(136, 'Mežica', 1),
(137, 'Miklavž na Dravskem polju', 1),
(138, 'Miren-Kostanjevica', 1),
(139, 'Mirna', 1),
(173, 'Mirna Peč', 1),
(140, 'Mislinja', 1),
(142, 'Mokronog-Trebelno', 1),
(112, 'Moravče', 1),
(10, 'Moravske Toplice', 1),
(143, 'Mozirje', 1),
(3, 'Murska Sobota', 1),
(144, 'Muta', 1),
(4, 'Naklo', 1),
(146, 'Nazarje', 1),
(24, 'Nova Gorica', 1),
(16, 'Novo mesto', 1),
(148, 'Odranci', 1),
(151, 'Oplotnica', 1),
(25, 'Ormož', 1),
(86, 'Osilnica', 1),
(106, 'Pesnica', 1),
(17, 'Piran', 1),
(120, 'Pivka', 1),
(150, 'Podčetrtek', 1),
(149, 'Podlehnik', 1),
(58, 'Podvelka', 1),
(152, 'Poljčane', 1),
(153, 'Polzela', 1),
(42, 'Postojna', 1),
(154, 'Prebold', 1),
(131, 'Preddvor', 1),
(92, 'Prevalje', 1),
(26, 'Ptuj', 1),
(157, 'Puconci', 1),
(88, 'Rače-Fram', 1),
(34, 'Radeče', 1),
(114, 'Radenci', 1),
(158, 'Radlje ob Dravi', 1),
(13, 'Radovljica', 1),
(35, 'Ravne na Koroškem', 1),
(159, 'Razkrižje', 1),
(160, 'Rečica ob Savinji', 1),
(104, 'Renče-Vogrsko', 1),
(190, 'Ribnica', 1),
(161, 'Ribnica na Pohorju', 1),
(32, 'Rogaška Slatina', 1),
(168, 'Rogašovci', 1),
(162, 'Rogatec', 1),
(29, 'Ruše', 1),
(11, 'Šalovci', 1),
(164, 'Selnica ob Dravi', 1),
(47, 'Semič', 1),
(103, 'Šempeter-Vrtojba', 1),
(201, 'Šenčur', 1),
(163, 'Šentilj', 1),
(200, 'Šentjernej', 1),
(54, 'Šentjur', 1),
(195, 'Šentrupert', 1),
(51, 'Sevnica', 1),
(83, 'Sežana', 1),
(90, 'Škocjan', 1),
(31, 'Škofja Loka', 1),
(202, 'Škofljica', 1),
(7, 'Slovenj Gradec', 1),
(1, 'Slovenska Bistrica', 1),
(128, 'Slovenske Konjice', 1),
(203, 'Šmarje pri Jelšah', 1),
(204, 'Šmarješke Toplice', 1),
(187, 'Šmartno ob Paki', 1),
(205, 'Šmartno pri Litiji', 1),
(193, 'Sodražica', 1),
(53, 'Solčava', 1),
(115, 'Šoštanj', 1),
(166, 'Središče ob Dravi', 1),
(167, 'Starše', 1),
(206, 'Štore', 1),
(178, 'Straža', 1),
(169, 'Sveta Ana', 1),
(198, 'Sveta Trojica v Slovenskih goricah', 1),
(64, 'Sveti Andraž v Slov. goricah', 1),
(170, 'Sveti Jurij ob Ščavnici', 1),
(110, 'Sveti Jurij v Slovenskih goricah', 1),
(171, 'Sveti Tomaž', 1),
(184, 'Tabor', 1),
(172, 'Tišina', 1),
(27, 'Tolmin', 1),
(28, 'Trbovlje', 1),
(175, 'Trebnje', 1),
(72, 'Trnovska vas', 1),
(50, 'Tržič', 1),
(176, 'Trzin', 1),
(177, 'Turnišče', 1),
(41, 'Velenje', 1),
(141, 'Velika Polana', 1),
(156, 'Velike Lašče', 1),
(179, 'Veržej', 1),
(180, 'Videm', 1),
(80, 'Vipava', 1),
(181, 'Vitanje', 1),
(182, 'Vodice', 1),
(93, 'Vojnik', 1),
(183, 'Vransko', 1),
(43, 'Vrhnika', 1),
(185, 'Vuzenica', 1),
(102, 'Zagorje ob Savi', 1),
(33, 'Žalec', 1),
(66, 'Zavrč', 1),
(207, 'Železniki', 1),
(208, 'Žetale', 1),
(209, 'Žiri', 1),
(210, 'Žirovnica', 1),
(186, 'Zreče', 1),
(155, 'Žužemberk', 1);

-- --------------------------------------------------------

--
-- Struktura tabele `profiles`
--

DROP TABLE IF EXISTS `profiles`;
CREATE TABLE IF NOT EXISTS `profiles` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `country_id` int(10) NOT NULL DEFAULT '1',
  `user_role` int(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`user_id`),
  KEY `country_id` (`country_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

--
-- Odloži podatke za tabelo `profiles`
--

INSERT INTO `profiles` (`user_id`, `first_name`, `last_name`, `country_id`, `user_role`) VALUES
(1, 'Dean', 'Gostiša', 1, 10);

-- --------------------------------------------------------

--
-- Struktura tabele `profiles_fields`
--

DROP TABLE IF EXISTS `profiles_fields`;
CREATE TABLE IF NOT EXISTS `profiles_fields` (
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
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=5 ;

--
-- Odloži podatke za tabelo `profiles_fields`
--

INSERT INTO `profiles_fields` (`id`, `varname`, `title`, `field_type`, `field_size`, `field_size_min`, `required`, `match`, `range`, `error_message`, `other_validator`, `default`, `widget`, `widgetparams`, `position`, `visible`) VALUES
(1, 'first_name', 'First Name', 'VARCHAR', 255, 3, 2, '', '', 'Incorrect First Name (length between 3 and 50 characters).', '', '', '', '', 1, 3),
(2, 'last_name', 'Last Name', 'VARCHAR', 255, 3, 2, '', '', 'Incorrect Last Name (length between 3 and 50 characters).', '', '', '', '', 2, 3),
(3, 'country_id', 'Country', 'INTEGER', 10, 0, 1, '', '', 'Choose country', '', '1', 'UWrelBelongsTo', '{"modelName":"Country","optionName":"country","emptyField":"---","relationName":"country"}', 0, 3),
(4, 'user_role', 'User Role', 'INTEGER', 1, 1, 3, '', '1==Contestant;5==Teacher;10==Country Administrator;15==System Administrator', 'Invalid user role.', '', '1', '', '', 0, 1);

-- --------------------------------------------------------

--
-- Struktura tabele `question`
--

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

-- --------------------------------------------------------

--
-- Struktura tabele `question_answer`
--

DROP TABLE IF EXISTS `question_answer`;
CREATE TABLE IF NOT EXISTS `question_answer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question_id` int(11) NOT NULL,
  `type` tinyint(1) NOT NULL DEFAULT '0' COMMENT '0 == wrong; 1 == correct',
  `value` text NOT NULL,
  PRIMARY KEY (`id`),
  KEY `question_id` (`question_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Struktura tabele `question_answer_translation`
--

DROP TABLE IF EXISTS `question_answer_translation`;
CREATE TABLE IF NOT EXISTS `question_answer_translation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question_answer_id` int(11) NOT NULL,
  `language_id` int(11) NOT NULL,
  `value` text NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `question_answer_id` (`question_answer_id`,`language_id`),
  KEY `language_id` (`language_id`),
  KEY `question_answer_id_2` (`question_answer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Struktura tabele `question_resource`
--

DROP TABLE IF EXISTS `question_resource`;
CREATE TABLE IF NOT EXISTS `question_resource` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question_id` int(11) NOT NULL,
  `filename` varchar(512) NOT NULL,
  `data` longblob NOT NULL,
  PRIMARY KEY (`id`),
  KEY `question_id` (`question_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Struktura tabele `question_translation`
--

DROP TABLE IF EXISTS `question_translation`;
CREATE TABLE IF NOT EXISTS `question_translation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question_id` int(11) NOT NULL,
  `language_id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `text` text,
  `data` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `question_id_2` (`question_id`,`language_id`),
  KEY `language_id` (`language_id`),
  KEY `question_id` (`question_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Struktura tabele `region`
--

DROP TABLE IF EXISTS `region`;
CREATE TABLE IF NOT EXISTS `region` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `country_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`,`country_id`),
  KEY `country_id` (`country_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=13 ;

--
-- Odloži podatke za tabelo `region`
--

INSERT INTO `region` (`id`, `name`, `country_id`) VALUES
(3, 'Gorenjska', 1),
(10, 'Goriška', 1),
(8, 'Jugovzhodna Slovenija', 1),
(5, 'Koroška', 1),
(12, 'Notranjsko-kraška', 1),
(9, 'Obalno-kraška', 1),
(4, 'Osrednjeslovenska', 1),
(1, 'Podravska', 1),
(2, 'Pomurska', 1),
(7, 'Savinjska', 1),
(6, 'Spodnjeposavska', 1),
(11, 'Zasavska', 1);

-- --------------------------------------------------------

--
-- Struktura tabele `school`
--

DROP TABLE IF EXISTS `school`;
CREATE TABLE IF NOT EXISTS `school` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `school_category_id` int(11) NOT NULL,
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
  KEY `region_id` (`region_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=973 ;

--
-- Odloži podatke za tabelo `school`
--

INSERT INTO `school` (`id`, `name`, `school_category_id`, `address`, `post`, `postal_code`, `municipality_id`, `region_id`, `country_id`, `tax_number`, `identifier`, `headmaster`) VALUES
(1, '2. osnovna šola Slovenska Bistrica', 1, NULL, 'Slovenska Bistrica', 2310, 1, 1, 1, '52959856', '3348008000', 'Sonja Arbeiter'),
(2, 'Biotehniška šola Maribor', 6, NULL, 'Maribor', 2000, 2, 1, 1, '42181216', '5085454000', 'Anton Krajnc'),
(3, 'Biotehniška šola Rakičan', 6, NULL, 'Murska Sobota', 9000, 3, 2, 1, '81849494', '5089794000', 'Štefan Smodiš'),
(4, 'Biotehniški center Naklo', 6, NULL, 'Naklo', 4202, 4, 3, 1, '66817994', '5088739000', 'mag. Marijan Pogačnik'),
(5, 'Biotehniški center Naklo, Srednja šola', 6, NULL, 'Naklo', 4202, 4, 3, 1, '66817994', '5088739001', 'Andreja Ahčin'),
(6, 'Biotehniški izobraževalni center Ljubljana', 6, NULL, 'Ljubljana', 1000, 5, 4, 1, '95277145', '5084571000', 'mag. Jasna Kržin Stepišnik'),
(7, 'Biotehniški izobraževalni center Ljubljana, Gimnazija in veterinarska šola', 6, NULL, 'Ljubljana', 1000, 5, 4, 1, '95277145', '5084571001', 'Breda Rudel'),
(8, 'Biotehniški izobraževalni center Ljubljana, Živilska šola', 6, NULL, 'Ljubljana', 1000, 5, 4, 1, '95277145', '5084571002', 'mag. Tatjana Šček Prebil'),
(9, 'Center za izobraževanje, rehabilitacijo in usposabljanje Kamnik, Srednja šola', 6, NULL, 'Kamnik', 1241, 6, 4, 1, '99621053', '5049768002', 'Saša Markovič'),
(10, 'Druga osnovna šola Slovenj Gradec', 1, NULL, 'Slovenj Gradec', 2380, 7, 5, 1, '22973389', '5635772000', 'Nada Duler'),
(11, 'Druga osnovna šola Slovenj Gradec Podružnica Pameče-Troblje', 1, NULL, 'Slovenj Gradec', 2380, 7, 5, 1, '22973389', '5635772001', ''),
(12, 'Dvojezična osnovna šola 1 Lendava', 1, NULL, 'Lendava - Lendva', 9220, 8, 2, 1, '50448625', '5089727000', 'Tatjana Sabo'),
(13, 'Dvojezična osnovna šola 1 Lendava Podružnica Gaberje', 1, NULL, 'Lendava - Lendva', 9220, 8, 2, 1, '50448625', '5089727003', ''),
(14, 'Dvojezična osnovna šola Dobrovnik', 1, NULL, 'Dobrovnik - Dobronak', 9223, 9, 2, 1, '97102318', '5086078000', 'Katarina Kovač'),
(15, 'Dvojezična osnovna šola Genterovci', 1, NULL, 'Dobrovnik - Dobronak', 9223, 8, 2, 1, '31391320', '5089735000', 'Valerija Šebjanič'),
(16, 'Dvojezična osnovna šola Prosenjakovci', 1, NULL, 'Prosenjakovci - Pártosfalva', 9207, 10, 2, 1, '67749925', '5243289000', 'Jožefa Herman'),
(17, 'Dvojezična osnovna šola Prosenjakovci Podružnica Domanjševci', 1, NULL, 'Križevci', 9206, 11, 2, 1, '67749925', '5243289001', '---'),
(18, 'Dvojezična osnovna šola Prosenjakovci Podružnica Hodoš', 1, NULL, 'Hodoš - Hodos', 9205, 12, 2, 1, '67749925', '5243289002', '---'),
(19, 'Dvojezična srednja šola Lendava', 6, NULL, 'Lendava - Lendva', 9220, 8, 2, 1, '39462692', '5084067000', 'Silvija Hajdinjak Prendl'),
(20, 'ERUDIO izobraževalni center', 6, NULL, 'Ljubljana', 1000, 5, 4, 1, '19618174', '5742307000', 'Dimitrij Miklič'),
(21, 'ERUDIO zasebna gimnazija', 6, NULL, 'Ljubljana', 1000, 5, 4, 1, '19618174', '5742307003', 'v. d. Simona Zupančič'),
(22, 'Ekonomska gimnazija in srednja šola Radovljica', 6, NULL, 'Radovljica', 4240, 13, 3, 1, '95864717', '5921724000', 'Ksenija Lipovšček'),
(23, 'Ekonomska in trgovska šola Brežice', 6, NULL, 'Brežice', 8250, 14, 6, 1, '51349728', '1458558000', 'Martin Šoško'),
(24, 'Ekonomska in trgovska šola Brežice, Poklicna in strokovna šola', 6, NULL, 'Brežice', 8250, 14, 6, 1, '51349728', '1458558001', 'Martin Šoško'),
(25, 'Ekonomska šola Celje', 6, NULL, 'Celje', 3000, 15, 7, 1, '56965346', '6280684000', 'v. d. Bernarda Marčeta'),
(26, 'Ekonomska šola Celje, Gimnazija in srednja šola', 6, NULL, 'Celje', 3000, 15, 7, 1, '56965346', '6280684001', 'v. d. Bernarda Marčeta'),
(27, 'Ekonomska šola Ljubljana', 6, NULL, 'Ljubljana', 1000, 5, 4, 1, '59942720', '1318861000', 'Eva Kardelj Cvetko'),
(28, 'Ekonomska šola Murska Sobota', 6, NULL, 'Murska Sobota', 9000, 3, 2, 1, '20192533', '5216214000', 'mag. Beno Klemenčič'),
(29, 'Ekonomska šola Murska Sobota, Srednja šola in gimnazija', 6, NULL, 'Murska Sobota', 9000, 3, 2, 1, '20192533', '5216214004', 'Darko Petrijan'),
(30, 'Ekonomska šola Novo mesto', 6, NULL, 'Novo mesto', 8000, 16, 8, 1, '84477849', '5089115000', 'Jože Zupančič'),
(31, 'Ekonomska šola Novo mesto, Srednja šola in gimnazija', 6, NULL, 'Novo mesto', 8000, 16, 8, 1, '84477849', '5089115004', 'Jože Zupančič'),
(32, 'Elektrotehniško-računalniška strokovna šola in gimnazija Ljubljana', 6, NULL, 'Ljubljana', 1000, 5, 4, 1, '83657533', '5084172000', 'Silvester Tratar'),
(33, 'Gimnazija Antonio Sema Piran', 6, NULL, 'Portorož - Portorose', 6320, 17, 9, 1, '54783020', '5086892000', 'Monika Jurman'),
(34, 'Gimnazija Bežigrad', 6, NULL, 'Ljubljana', 1000, 5, 4, 1, '64618471', '5083451000', 'Janez Šušteršič'),
(35, 'Gimnazija Bežigrad, Gimnazija', 6, NULL, 'Ljubljana', 1000, 5, 4, 1, '64618471', '5083451001', 'mag. Ciril Dominko'),
(36, 'Gimnazija Bežigrad, Mednarodna šola', 6, NULL, 'Ljubljana', 1000, 5, 4, 1, '64618471', '5083451002', 'dr. Mirko Mrčela'),
(37, 'Gimnazija Brežice', 6, NULL, 'Brežice', 8250, 14, 6, 1, '42615011', '1458540000', 'Uroš Škof'),
(38, 'Gimnazija Celje - Center', 6, NULL, 'Celje', 3000, 15, 7, 1, '44240562', '5082625000', 'Igor Majerle'),
(39, 'Gimnazija Franca Miklošiča Ljutomer', 6, NULL, 'Ljutomer', 9240, 18, 2, 1, '32934335', '5084652000', 'Zvonko Kustec'),
(40, 'Gimnazija Franceta Prešerna', 6, NULL, 'Kranj', 4000, 19, 3, 1, '84484047', '6286186000', 'v. d. Mirjam Bizjak'),
(41, 'Gimnazija Gian Rinaldo Carli Koper', 6, NULL, 'Koper - Capodistria', 6000, 20, 9, 1, '70662908', '5083885000', 'Luisa Angelini Ličen'),
(42, 'Gimnazija Jesenice', 6, NULL, 'Jesenice', 4270, 21, 3, 1, '93902751', '5854091000', 'mag. Lidija Dornig'),
(43, 'Gimnazija Jožeta Plečnika Ljubljana', 6, NULL, 'Ljubljana', 1000, 5, 4, 1, '71266909', '1214144000', 'Anton Grosek'),
(44, 'Gimnazija Jurija Vege Idrija', 6, NULL, 'Idrija', 5280, 22, 10, 1, '34857788', '5085969000', 'Borut Hvalec'),
(45, 'Gimnazija Koper', 6, NULL, 'Koper - Capodistria', 6000, 20, 9, 1, '61745685', '5083869000', 'Bruno Petrič'),
(46, 'Gimnazija Kranj', 6, NULL, 'Kranj', 4000, 19, 3, 1, '55313680', '5083923000', 'mag. Franc Rozman'),
(47, 'Gimnazija Ledina', 6, NULL, 'Ljubljana', 1000, 5, 4, 1, '24546208', '5084202000', 'Roman Vogrinc'),
(48, 'Gimnazija Litija', 6, NULL, 'Litija', 1270, 23, 4, 1, '56971192', '1201379000', 'Vida Poglajen'),
(49, 'Gimnazija Moste', 6, NULL, 'Ljubljana', 1000, 5, 4, 1, '79887520', '5084318000', 'Špela Škof Urh'),
(50, 'Gimnazija Murska Sobota', 6, NULL, 'Murska Sobota', 9000, 3, 2, 1, '78559537', '5508541000', 'Roman Činč'),
(51, 'Gimnazija Nova Gorica', 6, NULL, 'Nova Gorica', 5000, 24, 10, 1, '71839941', '5221161000', 'Bojan Bratina'),
(52, 'Gimnazija Novo mesto', 6, NULL, 'Novo mesto', 8000, 16, 8, 1, '77209737', '5089131000', 'Natalija Petakovič'),
(53, 'Gimnazija Ormož', 6, NULL, 'Ormož', 2270, 25, 1, 1, '62536630', '1323318000', 'mag. Blanka Erhartič'),
(54, 'Gimnazija Poljane', 6, NULL, 'Ljubljana', 1000, 5, 4, 1, '79262341', '5083524000', 'Bojan Končan'),
(55, 'Gimnazija Ptuj', 6, NULL, 'Ptuj', 2250, 26, 1, 1, '31808093', '1636855000', 'Melani Centrih'),
(56, 'Gimnazija Tolmin', 6, NULL, 'Tolmin', 5220, 27, 10, 1, '96796219', '5272661000', 'mag. Branka Hrast Debeljak'),
(57, 'Gimnazija Vič', 6, NULL, 'Ljubljana', 1000, 5, 4, 1, '54767695', '5084563000', 'mag. Alenka Krapež'),
(58, 'Gimnazija in ekonomska srednja šola Trbovlje', 6, NULL, 'Trbovlje', 1420, 28, 11, 1, '93274211', '5090202000', 'Jelena Keršnik'),
(59, 'Gimnazija in srednja kemijska šola Ruše', 6, NULL, 'Ruše', 2342, 29, 1, 1, '11732199', '5085861000', 'Marjan Kukovič'),
(60, 'Gimnazija in srednja šola Kočevje', 6, NULL, 'Kočevje', 1330, 30, 8, 1, '22854509', '6214312000', 'mag. Marjeta Kamšek'),
(61, 'Gimnazija in srednja šola Rudolfa Maistra Kamnik', 6, NULL, 'Kamnik', 1241, 6, 4, 1, '27380297', '5178924000', 'mag. Šemso Mujanović'),
(62, 'Gimnazija Šentvid', 6, NULL, 'Ljubljana - Šentvid', 1210, 5, 4, 1, '40605035', '5084962000', 'mag. Jaka Erker'),
(63, 'Gimnazija Šiška', 6, NULL, 'Ljubljana', 1000, 5, 4, 1, '57801606', '5671159000', 'Edi Kuklec'),
(64, 'Gimnazija Škofja Loka', 6, NULL, 'Škofja Loka', 4220, 31, 3, 1, '75358247', '5087864000', 'Jože Bogataj'),
(65, 'Gimnazija, elektro in pomorska šola Piran', 6, NULL, 'Piran - Pirano', 6330, 17, 9, 1, '84761750', '6286127000', 'v. d. Borut Butinar'),
(66, 'Grm Novo mesto - center biotehnike in turizma', 6, NULL, 'Novo mesto', 8000, 16, 8, 1, '46571558', '5089107000', 'Tone Hrovat'),
(67, 'Grm Novo mesto - center biotehnike in turizma, Kmetijska šola Grm in biotehniška gimnazija', 6, NULL, 'Novo mesto', 8000, 16, 8, 1, '46571558', '5089107005', 'Vida Hlebec'),
(68, 'Grm Novo mesto - center biotehnike in turizma, Srednja šola za gostinstvo in turizem', 6, NULL, 'Novo mesto', 8000, 16, 8, 1, '46571558', '5089107004', 'Jože Avsec'),
(69, 'I. Osnovna šola Rogaška Slatina', 1, NULL, 'Rogaška Slatina', 3250, 32, 7, 1, '16457617', '5087953000', 'Anita Skale'),
(70, 'I. gimnazija v Celju', 6, NULL, 'Celje', 3000, 15, 7, 1, '26398303', '5084717000', 'dr. Anton Šepetavc'),
(71, 'I. osnovna šola Celje', 1, NULL, 'Celje', 3000, 15, 7, 1, '90567226', '5082609000', 'Branko Močivnik'),
(72, 'I. osnovna šola Žalec', 1, NULL, 'Žalec', 3310, 33, 7, 1, '17565553', '5088534000', 'Tatjana Žgank Meža'),
(73, 'I. osnovna šola Žalec Podružnica Gotovlje', 1, NULL, 'Žalec', 3310, 33, 7, 1, '17565553', '5088534001', ''),
(74, 'I. osnovna šola Žalec Podružnica Ponikva', 1, NULL, 'Žalec', 3310, 33, 7, 1, '17565553', '5088534002', ''),
(75, 'II. Osnovna šola Rogaška Slatina Podružnica Sv. Florijan', 1, NULL, 'Rogaška Slatina', 3250, 32, 7, 1, NULL, '5278945002', ''),
(76, 'II. gimnazija Maribor', 6, NULL, 'Maribor', 2000, 2, 1, 1, '62721046', '5088917000', 'mag. Ivan Lorenčič'),
(77, 'II. osnovna šola Celje', 1, NULL, 'Celje', 3000, 15, 7, 1, '18983022', '5082617000', 'Igor Topole'),
(78, 'II.Osnovna šola Rogaška Slatina Podružnica Kostrivnica', 1, NULL, 'Podplat', 3241, 32, 7, 1, '60425571', '5278945001', ''),
(79, 'III. gimnazija Maribor', 6, NULL, 'Maribor', 2000, 2, 1, 1, '86876651', '5081297000', 'Janez Pastar'),
(80, 'III. osnovna šola Celje', 1, NULL, 'Celje', 3000, 15, 7, 1, '48097535', '5083613000', 'Ivan Janez Domitrovič'),
(81, 'IV. osnovna šola Celje', 1, NULL, 'Celje', 3000, 15, 7, 1, '82175420', '5082633000', 'Nevenka Matelič Nunčič'),
(82, 'Izobraževalni center Piramida Maribor', 6, NULL, 'Maribor', 2000, 2, 1, 1, '63009820', '5085438000', 'mag. Midhat Mulaosmanović'),
(83, 'Izobraževalni center Piramida Maribor, Srednja šola za prehrano in živilstvo', 6, NULL, 'Maribor', 2000, 2, 1, 1, '63009820', '5085438001', 'Midhat Mulaosmanović'),
(84, 'Javni zavod Osnovna šola Marjana Nemca Radeče', 1, NULL, 'Radeče', 1433, 34, 7, 1, '93174705', '5924502000', 'Katja Selčan'),
(85, 'Javni zavod Osnovna šola Marjana Nemca Radeče Podružnica Svibno', 1, NULL, 'Radeče', 1433, 34, 7, 1, '93174705', '5924502001', ''),
(86, 'Konservatorij za glasbo in balet Ljubljana', 6, NULL, 'Ljubljana', 1000, 5, 4, 1, '77065956', '5088763000', 'Dejan Prešiček'),
(87, 'Konservatorij za glasbo in balet Ljubljana, Srednja glasbena in baletna šola', 6, NULL, 'Ljubljana', 1000, 5, 4, 1, '77065956', '5088763002', 'Dejan Prešiček'),
(88, 'Konservatorij za glasbo in balet Maribor', 6, NULL, 'Maribor', 2000, 2, 1, 1, '48190675', '5110246000', 'Helena Meško'),
(89, 'Montessori inštitut, zavod', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '22779108', '2234572000', 'mag. Pavel Demšar'),
(90, 'Osnovna šola "Borcev za severno mejo" Maribor', 1, NULL, 'Maribor', 2000, 2, 1, 1, '27553078', '5197449000', 'Lučka Lazarev Šerbec'),
(91, 'Osnovna šola "Koroški jeklarji" Ravne na Koroškem', 1, NULL, 'Ravne na Koroškem', 2390, 35, 5, 1, '83712143', '5185815000', 'Aljaž Banko'),
(92, 'Osnovna šola 16. decembra Mojstrana', 1, NULL, 'Mojstrana', 4281, 36, 3, 1, '39376699', '5719054000', 'Darja Pikon'),
(93, 'Osnovna šola 8 talcev Logatec', 1, NULL, 'Logatec', 1370, 37, 4, 1, '45289018', '5084687000', 'Karmen Cunder'),
(94, 'Osnovna šola 8 talcev Logatec Podružnica Laze', 1, NULL, 'Logatec', 1370, 37, 4, 1, '45289018', '5084687001', ''),
(95, 'Osnovna šola Adama Bohoriča Brestanica', 1, NULL, 'Brestanica', 8280, 38, 6, 1, '38506467', '5083940000', 'Martina Ivačič'),
(96, 'Osnovna šola Angela Besednjaka Maribor', 1, NULL, 'Maribor', 2000, 2, 1, 1, '86623265', '5085187000', 'Vesna Kumer'),
(97, 'Osnovna šola Anice Černejeve Makole', 1, NULL, 'Makole', 2321, 39, 1, 1, '53210336', '5087651000', 'Jožica Kaučič'),
(98, 'Osnovna šola Antona Aškerca Rimske Toplice', 1, NULL, 'Rimske Toplice', 3272, 40, 7, 1, '81377231', '5924359000', 'Manica Skok'),
(99, 'Osnovna šola Antona Aškerca Rimske Toplice Podružnica Jurklošter', 1, NULL, 'Jurklošter', 3273, 40, 7, 1, NULL, '5924359002', ''),
(100, 'Osnovna šola Antona Aškerca Rimske Toplice Podružnica Lažiše', 1, NULL, 'Rimske Toplice', 3272, 40, 7, 1, NULL, '5924359003', ''),
(101, 'Osnovna šola Antona Aškerca Rimske Toplice Podružnica Sedraž', 1, NULL, 'Laško', 3270, 40, 7, 1, NULL, '5924359004', ''),
(102, 'Osnovna šola Antona Aškerca Rimske Toplice Podružnica Zidani Most', 1, NULL, 'Zidani Most', 1432, 40, 7, 1, NULL, '5924359005', ''),
(103, 'Osnovna šola Antona Aškerca Velenje', 1, NULL, 'Velenje', 3320, 41, 7, 1, '25656317', '5088224000', 'Zdenko Gorišek'),
(104, 'Osnovna šola Antona Aškerca Velenje Podružnica Pesje', 1, NULL, 'Velenje', 3320, 41, 7, 1, '25656317', '5088224001', ''),
(105, 'Osnovna šola Antona Globočnika Podružnica Bukovje', 1, NULL, 'Postojna', 6230, 42, 12, 1, '44439407', '5496829001', ''),
(106, 'Osnovna šola Antona Globočnika Podružnica Planina', 1, NULL, 'Planina', 6232, 42, 12, 1, '44439407', '5496829002', ''),
(107, 'Osnovna šola Antona Globočnika Podružnica Studeno', 1, NULL, 'Postojna', 6230, 42, 12, 1, '44439407', '5496829003', ''),
(108, 'Osnovna šola Antona Globočnika Postojna', 1, NULL, 'Postojna', 6230, 42, 12, 1, '44439407', '5496829000', 'Sabina Ileršič Kovšca'),
(109, 'Osnovna šola Antona Ingoliča Spodnja Polskava', 1, NULL, 'Pragersko', 2331, 1, 1, 1, '67396488', '5090032000', 'Danica Veber'),
(110, 'Osnovna šola Antona Ingoliča Spodnja Polskava Podružnica Pragersko', 1, NULL, 'Pragersko', 2331, 1, 1, 1, '67396488', '5090032001', ''),
(111, 'Osnovna šola Antona Ingoliča Spodnja Polskava Podružnica Zgornja Polskava', 1, NULL, 'Zgornja Polskava', 2314, 1, 1, 1, '67396488', '5090032002', ''),
(112, 'Osnovna šola Antona Martina Slomška Vrhnika', 1, NULL, 'Vrhnika', 1360, 43, 4, 1, '60066792', '1534980000', 'Darja Guzelj'),
(113, 'Osnovna šola Antona Tomaža Linharta Radovljica', 1, NULL, 'Radovljica', 4240, 13, 3, 1, '18782400', '5087341000', 'Zlata Rejc'),
(114, 'Osnovna šola Antona Tomaža Linharta Radovljica Podružnica Ljubno', 1, NULL, 'Podnart', 4244, 13, 3, 1, '18782400', '5087341002', '---'),
(115, 'Osnovna šola Antona Tomaža Linharta Radovljica Podružnica Mošnje', 1, NULL, 'Radovljica', 4240, 13, 3, 1, '18782400', '5087341003', '---'),
(116, 'Osnovna šola Antona Ukmarja Koper', 1, NULL, 'Koper - Capodistria', 6000, 20, 9, 1, '71906096', '5231825000', 'Gabrijela Dolinšek'),
(117, 'Osnovna šola Antona Šibelja - Stjenka Komen', 1, NULL, 'Komen', 6223, 44, 9, 1, '23027746', '5087554000', 'Nives Cek'),
(118, 'Osnovna šola Antona Šibelja - Stjenka Komen Podružnica Štanjel', 1, NULL, 'Štanjel', 6222, 44, 9, 1, '0', '5087554001', '---'),
(119, 'Osnovna šola Antona Žnideršiča Ilirska Bistrica', 1, NULL, 'Ilirska Bistrica', 6250, 45, 12, 1, '24128503', '5624525000', 'Karmen Šepec'),
(120, 'Osnovna šola Artiče', 1, NULL, 'Artiče', 8253, 14, 6, 1, '86290185', '5083559000', 'Vesna Bogovič'),
(121, 'Osnovna šola Bakovci', 1, NULL, 'Murska Sobota', 9000, 3, 2, 1, '10335234', '5088968000', 'Vanda Sobočan'),
(122, 'Osnovna šola Bakovci Podružnica Dokležovje', 1, NULL, 'Beltinci', 9231, 46, 2, 1, '10335234', '5088968001', '---'),
(123, 'Osnovna šola Belokranjskega odreda Semič', 1, NULL, 'Semič', 8333, 47, 8, 1, '78628326', '5085349000', 'Silva Jančan'),
(124, 'Osnovna šola Belokranjskega odreda Semič Podružnična šola Štrekljevec', 1, NULL, 'Semič', 8333, 47, 8, 1, '78628326', '5085349004', 'Simona Ritonja'),
(125, 'Osnovna šola Beltinci', 1, NULL, 'Beltinci', 9231, 46, 2, 1, '41251717', '5085560000', 'Mateja Horvat'),
(126, 'Osnovna šola Beltinci Podružnica Melinci', 1, NULL, 'Beltinci', 9231, 46, 2, 1, '41251717', '5085560004', '---'),
(127, 'Osnovna šola Benedikt', 1, NULL, 'Benedikt', 2234, 48, 1, 1, '83252517', '5084032000', 'Milan Gabrovec'),
(128, 'Osnovna šola Bežigrad', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '51149877', '5089913000', 'Maja Rakun Beber'),
(129, 'Osnovna šola Bistrica ob Sotli', 1, NULL, 'Bistrica ob Sotli', 3256, 49, 7, 1, '71028951', '5087902000', 'Bogomir Marčinković'),
(130, 'Osnovna šola Bistrica pri Tržiču', 1, NULL, 'Tržič', 4290, 50, 3, 1, '55429483', '5088135000', 'Štefan Žun'),
(131, 'Osnovna šola Bistrica pri Tržiču Podružnica Kovor', 1, NULL, 'Tržič', 4290, 50, 3, 1, '55429483', '5088135001', ''),
(132, 'Osnovna šola Bizeljsko', 1, NULL, 'Bizeljsko', 8259, 14, 6, 1, '92015930', '5088607000', 'Metka Kržan'),
(133, 'Osnovna šola Bičevje', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '43397883', '5084512000', 'Miriam Stanonik'),
(134, 'Osnovna šola Blanca', 1, NULL, 'Blanca', 8283, 51, 6, 1, '49104624', '5087473000', 'Vincenc Frece'),
(135, 'Osnovna šola Blaža Arniča Luče', 1, NULL, 'Luče', 3334, 52, 7, 1, '64095053', '5085551000', 'Valerija Robnik'),
(136, 'Osnovna šola Blaža Arniča Luče Podružnica Solčava', 1, NULL, 'Solčava', 3335, 53, 7, 1, '64095053', '5085551002', '---'),
(137, 'Osnovna šola Blaža Kocena Ponikva', 1, NULL, 'Ponikva', 3232, 54, 7, 1, '34597085', '5087783000', 'Andreja Ocvirk'),
(138, 'Osnovna šola Bogojina', 1, NULL, 'Bogojina', 9222, 10, 2, 1, '72026804', '5088976000', 'Sabina Juhart'),
(139, 'Osnovna šola Bojana Ilicha Maribor', 1, NULL, 'Maribor', 2000, 2, 1, 1, '90652363', '5085110000', 'Štefan Muraus'),
(140, 'Osnovna šola Borisa Kidriča Kidričevo', 1, NULL, 'Kidričevo', 2325, 55, 1, 1, '60809051', '5087066000', 'Alenka Kutnjak'),
(141, 'Osnovna šola Borisa Kidriča Podružnica Lovrenc na Dravskem polju', 1, NULL, 'Lovrenc na Dravskem polju', 2324, 55, 1, 1, '60809051', '5087066001', ''),
(142, 'Osnovna šola Bovec', 1, NULL, 'Bovec', 5230, 56, 10, 1, '61582476', '5090091000', 'Iztok Kenda'),
(143, 'Osnovna šola Bovec Podružnica Soča', 1, NULL, 'Soča', 5232, 56, 10, 1, '61582476', '5090091002', '---'),
(144, 'Osnovna šola Bovec Podružnica Žaga', 1, NULL, 'Srpenica', 5224, 56, 10, 1, '61582476', '5090091003', '---'),
(145, 'Osnovna šola Boštanj', 1, NULL, 'Boštanj', 8294, 51, 6, 1, '48285200', '5087481000', 'Vesna Vidic Jeraj'),
(146, 'Osnovna šola Božidarja Jakca Ljubljana', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '44901062', '5623758000', 'Nataša Krajnčan'),
(147, 'Osnovna šola Božidarja Jakca Ljubljana Podružnica Hrušica', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '44901062', '5623758001', '---'),
(148, 'Osnovna šola Branik', 1, NULL, 'Branik', 5295, 24, 10, 1, '33669040', '5085799000', 'Davorin Majhenič'),
(149, 'Osnovna šola Braslovče', 1, NULL, 'Braslovče', 3314, 57, 7, 1, '28733533', '5088496000', 'Andreja Zupan'),
(150, 'Osnovna šola Braslovče Podružnica Gomilsko', 1, NULL, 'Gomilsko', 3303, 57, 7, 1, '28733533', '5088496002', ''),
(151, 'Osnovna šola Braslovče Podružnica Letuš', 1, NULL, 'Šmartno ob Paki', 3327, 57, 7, 1, '28733533', '5088496001', ''),
(152, 'Osnovna šola Braslovče Podružnica Trnava', 1, NULL, 'Gomilsko', 3303, 57, 7, 1, NULL, '5088496004', ''),
(153, 'Osnovna šola Breg Ptuj', 1, NULL, 'Ptuj', 2250, 26, 1, 1, '70196958', '5087155000', 'Milan Fakin'),
(154, 'Osnovna šola Brezno - Podvelka', 1, NULL, 'Podvelka', 2363, 58, 5, 1, '42630142', '5089816000', 'Irena Jelenko'),
(155, 'Osnovna šola Brezno - Podvelka Podružnica Kapla na Kozjaku', 1, NULL, 'Kapla', 2362, 58, 5, 1, '42630142', '5089816005', '---'),
(156, 'Osnovna šola Brezno - Podvelka Podružnica Lehen na Pohorju', 1, NULL, 'Podvelka', 2363, 58, 5, 1, '42630142', '5089816001', 'Irena Jelenko'),
(157, 'Osnovna šola Brezovica Podružnica Notranje gorice', 1, NULL, 'Notranje Gorice', 1357, 59, 4, 1, '24113794', '5089646001', ''),
(158, 'Osnovna šola Brezovica pri Ljubljani', 1, NULL, 'Brezovica pri Ljubljani', 1351, 59, 4, 1, '24113794', '5089646000', 'Vladimir Hanžekovič'),
(159, 'Osnovna šola Brežice', 1, NULL, 'Brežice', 8250, 14, 6, 1, '97051667', '5085896000', 'Marija Lubšina Novak'),
(160, 'Osnovna šola Brinje Grosuplje', 1, NULL, 'Grosuplje', 1290, 60, 4, 1, '29928419', '1193481000', 'Irena Kogovšek'),
(161, 'Osnovna šola Brinje Grosuplje Podružnica Polica', 1, NULL, 'Grosuplje', 1290, 60, 4, 1, '29928419', '1193481001', '---'),
(162, 'Osnovna šola Brusnice', 1, NULL, 'Brusnice', 8321, 16, 8, 1, '49987836', '5086361000', 'Jasmina Hidek'),
(163, 'Osnovna šola Bršljin', 1, NULL, 'Novo mesto', 8000, 16, 8, 1, '78931606', '5086868000', 'Martina Picek'),
(164, 'Osnovna šola Cankova', 1, NULL, 'Cankova', 9261, 61, 2, 1, '10798226', '5085608000', 'Jolanda Maruško'),
(165, 'Osnovna šola Center Novo mesto', 1, NULL, 'Novo mesto', 8000, 16, 8, 1, '38521610', '5086825000', 'Marija Vranešič'),
(166, 'Osnovna šola Center Novo mesto Podružnica Mali Slatnik', 1, NULL, 'Novo mesto', 8000, 16, 8, 1, '38521610', '5086825001', '---'),
(167, 'Osnovna šola Cerklje ob Krki', 1, NULL, 'Cerklje ob Krki', 8263, 14, 6, 1, '16258193', '5083575000', 'Andreja Urbanč'),
(168, 'Osnovna šola Cerkno', 1, NULL, 'Cerkno', 5282, 62, 10, 1, '44292180', '5082960000', 'Milan Koželj'),
(169, 'Osnovna šola Cerkno Podružnica Novaki', 1, NULL, 'Cerkno', 5282, 62, 10, 1, '44292180', '5082960001', ''),
(170, 'Osnovna šola Cerkno Podružnica Šebrelje', 1, NULL, 'Cerkno', 5282, 62, 10, 1, '44292180', '5082960003', ''),
(171, 'Osnovna šola Cerkvenjak - Vitomarci', 1, NULL, 'Cerkvenjak', 2236, 63, 1, 1, '43386024', '5084016000', 'Mirko Žmavc'),
(172, 'Osnovna šola Cerkvenjak Podružnica Vitomarci', 1, NULL, 'Vitomarci', 2255, 64, 1, 1, '0', '5084016002', '---'),
(173, 'Osnovna šola Cirila Kosmača Piran', 1, NULL, 'Piran - Pirano', 6330, 17, 9, 1, '84652594', '5090075000', 'Zlata Milič'),
(174, 'Osnovna šola Cirila Kosmača Piran Podružnica Portorož', 1, NULL, 'Portorož - Portorose', 6320, 17, 9, 1, '84652594', '5090075001', '---'),
(175, 'Osnovna šola Cirkovce', 1, NULL, 'Cirkovce', 2326, 55, 1, 1, '70374619', '5086973000', 'Ivanka Korez'),
(176, 'Osnovna šola Cirkulane - Zavrč', 1, NULL, 'Cirkulane', 2282, 65, 1, 1, '68357753', '5089247000', 'Kristina Artenjak'),
(177, 'Osnovna šola Cirkulane Podružnica Zavrč', 1, NULL, 'Zavrč', 2283, 66, 1, 1, '68357753', '5089247001', '---'),
(178, 'Osnovna šola Col', 1, NULL, 'Col', 5273, 67, 10, 1, '11095822', '5082544000', 'Rajko Ipavec'),
(179, 'Osnovna šola Col Podružnica Podkraj', 1, NULL, 'Col', 5273, 67, 10, 1, '11095822', '5082544001', '---'),
(180, 'Osnovna šola Cvetka Golarja Škofja Loka', 1, NULL, 'Škofja Loka', 4220, 31, 3, 1, '72155680', '5087821000', 'Karla Krajnik'),
(181, 'Osnovna šola Cvetka Golarja Škofja Loka Podružnica Reteče', 1, NULL, 'Škofja Loka', 4220, 31, 3, 1, '72155680', '5087821001', '---'),
(182, 'Osnovna šola Danila Lokarja Ajdovščina', 1, NULL, 'Ajdovščina', 5270, 67, 10, 1, '42140153', '5082528000', 'Vladimir Bačič'),
(183, 'Osnovna šola Danila Lokarja Ajdovščina Podružnica Lokavec', 1, NULL, 'Ajdovščina', 5270, 67, 10, 1, '42140153', '5082528001', ''),
(184, 'Osnovna šola Danile Kumar Ljubljana', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '42494940', '5083389000', 'Mojca Mihelič'),
(185, 'Osnovna šola Danile Kumar Ljubljana, mednarodna šola', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '42494940', '5083389002', ''),
(186, 'Osnovna šola Dante Alighieri Izola', 1, NULL, 'Izola - Isola', 6310, 68, 9, 1, '88215857', '5089514000', 'Simona Angelini'),
(187, 'Osnovna šola Davorina Jenka Cerklje na Gorenjskem', 1, NULL, 'Cerklje na Gorenjskem', 4207, 69, 3, 1, '40296407', '5086027000', 'Damijana Božič Močnik'),
(188, 'Osnovna šola Davorina Jenka Podružnica Zalog', 1, NULL, 'Cerklje na Gorenjskem', 4207, 69, 3, 1, '40296407', '5086027001', '---'),
(189, 'Osnovna šola Dekani', 1, NULL, 'Dekani', 6271, 20, 9, 1, '18370071', '5083834000', 'Marjan Ruter'),
(190, 'Osnovna šola Deskle', 1, NULL, 'Deskle', 5210, 70, 10, 1, '82684669', '5085772000', 'Vojko Simčič'),
(191, 'Osnovna šola Destrnik - Trnovska vas', 1, NULL, 'Destrnik', 2253, 71, 1, 1, '68493002', '5086990000', 'Drago Skurjeni'),
(192, 'Osnovna šola Destrnik Podružnica Trnovska vas', 1, NULL, 'Trnovska vas', 2254, 72, 1, 1, '68493002', '5086990003', ''),
(193, 'Osnovna šola Dob', 1, NULL, 'Dob', 1233, 73, 4, 1, '98266144', '5084733000', 'Barbka Drobnič'),
(194, 'Osnovna šola Dob Podružnica Krtina', 1, NULL, 'Dob', 1233, 73, 4, 1, '98266144', '5084733001', ''),
(195, 'Osnovna šola Dobje', 1, NULL, 'Dobje pri Planini', 3224, 74, 7, 1, '84077867', '5582911000', 'Suzana Plemenitaš Centrih'),
(196, 'Osnovna šola Dobova', 1, NULL, 'Dobova', 8257, 14, 6, 1, '16691059', '5082579000', 'Ivana Baškovič'),
(197, 'Osnovna šola Dobova Podružnica Kapele', 1, NULL, 'Kapele', 8258, 14, 6, 1, '16691059', '5082579001', ''),
(198, 'Osnovna šola Dobravlje', 1, NULL, 'Dobravlje', 5263, 67, 10, 1, '89450116', '5085888000', 'Mirjam Kalin'),
(199, 'Osnovna šola Dobravlje Podružnica Skrilje', 1, NULL, 'Dobravlje', 5263, 67, 10, 1, '89450116', '5085888007', ''),
(200, 'Osnovna šola Dobravlje Podružnica Vipavski Križ', 1, NULL, 'Ajdovščina', 5270, 67, 10, 1, '89450116', '5085888005', ''),
(201, 'Osnovna šola Dobravlje Podružnica Vrtovin', 1, NULL, 'Črniče', 5262, 67, 10, 1, '89450116', '5085888006', ''),
(202, 'Osnovna šola Dobravlje Podružnica Šmarje', 1, NULL, 'Branik', 5295, 67, 10, 1, '89450116', '5085888004', ''),
(203, 'Osnovna šola Dobravlje Podružnica Črniče', 1, NULL, 'Črniče', 5262, 67, 10, 1, '89450116', '5085888002', ''),
(204, 'Osnovna šola Dobrepolje', 1, NULL, 'Videm - Dobrepolje', 1312, 75, 4, 1, '44770103', '5089956000', 'Ivan Grandovec'),
(205, 'Osnovna šola Dobrepolje Podružnica Kompolje', 1, NULL, 'Videm - Dobrepolje', 1312, 75, 4, 1, '44770103', '5089956001', ''),
(206, 'Osnovna šola Dobrepolje Podružnica Ponikve', 1, NULL, 'Videm - Dobrepolje', 1312, 75, 4, 1, '44770103', '5089956002', ''),
(207, 'Osnovna šola Dobrepolje Podružnica Struge', 1, NULL, 'Struge', 1313, 75, 4, 1, '44770103', '5089956003', ''),
(208, 'Osnovna šola Dobrna', 1, NULL, 'Dobrna', 3204, 76, 7, 1, '15988945', '5082668000', 'Darinka Stagoj'),
(209, 'Osnovna šola Dobrova', 1, NULL, 'Dobrova', 1356, 77, 4, 1, '13274546', '5084415000', 'Viljem Kovačič'),
(210, 'Osnovna šola Dobrovo', 1, NULL, 'Dobrovo v Brdih', 5212, 78, 10, 1, '45507201', '5089000000', 'Vesna Filej'),
(211, 'Osnovna šola Dobrovo Podružnica Kojsko', 1, NULL, 'Kojsko', 5211, 78, 10, 1, '45507201', '5089000003', ''),
(212, 'Osnovna šola Dolenjske Toplice', 1, NULL, 'Dolenjske Toplice', 8350, 79, 8, 1, '51655535', '5086370000', 'Irena Šmid Hudoklin'),
(213, 'Osnovna šola Domžale', 1, NULL, 'Domžale', 1230, 73, 4, 1, '94835039', '5082803000', 'Uroš Govc'),
(214, 'Osnovna šola Domžale Podružnica Ihan', 1, NULL, 'Domžale', 1230, 73, 4, 1, '94835039', '5082803001', '---'),
(215, 'Osnovna šola Dornberk', 1, NULL, 'Dornberk', 5294, 24, 10, 1, '30649366', '5085802000', 'Dragica Vidmar'),
(216, 'Osnovna šola Dornberk Podružnica Prvačina', 1, NULL, 'Prvačina', 5297, 24, 10, 1, '30649366', '5085802002', '---'),
(217, 'Osnovna šola Draga Bajca Vipava', 1, NULL, 'Vipava', 5271, 80, 10, 1, '10582789', '5083532000', 'Alenka Nussdorfer Bizjak'),
(218, 'Osnovna šola Draga Bajca Vipava Podružnica Goče', 1, NULL, 'Vipava', 5271, 80, 10, 1, '10582789', '5083532002', ''),
(219, 'Osnovna šola Draga Bajca Vipava Podružnica Podnanos', 1, NULL, 'Podnanos', 5272, 80, 10, 1, '10582789', '5083532004', ''),
(220, 'Osnovna šola Draga Bajca Vipava Podružnica Vrhpolje', 1, NULL, 'Vipava', 5271, 80, 10, 1, '10582789', '5083532005', ''),
(221, 'Osnovna šola Draga Kobala Maribor', 1, NULL, 'Maribor', 2000, 2, 1, 1, '87328704', '5085250000', 'Aleksander Jeršič'),
(222, 'Osnovna šola Draga Kobala Maribor Podružnica Brezje', 1, NULL, 'Maribor', 2000, 2, 1, 1, '87328704', '5085250001', ''),
(223, 'Osnovna šola Dragomelj', 1, NULL, 'Domžale', 1230, 73, 4, 1, '88530264', '2197197000', 'Metka Murn'),
(224, 'Osnovna šola Dragomirja Benčiča - Brkina Hrpelje', 1, NULL, 'Kozina', 6240, 81, 9, 1, '80880258', '5089379000', 'Janja Babič'),
(225, 'Osnovna šola Dragomirja Benčiča - Brkina Hrpelje Podružnica Obrov', 1, NULL, 'Obrov', 6243, 81, 9, 1, '80880258', '5089379003', ''),
(226, 'Osnovna šola Dragotina Ketteja Ilirska Bistrica', 1, NULL, 'Ilirska Bistrica', 6250, 45, 12, 1, '78261023', '5624533000', 'Ester Juriševič'),
(227, 'Osnovna šola Dramlje', 1, NULL, 'Dramlje', 3222, 54, 7, 1, '84523603', '5087775000', 'Stanislav Karel Jančič'),
(228, 'Osnovna šola Dravlje', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '79401392', '5204950000', 'Erna Čibej'),
(229, 'Osnovna šola Drska', 1, NULL, 'Novo mesto', 8000, 16, 8, 1, '63882612', '1574710000', 'Nevenka Kulovec'),
(230, 'Osnovna šola Duplek', 1, NULL, 'Spodnji Duplek', 2241, 82, 1, 1, '70388717', '5085233000', 'Đano Novak'),
(231, 'Osnovna šola Duplek Podružnica Dvorjane', 1, NULL, 'Spodnji Duplek', 2241, 82, 1, 1, '70388717', '5085233002', '---'),
(232, 'Osnovna šola Duplek Podružnica Zg. Duplek', 1, NULL, 'Spodnji Duplek', 2241, 82, 1, 1, '70388717', '5085233001', '---'),
(233, 'Osnovna šola Dutovlje', 1, NULL, 'Dutovlje', 6221, 83, 9, 1, '71215719', '5087546000', 'Doris Orel'),
(234, 'Osnovna šola Dutovlje Podružnica Tomaj', 1, NULL, 'Dutovlje', 6221, 83, 9, 1, '71215719', '5087546003', ''),
(235, 'Osnovna šola Dušana Bordona Semedela - Koper', 1, NULL, 'Koper - Capodistria', 6000, 20, 9, 1, '84366451', '5083141000', 'Vesna Lavriša'),
(236, 'Osnovna šola Dušana Flisa Hoče', 1, NULL, 'Hoče', 2311, 84, 1, 1, '37423754', '5085853000', 'Bojan Struger'),
(237, 'Osnovna šola Dušana Flisa Hoče Podružnica Reka-Pohorje', 1, NULL, 'Hoče', 2311, 84, 1, 1, '37423754', '5085853001', '---'),
(238, 'Osnovna šola Dušana Muniha Most na Soči', 1, NULL, 'Most na Soči', 5216, 27, 10, 1, '59594063', '5089506000', 'Karmen Kozorog'),
(239, 'Osnovna šola Dušana Muniha Most na Soči Podružnica Dolenja Trebuša', 1, NULL, 'Slap ob Idrijci', 5283, 27, 10, 1, '59594063', '5089506001', 'Karmen Kozorog'),
(240, 'Osnovna šola Dušana Muniha Most na Soči Podružnica Podmelec', 1, NULL, 'Most na Soči', 5216, 27, 10, 1, '59594063', '5089506004', 'Karmen Kozorog'),
(241, 'Osnovna šola Dušana Muniha Most na Soči Podružnica Šentviška gora', 1, NULL, 'Slap ob Idrijci', 5283, 27, 10, 1, '59594063', '5089506005', 'Karmen Kozorog'),
(242, 'Osnovna šola Elvire Vatovec Prade - Koper', 1, NULL, 'Koper - Capodistria', 6000, 20, 9, 1, '22889426', '5083168000', 'Franka Pegan Glavina'),
(243, 'Osnovna šola Elvire Vatovec Prade - Koper Podružnica Sv. Anton', 1, NULL, 'Pobegi', 6276, 20, 9, 1, '22889426', '5083168001', ''),
(244, 'Osnovna šola F. S. Finžgarja Lesce', 1, NULL, 'Lesce', 4248, 13, 3, 1, '61563455', '5087325000', 'Janez Zupan'),
(245, 'Osnovna šola F. S. Finžgarja Lesce Podružnica Begunje', 1, NULL, 'Begunje na Gorenjskem', 4275, 13, 3, 1, NULL, '5087325001', ''),
(246, 'Osnovna šola Fara', 1, NULL, 'Kostel', 1336, 85, 8, 1, '56815905', '5083095000', 'Martin Marinč'),
(247, 'Osnovna šola Fara Podružnica Osilnica', 1, NULL, 'Osilnica', 1337, 86, 8, 1, '56815905', '5083095001', ''),
(248, 'Osnovna šola Ferda Vesela Podružnica v Centru za zdravljenje bolezni otrok', 1, NULL, 'Šentvid pri Stični', 1296, 87, 4, 1, '0', '5085357003', '---'),
(249, 'Osnovna šola Ferda Vesela Šentvid pri Stični', 1, NULL, 'Šentvid pri Stični', 1296, 87, 4, 1, '59034220', '5085357000', 'Janez Peterlin'),
(250, 'Osnovna šola Ferda Vesela Šentvid pri Stični Podružnica Temenica', 1, NULL, 'Šentvid pri Stični', 1296, 87, 4, 1, '59034220', '5085357002', '---'),
(251, 'Osnovna šola Fokovci', 1, NULL, 'Fokovci', 9208, 10, 2, 1, '79277802', '5085624000', 'Suzana Deutsch'),
(252, 'Osnovna šola Fram', 1, NULL, 'Fram', 2313, 88, 1, 1, '20947879', '5085241000', 'Zoran Kregar'),
(253, 'Osnovna šola Frana Albrehta Kamnik', 1, NULL, 'Kamnik', 1241, 6, 4, 1, '64526208', '5083036000', 'Rafko Lah'),
(254, 'Osnovna šola Frana Albrehta Kamnik Podružnica Mekinje', 1, NULL, 'Kamnik', 1241, 6, 4, 1, '64526208', '5083036002', ''),
(255, 'Osnovna šola Frana Albrehta Kamnik Podružnica Nevlje', 1, NULL, 'Kamnik', 1241, 6, 4, 1, '64526208', '5083036003', ''),
(256, 'Osnovna šola Frana Albrehta Kamnik Podružnica Tunjice', 1, NULL, 'Kamnik', 1241, 6, 4, 1, '64526208', '5083036004', ''),
(257, 'Osnovna šola Frana Albrehta Kamnik Podružnica Vranja peč', 1, NULL, 'Kamnik', 1241, 6, 4, 1, '64526208', '5083036005', ''),
(258, 'Osnovna šola Frana Erjavca Nova Gorica', 1, NULL, 'Nova Gorica', 5000, 24, 10, 1, '50989456', '5221625000', 'Mirjam Bratož'),
(259, 'Osnovna šola Frana Kocbeka Gornji Grad', 1, NULL, 'Gornji grad', 3342, 89, 7, 1, '50597698', '5088933000', 'Lilijana Bele'),
(260, 'Osnovna šola Frana Kocbeka Gornji grad Podružnica Bočna', 1, NULL, 'Gornji grad', 3342, 89, 7, 1, '50597698', '5088933005', '---'),
(261, 'Osnovna šola Frana Kocbeka Gornji grad Podružnica Nova Štifta', 1, NULL, 'Gornji grad', 3342, 89, 7, 1, '50597698', '5088933003', '---'),
(262, 'Osnovna šola Frana Kranjca Celje', 1, NULL, 'Celje', 3000, 15, 7, 1, '27612457', '5082641000', 'Danica Šalej'),
(263, 'Osnovna šola Frana Metelka Škocjan', 1, NULL, 'Škocjan', 8275, 90, 8, 1, '70483345', '5086388000', 'Irena Čengija Peterlin'),
(264, 'Osnovna šola Frana Metelka Škocjan Podružnica Bučka', 1, NULL, 'Bučka', 8276, 90, 8, 1, '70483345', '5086388002', '---'),
(265, 'Osnovna šola Frana Roša Celje', 1, NULL, 'Celje', 3000, 15, 7, 1, '89921658', '5186650000', 'Mojca Kolin'),
(266, 'Osnovna šola Franca Lešnika - Vuka Slivnica pri Mariboru', 1, NULL, 'Orehova vas', 2312, 84, 1, 1, '69830835', '5085306000', 'Anton Obreht'),
(267, 'Osnovna šola Franca Rozmana - Staneta Ljubljana', 1, NULL, 'Ljubljana - Šentvid', 1210, 5, 4, 1, '55290639', '5086701000', 'Božo Starašinič'),
(268, 'Osnovna šola Franca Rozmana - Staneta Maribor', 1, NULL, 'Maribor', 2000, 2, 1, 1, '25901010', '5085837000', 'Breda Kutnjak'),
(269, 'Osnovna šola Franca Rozmana - Staneta Maribor Podružnica Košaki', 1, NULL, 'Maribor', 2000, 2, 1, 1, '25901010', '5085837001', '---'),
(270, 'Osnovna šola Franceta Bevka Ljubljana', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '75844818', '5083419000', 'Barbara Kampjut'),
(271, 'Osnovna šola Franceta Bevka Tolmin', 1, NULL, 'Tolmin', 5220, 27, 10, 1, '27755975', '5272653000', 'Vladimir Mavri'),
(272, 'Osnovna šola Franceta Bevka Tolmin Podružnica Anton Majnik Volče', 1, NULL, 'Tolmin', 5220, 27, 10, 1, '27755975', '5272653001', ''),
(273, 'Osnovna šola Franceta Bevka Tolmin Podružnica Kamno', 1, NULL, 'Tolmin', 5220, 27, 10, 1, '27755975', '5272653002', ''),
(274, 'Osnovna šola Franceta Prešerna Kranj', 1, NULL, 'Kranj', 4000, 19, 3, 1, '94256454', '5086035000', 'Aleš Žitnik'),
(275, 'Osnovna šola Franceta Prešerna Maribor', 1, NULL, 'Maribor', 2000, 2, 1, 1, '78028116', '5085195000', 'Marta Otič'),
(276, 'Osnovna šola Franceta Prešerna Podružnica Kokrica', 1, NULL, 'Kranj', 4000, 19, 3, 1, '94256454', '5086035002', 'Dijana Korošec'),
(277, 'Osnovna šola Franceta Prešerna Podružnica Stane Lenardon Razvanje', 1, NULL, 'Maribor', 2000, 2, 1, 1, '78028116', '5085195001', ''),
(278, 'Osnovna šola Franceta Prešerna Črenšovci', 1, NULL, 'Črenšovci', 9232, 91, 2, 1, '16814487', '5089697000', 'Marija Horvat'),
(279, 'Osnovna šola Franja Goloba Prevalje', 1, NULL, 'Prevalje', 2391, 92, 5, 1, '73077500', '5087384000', 'Mira Hancman'),
(280, 'Osnovna šola Franja Goloba Prevalje Podružnica Holmec', 1, NULL, 'Prevalje', 2391, 92, 5, 1, '73077500', '5087384002', ''),
(281, 'Osnovna šola Franja Goloba Prevalje Podružnica Leše', 1, NULL, 'Prevalje', 2391, 92, 5, 1, '73077500', '5087384001', ''),
(282, 'Osnovna šola Franja Goloba Prevalje Podružnica Šentanel', 1, NULL, 'Prevalje', 2391, 92, 5, 1, '73077500', '5087384003', ''),
(283, 'Osnovna šola Franja Malgaja Šentjur', 1, NULL, 'Šentjur', 3230, 54, 7, 1, '48313033', '5087805000', 'Marjan Gradišnik'),
(284, 'Osnovna šola Franja Malgaja Šentjur Podružnica Blagovna', 1, NULL, 'Šentjur', 3230, 54, 7, 1, '48313033', '5087805001', ''),
(285, 'Osnovna šola Frankolovo', 1, NULL, 'Frankolovo', 3213, 93, 7, 1, '12132233', '5084709000', 'Peter Žurej'),
(286, 'Osnovna šola Gabrovka - Dole', 1, NULL, 'Gabrovka', 1274, 23, 4, 1, '84580062', '5084873000', 'Igor Hostnik'),
(287, 'Osnovna šola Gabrovka Podružnica Dole pri Litiji', 1, NULL, 'Dole pri Litiji', 1273, 23, 4, 1, '84580062', '5084873001', '---'),
(288, 'Osnovna šola Globoko', 1, NULL, 'Globoko', 8254, 14, 6, 1, '45800316', '5082587000', 'Rozika Vodopivec'),
(289, 'Osnovna šola Gorica Velenje', 1, NULL, 'Velenje', 3320, 41, 7, 1, '55683398', '5221340000', 'Ivan Planinc'),
(290, 'Osnovna šola Gorica Velenje Podružnica Vinska Gora', 1, NULL, 'Velenje', 3320, 41, 7, 1, '55683398', '5221340001', ''),
(291, 'Osnovna šola Gorišnica', 1, NULL, 'Gorišnica', 2272, 94, 1, 1, '52630692', '5087023000', 'Milan Šilak'),
(292, 'Osnovna šola Gorje', 1, NULL, 'Zgornje Gorje', 4247, 95, 3, 1, '99229692', '5087317000', 'Milan Rejc'),
(293, 'Osnovna šola Gornja Radgona', 1, NULL, 'Gornja Radgona', 9250, 96, 2, 1, '18671624', '5083745000', 'Dušan Zagorc'),
(294, 'Osnovna šola Gornji Petrovci', 1, NULL, 'Petrovci', 9203, 97, 2, 1, '61749206', '5085586000', 'Johann Laco'),
(295, 'Osnovna šola Grad', 1, NULL, 'Grad', 9264, 98, 2, 1, '23698110', '5085594000', 'Viktor Navotnik'),
(296, 'Osnovna šola Gradec', 1, NULL, 'Litija', 1270, 23, 4, 1, '42070651', '5689155000', 'Tatjana Gombač'),
(297, 'Osnovna šola Gradec Podružnica Hotič', 1, NULL, 'Litija', 1270, 23, 4, 1, '42070651', '5689155001', 'Elizabeta Bučar'),
(298, 'Osnovna šola Gradec Podružnica Jevnica', 1, NULL, 'Kresnice', 1281, 23, 4, 1, '42070651', '5689155002', 'Darja Rajšek'),
(299, 'Osnovna šola Gradec Podružnica Kresnice', 1, NULL, 'Kresnice', 1281, 23, 4, 1, '42070651', '5689155004', 'Angelca Koprivnikar'),
(300, 'Osnovna šola Gradec Podružnica Vače', 1, NULL, 'Vače', 1252, 23, 4, 1, '42070651', '5689155007', 'Aleksandra Štrus'),
(301, 'Osnovna šola Griže', 1, NULL, 'Griže', 3302, 33, 7, 1, '75852390', '5090059000', 'Marija Pavčnik'),
(302, 'Osnovna šola Griže Podružnica Liboje', 1, NULL, 'Petrovče', 3301, 33, 7, 1, '75852390', '5090059001', ''),
(303, 'Osnovna šola Grm Novo mesto', 1, NULL, 'Novo mesto', 8000, 16, 8, 1, '87598167', '5086850000', 'Sonja Simčič'),
(304, 'Osnovna šola Gustava Šiliha Laporje', 1, NULL, 'Laporje', 2318, 1, 1, 1, '36415006', '5087643000', 'Margareta Voglar'),
(305, 'Osnovna šola Gustava Šiliha Velenje', 1, NULL, 'Velenje', 3320, 41, 7, 1, '87755246', '5088208000', 'Liljana Lihteneker'),
(306, 'Osnovna šola Gustava Šiliha Velenje Podružnica Šentilj', 1, NULL, 'Velenje', 3320, 41, 7, 1, '87755246', '5088208002', ''),
(307, 'Osnovna šola Hajdina', 1, NULL, 'Hajdina', 2288, 99, 1, 1, '33939314', '5087031000', 'Vesna Mesarič Lorber'),
(308, 'Osnovna šola Hinka Smrekarja Ljubljana', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '23541300', '5084369000', 'Rebeka Velak'),
(309, 'Osnovna šola Horjul', 1, NULL, 'Horjul', 1354, 100, 4, 1, '99488493', '5084423000', 'Primož Garafol'),
(310, 'Osnovna šola Hruševec Šentjur', 1, NULL, 'Šentjur', 3230, 54, 7, 1, '54735289', '5914914000', 'Robert Gajšek'),
(311, 'Osnovna šola Hruševec Šentjur Podružnica Kalobje', 1, NULL, 'Kalobje', 3233, 54, 7, 1, NULL, '5914914001', ''),
(312, 'Osnovna šola Hudinja', 1, NULL, 'Celje', 3000, 15, 7, 1, '73042323', '5082650000', 'Jože Berk'),
(313, 'Osnovna šola I Murska Sobota', 1, NULL, 'Murska Sobota', 9000, 3, 2, 1, '28051076', '5640245000', 'Tanja Cesnik'),
(314, 'Osnovna šola II Murska Sobota', 1, NULL, 'Murska Sobota', 9000, 3, 2, 1, '10690336', '5640270000', 'Suzana Fartelj'),
(315, 'Osnovna šola II Murska Sobota Podružnica Krog', 1, NULL, 'Murska Sobota', 9000, 3, 2, 1, '10690336', '5640270001', '---'),
(316, 'Osnovna šola III Murska Sobota', 1, NULL, 'Murska Sobota', 9000, 3, 2, 1, '53080548', '5640261000', 'Dominika Sraka'),
(317, 'Osnovna šola Idrija', 1, NULL, 'Idrija', 5280, 22, 10, 1, '75180596', '5082986000', 'Nikolaja Munih'),
(318, 'Osnovna šola Idrija Podružnica Godovič', 1, NULL, 'Godovič', 5275, 22, 10, 1, '75180596', '5082986001', ''),
(319, 'Osnovna šola Idrija Podružnica Zavratec', 1, NULL, 'Rovte', 1373, 22, 10, 1, '75180596', '5082986006', ''),
(320, 'Osnovna šola Ig', 1, NULL, 'Ig', 1292, 101, 4, 1, '72025735', '5084431000', 'Biserka Vičič Malnar'),
(321, 'Osnovna šola Ig Podružnica Golo', 1, NULL, 'Ig', 1292, 101, 4, 1, '72025735', '5084431001', ''),
(322, 'Osnovna šola Ig Podružnica Iška vas', 1, NULL, 'Ig', 1292, 101, 4, 1, '72025735', '5084431002', ''),
(323, 'Osnovna šola Ig Podružnica Tomišelj', 1, NULL, 'Ig', 1292, 101, 4, 1, '72025735', '5084431003', ''),
(324, 'Osnovna šola Istrskega odreda Gračišče', 1, NULL, 'Gračišče', 6272, 20, 9, 1, '78522625', '5083133000', 'Vanja Košpenda'),
(325, 'Osnovna šola Ivana Babiča - Jagra Marezige', 1, NULL, 'Marezige', 6273, 20, 9, 1, '34559477', '5083150000', 'Adelina Pahor'),
(326, 'Osnovna šola Ivana Cankarja Ljutomer', 1, NULL, 'Ljutomer', 9240, 18, 2, 1, '92006582', '5085012000', 'Darja Kosič Auer'),
(327, 'Osnovna šola Ivana Cankarja Ljutomer Podružnica Cven', 1, NULL, 'Ljutomer', 9240, 18, 2, 1, '92006582', '5085012002', ''),
(328, 'Osnovna šola Ivana Cankarja Trbovlje', 1, NULL, 'Trbovlje', 1420, 28, 11, 1, '59416815', '5889286000', 'Mojca Lazar Doberlet'),
(329, 'Osnovna šola Ivana Cankarja Vrhnika', 1, NULL, 'Vrhnika', 1360, 43, 4, 1, '78824966', '5088330000', 'Polonca Šurca Gerdina'),
(330, 'Osnovna šola Ivana Cankarja Vrhnika Podružnica Drenov grič', 1, NULL, 'Vrhnika', 1360, 43, 4, 1, '0', '5088330001', '---'),
(331, 'Osnovna šola Ivana Groharja Škofja Loka', 1, NULL, 'Škofja Loka', 4220, 31, 3, 1, '94792259', '5263620000', 'Marko Primožič'),
(332, 'Osnovna šola Ivana Groharja Škofja Loka Podružnica Bukovica', 1, NULL, 'Selca', 4227, 31, 3, 1, '94792259', '5263620001', '---'),
(333, 'Osnovna šola Ivana Groharja Škofja Loka Podružnica Bukovščica', 1, NULL, 'Selca', 4227, 31, 3, 1, '94792259', '5263620002', '---'),
(334, 'Osnovna šola Ivana Groharja Škofja Loka Podružnica Lenart', 1, NULL, 'Selca', 4227, 31, 3, 1, '94792259', '5263620003', '---'),
(335, 'Osnovna šola Ivana Kavčiča Izlake', 1, NULL, 'Izlake', 1411, 102, 11, 1, '33761663', '5088372000', 'Tatjana Krautberger'),
(336, 'Osnovna šola Ivana Kavčiča Izlake Podružnica Mlinše', 1, NULL, 'Izlake', 1411, 102, 11, 1, '33761663', '5088372002', '---'),
(337, 'Osnovna šola Ivana Roba Šempeter pri Gorici', 1, NULL, 'Šempeter pri Gorici', 5290, 103, 10, 1, '11522399', '5089069000', 'Slavica Bragato'),
(338, 'Osnovna šola Ivana Roba Šempeter pri Gorici Podružnica Vogrsko', 1, NULL, 'Volčja Draga', 5293, 104, 10, 1, '11522399', '5089069001', '---'),
(339, 'Osnovna šola Ivana Roba Šempeter pri Gorici Podružnica Vrtojba', 1, NULL, 'Šempeter pri Gorici', 5290, 103, 10, 1, '11522399', '5089069002', '---'),
(340, 'Osnovna šola Ivana Skvarče Zagorje', 1, NULL, 'Zagorje ob Savi', 1410, 102, 11, 1, '44831994', '5088402000', 'Alenka Ašič'),
(341, 'Osnovna šola Ivana Skvarče Zagorje Podružnica Podkum', 1, NULL, 'Podkum', 1414, 102, 11, 1, '44831994', '5088402002', '---'),
(342, 'Osnovna šola Ivana Skvarče Zagorje Podružnica Čemšenik', 1, NULL, 'Čemšenik', 1413, 102, 11, 1, '44831994', '5088402001', '---'),
(343, 'Osnovna šola Ivana Tavčarja Gorenja vas', 1, NULL, 'Gorenja vas', 4224, 105, 3, 1, '72397870', '5087813000', 'Izidor Selak'),
(344, 'Osnovna šola Ivana Tavčarja Gorenja vas Podružnica Lučine', 1, NULL, 'Gorenja vas', 4224, 105, 3, 1, '72397870', '5087813003', ''),
(345, 'Osnovna šola Ivana Tavčarja Gorenja vas Podružnica Sovodenj', 1, NULL, 'Sovodenj', 4225, 105, 3, 1, '72397870', '5087813005', '---'),
(346, 'Osnovna šola Ivanjkovci', 1, NULL, 'Ivanjkovci', 2259, 25, 1, 1, '41002270', '5900026000', 'Nada Pignar'),
(347, 'Osnovna šola Jakoba Aljaža Kranj', 1, NULL, 'Kranj', 4000, 19, 3, 1, '45147990', '5204941000', 'Milan Rogelj'),
(348, 'Osnovna šola Jakobski Dol', 1, NULL, 'Jakobski dol', 2222, 106, 1, 1, '10092293', '5088836000', 'Zdravko Šoštarić'),
(349, 'Osnovna šola Janka Glazerja Ruše', 1, NULL, 'Ruše', 2342, 29, 1, 1, '51038315', '5088852000', 'Ladislav Pepelnik'),
(350, 'Osnovna šola Janka Kersnika Brdo - Lukovica', 1, NULL, 'Lukovica', 1225, 107, 4, 1, '50409484', '5082790000', 'Anja Podlesnik Fetih'),
(351, 'Osnovna šola Janka Kersnika Brdo - Lukovica Podružnica Blagovica', 1, NULL, 'Blagovica', 1223, 107, 4, 1, '50409484', '5082790001', ''),
(352, 'Osnovna šola Janka Kersnika Brdo - Lukovica Podružnica Krašnja', 1, NULL, 'Lukovica', 1225, 107, 4, 1, '50409484', '5082790003', ''),
(353, 'Osnovna šola Janka Modra Dol pri Ljubljani', 1, NULL, 'Dol pri Ljubljani', 1262, 108, 4, 1, '63332248', '5083354000', 'Gregor Pečan'),
(354, 'Osnovna šola Janka Modra Dol pri Ljubljani Podružnica Dolsko', 1, NULL, 'Dol pri Ljubljani', 1262, 108, 4, 1, '63332248', '5083354003', '---'),
(355, 'Osnovna šola Janka Modra Dol pri Ljubljani Podružnica Senožeti', 1, NULL, 'Dol pri Ljubljani', 1262, 108, 4, 1, '63332248', '5083354004', '---'),
(356, 'Osnovna šola Janka Padežnika Maribor', 1, NULL, 'Maribor', 2000, 2, 1, 1, '82112037', '5085217000', 'Sonja Filipič'),
(357, 'Osnovna šola Janka Ribiča Cezanjevci', 1, NULL, 'Ljutomer', 9240, 18, 2, 1, '94576980', '5084628000', 'Brigita Hojnik'),
(358, 'Osnovna šola Jarenina', 1, NULL, 'Jarenina', 2221, 106, 1, 1, '26152363', '5088844000', 'Alen Krajnc'),
(359, 'Osnovna šola Jelšane', 1, NULL, 'Jelšane', 6254, 45, 12, 1, '83556788', '5083010000', 'Branka Špende Mandić'),
(360, 'Osnovna šola Josipa Vandota Kranjska Gora', 1, NULL, 'Kranjska Gora', 4280, 36, 3, 1, '65736290', '5719038000', 'Cvetka Pavlovčič'),
(361, 'Osnovna šola Jožeta Gorjupa Kostanjevica na Krki', 1, NULL, 'Kostanjevica na Krki', 8311, 109, 6, 1, '47511788', '5083958000', 'Melita Skušek'),
(362, 'Osnovna šola Jožeta Hudalesa Jurovski dol', 1, NULL, 'Jurovski Dol', 2223, 110, 1, 1, '40918807', '5090105000', 'Stanislav Senekovič'),
(363, 'Osnovna šola Jožeta Krajca Rakek', 1, NULL, 'Rakek', 1381, 111, 12, 1, '36025283', '5082757000', 'Anita Ivančič'),
(364, 'Osnovna šola Jožeta Krajca Rakek Podružnica Rudolfa Maistra Unec', 1, NULL, 'Rakek', 1381, 111, 12, 1, '36025283', '5082757001', '---'),
(365, 'Osnovna šola Jožeta Moškriča Ljubljana', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '26121018', '5084954000', 'Simona Kralj'),
(366, 'Osnovna šola Jurija Dalmatina Krško', 1, NULL, 'Krško', 8270, 38, 6, 1, '25512030', '5083974000', 'Antonija Glas Smodič'),
(367, 'Osnovna šola Jurija Vege Moravče', 1, NULL, 'Moravče', 1251, 112, 4, 1, '11448750', '5082838000', 'Nuška Pohlin Schvvarzbartl'),
(368, 'Osnovna šola Jurija Vege Moravče Podružnica Vrhpolje', 1, NULL, 'Moravče', 1251, 112, 4, 1, '11448750', '5082838001', '---'),
(369, 'Osnovna šola Juršinci', 1, NULL, 'Juršinci', 2256, 113, 1, 1, '52707806', '5087040000', 'Jelka Svenšek'),
(370, 'Osnovna šola Kamnica', 1, NULL, 'Kamnica', 2351, 2, 1, 1, '31795609', '5086710000', 'Tomaž Čeplak'),
(371, 'Osnovna šola Kamnica Podružnica Bresternica', 1, NULL, 'Bresternica', 2354, 2, 1, 1, '31795609', '5086710001', '---'),
(372, 'Osnovna šola Kanal', 1, NULL, 'Kanal', 5213, 70, 10, 1, '87540266', '5089018000', 'Ljudmila Zimic'),
(373, 'Osnovna šola Kapela', 1, NULL, 'Radenci', 9252, 114, 2, 1, '26126885', '5084776000', 'Anastazija Avsec'),
(374, 'Osnovna šola Karla Destovnika Kajuha Ljubljana', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '10592849', '5086655000', 'Sonja Šorli'),
(375, 'Osnovna šola Karla Destovnika-Kajuha  Šoštanj Podružnica Topolšica', 1, NULL, 'Topolšica', 3326, 115, 7, 1, NULL, '2136147002', ''),
(376, 'Osnovna šola Karla Destovnika-Kajuha Šoštanj', 1, NULL, 'Šoštanj', 3325, 115, 7, 1, '96822341', '2136147000', 'Majda Zaveršnik Puc'),
(377, 'Osnovna šola Karla Destovnika-Kajuha Šoštanj Podružnica Ravne', 1, NULL, 'Šoštanj', 3325, 115, 7, 1, NULL, '2136147003', ''),
(378, 'Osnovna šola Kašelj', 1, NULL, 'Ljubljana - Polje', 1260, 5, 4, 1, '21120234', '3765229000', 'Matjaž Zajelšnik'),
(379, 'Osnovna šola Ketteja in Murna Ljubljana', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '48351784', '5084270000', 'Jasmina Zupančič'),
(380, 'Osnovna šola Kobilje', 1, NULL, 'Kobilje', 9227, 116, 2, 1, '48379611', '5089719000', 'Milena Ivanuša'),
(381, 'Osnovna šola Kolezija', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '38359073', '5428394000', 'Lidija Žigon'),
(382, 'Osnovna šola Komandanta Staneta Dragatuš', 1, NULL, 'Dragatuš', 8343, 117, 8, 1, '83415394', '5082773000', 'Stanislav Dražumerič'),
(383, 'Osnovna šola Komenda - Moste', 1, NULL, 'Komenda', 1218, 118, 4, 1, '37317296', '5083052000', 'Mira Rek'),
(384, 'Osnovna šola Komenda - Moste Podružnica Moste', 1, NULL, 'Komenda', 1218, 118, 4, 1, '37317296', '5083052001', '---'),
(385, 'Osnovna šola Koper', 1, NULL, 'Koper - Capodistria', 6000, 20, 9, 1, '25866702', '2229463000', 'Anton Baloh'),
(386, 'Osnovna šola Koprivnica', 1, NULL, 'Koprivnica', 8282, 38, 6, 1, '10360077', '5086043000', 'Jože Ivačič'),
(387, 'Osnovna šola Korena', 1, NULL, 'Zgornja Korena', 2242, 82, 1, 1, '60415266', '5088887000', 'Darko Rebernik'),
(388, 'Osnovna šola Koroška Bela Jesenice', 1, NULL, 'Jesenice', 4270, 21, 3, 1, '44425465', '5719046000', 'Sanda Zupan'),
(389, 'Osnovna šola Koroška Bela Jesenice Podružnica Blejska Dobrava', 1, NULL, 'Blejska Dobrava', 4273, 21, 3, 1, '44425465', '5719046001', 'Sanda Zupan'),
(390, 'Osnovna šola Koroški jeklarji Ravne na Koroškem Podružnica Kotlje', 1, NULL, 'Kotlje', 2394, 35, 5, 1, '83712143', '5185815001', '');
INSERT INTO `school` (`id`, `name`, `school_category_id`, `address`, `post`, `postal_code`, `municipality_id`, `region_id`, `country_id`, `tax_number`, `identifier`, `headmaster`) VALUES
(391, 'Osnovna šola Koseze', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '85738271', '5062926000', 'Ana Kuhar Režek'),
(392, 'Osnovna šola Kozje', 1, NULL, 'Kozje', 3260, 119, 7, 1, '56311761', '5087929000', 'Roman Gradišek'),
(393, 'Osnovna šola Košana', 1, NULL, 'Košana', 6256, 120, 12, 1, '11274824', '5086922000', 'Neva Brce'),
(394, 'Osnovna šola Križe', 1, NULL, 'Križe', 4294, 50, 3, 1, '57553629', '5088127000', 'Erna Meglič'),
(395, 'Osnovna šola Križevci', 1, NULL, 'Križevci pri Ljutomeru', 9242, 121, 2, 1, '93578253', '5084636000', 'Lidija Koroša'),
(396, 'Osnovna šola Krmelj', 1, NULL, 'Krmelj', 8296, 51, 6, 1, '20318936', '5087520000', 'Gusta Mirt'),
(397, 'Osnovna šola Kungota', 1, NULL, 'Zgornja Kungota', 2201, 122, 1, 1, '58552561', '5085152000', 'Vojislav Lazarev'),
(398, 'Osnovna šola Kungota Podružnica Spodnja Kungota', 1, NULL, 'Pesnica pri Mariboru', 2211, 122, 1, 1, '58552561', '5085152001', ''),
(399, 'Osnovna šola Kungota Podružnica Svečina', 1, NULL, 'Zgornja Kungota', 2201, 122, 1, 1, '58552561', '5085152002', ''),
(400, 'Osnovna šola Kuzma', 1, NULL, 'Kuzma', 9263, 123, 2, 1, '77414900', '5085632000', 'Jožef Škalič'),
(401, 'Osnovna šola Lava Celje', 1, NULL, 'Celje', 3000, 15, 7, 1, '27299627', '5062799000', 'Marijana Kolenko'),
(402, 'Osnovna šola Ledina', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '89487273', '5084148000', 'Marija Valenčak'),
(403, 'Osnovna šola Lenart', 1, NULL, 'Lenart v Slov. goricah', 2230, 124, 1, 1, '27905918', '5086639000', 'Marjan Zadravec'),
(404, 'Osnovna šola Leona Štuklja Maribor', 1, NULL, 'Maribor', 2000, 2, 1, 1, '59613432', '5610494000', 'Darko Madžarac'),
(405, 'Osnovna šola Lesično', 1, NULL, 'Lesično', 3261, 119, 7, 1, '68680210', '5087937000', 'Irena Krajnc'),
(406, 'Osnovna šola Leskovec pri Krškem', 1, NULL, 'Leskovec pri Krškem', 8273, 38, 6, 1, '76398137', '5085047000', 'Anton Bizjak'),
(407, 'Osnovna šola Leskovec pri Krškem, Podružnica Veliki Podlog', 1, NULL, 'Leskovec pri Krškem', 8273, 38, 6, 1, '76398137', '5085047001', '---'),
(408, 'Osnovna šola Litija', 1, NULL, 'Litija', 1270, 23, 4, 1, '17567734', '5689147000', 'Peter Strle'),
(409, 'Osnovna šola Litija Podružnica Darinke Ribič Polšnik', 1, NULL, 'Polšnik', 1272, 23, 4, 1, '17567734', '5689147003', '---'),
(410, 'Osnovna šola Litija Podružnica Sava', 1, NULL, 'Sava', 1282, 23, 4, 1, '17567734', '5689147002', '---'),
(411, 'Osnovna šola Livada Ljubljana', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '85566543', '5375827000', 'Goran Popović'),
(412, 'Osnovna šola Livada Velenje', 1, NULL, 'Velenje', 3320, 41, 7, 1, '45242372', '5081939000', 'Tatjana Zafošnik Kanduti'),
(413, 'Osnovna šola Livada Velenje Podružnica Cirkovce', 1, NULL, 'Velenje', 3320, 41, 7, 1, '45242372', '5081939001', '---'),
(414, 'Osnovna šola Livada Velenje Podružnica Škale', 1, NULL, 'Velenje', 3320, 41, 7, 1, '45242372', '5081939002', '---'),
(415, 'Osnovna šola Livade - Izola', 1, NULL, 'Izola - Isola', 6310, 68, 9, 1, '17796989', '5859921000', 'Maja Cetin'),
(416, 'Osnovna šola Ljubečna', 1, NULL, 'Ljubečna', 3202, 15, 7, 1, '68305192', '1262823000', 'Martin Grosek'),
(417, 'Osnovna šola Ljubno ob Savinji', 1, NULL, 'Ljubno ob Savinji', 3333, 125, 7, 1, '67789943', '5088941000', 'Rajko Pintar'),
(418, 'Osnovna šola Ljudski vrt Ptuj', 1, NULL, 'Ptuj', 2250, 26, 1, 1, '86058932', '5087147000', 'Tatjana Vaupotič'),
(419, 'Osnovna šola Ljudski vrt Ptuj Podružnica Grajena', 1, NULL, 'Ptuj', 2250, 26, 1, 1, '86058932', '5087147001', '---'),
(420, 'Osnovna šola Log - Dragomer', 1, NULL, 'Brezovica pri Ljubljani', 1351, 126, 4, 1, '49698125', '5207045000', 'Mihaela Mrzlikar'),
(421, 'Osnovna šola Log - Dragomer, Podružnična šola Bevke', 1, NULL, 'Log pri Brezovici', 1358, 43, 4, 1, '49698125', '5207045001', '---'),
(422, 'Osnovna šola Loka Črnomelj', 1, NULL, 'Črnomelj', 8340, 117, 8, 1, '67958451', '5289211000', 'Damjana Vraničar'),
(423, 'Osnovna šola Loka Črnomelj Podružnica Adlešiči', 1, NULL, 'Adlešiči', 8341, 117, 8, 1, '67958451', '5289211002', ''),
(424, 'Osnovna šola Loka Črnomelj Podružnica Griblje', 1, NULL, 'Gradac', 8332, 117, 8, 1, '67958451', '5289211001', ''),
(425, 'Osnovna šola Louisa Adamiča Grosuplje', 1, NULL, 'Grosuplje', 1290, 60, 4, 1, '29424445', '5085993000', 'Janja Zupančič'),
(426, 'Osnovna šola Louisa Adamiča Grosuplje Podružnica Kopanj', 1, NULL, 'Grosuplje', 1290, 60, 4, 1, '29424445', '5085993004', '---'),
(427, 'Osnovna šola Louisa Adamiča Grosuplje Podružnica Šmarje Sap', 1, NULL, 'Šmarje - Sap', 1293, 60, 4, 1, '29424445', '5085993001', '---'),
(428, 'Osnovna šola Louisa Adamiča Grosuplje Podružnica Št.Jurij', 1, NULL, 'Grosuplje', 1290, 60, 4, 1, '29424445', '5085993005', '---'),
(429, 'Osnovna šola Louisa Adamiča Grosuplje Podružnica Žalna', 1, NULL, 'Grosuplje', 1290, 60, 4, 1, '0', '5085993007', '---'),
(430, 'Osnovna šola Lovrenc na Pohorju', 1, NULL, 'Lovrenc na Pohorju', 2344, 127, 1, 1, '89983882', '5085179000', 'Marija Osvald Novak'),
(431, 'Osnovna šola Loče', 1, NULL, 'Loče', 3215, 128, 7, 1, '49210220', '5089433000', 'Metka Ambrož Bezenšek'),
(432, 'Osnovna šola Loče Podružnica Jernej', 1, NULL, 'Loče', 3215, 128, 7, 1, '49210220', '5089433001', ''),
(433, 'Osnovna šola Loče Podružnica Žiče', 1, NULL, 'Loče', 3215, 128, 7, 1, '49210220', '5089433002', ''),
(434, 'Osnovna šola Lucija', 1, NULL, 'Portorož - Portorose', 6320, 17, 9, 1, '11997907', '5089174000', 'Katja Arzenšek'),
(435, 'Osnovna šola Lucija Podružnica Strunjan', 1, NULL, 'Portorož - Portorose', 6320, 17, 9, 1, '11997907', '5089174001', ''),
(436, 'Osnovna šola Lucijana Bratkoviča Bratuša Renče', 1, NULL, 'Renče', 5292, 104, 10, 1, '44215932', '5089034000', 'Bogomir Furlan'),
(437, 'Osnovna šola Lucijana Bratkoviča Bratuša Renče Podružnica Bukovica', 1, NULL, 'Volčja Draga', 5293, 104, 10, 1, '44215932', '5089034001', '---'),
(438, 'Osnovna šola Ludvika Pliberška Maribor', 1, NULL, 'Maribor', 2000, 2, 1, 1, '84740299', '5086728000', 'Lidija Todorović'),
(439, 'Osnovna šola Majde Vrhovnik Ljubljana', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '36181455', '5083486000', 'Mateja Urbančič Jelovšek'),
(440, 'Osnovna šola Majšperk', 1, NULL, 'Majšperk', 2322, 129, 1, 1, '57555559', '5087074000', 'Branko Lah'),
(441, 'Osnovna šola Majšperk Podružnica Ptujska gora', 1, NULL, 'Ptujska gora', 2323, 129, 1, 1, '57555559', '5087074002', ''),
(442, 'Osnovna šola Majšperk Podružnica Stoperce', 1, NULL, 'Stoperce', 2289, 129, 1, 1, '57555559', '5087074003', ''),
(443, 'Osnovna šola Maksa Durjave Maribor', 1, NULL, 'Maribor', 2000, 2, 1, 1, '81376847', '5085209000', 'Jolanda Friš Lozej'),
(444, 'Osnovna šola Maksa Pleteršnika Pišece', 1, NULL, 'Pišece', 8255, 14, 6, 1, '77693809', '5082595000', 'Irena Markovič'),
(445, 'Osnovna šola Mala Nedelja', 1, NULL, 'Mala Nedelja', 9243, 18, 2, 1, '36663417', '5084610000', 'Breda Žunič'),
(446, 'Osnovna šola Malečnik', 1, NULL, 'Malečnik', 2229, 2, 1, 1, '79836682', '5206634000', 'Rudolf Sedič'),
(447, 'Osnovna šola Marije Vere Kamnik', 1, NULL, 'Kamnik', 1241, 6, 4, 1, '52634876', '5268931000', 'Violeta Vodlan'),
(448, 'Osnovna šola Markovci', 1, NULL, 'Markovci', 2281, 130, 1, 1, '19017910', '5087104000', 'Ivan Štrafela'),
(449, 'Osnovna šola Martina Konšaka Maribor', 1, NULL, 'Maribor', 2000, 2, 1, 1, '53839773', '5085268000', 'Damir Orehovec'),
(450, 'Osnovna šola Martina Krpana Ljubljana', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '98721089', '5236681000', 'Barbara Žitnik Ternovec'),
(451, 'Osnovna šola Matije Valjavca Preddvor', 1, NULL, 'Preddvor', 4205, 131, 3, 1, '75535211', '5083214000', 'Mateja Sajovec'),
(452, 'Osnovna šola Matije Valjavca Preddvor Podružnica Jezersko', 1, NULL, 'Zgornje Jezersko', 4206, 132, 3, 1, '75535211', '5083214001', ''),
(453, 'Osnovna šola Matije Valjavca Preddvor Podružnica Kokra', 1, NULL, 'Preddvor', 4205, 131, 3, 1, '75535211', '5083214002', ''),
(454, 'Osnovna šola Matije Čopa Kranj', 1, NULL, 'Kranj', 4000, 19, 3, 1, '93323611', '5279976000', 'Matija Horvat'),
(455, 'Osnovna šola Medvode', 1, NULL, 'Medvode', 1215, 133, 4, 1, '26623404', '5222575000', 'Vojko Bizant'),
(456, 'Osnovna šola Mengeš', 1, NULL, 'Mengeš', 1234, 134, 4, 1, '94625387', '5082820000', 'Milan Burkeljca'),
(457, 'Osnovna šola Metlika', 1, NULL, 'Metlika', 8330, 135, 8, 1, '25802925', '5088925000', 'Jože Mozetič'),
(458, 'Osnovna šola Metlika Podružnica Suhor', 1, NULL, 'Suhor', 8331, 135, 8, 1, '25802925', '5088925001', ''),
(459, 'Osnovna šola Mežica', 1, NULL, 'Mežica', 2392, 136, 5, 1, '93869126', '5087376000', 'Janko Plešnik'),
(460, 'Osnovna šola Mihe Pintarja - Toleda Velenje', 1, NULL, 'Velenje', 3320, 41, 7, 1, '39145522', '5088216000', 'Anton Skok'),
(461, 'Osnovna šola Mihe Pintarja - Toleda Velenje Podružnica Plešivec', 1, NULL, 'Velenje', 3320, 41, 7, 1, '39145522', '5088216002', ''),
(462, 'Osnovna šola Miklavž na Dravskem polju', 1, NULL, 'Miklavž na Dravskem polju', 2204, 137, 1, 1, '70073627', '5085276000', 'Dušanka Mihalič Mali'),
(463, 'Osnovna šola Miklavž na Dravskem polju Podružnica Dobrovce', 1, NULL, 'Miklavž na Dravskem polju', 2204, 137, 1, 1, '70073627', '5085276001', '---'),
(464, 'Osnovna šola Miklavž pri Ormožu', 1, NULL, 'Miklavž pri Ormožu', 2275, 25, 1, 1, '29832063', '5089158000', 'Vlado Hebar'),
(465, 'Osnovna šola Miklavž pri Ormožu Podružnica Kog', 1, NULL, 'Kog', 2276, 25, 1, 1, '29832063', '5089158002', ''),
(466, 'Osnovna šola Milana Majcna Šentjanž', 1, NULL, 'Šentjanž', 8297, 51, 6, 1, '68625260', '5089328000', 'Marija Brce'),
(467, 'Osnovna šola Milana Šuštaršiča Ljubljana', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '11555050', '5204291000', 'Irena Kodrič'),
(468, 'Osnovna šola Milojke Štrukelj Nova Gorica', 1, NULL, 'Nova Gorica', 5000, 24, 10, 1, '96298197', '5089352000', 'Tatjana Krapše'),
(469, 'Osnovna šola Milojke Štrukelj Nova Gorica Podružnica Ledine', 1, NULL, 'Nova Gorica', 5000, 24, 10, 1, '96298197', '5089352001', '---'),
(470, 'Osnovna šola Mirana Jarca Ljubljana', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '32234945', '5084105000', 'Danica Večerić'),
(471, 'Osnovna šola Mirana Jarca Črnomelj', 1, NULL, 'Črnomelj', 8340, 117, 8, 1, '38693313', '5082765000', 'Boris Mužar'),
(472, 'Osnovna šola Miren', 1, NULL, 'Miren', 5291, 138, 10, 1, '57887411', '5085829000', 'Danijela Kosovelj'),
(473, 'Osnovna šola Miren Podružnica Bilje', 1, NULL, 'Renče', 5292, 138, 10, 1, '57887411', '5085829001', ''),
(474, 'Osnovna šola Miren Podružnica Kostanjevica', 1, NULL, 'Kostanjevica na Krasu', 5296, 138, 10, 1, '57887411', '5085829002', ''),
(475, 'Osnovna šola Mirna', 1, NULL, 'Mirna', 8233, 139, 8, 1, '49417398', '5090083000', 'Anica Marinčič'),
(476, 'Osnovna šola Miroslava Vilharja Postojna', 1, NULL, 'Postojna', 6230, 42, 12, 1, '92694969', '5496837000', 'Pia De Paulisdebevec'),
(477, 'Osnovna šola Miroslava Vilharja Postojna Podružnica Hruševje', 1, NULL, 'Hruševje', 6225, 42, 12, 1, '92694969', '5496837001', '---'),
(478, 'Osnovna šola Mislinja', 1, NULL, 'Mislinja', 2382, 140, 5, 1, '53705181', '5087589000', 'Natalija Aber Jordan'),
(479, 'Osnovna šola Mislinja Podružnica Dolič', 1, NULL, 'Mislinja', 2382, 140, 5, 1, '53705181', '5087589001', '---'),
(480, 'Osnovna šola Mislinja Podružnica Završe', 1, NULL, 'Mislinja', 2382, 140, 5, 1, '53705181', '5087589003', '---'),
(481, 'Osnovna šola Miška Kranjca Ljubljana', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '47126027', '5255279000', 'Irena Rozman'),
(482, 'Osnovna šola Miška Kranjca Velika Polana', 1, NULL, 'Velika Polana', 9225, 141, 2, 1, '29619904', '5089760000', 'Ivan Kramperšek'),
(483, 'Osnovna šola Mladika Ptuj', 1, NULL, 'Ptuj', 2250, 26, 1, 1, '80951147', '5087163000', 'Bogomir Širovnik'),
(484, 'Osnovna šola Mokronog', 1, NULL, 'Mokronog', 8230, 142, 8, 1, '11475064', '5088062000', 'Zvonimira Kostrevc'),
(485, 'Osnovna šola Mokronog Podružnica Trebelno', 1, NULL, 'Trebelno', 8231, 142, 8, 1, '11475064', '5088062002', ''),
(486, 'Osnovna šola Mozirje', 1, NULL, 'Mozirje', 3330, 143, 7, 1, '86633619', '5088950000', 'Andreja Hramec'),
(487, 'Osnovna šola Mozirje Podružnica Lepa njiva', 1, NULL, 'Mozirje', 3330, 143, 7, 1, '86633619', '5088950001', ''),
(488, 'Osnovna šola Mozirje Podružnica Šmihel nad Mozirjem', 1, NULL, 'Mozirje', 3330, 143, 7, 1, '86633619', '5088950004', ''),
(489, 'Osnovna šola Muta', 1, NULL, 'Muta', 2366, 144, 5, 1, '69843716', '5087287000', 'Anita Ambrož'),
(490, 'Osnovna šola N.H. Rajka Hrastnik', 1, NULL, 'Hrastnik', 1430, 145, 11, 1, '90342593', '5089905000', 'Marina Kmet'),
(491, 'Osnovna šola N.H. Rajka Hrastnik Podružnica Dol pri Hrastniku', 1, NULL, 'Dol pri Hrastniku', 1431, 145, 11, 1, '90342593', '5089905001', '--'),
(492, 'Osnovna šola Naklo', 1, NULL, 'Naklo', 4202, 4, 3, 1, '53817753', '1193830000', 'Milan Bohinec'),
(493, 'Osnovna šola Naklo Podružnica Duplje', 1, NULL, 'Duplje', 4203, 4, 3, 1, '53817753', '1193830001', 'Mihaela Križaj Trebušak'),
(494, 'Osnovna šola Naklo Podružnica Podbrezje', 1, NULL, 'Naklo', 4202, 4, 3, 1, '53817753', '1193830002', 'Mateja Jarc'),
(495, 'Osnovna šola Nazarje', 1, NULL, 'Nazarje', 3331, 146, 7, 1, '34152563', '1253484000', 'Vesna Lešnik'),
(496, 'Osnovna šola Nazarje Podružnica Šmartno ob Dreti', 1, NULL, 'Šmartno ob Dreti', 3341, 146, 7, 1, NULL, '1253484001', ''),
(497, 'Osnovna šola Neznanih talcev Dravograd', 1, NULL, 'Dravograd', 2370, 147, 5, 1, '62927892', '5082889000', 'Marjan Kovše'),
(498, 'Osnovna šola Neznanih talcev Dravograd Podružnica Libeliče', 1, NULL, 'Libeliče', 2372, 147, 5, 1, '62927892', '5082889002', ''),
(499, 'Osnovna šola Neznanih talcev Dravograd Podružnica Ojstrica', 1, NULL, 'Dravograd', 2370, 147, 5, 1, '62927892', '5082889003', ''),
(500, 'Osnovna šola Neznanih talcev Dravograd Podružnica Trbonje', 1, NULL, 'Trbonje', 2371, 147, 5, 1, '62927892', '5082889005', ''),
(501, 'Osnovna šola Neznanih talcev Dravograd Podružnica Črneče', 1, NULL, 'Dravograd', 2370, 147, 5, 1, '62927892', '5082889001', ''),
(502, 'Osnovna šola Notr. odred Cerknica Podružnica Maksim Gaspari Begunje pri Cerknici', 1, NULL, 'Begunje pri Cerknici', 1382, 111, 12, 1, '54018471', '5082722001', '---'),
(503, 'Osnovna šola Notranjski odred Cerknica', 1, NULL, 'Cerknica', 1380, 111, 12, 1, '54018471', '5082722000', 'Marija Braniselj'),
(504, 'Osnovna šola Notranjski odred Cerknica Podružnica "11.maj" Grahovo', 1, NULL, 'Grahovo', 1384, 111, 12, 1, '54018471', '5082722002', '---'),
(505, 'Osnovna šola Nove Fužine', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '59223332', '5280052000', 'Damjana Korošec'),
(506, 'Osnovna šola Nove Jarše', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '15729257', '5273935000', 'Štefka Brodar'),
(507, 'Osnovna šola Ob Dravinji Podružnica Tepanje', 1, NULL, 'Slovenske Konjice', 3210, 128, 7, 1, '11833173', '5089441001', ''),
(508, 'Osnovna šola Ob Dravinji Slovenske Konjice', 1, NULL, 'Slovenske Konjice', 3210, 128, 7, 1, '11833173', '5089441000', 'Nevenka Brdnik'),
(509, 'Osnovna šola Ob Rinži Kočevje', 1, NULL, 'Kočevje', 1330, 30, 8, 1, '90536398', '5621712000', 'Darja Delač Felda'),
(510, 'Osnovna šola Ob Rinži Kočevje Podružnica Kočevska Reka', 1, NULL, 'Kočevska Reka', 1338, 30, 8, 1, '90536398', '5621712001', ''),
(511, 'Osnovna šola Ob Rinži Kočevje Podružnica Livold', 1, NULL, 'Kočevje', 1330, 30, 8, 1, '90536398', '5621712002', ''),
(512, 'Osnovna šola Odranci', 1, NULL, 'Odranci', 9233, 148, 2, 1, '21296626', '5089743000', 'Marija Smolko'),
(513, 'Osnovna šola Olge Meglič Ptuj', 1, NULL, 'Ptuj', 2250, 26, 1, 1, '73389439', '5174309000', 'Diana Bohak Sabath'),
(514, 'Osnovna šola Orehek Kranj', 1, NULL, 'Kranj', 4000, 19, 3, 1, '72290480', '1319841000', 'Ivka Sodnik'),
(515, 'Osnovna šola Orehek Kranj Podružnica Mavčiče', 1, NULL, 'Mavčiče', 4211, 19, 3, 1, '72290480', '1319841001', '---'),
(516, 'Osnovna šola Ormož', 1, NULL, 'Ormož', 2270, 25, 1, 1, '59310197', '5089875000', 'Bojan Burgar'),
(517, 'Osnovna šola Oskarja Kovačiča Ljubljana', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '81115997', '5088798000', 'Olga Kolar'),
(518, 'Osnovna šola Oskarja Kovačiča Ljubljana Podružnica Rudnik', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '81115997', '5088798003', 'Olga Kolar'),
(519, 'Osnovna šola Oskarja Kovačiča Škofije', 1, NULL, 'Škofije', 6281, 20, 9, 1, '39097293', '5084822000', 'Vlasta Urška Baraga'),
(520, 'Osnovna šola Otlica', 1, NULL, 'Ajdovščina', 5270, 67, 10, 1, '65681924', '5082536000', 'Aleksander Popit'),
(521, 'Osnovna šola Otočec', 1, NULL, 'Otočec', 8222, 16, 8, 1, '95753443', '5086264000', 'Mojca Miklič'),
(522, 'Osnovna šola Partizanska bolnišnica Jesen Tinje', 1, NULL, 'Zgornja Ložnica', 2316, 1, 1, 1, '29406285', '5012554000', 'Ivan Kovačič'),
(523, 'Osnovna šola Pesnica', 1, NULL, 'Pesnica pri Mariboru', 2211, 106, 1, 1, '83806547', '5085128000', 'Andi Brlič'),
(524, 'Osnovna šola Pesnica Podružnica Pernica', 1, NULL, 'Pernica', 2231, 106, 1, 1, '83806547', '5085128001', ''),
(525, 'Osnovna šola Petrovče', 1, NULL, 'Petrovče', 3301, 33, 7, 1, '94658609', '5088569000', 'Irena Kolar'),
(526, 'Osnovna šola Petrovče Podružnica Trje', 1, NULL, 'Žalec', 3310, 33, 7, 1, NULL, '5088569003', ''),
(527, 'Osnovna šola Pier Paolo Vergerio il Vecchio Koper', 1, NULL, 'Koper - Capodistria', 6000, 20, 9, 1, '41881761', '5084849000', 'Guido Križman'),
(528, 'Osnovna šola Pier Paolo Vergerio il Vecchio Koper Podružnica Bertoki', 1, NULL, 'Koper - Capodistria', 6000, 20, 9, 1, '41881761', '5084849001', '---'),
(529, 'Osnovna šola Pier Paolo Vergerio il Vecchio Koper Podružnica Hrvatini', 1, NULL, 'Ankaran - Ancarano', 6280, 20, 9, 1, '41881761', '5084849002', '---'),
(530, 'Osnovna šola Pier Paolo Vergerio il Vecchio Koper Podružnica Semedela', 1, NULL, 'Koper - Capodistria', 6000, 20, 9, 1, '41881761', '5084849003', '---'),
(531, 'Osnovna šola Pirniče', 1, NULL, 'Medvode', 1215, 133, 4, 1, '52479668', '5084393000', 'Martina Kutnar'),
(532, 'Osnovna šola Pivka', 1, NULL, 'Pivka', 6257, 120, 12, 1, '42909872', '5089212000', 'Alenka Tomšič'),
(533, 'Osnovna šola Pivka Podružnica Zagorje', 1, NULL, 'Pivka', 6257, 120, 12, 1, '42909872', '5089212003', '---'),
(534, 'Osnovna šola Pivka Podružnica Šmihel', 1, NULL, 'Pivka', 6257, 120, 12, 1, '42909872', '5089212001', '---'),
(535, 'Osnovna šola Planina pri Sevnici', 1, NULL, 'Planina pri Sevnici', 3225, 54, 7, 1, '18080774', '5089450000', 'Matejka Zendzianowsky'),
(536, 'Osnovna šola Pod goro Slovenske Konjice', 1, NULL, 'Slovenske Konjice', 3210, 128, 7, 1, '67612261', '5087716000', 'Darja Ravnik'),
(537, 'Osnovna šola Pod goro Slovenske Konjice Podružnica Špitalič', 1, NULL, 'Loče', 3215, 128, 7, 1, '67612261', '5087716002', ''),
(538, 'Osnovna šola Podbočje', 1, NULL, 'Podbočje', 8312, 38, 6, 1, '57625166', '5086051000', 'Branko Strgar'),
(539, 'Osnovna šola Podgora - Kuteževo', 1, NULL, 'Ilirska Bistrica', 6250, 45, 12, 1, '12391263', '5086019000', 'Mirjam Vrh'),
(540, 'Osnovna šola Podgorje', 1, NULL, 'Podgorje pri Slovenj Gradcu', 2381, 7, 5, 1, '93058187', '5087597000', 'Aljoša Lavrinšek'),
(541, 'Osnovna šola Podgorje Podružnica Razbor', 1, NULL, 'Podgorje pri Slovenj Gradcu', 2381, 7, 5, 1, '93058187', '5087597002', ''),
(542, 'Osnovna šola Podgorje Podružnica Šmiklavž', 1, NULL, 'Podgorje pri Slovenj Gradcu', 2381, 7, 5, 1, '93058187', '5087597001', ''),
(543, 'Osnovna šola Podlehnik', 1, NULL, 'Podlehnik', 2286, 149, 1, 1, '88073106', '5087112000', 'Dejan Kopold'),
(544, 'Osnovna šola Podzemelj', 1, NULL, 'Gradac', 8332, 135, 8, 1, '68512902', '5085543000', 'Stanko Vlašič'),
(545, 'Osnovna šola Podčetrtek', 1, NULL, 'Podčetrtek', 3254, 150, 7, 1, '96126043', '5087945000', 'Darko Pepevnik'),
(546, 'Osnovna šola Podčetrtek Podružnica Pristava pri Mestinju', 1, NULL, 'Pristava pri Mestinju', 3253, 150, 7, 1, '96126043', '5087945001', '---'),
(547, 'Osnovna šola Pohorskega bataljona Oplotnica', 1, NULL, 'Oplotnica', 2317, 151, 1, 1, '12215279', '5087660000', 'Matjaž Vrtovec'),
(548, 'Osnovna šola Pohorskega bataljona Oplotnica Podružnica Kebelj', 1, NULL, 'Oplotnica', 2317, 1, 1, 1, '12215279', '5087660001', ''),
(549, 'Osnovna šola Pohorskega bataljona Oplotnica Podružnica Prihova', 1, NULL, 'Oplotnica', 2317, 151, 1, 1, '12215279', '5087660002', ''),
(550, 'Osnovna šola Pohorskega odreda Slov. Bistrica Podružnica Zgornja Ložnica', 1, NULL, 'Zgornja Ložnica', 2316, 1, 1, 1, '48238112', '5087686001', ''),
(551, 'Osnovna šola Pohorskega odreda Slovenska Bistrica', 1, NULL, 'Slovenska Bistrica', 2310, 1, 1, 1, '48238112', '5087686000', 'Tatjana Pufič'),
(552, 'Osnovna šola Polhov Gradec', 1, NULL, 'Polhov Gradec', 1355, 77, 4, 1, '36290530', '5084466000', 'Jernej Klemen'),
(553, 'Osnovna šola Polhov Gradec Podružnica Šentjošt', 1, NULL, 'Horjul', 1354, 77, 4, 1, '36290530', '5084466002', '---'),
(554, 'Osnovna šola Polhov Gradec Podružnica Črni vrh', 1, NULL, 'Polhov Gradec', 1355, 77, 4, 1, '36290530', '5084466001', '---'),
(555, 'Osnovna šola Poljane', 1, NULL, 'Poljane nad Škofjo Loko', 4223, 105, 3, 1, '95058354', '1199498000', 'Metka Debeljak'),
(556, 'Osnovna šola Poljane Ljubljana', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '73742309', '5083494000', 'Žarko Tomšič'),
(557, 'Osnovna šola Poljane Podružnica Javorje', 1, NULL, 'Poljane nad Škofjo Loko', 4223, 105, 3, 1, NULL, '1199498001', ''),
(558, 'Osnovna šola Polje', 1, NULL, 'Ljubljana - Polje', 1260, 5, 4, 1, '99728508', '5084288000', 'Barbara Smrekar'),
(559, 'Osnovna šola Poljčane', 1, NULL, 'Poljčane', 2319, 152, 1, 1, '17144442', '5087678000', 'Francka Mravlje'),
(560, 'Osnovna šola Polzela', 1, NULL, 'Polzela', 3313, 153, 7, 1, '33941688', '5088500000', 'Bernardka Sopčič'),
(561, 'Osnovna šola Polzela Podružnica Andraž', 1, NULL, 'Polzela', 3313, 153, 7, 1, '33941688', '5088500001', ''),
(562, 'Osnovna šola Prebold', 1, NULL, 'Prebold', 3312, 154, 7, 1, '81995270', '5088518000', 'Oton Račečič'),
(563, 'Osnovna šola Predoslje Kranj', 1, NULL, 'Kranj', 4000, 19, 3, 1, '53580664', '5083222000', 'Tomaž Balderman'),
(564, 'Osnovna šola Preserje', 1, NULL, 'Preserje', 1352, 59, 4, 1, '92875602', '5084474000', 'Igor Selan'),
(565, 'Osnovna šola Preserje Podružnica Jezero', 1, NULL, 'Preserje', 1352, 59, 4, 1, '92875602', '5084474001', ''),
(566, 'Osnovna šola Preserje Podružnica Rakitna', 1, NULL, 'Preserje', 1352, 59, 4, 1, '92875602', '5084474002', ''),
(567, 'Osnovna šola Preserje pri Radomljah', 1, NULL, 'Radomlje', 1235, 73, 4, 1, '68428120', '5084741000', 'Ana Nuša Kern'),
(568, 'Osnovna šola Preska', 1, NULL, 'Medvode', 1215, 133, 4, 1, '34416170', '5084334000', 'Primož Jurman'),
(569, 'Osnovna šola Preska Podružnica Sora', 1, NULL, 'Medvode', 1215, 133, 4, 1, '34416170', '5084334001', ''),
(570, 'Osnovna šola Preska Podružnica Topol', 1, NULL, 'Medvode', 1215, 133, 4, 1, '34416170', '5084334002', ''),
(571, 'Osnovna šola Prestranek', 1, NULL, 'Prestranek', 6258, 42, 12, 1, '98956574', '5086949000', 'Nataša Režek Donev'),
(572, 'Osnovna šola Prevole', 1, NULL, 'Hinje', 8362, 155, 8, 1, '69795819', '5086272000', 'Marija Breceljnik'),
(573, 'Osnovna šola Prežihovega Voranca Bistrica', 1, NULL, 'Črenšovci', 9232, 91, 2, 1, '94330522', '5089751000', 'Terezija Zamuda'),
(574, 'Osnovna šola Prežihovega Voranca Jesenice', 1, NULL, 'Jesenice', 4270, 21, 3, 1, '71303103', '5719097000', 'Robert Kerštajn'),
(575, 'Osnovna šola Prežihovega Voranca Ljubljana', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '32732686', '5084156000', 'Marjan Gorup'),
(576, 'Osnovna šola Prežihovega Voranca Maribor', 1, NULL, 'Maribor', 2000, 2, 1, 1, '97870692', '5085101000', 'Janja Bukovec'),
(577, 'Osnovna šola Prežihovega Voranca Ravne na Koroškem', 1, NULL, 'Ravne na Koroškem', 2390, 35, 5, 1, '26935465', '5087392000', 'Stanislav Osojnik'),
(578, 'Osnovna šola Primoža Trubarja Laško', 1, NULL, 'Laško', 3270, 40, 7, 1, '29610249', '5924332000', 'Ljudmila Pušnik'),
(579, 'Osnovna šola Primoža Trubarja Laško Podružnica Debro', 1, NULL, 'Laško', 3270, 40, 7, 1, '0', '5924332006', '---'),
(580, 'Osnovna šola Primoža Trubarja Laško Podružnica Rečica', 1, NULL, 'Laško', 3270, 40, 7, 1, '29610249', '5924332004', '---'),
(581, 'Osnovna šola Primoža Trubarja Laško Podružnica Vrh', 1, NULL, 'Laško', 3270, 40, 7, 1, '29610249', '5924332003', '---'),
(582, 'Osnovna šola Primoža Trubarja Laško Podružnica Šentrupert', 1, NULL, 'Šentrupert', 3271, 40, 7, 1, '0', '5924332001', '---'),
(583, 'Osnovna šola Primoža Trubarja Velike Lašče', 1, NULL, 'Velike Lašče', 1315, 156, 4, 1, '21805865', '5084539000', 'Metoda Kolar'),
(584, 'Osnovna šola Primoža Trubarja Velike Lašče Podružnica Rob', 1, NULL, 'Rob', 1314, 156, 4, 1, '21805865', '5084539002', '---'),
(585, 'Osnovna šola Primoža Trubarja Velike Lašče Podružnica Turjak', 1, NULL, 'Turjak', 1311, 156, 4, 1, '21805865', '5084539003', '---'),
(586, 'Osnovna šola Prule', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '89177606', '5084164000', 'Dušan Merc'),
(587, 'Osnovna šola Puconci', 1, NULL, 'Puconci', 9201, 157, 2, 1, '96341742', '5085691000', 'Ernest Nemec'),
(588, 'Osnovna šola Puconci Podružnica Bodonci', 1, NULL, 'Bodonci', 9265, 157, 2, 1, '96341742', '5085691002', '---'),
(589, 'Osnovna šola Puconci Podružnica Mačkovci', 1, NULL, 'Mačkovci', 9202, 157, 2, 1, '96341742', '5085691003', '---'),
(590, 'Osnovna šola Rada Robiča Limbuš', 1, NULL, 'Limbuš', 2341, 2, 1, 1, '61528714', '5085845000', 'Rado Wutej'),
(591, 'Osnovna šola Radenci', 1, NULL, 'Radenci', 9252, 114, 2, 1, '57189684', '5082919000', 'Nataša Zmazek'),
(592, 'Osnovna šola Radlje ob Dravi', 1, NULL, 'Radlje ob Dravi', 2360, 158, 5, 1, '54093899', '5089271000', 'Damjan Osrajnik'),
(593, 'Osnovna šola Radlje ob Dravi Podružnica Remšnik', 1, NULL, 'Podvelka', 2363, 158, 5, 1, '54093899', '5089271005', ''),
(594, 'Osnovna šola Radlje ob Dravi Podružnica Vuhred', 1, NULL, 'Vuhred', 2365, 158, 5, 1, '54093899', '5089271001', ''),
(595, 'Osnovna šola Raka', 1, NULL, 'Raka', 8274, 38, 6, 1, '61576824', '5083281000', 'Milvana Bizjan'),
(596, 'Osnovna šola Razkrižje', 1, NULL, 'Razkrižje', 9246, 159, 2, 1, '10804412', '5089344000', 'Mileva Kralj Buzeti'),
(597, 'Osnovna šola Rače', 1, NULL, 'Rače', 2327, 88, 1, 1, '97890898', '5085292000', 'Jožef Jurič'),
(598, 'Osnovna šola Rečica ob Savinji', 1, NULL, 'Rečica ob Savinji', 3332, 160, 7, 1, '71818065', '5171008000', 'Peter Podgoršek'),
(599, 'Osnovna šola Ribnica na Pohorju', 1, NULL, 'Ribnica na Pohorju', 2364, 161, 5, 1, '93310510', '5087252000', 'Franc Vobovnik'),
(600, 'Osnovna šola Riharda Jakopiča Ljubljana', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '43483461', '5086132000', 'Tatjana Slavičić'),
(601, 'Osnovna šola Rodica Domžale', 1, NULL, 'Domžale', 1230, 73, 4, 1, '34707735', '5083737000', 'Milena Vidovič'),
(602, 'Osnovna šola Rogatec', 1, NULL, 'Rogatec', 3252, 162, 7, 1, '98183443', '5087970000', 'Viljem Prevolšek'),
(603, 'Osnovna šola Rogatec Podružnica Dobovec', 1, NULL, 'Rogatec', 3252, 162, 7, 1, '98183443', '5087970001', ''),
(604, 'Osnovna šola Rogatec Podružnica Donačka gora', 1, NULL, 'Rogatec', 3252, 162, 7, 1, '98183443', '5087970002', ''),
(605, 'Osnovna šola Rovte', 1, NULL, 'Rovte', 1373, 37, 4, 1, '57121133', '5912792000', 'Mitja Turk'),
(606, 'Osnovna šola Rovte Podružnica Vrh Svetih treh kraljev', 1, NULL, 'Rovte', 1373, 37, 4, 1, '57121133', '5912792001', ''),
(607, 'Osnovna šola Rudija Mahniča - Brkinca Pregarje', 1, NULL, 'Obrov', 6243, 45, 12, 1, '75401665', '5090164000', 'Manica Renko'),
(608, 'Osnovna šola Rudolfa Maistra Šentilj v Slov. goricah', 1, NULL, 'Šentilj v Slov. goricah', 2212, 163, 1, 1, '62160559', '5086167000', 'Jelka Weldt'),
(609, 'Osnovna šola Rudolfa Maistra Šentilj v Slov.goricah Podružnica Ceršak', 1, NULL, 'Ceršak', 2215, 163, 1, 1, '62160559', '5086167001', ''),
(610, 'Osnovna šola Rudolfa Ukoviča Podgrad', 1, NULL, 'Podgrad', 6244, 45, 12, 1, '40184277', '5083800000', 'Milan Dekleva'),
(611, 'Osnovna šola Sava Kladnika Podružnica Loka', 1, NULL, 'Loka pri Zidanem Mostu', 1434, 51, 6, 1, '69230307', '5087490002', ''),
(612, 'Osnovna šola Sava Kladnika Podružnica Studenec', 1, NULL, 'Studenec', 8293, 51, 6, 1, '69230307', '5087490003', ''),
(613, 'Osnovna šola Sava Kladnika Sevnica', 1, NULL, 'Sevnica', 8290, 51, 6, 1, '69230307', '5087490000', 'Mirjana Jelančič'),
(614, 'Osnovna šola Savsko naselje', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '71148922', '5083362000', 'Verica Šenica Pavletič'),
(615, 'Osnovna šola Selnica ob Dravi', 1, NULL, 'Selnica ob Dravi', 2352, 164, 1, 1, '21101736', '5085136000', 'Jožica Ozmec'),
(616, 'Osnovna šola Selnica ob Dravi Podružnica Duh na Ostrem vrhu', 1, NULL, 'Sv. Duh na Ostrem Vrhu', 2353, 164, 1, 1, '21101736', '5085136001', ''),
(617, 'Osnovna šola Selnica ob Dravi Podružnica Gradišče na Kozjaku', 1, NULL, 'Ožbalt', 2361, 164, 1, 1, '21101736', '5085136002', ''),
(618, 'Osnovna šola Sečovlje', 1, NULL, 'Sečovlje - Sicciole', 6333, 17, 9, 1, '93348428', '5086876000', 'Mirela Flego'),
(619, 'Osnovna šola Sečovlje Podružnična šola in vrtec Sveti Peter', 1, NULL, 'Sečovlje - Sicciole', 6333, 17, 9, 1, '93348428', '5086876001', '---'),
(620, 'Osnovna šola Simona Gregorčiča Kobarid', 1, NULL, 'Kobarid', 5222, 165, 10, 1, '51971020', '5089832000', 'Melita Jakelj'),
(621, 'Osnovna šola Simona Gregorčiča Kobarid Podružnica Breginj', 1, NULL, 'Breginj', 5223, 165, 10, 1, '51971020', '5089832001', ''),
(622, 'Osnovna šola Simona Gregorčiča Kobarid Podružnica Drežnica', 1, NULL, 'Kobarid', 5222, 165, 10, 1, '51971020', '5089832003', ''),
(623, 'Osnovna šola Simona Gregorčiča Kobarid Podružnica Smast', 1, NULL, 'Kobarid', 5222, 165, 10, 1, '51971020', '5089832004', ''),
(624, 'Osnovna šola Simona Jenka Kranj', 1, NULL, 'Kranj', 4000, 19, 3, 1, '43026141', '5083192000', 'Rudolf Planinšek'),
(625, 'Osnovna šola Simona Jenka Kranj Podružnica Center', 1, NULL, 'Kranj', 4000, 19, 3, 1, '43026141', '5083192005', ''),
(626, 'Osnovna šola Simona Jenka Kranj Podružnica Goriče', 1, NULL, 'Golnik', 4204, 19, 3, 1, '43026141', '5083192001', ''),
(627, 'Osnovna šola Simona Jenka Kranj Podružnica Primskovo', 1, NULL, 'Kranj', 4000, 19, 3, 1, '43026141', '5083192002', ''),
(628, 'Osnovna šola Simona Jenka Kranj Podružnica Trstenik', 1, NULL, 'Golnik', 4204, 19, 3, 1, '43026141', '5083192003', ''),
(629, 'Osnovna šola Simona Jenka Smlednik', 1, NULL, 'Smlednik', 1216, 133, 4, 1, '11413743', '5084385000', 'Marko Valenčič'),
(630, 'Osnovna šola Simona Kosa Podbrdo', 1, NULL, 'Podbrdo', 5243, 27, 10, 1, '86390465', '5088011000', 'Polona Kenda'),
(631, 'Osnovna šola Sladki Vrh', 1, NULL, 'Sladki vrh', 2214, 163, 1, 1, '74840959', '5085144000', 'Andreja Košti'),
(632, 'Osnovna šola Sladki Vrh Podružnica Velka', 1, NULL, 'Zgornja Velka', 2213, 163, 1, 1, '74840959', '5085144002', '---'),
(633, 'Osnovna šola Slave Klavore Maribor', 1, NULL, 'Maribor', 2000, 2, 1, 1, '38028654', '5085322000', 'Stanislava Frangež'),
(634, 'Osnovna šola Slivnica pri Celju', 1, NULL, 'Gorica pri Slivnici', 3263, 54, 7, 1, '33404569', '5087791000', 'Marjeta Košak'),
(635, 'Osnovna šola Slivnica pri Celju Podružnica Loka pri Žusmu', 1, NULL, 'Loka pri Žusmu', 3223, 54, 7, 1, '33404569', '5087791003', '---'),
(636, 'Osnovna šola Slivnica pri Celju Podružnica Prevorje', 1, NULL, 'Prevorje', 3262, 54, 7, 1, '33404569', '5087791002', '---'),
(637, 'Osnovna šola Solkan', 1, NULL, 'Solkan', 5250, 24, 10, 1, '15978346', '5089042000', 'Marijan Kogoj'),
(638, 'Osnovna šola Solkan Podružnica Grgar', 1, NULL, 'Grgar', 5251, 24, 10, 1, '15978346', '5089042002', ''),
(639, 'Osnovna šola Solkan Podružnica Trnovo', 1, NULL, 'Trnovo pri Gorici', 5252, 24, 10, 1, '15978346', '5089042003', ''),
(640, 'Osnovna šola Sostro', 1, NULL, 'Ljubljana - Dobrunje', 1261, 5, 4, 1, '19630646', '5086124000', 'Mojca Pajnič Kirn'),
(641, 'Osnovna šola Sostro Podružnica Besnica', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '19630646', '5086124001', ''),
(642, 'Osnovna šola Sostro Podružnica Janče', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '19630646', '5086124002', ''),
(643, 'Osnovna šola Sostro Podružnica Lipoglav', 1, NULL, 'Šmarje - Sap', 1293, 5, 4, 1, '19630646', '5086124004', ''),
(644, 'Osnovna šola Sostro Podružnica Prežganje', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '19630646', '5086124005', ''),
(645, 'Osnovna šola Spodnja Idrija', 1, NULL, 'Spodnja Idrija', 5281, 22, 10, 1, '10527397', '5083788000', 'Radko Vehar'),
(646, 'Osnovna šola Spodnja Idrija Podružnica Ledine', 1, NULL, 'Spodnja Idrija', 5281, 22, 10, 1, '10527397', '5083788002', '---'),
(647, 'Osnovna šola Spodnja Šiška', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '94204390', '5084326000', 'Franci Hočevar'),
(648, 'Osnovna šola Središče ob Dravi', 1, NULL, 'Središče ob Dravi', 2277, 166, 1, 1, '92129196', '5086426000', 'Jasna Munda'),
(649, 'Osnovna šola Srečka Kosovela Sežana', 1, NULL, 'Sežana', 6210, 83, 9, 1, '94094306', '5210429000', 'Jadranka Mihalič'),
(650, 'Osnovna šola Srečka Kosovela Sežana Podružnica Lokev', 1, NULL, 'Lokev', 6219, 83, 9, 1, '94094306', '5210429001', '---'),
(651, 'Osnovna šola Staneta Žagarja Kranj', 1, NULL, 'Kranj', 4000, 19, 3, 1, '88156176', '5083206000', 'Fani Bevk'),
(652, 'Osnovna šola Staneta Žagarja Lipnica', 1, NULL, 'Kropa', 4245, 13, 3, 1, '81968060', '5087333000', 'Alenka Cuder'),
(653, 'Osnovna šola Staneta Žagarja Lipnica Podružnica Ovsiše', 1, NULL, 'Podnart', 4244, 13, 3, 1, '81968060', '5087333001', ''),
(654, 'Osnovna šola Stara Cerkev', 1, NULL, 'Stara Cerkev', 1332, 30, 8, 1, '72111763', '5621739000', 'Sonja Veber'),
(655, 'Osnovna šola Stara Cerkev Podružnica Željne', 1, NULL, 'Kočevje', 1330, 30, 8, 1, '72111763', '5621739001', ''),
(656, 'Osnovna šola Stari trg ob Kolpi', 1, NULL, 'Stari trg ob Kolpi', 8342, 117, 8, 1, '11215526', '5086477000', 'Alojz Hudelja'),
(657, 'Osnovna šola Starše', 1, NULL, 'Starše', 2205, 167, 1, 1, '25722824', '5085314000', 'Franc Kekec'),
(658, 'Osnovna šola Starše Podružnica Marjeta na Dravskem polju', 1, NULL, 'Marjeta na Dravskem polju', 2206, 167, 1, 1, '25722824', '5085314001', '---'),
(659, 'Osnovna šola Stična', 1, NULL, 'Ivančna Gorica', 1295, 87, 4, 1, '67259375', '5623677000', 'Marjan Potokar'),
(660, 'Osnovna šola Stična Podružnica Ambrus', 1, NULL, 'Zagradec', 1303, 87, 4, 1, '67259375', '5623677002', ''),
(661, 'Osnovna šola Stična Podružnica Krka', 1, NULL, 'Krka', 1301, 87, 4, 1, '67259375', '5623677003', ''),
(662, 'Osnovna šola Stična Podružnica Muljava', 1, NULL, 'Ivančna Gorica', 1295, 87, 4, 1, '67259375', '5623677004', ''),
(663, 'Osnovna šola Stična Podružnica Stična', 1, NULL, 'Ivančna Gorica', 1295, 87, 4, 1, '67259375', '5623677006', ''),
(664, 'Osnovna šola Stična Podružnica Višnja Gora', 1, NULL, 'Višnja Gora', 1294, 87, 4, 1, '67259375', '5623677001', ''),
(665, 'Osnovna šola Stična Podružnica Zagradec', 1, NULL, 'Zagradec', 1303, 87, 4, 1, '67259375', '5623677005', ''),
(666, 'Osnovna šola Stopiče', 1, NULL, 'Stopiče', 8322, 16, 8, 1, '92232787', '5086833000', 'Mateja Andrejčič'),
(667, 'Osnovna šola Stopiče Podružnica Dolž', 1, NULL, 'Novo mesto', 8000, 16, 8, 1, '92232787', '5086833001', '---'),
(668, 'Osnovna šola Stopiče Podružnica Podgrad', 1, NULL, 'Novo mesto', 8000, 16, 8, 1, '92232787', '5086833002', '---'),
(669, 'Osnovna šola Stranje', 1, NULL, 'Stahovica', 1242, 6, 4, 1, '21169012', '5083818000', 'Boris Jemec'),
(670, 'Osnovna šola Stranje Podružnica Gozd', 1, NULL, 'Stahovica', 1242, 6, 4, 1, '21169012', '5083818001', ''),
(671, 'Osnovna šola Stražišče Kranj', 1, NULL, 'Kranj', 4000, 19, 3, 1, '80750842', '5085365000', 'Pavel Srečnik'),
(672, 'Osnovna šola Stražišče Kranj Podružnica Besnica', 1, NULL, 'Zgornja Besnica', 4201, 19, 3, 1, '80750842', '5085365001', ''),
(673, 'Osnovna šola Stražišče Kranj Podružnica Podblica', 1, NULL, 'Zgornja Besnica', 4201, 19, 3, 1, '80750842', '5085365004', ''),
(674, 'Osnovna šola Stražišče Kranj Podružnica Žabnica', 1, NULL, 'Žabnica', 4209, 19, 3, 1, '80750842', '5085365005', ''),
(675, 'Osnovna šola Stročja vas', 1, NULL, 'Ljutomer', 9240, 18, 2, 1, '91516943', '5085004000', 'Mateja Leskovar'),
(676, 'Osnovna šola Sv. Jurij Rogašovci Podružnica Pertoča', 1, NULL, 'Rogašovci', 9262, 168, 2, 1, '99951525', '5085705001', '---'),
(677, 'Osnovna šola Sveta Ana', 1, NULL, 'Sv. Ana v Slov. goricah', 2233, 169, 1, 1, '81069472', '5084865000', 'Boris Mlakar'),
(678, 'Osnovna šola Sveta Ana Podružnica Lokavec pri Zgornji Velki', 1, NULL, 'Sv. Ana v Slov. goricah', 2233, 169, 1, 1, '81069472', '5084865001', ''),
(679, 'Osnovna šola Sveti Jurij Rogašovci', 1, NULL, 'Rogašovci', 9262, 168, 2, 1, '99951525', '5085705000', 'Aleksander Mencigar'),
(680, 'Osnovna šola Sveti Jurij ob Ščavnici', 1, NULL, 'Sveti Jurij ob Ščavnici', 9244, 170, 2, 1, '19644051', '5083753000', 'Marko Kraner'),
(681, 'Osnovna šola Sveti Tomaž', 1, NULL, 'Sv.Tomaž', 2258, 171, 1, 1, '70846057', '5089166000', 'Pepca Kupčič'),
(682, 'Osnovna šola Tabor I Maribor', 1, NULL, 'Maribor', 2000, 2, 1, 1, '50654802', '5610508000', 'Jožica Rapac'),
(683, 'Osnovna šola Tabor Logatec', 1, NULL, 'Logatec', 1370, 37, 4, 1, '24675750', '5085071000', 'Miša Stržinar'),
(684, 'Osnovna šola Tabor Logatec Podružnica Hotedršica', 1, NULL, 'Hotedršica', 1372, 37, 4, 1, '24675750', '5085071001', ''),
(685, 'Osnovna šola Tabor Logatec Podružnica Rovtarske Žibrše', 1, NULL, 'Rovte', 1373, 37, 4, 1, '24675750', '5085071002', ''),
(686, 'Osnovna šola Tišina', 1, NULL, 'Tišina', 9251, 172, 2, 1, '56492987', '5085721000', 'Sonja Rošer'),
(687, 'Osnovna šola Tišina Podružnica Gederovci', 1, NULL, 'Tišina', 9251, 172, 2, 1, '56492987', '5085721001', '---'),
(688, 'Osnovna šola Toma Brejca Kamnik', 1, NULL, 'Kamnik', 1241, 6, 4, 1, '31285805', '5083044000', 'Mojca Rode Škrjanc'),
(689, 'Osnovna šola Toneta Okrogarja Zagorje', 1, NULL, 'Zagorje ob Savi', 1410, 102, 11, 1, '62408534', '5088399000', 'Bronislav Urbanija'),
(690, 'Osnovna šola Toneta Okrogarja Zagorje Podružnica Kisovec', 1, NULL, 'Kisovec', 1412, 102, 11, 1, '62408534', '5088399001', '---'),
(691, 'Osnovna šola Toneta Okrogarja Zagorje Podružnica Šentlambert', 1, NULL, 'Zagorje ob Savi', 1410, 102, 11, 1, '62408534', '5088399002', '---'),
(692, 'Osnovna šola Toneta Pavčka Mirna Peč', 1, NULL, 'Mirna Peč', 8216, 173, 8, 1, '57013357', '5086256000', 'Danijel Brezovar'),
(693, 'Osnovna šola Toneta Tomšiča Knežak', 1, NULL, 'Knežak', 6253, 45, 12, 1, '46127356', '5083796000', 'Tea Gustinčič'),
(694, 'Osnovna šola Toneta Šraja Aljoše', 1, NULL, 'Nova Vas', 1385, 174, 12, 1, '22081453', '5082749000', 'Milena Mišič'),
(695, 'Osnovna šola Toneta Čufarja', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '98088742', '5088755000', 'Tanja Grünfeld'),
(696, 'Osnovna šola Toneta Čufarja Jesenice', 1, NULL, 'Jesenice', 4270, 21, 3, 1, '56149425', '5719089000', 'Branka Ščap'),
(697, 'Osnovna šola Toneta Čufarja Maribor', 1, NULL, 'Maribor', 2000, 2, 1, 1, '26804964', '5085284000', 'Špela Drstvenšek'),
(698, 'Osnovna šola Tončke Čeč Trbovlje', 1, NULL, 'Trbovlje', 1420, 28, 11, 1, '96660902', '5899508000', 'Katarina Pajer'),
(699, 'Osnovna šola Trbovlje', 1, NULL, 'Trbovlje', 1420, 28, 11, 1, '55876811', '5889235000', 'Klementina Šuligoj'),
(700, 'Osnovna šola Trbovlje Podružnica Alojza Hohkrauta', 1, NULL, 'Trbovlje', 1420, 28, 11, 1, '55876811', '5889235001', '---'),
(701, 'Osnovna šola Trbovlje Podružnica Dobovec', 1, NULL, 'Dobovec', 1423, 28, 11, 1, '55876811', '5889235002', '---'),
(702, 'Osnovna šola Trebnje', 1, NULL, 'Trebnje', 8210, 175, 8, 1, '41249356', '5088097000', 'Rado Kostrevc'),
(703, 'Osnovna šola Trebnje Podružnica Dobrnič', 1, NULL, 'Dobrnič', 8211, 175, 8, 1, '41249356', '5088097002', ''),
(704, 'Osnovna šola Trebnje Podružnica Dolenja Nemška vas', 1, NULL, 'Trebnje', 8210, 175, 8, 1, '41249356', '5088097003', ''),
(705, 'Osnovna šola Trebnje Podružnica Šentlovrenc', 1, NULL, 'Velika Loka', 8212, 175, 8, 1, '41249356', '5088097004', ''),
(706, 'Osnovna šola Trnovo', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '67940650', '5084440000', 'Irena Kokovnik'),
(707, 'Osnovna šola Trzin', 1, NULL, 'Trzin', 1236, 176, 4, 1, '54697751', '5255287000', 'mag. Helena Mazi Golob'),
(708, 'Osnovna šola Tržišče', 1, NULL, 'Tržišče', 8295, 51, 6, 1, '33629927', '5087503000', 'Zvonka Mrgole'),
(709, 'Osnovna šola Tržič', 1, NULL, 'Tržič', 4290, 50, 3, 1, '41934911', '5088143000', 'Stanislav Grum'),
(710, 'Osnovna šola Tržič Podružnica Lom pod Storžičem', 1, NULL, 'Tržič', 4290, 50, 3, 1, '41934911', '5088143001', ''),
(711, 'Osnovna šola Tržič Podružnica Podljubelj', 1, NULL, 'Tržič', 4290, 50, 3, 1, '41934911', '5088143003', ''),
(712, 'Osnovna šola Turnišče', 1, NULL, 'Turnišče', 9224, 177, 2, 1, '12307572', '5084059000', 'Melita Olaj'),
(713, 'Osnovna šola Valentina Vodnika Ljubljana', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '94718164', '5084342000', 'Vesna Žagar Gabrovšek'),
(714, 'Osnovna šola Vavta vas', 1, NULL, 'Straža pri Novem mestu', 8351, 178, 8, 1, '86730738', '5086329000', 'Anton Virant'),
(715, 'Osnovna šola Velika Dolina', 1, NULL, 'Jesenice na Dolenjskem', 8261, 14, 6, 1, '81190344', '5083583000', 'Mojca Bregar Goričar'),
(716, 'Osnovna šola Velika Nedelja', 1, NULL, 'Velika Nedelja', 2274, 25, 1, 1, '82142211', '5090148000', 'Anton Žumbar'),
(717, 'Osnovna šola Velika Nedelja Podružnica Podgorci', 1, NULL, 'Podgorci', 2273, 25, 1, 1, '82142211', '5090148001', '---'),
(718, 'Osnovna šola Veliki Gaber', 1, NULL, 'Veliki Gaber', 8213, 175, 8, 1, '47660759', '5088119000', 'Barbara Brezigar'),
(719, 'Osnovna šola Venclja Perka Domžale', 1, NULL, 'Domžale', 1230, 73, 4, 1, '16670884', '5082811000', 'Irena Vavpetič'),
(720, 'Osnovna šola Veržej', 1, NULL, 'Veržej', 9241, 179, 2, 1, '32512864', '5051215000', 'Borut Casar'),
(721, 'Osnovna šola Vide Pregarc Ljubljana', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '52386368', '5084300000', 'Darja Krivec'),
(722, 'Osnovna šola Videm', 1, NULL, 'Videm pri Ptuju', 2284, 180, 1, 1, '13592793', '5087171000', 'Helena Šegula'),
(723, 'Osnovna šola Videm pri Ptuju Podružnica Leskovec', 1, NULL, 'Zgornji Leskovec', 2285, 180, 1, 1, '13592793', '5087171002', ''),
(724, 'Osnovna šola Videm pri Ptuju Podružnica Sela', 1, NULL, 'Lovrenc na Dravskem polju', 2324, 180, 1, 1, '13592793', '5087171001', ''),
(725, 'Osnovna šola Vincenzo e Diego de Castro Piran', 1, NULL, 'Piran - Pirano', 6330, 17, 9, 1, '53413440', '5086442000', 'Dolores Bressan'),
(726, 'Osnovna šola Vincenzo e Diego de Castro Piran Podružnica Lucija', 1, NULL, 'Portorož - Portorose', 6320, 17, 9, 1, '53413440', '5086442001', ''),
(727, 'Osnovna šola Vincenzo e Diego de Castro Piran Podružnica Sečovlje', 1, NULL, 'Sečovlje - Sicciole', 6333, 17, 9, 1, '53413440', '5086442006', ''),
(728, 'Osnovna šola Vinica', 1, NULL, 'Vinica', 8344, 117, 8, 1, '75824973', '5082781000', 'Ines Žlogar'),
(729, 'Osnovna šola Vitanje', 1, NULL, 'Vitanje', 3205, 181, 7, 1, '65089600', '5087724000', 'Tilka Jakob'),
(730, 'Osnovna šola Vižmarje - Brod', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '31191070', '5084407000', 'Nevenka Lamut'),
(731, 'Osnovna šola Vič', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '35103086', '5084458000', 'Ana Vehar'),
(732, 'Osnovna šola Vodice', 1, NULL, 'Vodice', 1217, 182, 4, 1, '23124741', '5084377000', 'Cilka Marenče'),
(733, 'Osnovna šola Vodice Podružnica Utik', 1, NULL, 'Vodice', 1217, 182, 4, 1, '23124741', '5084377002', ''),
(734, 'Osnovna šola Vodmat', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '43102913', '5083478000', 'Mateja Petrič'),
(735, 'Osnovna šola Vojke Šmuc Izola', 1, NULL, 'Izola - Isola', 6310, 68, 9, 1, '79063152', '5083028000', 'Lenčka Prelovšek'),
(736, 'Osnovna šola Vojke Šmuc Izola Podružnica Korte', 1, NULL, 'Izola - Isola', 6310, 68, 9, 1, '79063152', '5083028001', ''),
(737, 'Osnovna šola Vojnik', 1, NULL, 'Vojnik', 3212, 93, 7, 1, '95289763', '5082684000', 'Majda Rojc'),
(738, 'Osnovna šola Vojnik Podružnica Nova Cerkev', 1, NULL, 'Nova Cerkev', 3203, 93, 7, 1, '95289763', '5082684002', ''),
(739, 'Osnovna šola Vojnik Podružnica Socka', 1, NULL, 'Nova Cerkev', 3203, 93, 7, 1, '95289763', '5082684001', ''),
(740, 'Osnovna šola Vojnik Podružnica Šmartno v Rožni dolini', 1, NULL, 'Šmartno v Rožni dolini', 3201, 15, 7, 1, '95289763', '5082684003', ''),
(741, 'Osnovna šola Voličina', 1, NULL, 'Voličina', 2232, 124, 1, 1, '60776641', '5084008000', 'Anton Goznik'),
(742, 'Osnovna šola Vransko - Tabor', 1, NULL, 'Vransko', 3305, 183, 7, 1, '65135482', '5088526000', 'Majda Pikl'),
(743, 'Osnovna šola Vransko Podružnica Tabor', 1, NULL, 'Tabor', 3304, 184, 7, 1, '65135482', '5088526001', ''),
(744, 'Osnovna šola Vrhovci', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '34317627', '5084989000', 'Marjanca Vampelj'),
(745, 'Osnovna šola Vuzenica', 1, NULL, 'Vuzenica', 2367, 185, 5, 1, '64020673', '5087279000', 'Miran Kus'),
(746, 'Osnovna šola XIV. divizije Senovo', 1, NULL, 'Senovo', 8281, 38, 6, 1, '26071240', '5083966000', 'Vinko Hostar'),
(747, 'Osnovna šola Zadobrova', 1, NULL, 'Ljubljana - Polje', 1260, 5, 4, 1, '32930798', '5205239000', 'Vladimir Znoj'),
(748, 'Osnovna šola Zalog', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '75894190', '5084296000', 'Rajko Mahkovic'),
(749, 'Osnovna šola Zbora odposlancev Kočevje', 1, NULL, 'Kočevje', 1330, 30, 8, 1, '95886478', '5084857000', 'Peter Pirc'),
(750, 'Osnovna šola Zreče', 1, NULL, 'Zreče', 3214, 186, 7, 1, '69998558', '5087732000', 'Ivan Olup'),
(751, 'Osnovna šola Zreče Podružnica Gorenje', 1, NULL, 'Zreče', 3214, 186, 7, 1, '69998558', '5087732001', ''),
(752, 'Osnovna šola Zreče Podružnica Stranice', 1, NULL, 'Stranice', 3206, 186, 7, 1, NULL, '5087732002', ''),
(753, 'Osnovna šola bratov Letonja Šmartno ob Paki', 1, NULL, 'Šmartno ob Paki', 3327, 187, 7, 1, '40878333', '5088178000', 'Bojan Juras'),
(754, 'Osnovna šola bratov Polančičev Maribor', 1, NULL, 'Maribor', 2000, 2, 1, 1, '36197254', '5085080000', 'Brigita Smogavec'),
(755, 'Osnovna šola dr. Aleš Bebler - Primož Hrvatini', 1, NULL, 'Ankaran - Ancarano', 6280, 20, 9, 1, '95309578', '5088704000', 'Branka Likon'),
(756, 'Osnovna šola dr. Aleš Bebler - Primož Hrvatini Podružnica Ankaran', 1, NULL, 'Ankaran - Ancarano', 6280, 20, 9, 1, '95309578', '5088704004', '---'),
(757, 'Osnovna šola dr. Antona Debeljaka Loški Potok', 1, NULL, 'Loški Potok', 1318, 188, 8, 1, '58814515', '5087422000', 'Janez Mihelič'),
(758, 'Osnovna šola dr. Antona Debeljaka Loški Potok Podružnica Podpreska', 1, NULL, 'Draga', 1319, 188, 8, 1, '58814515', '5087422002', ''),
(759, 'Osnovna šola dr. Antona Trstenjaka Negova', 1, NULL, 'Spodnji Ivanjci', 9245, 96, 2, 1, '92256457', '5082897000', 'Slavica Trstenjak'),
(760, 'Osnovna šola dr. Bogomirja Magajne Divača', 1, NULL, 'Divača', 6215, 189, 9, 1, '96121840', '5089336000', 'Damijana Gustinčič'),
(761, 'Osnovna šola dr. Bogomirja Magajne Divača Podružnica Senožeče', 1, NULL, 'Senožeče', 6224, 189, 9, 1, '96121840', '5089336002', ''),
(762, 'Osnovna šola dr. Bogomirja Magajne Divača Podružnica Vreme', 1, NULL, 'Vremski Britof', 6217, 189, 9, 1, '96121840', '5089336003', ''),
(763, 'Osnovna šola dr. Franceta Prešerna Ribnica', 1, NULL, 'Ribnica', 1310, 190, 8, 1, '66532060', '5087449000', 'Andreja Modic'),
(764, 'Osnovna šola dr. Franceta Prešerna Ribnica Podružnica Dolenja vas', 1, NULL, 'Dolenja vas', 1331, 190, 8, 1, '66532060', '5087449001', ''),
(765, 'Osnovna šola dr. Franceta Prešerna Ribnica Podružnica Sušje', 1, NULL, 'Ribnica', 1310, 190, 8, 1, '66532060', '5087449002', ''),
(766, 'Osnovna šola dr. Franja Žgeča Dornava', 1, NULL, 'Dornava', 2252, 191, 1, 1, '31182194', '5087015000', 'Iztok Hrastar'),
(767, 'Osnovna šola dr. Franja Žgeča Dornava Podružnica Polenšak', 1, NULL, 'Polenšak', 2257, 191, 1, 1, '31182194', '5087015001', ''),
(768, 'Osnovna šola dr. Ivana Korošca Borovnica', 1, NULL, 'Borovnica', 1353, 192, 4, 1, '27688836', '5088321000', 'Daniel Horvat'),
(769, 'Osnovna šola dr. Ivana Prijatelja Sodražica', 1, NULL, 'Sodražica', 1317, 193, 8, 1, '41016017', '5087465000', 'Majda Kovačič Cimperman'),
(770, 'Osnovna šola dr. Ivana Prijatelja Sodražica Podružnica Sv. Gregor', 1, NULL, 'Ortnek', 1316, 190, 8, 1, '41016017', '5087465001', ''),
(771, 'Osnovna šola dr. Janeza Mencingerja Boh. Bistrica Podružnica Srednja vas', 1, NULL, 'Srednja vas v Bohinju', 4267, 194, 3, 1, '51576597', '5087309002', ''),
(772, 'Osnovna šola dr. Janeza Mencingerja Bohinjska Bistrica', 1, NULL, 'Bohinjska Bistrica', 4264, 194, 3, 1, '51576597', '5087309000', 'Mojca Rozman'),
(773, 'Osnovna šola dr. Jožeta Pučnika Črešnjevec', 1, NULL, 'Slovenska Bistrica', 2310, 1, 1, 1, '33029512', '5087635000', 'Lidija Milošič'),
(774, 'Osnovna šola dr. Pavla Lunačka Šentrupert', 1, NULL, 'Šentrupert', 8232, 195, 8, 1, '79666981', '5088089000', 'Miroslava Brezovar'),
(775, 'Osnovna šola dr. Vita Kraigherja Ljubljana', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '69049408', '5083397000', 'Ljubomir Brezočnik'),
(776, 'Osnovna šola heroja J.Hribarja Stari trg pri Ložu Podružnica Iga vas', 1, NULL, 'Stari trg pri Ložu', 1386, 196, 12, 1, '58122982', '5089891001', ''),
(777, 'Osnovna šola heroja Janeza Hribarja Stari trg pri Ložu', 1, NULL, 'Stari trg pri Ložu', 1386, 196, 12, 1, '58122982', '5089891000', 'Sonja Jozelj'),
(778, 'Osnovna šola in vrtec Apače', 1, NULL, 'Apače', 9253, 197, 2, 1, '34766219', '5084768000', 'Violeta Kardinar'),
(779, 'Osnovna šola in vrtec Apače Podružnica Stogovci', 1, NULL, 'Apače', 9253, 197, 2, 1, '0', '5084768001', '---'),
(780, 'Osnovna šola in vrtec Sveta Trojica', 1, NULL, 'Sv. Trojica v Slov. goricah', 2235, 198, 1, 1, '94208247', '5084024000', 'Darko Škerget'),
(781, 'Osnovna šola narodnega heroja Maksa Pečarja', 1, NULL, 'Ljubljana - Črnuče', 1231, 5, 4, 1, '79338119', '5084091000', 'Zlatka Vlasta Zgonc');
INSERT INTO `school` (`id`, `name`, `school_category_id`, `address`, `post`, `postal_code`, `municipality_id`, `region_id`, `country_id`, `tax_number`, `identifier`, `headmaster`) VALUES
(782, 'Osnovna šola prof. dr. Josipa Plemlja Bled', 1, NULL, 'Bled', 4260, 199, 3, 1, '56918518', '5087295000', 'Ludvik Hajdinjak'),
(783, 'Osnovna šola prof. dr. Josipa Plemlja Bled Podružnica Bohinjska Bela', 1, NULL, 'Bohinjska Bela', 4263, 199, 3, 1, '56918518', '5087295001', ''),
(784, 'Osnovna šola prof. dr. Josipa Plemlja Bled Podružnica Ribno', 1, NULL, 'Bled', 4260, 199, 3, 1, '56918518', '5087295002', ''),
(785, 'Osnovna šola Šalek', 1, NULL, 'Velenje', 3320, 41, 7, 1, '85859966', '5278902000', 'Irena Poljanšek Sivka'),
(786, 'Osnovna šola Šalovci', 1, NULL, 'Šalovci', 9204, 11, 2, 1, '81487754', '5085713000', 'Jolanda Lazar'),
(787, 'Osnovna šola Šempas', 1, NULL, 'Šempas', 5261, 24, 10, 1, '76094693', '5086353000', 'Jadranka Kočevar'),
(788, 'Osnovna šola Šempeter v Savinjski dolini', 1, NULL, 'Šempeter v Savinjski dolini', 3311, 33, 7, 1, '77871430', '5088577000', 'Petra Stepišnik'),
(789, 'Osnovna šola Šentjanž pri Dravogradu', 1, NULL, 'Šentjanž pri Dravogradu', 2373, 147, 5, 1, '61137014', '5914183000', 'Dragica Jurjec'),
(790, 'Osnovna šola Šentjernej', 1, NULL, 'Šentjernej', 8310, 200, 8, 1, '77005821', '5086299000', 'Viktorija Rangus'),
(791, 'Osnovna šola Šentjernej Podružnica Orehovica', 1, NULL, 'Šentjernej', 8310, 200, 8, 1, '77005821', '5086299002', ''),
(792, 'Osnovna šola Šentvid', 1, NULL, 'Ljubljana - Šentvid', 1210, 5, 4, 1, '51719070', '5090016000', 'Nada Paj'),
(793, 'Osnovna šola Šenčur', 1, NULL, 'Šenčur', 4208, 201, 3, 1, '36605069', '5083249000', 'Majda Vehovec'),
(794, 'Osnovna šola Šenčur Podružnica Olševek', 1, NULL, 'Preddvor', 4205, 201, 3, 1, '0', '5083249003', '---'),
(795, 'Osnovna šola Šenčur Podružnica Trboje', 1, NULL, 'Kranj', 4000, 201, 3, 1, '0', '5083249004', '---'),
(796, 'Osnovna šola Šenčur Podružnica Voklo', 1, NULL, 'Šenčur', 4208, 201, 3, 1, '36605069', '5083249001', '---'),
(797, 'Osnovna šola Škofja Loka - Mesto', 1, NULL, 'Škofja Loka', 4220, 31, 3, 1, '24921394', '5089468000', 'Doris Kužel'),
(798, 'Osnovna šola Škofljica', 1, NULL, 'Škofljica', 1291, 202, 4, 1, '59782820', '5084482000', 'Roman Brunšek'),
(799, 'Osnovna šola Škofljica Podružnica Lavrica', 1, NULL, 'Škofljica', 1291, 202, 4, 1, NULL, '5084482002', ''),
(800, 'Osnovna šola Škofljica Podružnica Želimlje', 1, NULL, 'Škofljica', 1291, 202, 4, 1, '59782820', '5084482001', ''),
(801, 'Osnovna šola Šmarje pri Jelšah', 1, NULL, 'Šmarje pri Jelšah', 3240, 203, 7, 1, '94363455', '5087988000', 'Stanislav Šket'),
(802, 'Osnovna šola Šmarje pri Jelšah Podružnica Kristan vrh', 1, NULL, 'Podplat', 3241, 203, 7, 1, '94363455', '5087988006', ''),
(803, 'Osnovna šola Šmarje pri Jelšah Podružnica Mestinje', 1, NULL, 'Podplat', 3241, 203, 7, 1, '94363455', '5087988005', ''),
(804, 'Osnovna šola Šmarje pri Jelšah Podružnica Sladka gora', 1, NULL, 'Šmarje pri Jelšah', 3240, 203, 7, 1, '94363455', '5087988004', ''),
(805, 'Osnovna šola Šmarje pri Jelšah Podružnica Sv. Štefan', 1, NULL, 'Sveti Štefan', 3264, 203, 7, 1, '94363455', '5087988002', ''),
(806, 'Osnovna šola Šmarje pri Jelšah Podružnica Zibika', 1, NULL, 'Pristava pri Mestinju', 3253, 203, 7, 1, '94363455', '5087988001', ''),
(807, 'Osnovna šola Šmarje pri Jelšah Podružnica Šentvid pri Grobelnem', 1, NULL, 'Grobelno', 3231, 203, 7, 1, '94363455', '5087988003', ''),
(808, 'Osnovna šola Šmarje pri Kopru', 1, NULL, 'Šmarje', 6274, 20, 9, 1, '98962043', '5083842000', 'Edi Glavina'),
(809, 'Osnovna šola Šmarjeta', 1, NULL, 'Šmarješke Toplice', 8220, 204, 8, 1, '73055956', '5086302000', 'Nevenka Lahne'),
(810, 'Osnovna šola Šmartno na Pohorju', 1, NULL, 'Šmartno na Pohorju', 2315, 1, 1, 1, '15317765', '5089425000', 'Nevenka Potisk Dovnik'),
(811, 'Osnovna šola Šmartno pod Šmarno goro', 1, NULL, 'Ljubljana - Šmartno', 1211, 5, 4, 1, '61510971', '5133785000', 'Maksimiljan Košir'),
(812, 'Osnovna šola Šmartno pri Litiji', 1, NULL, 'Šmartno pri Litiji', 1275, 205, 4, 1, '76955052', '5084083000', 'Albert Pavli'),
(813, 'Osnovna šola Šmartno pri Litiji Podružnica Kostrevnica', 1, NULL, 'Šmartno pri Litiji', 1275, 205, 4, 1, '76955052', '5084083005', '---'),
(814, 'Osnovna šola Šmartno pri Litiji Podružnica Primskovo na Dol.', 1, NULL, 'Šmartno pri Litiji', 1275, 205, 4, 1, '76955052', '5084083001', '---'),
(815, 'Osnovna šola Šmartno pri Litiji Podružnica Štangarske Poljane', 1, NULL, 'Šmartno pri Litiji', 1275, 205, 4, 1, '76955052', '5084083004', '---'),
(816, 'Osnovna šola Šmartno pri Slovenj Gradcu', 1, NULL, 'Šmartno pri Slovenj Gradcu', 2383, 7, 5, 1, '15598586', '5089409000', 'Zdravko Jamnikar'),
(817, 'Osnovna šola Šmartno v Tuhinju', 1, NULL, 'Laze v Tuhinju', 1219, 6, 4, 1, '47328304', '5950686000', 'Jožica Hribar'),
(818, 'Osnovna šola Šmartno v Tuhinju Podružnica Motnik', 1, NULL, 'Motnik', 1221, 6, 4, 1, NULL, '5950686001', ''),
(819, 'Osnovna šola Šmartno v Tuhinju Podružnica Sela', 1, NULL, 'Kamnik', 1241, 6, 4, 1, NULL, '5950686002', ''),
(820, 'Osnovna šola Šmartno v Tuhinju Podružnica Zgornji Tuhinj', 1, NULL, 'Laze v Tuhinju', 1219, 6, 4, 1, NULL, '5950686003', ''),
(821, 'Osnovna šola Šmihel Novo mesto', 1, NULL, 'Novo mesto', 8000, 16, 8, 1, '39971953', '5086841000', 'Irena Hlača'),
(822, 'Osnovna šola Šmihel Novo mesto Podružnica Birčna vas', 1, NULL, 'Novo mesto', 8000, 16, 8, 1, '39971953', '5086841001', '---'),
(823, 'Osnovna šola Štore', 1, NULL, 'Štore', 3220, 206, 7, 1, '24735779', '5082676000', 'Franc Rumpf'),
(824, 'Osnovna šola Štore Podružnica Kompole', 1, NULL, 'Štore', 3220, 206, 7, 1, '24735779', '5082676001', ''),
(825, 'Osnovna šola Šturje Ajdovščina', 1, NULL, 'Ajdovščina', 5270, 67, 10, 1, '39855210', '2294460000', 'Ava Curk'),
(826, 'Osnovna šola Šturje Ajdovščina Podružnica Budanje', 1, NULL, 'Vipava', 5271, 67, 10, 1, '39855210', '2294460001', 'Glej matično šolo'),
(827, 'Osnovna šola Železniki', 1, NULL, 'Železniki', 4228, 207, 3, 1, '36326020', '5087830000', 'Franc Rant'),
(828, 'Osnovna šola Železniki Podružnica Davča', 1, NULL, 'Železniki', 4228, 207, 3, 1, '36326020', '5087830001', ''),
(829, 'Osnovna šola Železniki Podružnica Dražgoše', 1, NULL, 'Železniki', 4228, 207, 3, 1, '36326020', '5087830002', ''),
(830, 'Osnovna šola Železniki Podružnica Selca', 1, NULL, 'Selca', 4227, 207, 3, 1, '36326020', '5087830004', ''),
(831, 'Osnovna šola Železniki Podružnica Sorica', 1, NULL, 'Sorica', 4229, 207, 3, 1, '36326020', '5087830005', ''),
(832, 'Osnovna šola Žetale', 1, NULL, 'Žetale', 2287, 208, 1, 1, '59442018', '5968330000', 'Anton Butolen'),
(833, 'Osnovna šola Žiri', 1, NULL, 'Žiri', 4226, 209, 3, 1, '79208843', '5089476000', 'Marijan Žakelj'),
(834, 'Osnovna šola Žirovnica', 1, NULL, 'Žirovnica', 4274, 210, 3, 1, '55702759', '5719062000', 'Valentin Sodja'),
(835, 'Osnovna šola Žužemberk', 1, NULL, 'Žužemberk', 8360, 155, 8, 1, '97836311', '5086337000', 'Mira Kovač'),
(836, 'Osnovna šola Žužemberk Podružnica Ajdovec', 1, NULL, 'Dvor', 8361, 155, 8, 1, '97836311', '5086337001', ''),
(837, 'Osnovna šola Žužemberk Podružnica Dvor', 1, NULL, 'Dvor', 8361, 155, 8, 1, '97836311', '5086337002', ''),
(838, 'Osnovna šola Žužemberk Podružnica Šmihel', 1, NULL, 'Žužemberk', 8360, 155, 8, 1, '97836311', '5086337003', ''),
(839, 'Osnovna šola Čepovan', 1, NULL, 'Čepovan', 5253, 24, 10, 1, '46864237', '5088992000', 'Helena Hvala'),
(840, 'Osnovna šola Črna na Koroškem', 1, NULL, 'Črna na Koroškem', 2393, 211, 5, 1, '98266225', '5087368000', 'Romana Košutnik'),
(841, 'Osnovna šola Črna na Koroškem Podružnica Javorje', 1, NULL, 'Črna na Koroškem', 2393, 211, 5, 1, '98266225', '5087368001', '---'),
(842, 'Osnovna šola Črna na Koroškem Podružnica Koprivna', 1, NULL, 'Črna na Koroškem', 2393, 211, 5, 1, '98266225', '5087368002', '---'),
(843, 'Osnovna šola Črna na Koroškem Podružnica Žerjav', 1, NULL, 'Črna na Koroškem', 2393, 211, 5, 1, '98266225', '5087368003', '---'),
(844, 'Osnovna šola Črni Vrh', 1, NULL, 'Črni vrh nad Idrijo', 5274, 22, 10, 1, '55214959', '5082978000', 'Irena Kenk'),
(845, 'Prometna šola Maribor', 6, NULL, 'Maribor', 2000, 2, 1, 1, '49707728', '5183120000', 'mag. Oton Mlakar'),
(846, 'Prometna šola Maribor, Srednja prometna šola in dijaški dom', 6, NULL, 'Maribor', 2000, 2, 1, 1, '49707728', '5183120003', 'mag. Mateja Turk'),
(847, 'Prva gimnazija Maribor', 6, NULL, 'Maribor', 2000, 2, 1, 1, '41623878', '5085535000', 'Herman Pušnik'),
(848, 'Prva osnovna šola Slovenj Gradec', 1, NULL, 'Slovenj Gradec', 2380, 7, 5, 1, '23083972', '5089395000', 'Zvonka Murko'),
(849, 'Prva osnovna šola Slovenj Gradec Podružnica Sele-Vrhe', 1, NULL, 'Slovenj Gradec', 2380, 7, 5, 1, '23083972', '5089395002', ''),
(850, 'Srednja ekonomska šola Ljubljana', 6, NULL, 'Ljubljana', 1000, 5, 4, 1, '43787991', '5084199000', 'Andreja Preskar'),
(851, 'Srednja ekonomska šola Maribor', 6, NULL, 'Maribor', 2000, 2, 1, 1, '39643735', '5085527000', 'Darja Cizel'),
(852, 'Srednja ekonomsko - poslovna šola Koper', 6, NULL, 'Koper - Capodistria', 6000, 20, 9, 1, '26806088', '5088712000', 'Branka Žerjal v. d.'),
(853, 'Srednja frizerska šola Ljubljana', 6, NULL, 'Ljubljana', 1000, 5, 4, 1, '42992206', '5653347000', 'mag. Primož Hvala Kamenšček'),
(854, 'Srednja gostinska in turistična šola Radovljica', 6, NULL, 'Radovljica', 4240, 13, 3, 1, '29929610', '5921678000', 'Marjana Potočnik'),
(855, 'Srednja gozdarska in lesarska šola Postojna', 6, NULL, 'Postojna', 6230, 42, 12, 1, '55477232', '5089808000', 'Cvetka Kernel'),
(856, 'Srednja gradbena šola in gimnazija Maribor', 6, NULL, 'Maribor', 2000, 2, 1, 1, '77098846', '5089930000', 'Alenka Ambrož Jurgec'),
(857, 'Srednja gradbena, geodetska in okoljevarstvena šola Ljubljana', 6, NULL, 'Ljubljana', 1000, 5, 4, 1, '54108411', '5084130000', 'Vojko Goričan'),
(858, 'Srednja medijska in grafična šola Ljubljana', 6, NULL, 'Ljubljana', 1000, 5, 4, 1, '77459849', '5086671000', 'Ana Šterbenc'),
(859, 'Srednja poklicna in strokovna šola Bežigrad-Ljubljana', 6, NULL, 'Ljubljana', 1000, 5, 4, 1, '55517951', '5089883000', 'Frančiška Al-Mansour'),
(860, 'Srednja poklicna in strokovna šola Bežigrad-Ljubljana, Srednja poklicna in strokovna šola Bežigrad', 6, NULL, 'Ljubljana', 1000, 5, 4, 1, '55517951', '5089883001', ''),
(861, 'Srednja poklicna in tehniška šola Murska Sobota', 6, NULL, 'Murska Sobota', 9000, 3, 2, 1, '54021839', '5508550000', 'Ludvik Sukič'),
(862, 'Srednja tehniška in poklicna šola Trbovlje', 6, NULL, 'Trbovlje', 1420, 28, 11, 1, '15203298', '5243297000', 'Marjetka Bizjak'),
(863, 'Srednja tehniška šola Koper', 6, NULL, 'Koper - Capodistria', 6000, 20, 9, 1, '67914063', '5083176000', 'Iztok Drožina'),
(864, 'Srednja trgovska šola Ljubljana', 6, NULL, 'Ljubljana', 1000, 5, 4, 1, '95740791', '5086647000', 'Marjan Jerič'),
(865, 'Srednja trgovska šola Maribor', 6, NULL, 'Maribor', 2000, 2, 1, 1, '17683785', '5086744000', 'Alojz Velički'),
(866, 'Srednja upravno - administrativna šola Ljubljana', 6, NULL, 'Ljubljana', 1000, 5, 4, 1, '50498720', '5086094000', 'Dušan Vodeb'),
(867, 'Srednja vzgojiteljska šola in gimnazija Ljubljana', 6, NULL, 'Ljubljana', 1000, 5, 4, 1, '47364220', '5084903000', 'Alojz Pluško'),
(868, 'Srednja zdravstvena in kozmetična šola Maribor', 6, NULL, 'Maribor', 2000, 2, 1, 1, '86411462', '5088895000', 'Nevenka Kisner'),
(869, 'Srednja zdravstvena šola Celje', 6, NULL, 'Celje', 3000, 15, 7, 1, '52910946', '5083621000', 'Katja Pogelšek Žilavec'),
(870, 'Srednja zdravstvena šola Ljubljana', 6, NULL, 'Ljubljana', 1000, 5, 4, 1, '31987249', '5242045000', 'Marija Verbič'),
(871, 'Srednja zdravstvena šola Murska Sobota', 6, NULL, 'Murska Sobota', 9000, 3, 2, 1, '45797781', '5085748000', 'Zlatka Lebar'),
(872, 'Srednja šola Domžale', 6, NULL, 'Domžale', 1230, 73, 4, 1, '28922026', '5084750000', 'mag. Primož Škofic'),
(873, 'Srednja šola Domžale, Gimnazija', 6, NULL, 'Domžale', 1230, 73, 4, 1, '28922026', '5084750005', 'Primož Škofic'),
(874, 'Srednja šola Domžale, Poklicna in strokovna šola', 6, NULL, 'Domžale', 1230, 73, 4, 1, '28922026', '5084750004', 'Marko Mlakar'),
(875, 'Srednja šola Izola', 6, NULL, 'Izola - Isola', 6310, 68, 9, 1, '83800280', '6285996000', 'v. d. Adelija Perne'),
(876, 'Srednja šola Jesenice', 6, NULL, 'Jesenice', 4270, 21, 3, 1, '62275348', '5854105000', 'Stanko Vidmar'),
(877, 'Srednja šola Josipa Jurčiča Ivančna Gorica', 6, NULL, 'Ivančna Gorica', 1295, 87, 4, 1, '11898852', '5623685000', 'Milan Jevnikar'),
(878, 'Srednja šola Pietro Coppo Izola', 6, NULL, 'Izola - Isola', 6310, 68, 9, 1, '47081961', '5083893000', 'Alberto Scheriani'),
(879, 'Srednja šola Slovenska Bistrica', 6, NULL, 'Slovenska Bistrica', 2310, 1, 1, 1, '10927140', '1429221000', 'mag. Iva Pučnik Ozimič'),
(880, 'Srednja šola Veno Pilon Ajdovščina', 6, NULL, 'Ajdovščina', 5270, 67, 10, 1, '13997360', '5084997000', 'mag. Alojz Likar'),
(881, 'Srednja šola Zagorje', 6, NULL, 'Zagorje ob Savi', 1410, 102, 11, 1, '62434934', '5263603000', 'Anica Ule Maček'),
(882, 'Srednja šola tehniških strok Šiška', 6, NULL, 'Ljubljana', 1000, 5, 4, 1, '57726612', '5631564000', 'Darinka Martincic Zalokar'),
(883, 'Srednja šola za farmacijo, kozmetiko in zdravstvo', 6, NULL, 'Ljubljana', 1000, 5, 4, 1, '45091501', '5084911000', 'Marija Šušteršič'),
(884, 'Srednja šola za gostinstvo in turizem Celje', 6, NULL, 'Celje', 3000, 15, 7, 1, '16722841', '5085900000', 'Iztok Leskovar'),
(885, 'Srednja šola za gostinstvo in turizem Maribor', 6, NULL, 'Maribor', 2000, 2, 1, 1, '79487491', '5086752000', 'Dušan Erjavec'),
(886, 'Srednja šola za gostinstvo in turizem Radenci', 6, NULL, 'Radenci', 9252, 114, 2, 1, '90515781', '5084784000', 'Janja Prašnikar Neuvirt'),
(887, 'Srednja šola za gostinstvo in turizem v Ljubljani', 6, NULL, 'Ljubljana', 1000, 5, 4, 1, '65441419', '5084890000', 'Marjeta Smole'),
(888, 'Srednja šola za oblikovanje Maribor', 6, NULL, 'Maribor', 2000, 2, 1, 1, '72453117', '5086736000', 'Irena Labaš'),
(889, 'Srednja šola za oblikovanje in fotografijo Ljubljana', 6, NULL, 'Ljubljana', 1000, 5, 4, 1, '64067076', '5086108000', 'Gregor Markelj'),
(890, 'Srednja šola Črnomelj', 6, NULL, 'Črnomelj', 8340, 117, 8, 1, '72429968', '5085934000', 'Stanislav Vrščaj'),
(891, 'VIZ II. OŠ Rogaška Slatina', 1, NULL, 'Rogaška Slatina', 3250, 32, 7, 1, '60425571', '5278945000', 'mag. Karla Škrinjarić'),
(892, 'Waldorfska šola Ljubljana', 1, NULL, 'Ljubljana', 1000, 5, 4, 1, '65714415', '5642574000', 'Iztok Kordiš'),
(893, 'Waldorfska šola Ljubljana, enota Celje', 1, NULL, 'Celje', 3000, 15, 7, 1, '65714415', '5642574009', 'Boštjan Štrajhar'),
(894, 'Waldorfska šola Ljubljana, enota Gorenjska', 1, NULL, 'Radovljica', 4240, 13, 3, 1, '65714415', '5642574010', ''),
(895, 'Waldorfska šola Ljubljana, enota Maribor', 1, NULL, 'Maribor', 2000, 2, 1, 1, '65714415', '5642574003', 'Maksimiljan Rimele'),
(896, 'Zavod Antona Martina Slomška', 6, NULL, 'Maribor', 2000, 2, 1, 1, '26341395', '5921449000', 'dr. Ivan Štuhec'),
(897, 'Zavod Antona Martina Slomška, Škofijska gimnazija Antona Martina Slomška', 6, NULL, 'Maribor', 2000, 2, 1, 1, '26341395', '5921449001', 'Irena Rebolj Kraner'),
(898, 'Zavod sv. Frančiška Saleškega Gimnazija Želimlje', 6, NULL, 'Škofljica', 1291, 202, 4, 1, '18346308', '5502098000', 'Peter Polc'),
(899, 'Zavod sv. Stanislava', 6, NULL, 'Ljubljana - Šentvid', 1210, 5, 4, 1, '13707787', '5699827000', 'dr. Roman Globokar'),
(900, 'Zavod sv. Stanislava, Osnovna šola Alojzija Šuštarja Ljubljana', 1, NULL, 'Ljubljana - Šentvid', 1210, 5, 4, 1, '13707787', '5699827003', 'Marina Rugelj'),
(901, 'Zavod sv. Stanislava, Škofijska klasična gimnazija', 6, NULL, 'Ljubljana - Šentvid', 1210, 5, 4, 1, '13707787', '5699827001', 'Jožef Pucihar'),
(902, 'Škofijska gimnazija Vipava', 6, NULL, 'Vipava', 5271, 80, 10, 1, '42192790', '5221749000', 'Vladimir Anžel'),
(903, 'Šola za hortikulturo in vizualne umetnosti Celje', 6, NULL, 'Celje', 3000, 15, 7, 1, '83625950', '1201794000', 'Rafael Hrustel'),
(904, 'Šola za hortikulturo in vizualne umetnosti Celje, Srednja poklicna in strokovna šola', 6, NULL, 'Celje', 3000, 15, 7, 1, '83625950', '1201794001', 'Rafael Hrustel v. d.'),
(905, 'Šolski center Celje', 6, NULL, 'Celje', 3000, 15, 7, 1, '76965007', '5082692000', 'Igor Dosedla'),
(906, 'Šolski center Celje, Gimnazija Lava', 6, NULL, 'Celje', 3000, 15, 7, 1, '76965007', '5082692001', 'Marija Gubenšek Vezočnik'),
(907, 'Šolski center Celje, Srednja šola za gradbeništvo in varovanje okolja', 6, NULL, 'Celje', 3000, 15, 7, 1, '76965007', '5082692004', 'Irena Posavec'),
(908, 'Šolski center Celje, Srednja šola za kemijo, elektrotehniko in računalništvo', 6, NULL, 'Celje', 3000, 15, 7, 1, '76965007', '5082692003', 'Mojmir Klovar'),
(909, 'Šolski center Celje, Srednja šola za storitvene dejavnosti in logistiko', 6, NULL, 'Celje', 3000, 15, 7, 1, '76965007', '5082692008', 'Veronika Kokot'),
(910, 'Šolski center Celje, Srednja šola za strojništvo, mehatroniko in medije', 6, NULL, 'Celje', 3000, 15, 7, 1, '76965007', '5082692002', 'Ludvik Aškerc'),
(911, 'Šolski center Kranj', 6, NULL, 'Kranj', 4000, 19, 3, 1, '12782076', '6286259000', 'v. d. Jože Drenovec'),
(912, 'Šolski center Kranj, Srednja ekonomska, storitvena in gradbena šola', 6, NULL, 'Kranj', 4000, 19, 3, 1, '12782076', '6286259005', 'v. d. Damjana Furlan Lazar'),
(913, 'Šolski center Kranj, Srednja šola za elektrotehniko in računalništvo', 6, NULL, 'Kranj', 4000, 19, 3, 1, '12782076', '6286259004', 'v. d. Saša Kocijančič'),
(914, 'Šolski center Kranj, Strokovna gimnazija', 6, NULL, 'Kranj', 4000, 19, 3, 1, '12782076', '6286259003', 'v. d. Zdenka Varl'),
(915, 'Šolski center Krško - Sevnica', 6, NULL, 'Krško', 8270, 38, 6, 1, '36867578', '5083982000', 'mag. Alenka Žuraj Balog'),
(916, 'Šolski center Krško - Sevnica, Gimnazija Krško', 6, NULL, 'Krško', 8270, 38, 6, 1, NULL, '5083982003', 'Erna Župan'),
(917, 'Šolski center Krško - Sevnica, Srednja poklicna in strokovna šola Krško', 6, NULL, 'Krško', 8270, 38, 6, 1, NULL, '5083982002', 'Jože Pavlovič'),
(918, 'Šolski center Krško - Sevnica, Srednja šola Sevnica', 6, NULL, 'Sevnica', 8290, 51, 6, 1, '36867578', '5083982001', 'Alenka Žuraj Balog'),
(919, 'Šolski center Ljubljana', 6, NULL, 'Ljubljana', 1000, 5, 4, 1, '73059471', '1430971000', 'Nives Počkar'),
(920, 'Šolski center Ljubljana, Gimnazija Antona Aškerca', 6, NULL, 'Ljubljana', 1000, 5, 4, 1, '73059471', '1430971001', 'v. d. Zdenka Može Jedrejčić'),
(921, 'Šolski center Ljubljana, Srednja lesarska šola', 6, NULL, 'Ljubljana', 1000, 5, 4, 1, '73059471', '1430971003', 'mag. Majda Kanop'),
(922, 'Šolski center Ljubljana, Srednja strojna in kemijska šola', 6, NULL, 'Ljubljana', 1000, 5, 4, 1, '73059471', '1430971004', 'Zdenko Nosan'),
(923, 'Šolski center Maribor', 6, NULL, 'Maribor', 2000, 2, 1, 1, '76632733', '6278523000', 'v. d. Drago Kamenik'),
(924, 'Šolski center Maribor, Srednja elektro-računalniška šola', 6, NULL, 'Maribor', 2000, 2, 1, 1, '76632733', '6278523001', 'Irena Srša Žnidarič'),
(925, 'Šolski center Maribor, Srednja lesarska šola', 6, NULL, 'Maribor', 2000, 2, 1, 1, '76632733', '6278523003', 'Aleš Hus'),
(926, 'Šolski center Maribor, Srednja strojna šola', 6, NULL, 'Maribor', 2000, 2, 1, 1, '76632733', '6278523005', 'Drago Kamenik'),
(927, 'Šolski center Nova Gorica', 6, NULL, 'Nova Gorica', 5000, 24, 10, 1, '69993211', '5089085000', 'Egon Pipan'),
(928, 'Šolski center Nova Gorica, Biotehniška šola', 6, NULL, 'Šempeter pri Gorici', 5290, 103, 10, 1, '69993211', '5089085006', 'Barbara Miklavčič Velikonja'),
(929, 'Šolski center Nova Gorica, Elektrotehniška in računalniška šola', 6, NULL, 'Nova Gorica', 5000, 24, 10, 1, '69993211', '5089085002', 'Robert Peršič'),
(930, 'Šolski center Nova Gorica, Gimnazija in zdravstvena šola', 6, NULL, 'Nova Gorica', 5000, 24, 10, 1, '69993211', '5089085008', 'Vesna Žele'),
(931, 'Šolski center Nova Gorica, Srednja ekonomska in trgovska šola', 6, NULL, 'Nova Gorica', 5000, 24, 10, 1, '69993211', '5089085010', 'v. d. Inga Krusič Lamut'),
(932, 'Šolski center Nova Gorica, Strojna, prometna in lesarska šola', 6, NULL, 'Nova Gorica', 5000, 24, 10, 1, '69993211', '5089085007', 'Simon Kragelj'),
(933, 'Šolski center Novo mesto', 6, NULL, 'Novo mesto', 8000, 16, 8, 1, '68565127', '5258782000', 'Štefan David'),
(934, 'Šolski center Novo mesto, Srednja elektro šola in tehniška gimnazija', 6, NULL, 'Novo mesto', 8000, 16, 8, 1, '68565127', '5258782001', 'Boris Plut'),
(935, 'Šolski center Novo mesto, Srednja gradbena in lesarska šola', 6, NULL, 'Novo mesto', 8000, 16, 8, 1, '68565127', '5258782003', 'Damjana Gruden'),
(936, 'Šolski center Novo mesto, Srednja strojna šola', 6, NULL, 'Novo mesto', 8000, 16, 8, 1, '68565127', '5258782002', 'Sebastijan Brežnjak'),
(937, 'Šolski center Novo mesto, Srednja zdravstvena in kemijska šola', 6, NULL, 'Novo mesto', 8000, 16, 8, 1, '68565127', '5258782004', 'Miran Grom'),
(938, 'Šolski center Novo mesto, Srednja šola Metlika', 6, NULL, 'Metlika', 8330, 135, 8, 1, '68565127', '5258782006', 'Branka Klarić'),
(939, 'Šolski center Postojna', 6, NULL, 'Postojna', 6230, 42, 12, 1, '17067006', '5086957000', 'Helena Posega Dolenc'),
(940, 'Šolski center Postojna, Gimnazija Ilirska Bistrica', 6, NULL, 'Ilirska Bistrica', 6250, 45, 12, 1, '17067006', '5086957002', 'Helena Posega Dolenc'),
(941, 'Šolski center Postojna, Srednja šola', 6, NULL, 'Postojna', 6230, 42, 12, 1, '17067006', '5086957001', 'Helena Posega Dolenc'),
(942, 'Šolski center Ptuj', 6, NULL, 'Ptuj', 2250, 26, 1, 1, '23369809', '5064678000', 'Branko Kumer'),
(943, 'Šolski center Ptuj, Biotehniška šola', 6, NULL, 'Ptuj', 2250, 26, 1, 1, '23369809', '5064678003', 'dr. Vladimir Korošec'),
(944, 'Šolski center Ptuj, Ekonomska šola', 6, NULL, 'Ptuj', 2250, 26, 1, 1, '23369809', '5064678002', 'mag. Branka Kampl Regvat'),
(945, 'Šolski center Ptuj, Elektro in računalniška šola', 6, NULL, 'Ptuj', 2250, 26, 1, 1, '23369809', '5064678004', 'Rajko Fajt'),
(946, 'Šolski center Ptuj, Strojna šola', 6, NULL, 'Ptuj', 2250, 26, 1, 1, '23369809', '5064678005', 'Bojan Lampret'),
(947, 'Šolski center Ravne na Koroškem', 6, NULL, 'Ravne na Koroškem', 2390, 35, 5, 1, '27201163', '2345188000', 'Dragomir Benko'),
(948, 'Šolski center Ravne na Koroškem, Gimnazija', 6, NULL, 'Ravne na Koroškem', 2390, 35, 5, 1, '27201163', '2345188001', 'Dragomir Benko'),
(949, 'Šolski center Ravne na Koroškem, Srednja šola', 6, NULL, 'Ravne na Koroškem', 2390, 35, 5, 1, '27201163', '2345188002', 'Ivanka Stopar'),
(950, 'Šolski center Rogaška Slatina', 6, NULL, 'Rogaška Slatina', 3250, 32, 7, 1, '21344205', '5087996000', 'Anita Pihlar'),
(951, 'Šolski center Slovenj Gradec', 6, NULL, 'Slovenj Gradec', 2380, 7, 5, 1, '73346276', '5089417000', 'mag. Gabrijela Kotnik'),
(952, 'Šolski center Slovenj Gradec, Gimnazija', 6, NULL, 'Slovenj Gradec', 2380, 7, 5, 1, '73346276', '5089417001', 'mag. Stane Berzelak'),
(953, 'Šolski center Slovenj Gradec, Srednja zdravstvena šola', 6, NULL, 'Slovenj Gradec', 2380, 7, 5, 1, '73346276', '5089417002', 'Blaž Šušel'),
(954, 'Šolski center Slovenj Gradec, Srednja šola Slovenj Gradec in Muta', 6, NULL, 'Slovenj Gradec', 2380, 7, 5, 1, '73346276', '5089417007', 'Bernard Kresnik v. d.'),
(955, 'Šolski center Slovenske Konjice - Zreče', 6, NULL, 'Slovenske Konjice', 3210, 128, 7, 1, '93550049', '5052343000', 'mag. Milan Sojč'),
(956, 'Šolski center Slovenske Konjice - Zreče, Gimnazija Slovenske Konjice', 6, NULL, 'Slovenske Konjice', 3210, 128, 7, 1, '93550049', '5052343001', 'Milan Sojč'),
(957, 'Šolski center Slovenske Konjice - Zreče, Srednja poklicna in strokovna šola Zreče', 6, NULL, 'Zreče', 3214, 186, 7, 1, '93550049', '5052343002', 'Milan Sojč'),
(958, 'Šolski center Srečka Kosovela Sežana', 6, NULL, 'Sežana', 6210, 83, 9, 1, '74080601', '5009189000', 'Dušan Štolfa'),
(959, 'Šolski center Srečka Kosovela Sežana, Gimnazija in ekonomska šola', 6, NULL, 'Sežana', 6210, 83, 9, 1, '74080601', '5009189004', 'Dušan Štolfa'),
(960, 'Šolski center Velenje', 6, NULL, 'Velenje', 3320, 41, 7, 1, '98282522', '5243050000', 'mag. Ivan Kotnik'),
(961, 'Šolski center Velenje, Elektro in računalniška šola', 6, NULL, 'Velenje', 3320, 41, 7, 1, '98282522', '5243050005', 'Simon Konečnik'),
(962, 'Šolski center Velenje, Gimnazija', 6, NULL, 'Velenje', 3320, 41, 7, 1, '98282522', '5243050001', 'Rajmund Valcl'),
(963, 'Šolski center Velenje, Rudarska šola', 6, NULL, 'Velenje', 3320, 41, 7, 1, '98282522', '5243050002', 'mag. Albin Vrabič'),
(964, 'Šolski center Velenje, Strojna šola', 6, NULL, 'Velenje', 3320, 41, 7, 1, '98282522', '5243050003', 'Janko Pogorelčnik'),
(965, 'Šolski center Velenje, Šola za storitvene dejavnosti', 6, NULL, 'Velenje', 3320, 41, 7, 1, '98282522', '5243050004', 'Mateja Klemenčič'),
(966, 'Šolski center za pošto, ekonomijo in telekomunikacije Ljubljana', 6, NULL, 'Ljubljana', 1000, 5, 4, 1, '76893375', '5083435000', 'Ida Srebotnik'),
(967, 'Šolski center za pošto, ekonomijo in telekomunikacije Ljubljana, Srednja tehniška in strokovna šola', 6, NULL, 'Ljubljana', 1000, 5, 4, 1, '76893375', '5083435001', 'Srečko Lanjšček'),
(968, 'Šolski center Šentjur', 6, NULL, 'Šentjur', 3230, 54, 7, 1, '11775823', '1214438000', 'mag. Branko Šket'),
(969, 'Šolski center Šentjur, Srednja poklicna in strokovna šola', 6, NULL, 'Šentjur', 3230, 54, 7, 1, '11775823', '1214438002', 'mag. Janez Vodopivc'),
(970, 'Šolski center Škofja Loka', 6, NULL, 'Škofja Loka', 4220, 31, 3, 1, '13129635', '5087872000', 'Martin Pivk'),
(971, 'Šolski center Škofja Loka, Srednja šola za lesarstvo', 6, NULL, 'Škofja Loka', 4220, 31, 3, 1, '13129635', '5087872004', 'Milan Štigl'),
(972, 'Šolski center Škofja Loka, Srednja šola za strojništvo', 6, NULL, 'Škofja Loka', 4220, 31, 3, 1, '13129635', '5087872001', 'mag. Mojca Šmelcer');

-- --------------------------------------------------------

--
-- Struktura tabele `school_category`
--

DROP TABLE IF EXISTS `school_category`;
CREATE TABLE IF NOT EXISTS `school_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `active` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=15 ;

--
-- Odloži podatke za tabelo `school_category`
--

INSERT INTO `school_category` (`id`, `name`, `active`) VALUES
(1, 'osnovna šola', 1),
(2, 'druge organizacija za izobraževanje odraslih', 0),
(3, 'višja strokovna šola', 0),
(4, 'vrtec', 0),
(5, 'ljudska univerza', 0),
(6, 'srednja šola', 1),
(7, 'šolske in obšolske dejavnosti', 0),
(8, 'Zavod za otroke s posebnimi potrebami', 0),
(9, 'osnovna šola za otroke s posebnimi potrebami', 0),
(10, 'Center za usposabljanje, delo in varstvo', 0),
(11, 'dijaški dom', 0),
(12, 'osnovno šolstvo (strokovne službe)', 0),
(13, 'glasbena šola', 0),
(14, 'svetovalni centri', 0);

-- --------------------------------------------------------

--
-- Struktura tabele `school_mentor`
--

DROP TABLE IF EXISTS `school_mentor`;
CREATE TABLE IF NOT EXISTS `school_mentor` (
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
  KEY `activated_by` (`activated_by`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Struktura tabele `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
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
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

--
-- Odloži podatke za tabelo `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `email`, `activkey`, `createtime`, `lastvisit`, `superuser`, `status`, `create_at`, `lastvisit_at`) VALUES
(1, 'admin', 'cecf42e9047e907a82379ad0e5bed03b3c565b1d707e199a14133950bf81c97f92e8e80ea8e466a3143c46229f79f377ed796cb17dc733c78b0ed1903a3c88ca', 'dean@black.si', '17105eaf793113a224e39463852f91267a26511bda9a30a81869bc27b8f35919931089bba8dfcabcfff40b5464b4086286eb5f2d6f4abd46bc0215bd4529ee10', 1353095367, 1361784920, 1, 1, '0000-00-00 00:00:00', '0000-00-00 00:00:00');

--
-- Omejitve tabel za povzetek stanja
--

--
-- Omejitve za tabelo `award`
--
ALTER TABLE `award`
  ADD CONSTRAINT `award_ibfk_1` FOREIGN KEY (`competition_user_id`) REFERENCES `competition_user` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Omejitve za tabelo `competition_category`
--
ALTER TABLE `competition_category`
  ADD CONSTRAINT `competition_category_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Omejitve za tabelo `competition_category_active`
--
ALTER TABLE `competition_category_active`
  ADD CONSTRAINT `competition_category_active_ibfk_1` FOREIGN KEY (`competition_id`) REFERENCES `competition` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `competition_category_active_ibfk_2` FOREIGN KEY (`competition_category_id`) REFERENCES `competition_category` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Omejitve za tabelo `competition_category_school`
--
ALTER TABLE `competition_category_school`
  ADD CONSTRAINT `competition_category_school_ibfk_1` FOREIGN KEY (`competition_id`) REFERENCES `competition` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `competition_category_school_ibfk_2` FOREIGN KEY (`competition_category_id`) REFERENCES `competition_category` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `competition_category_school_ibfk_3` FOREIGN KEY (`school_id`) REFERENCES `school` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Omejitve za tabelo `competition_category_school_mentor`
--
ALTER TABLE `competition_category_school_mentor`
  ADD CONSTRAINT `competition_category_school_mentor_ibfk_1` FOREIGN KEY (`disqualified_by`) REFERENCES `users` (`id`) ON DELETE SET NULL ON UPDATE NO ACTION,
  ADD CONSTRAINT `competition_category_school_mentor_ibfk_2` FOREIGN KEY (`competition_category_school_id`) REFERENCES `competition_category_school` (`competition_id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `competition_category_school_mentor_ibfk_3` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Omejitve za tabelo `competition_category_translation`
--
ALTER TABLE `competition_category_translation`
  ADD CONSTRAINT `competition_category_translation_ibfk_1` FOREIGN KEY (`competition_category_id`) REFERENCES `competition_category` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `competition_category_translation_ibfk_2` FOREIGN KEY (`language_id`) REFERENCES `language` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Omejitve za tabelo `competition_committee`
--
ALTER TABLE `competition_committee`
  ADD CONSTRAINT `competition_committee_ibfk_1` FOREIGN KEY (`competition_id`) REFERENCES `competition` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `competition_committee_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Omejitve za tabelo `competition_country`
--
ALTER TABLE `competition_country`
  ADD CONSTRAINT `competition_country_ibfk_1` FOREIGN KEY (`competition_id`) REFERENCES `competition` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `competition_country_ibfk_2` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Omejitve za tabelo `competition_question`
--
ALTER TABLE `competition_question`
  ADD CONSTRAINT `competition_question_ibfk_3` FOREIGN KEY (`question_id`) REFERENCES `question` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `competition_question_ibfk_2` FOREIGN KEY (`competition_id`) REFERENCES `competition` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Omejitve za tabelo `competition_question_category`
--
ALTER TABLE `competition_question_category`
  ADD CONSTRAINT `competition_question_category_ibfk_1` FOREIGN KEY (`competition_question_id`) REFERENCES `competition_question` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `competition_question_category_ibfk_2` FOREIGN KEY (`competition_category_id`) REFERENCES `competition_category` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `competition_question_category_ibfk_3` FOREIGN KEY (`competiton_question_difficulty_id`) REFERENCES `competition_question_difficulty` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Omejitve za tabelo `competition_question_difficulty`
--
ALTER TABLE `competition_question_difficulty`
  ADD CONSTRAINT `competition_question_difficulty_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Omejitve za tabelo `competition_question_difficulty_translation`
--
ALTER TABLE `competition_question_difficulty_translation`
  ADD CONSTRAINT `competition_question_difficulty_translation_ibfk_1` FOREIGN KEY (`competition_question_difficulty_id`) REFERENCES `competition_question_difficulty` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `competition_question_difficulty_translation_ibfk_2` FOREIGN KEY (`language_id`) REFERENCES `language` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Omejitve za tabelo `competition_translation`
--
ALTER TABLE `competition_translation`
  ADD CONSTRAINT `competition_translation_ibfk_1` FOREIGN KEY (`competition_id`) REFERENCES `competition` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `competition_translation_ibfk_2` FOREIGN KEY (`language_id`) REFERENCES `language` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Omejitve za tabelo `competition_user`
--
ALTER TABLE `competition_user`
  ADD CONSTRAINT `competition_user_ibfk_1` FOREIGN KEY (`competition_id`) REFERENCES `competition` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `competition_user_ibfk_2` FOREIGN KEY (`competition_category_id`) REFERENCES `competition_category` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `competition_user_ibfk_3` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE SET NULL ON UPDATE NO ACTION,
  ADD CONSTRAINT `competition_user_ibfk_4` FOREIGN KEY (`competition_category_school_mentor_id`) REFERENCES `competition_category_school_mentor` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `competition_user_ibfk_5` FOREIGN KEY (`school_id`) REFERENCES `school` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `competition_user_ibfk_6` FOREIGN KEY (`disqualified_request_by`) REFERENCES `users` (`id`) ON DELETE SET NULL ON UPDATE NO ACTION,
  ADD CONSTRAINT `competition_user_ibfk_7` FOREIGN KEY (`disqualified_by`) REFERENCES `users` (`id`) ON DELETE SET NULL ON UPDATE NO ACTION;

--
-- Omejitve za tabelo `competition_user_question`
--
ALTER TABLE `competition_user_question`
  ADD CONSTRAINT `competition_user_question_ibfk_3` FOREIGN KEY (`question_answer_id`) REFERENCES `question_answer` (`id`) ON DELETE SET NULL ON UPDATE NO ACTION,
  ADD CONSTRAINT `competition_user_question_ibfk_1` FOREIGN KEY (`competition_user_id`) REFERENCES `competition_user` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `competition_user_question_ibfk_2` FOREIGN KEY (`competition_question_id`) REFERENCES `competition_question` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Omejitve za tabelo `competition_user_question_answer`
--
ALTER TABLE `competition_user_question_answer`
  ADD CONSTRAINT `competition_user_question_answer_ibfk_2` FOREIGN KEY (`question_answer_id`) REFERENCES `question_answer` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `competition_user_question_answer_ibfk_1` FOREIGN KEY (`competition_user_question_id`) REFERENCES `competition_user_question` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Omejitve za tabelo `country_administrator`
--
ALTER TABLE `country_administrator`
  ADD CONSTRAINT `country_administrator_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `country_administrator_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Omejitve za tabelo `country_language`
--
ALTER TABLE `country_language`
  ADD CONSTRAINT `country_language_ibfk_2` FOREIGN KEY (`language_id`) REFERENCES `language` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `country_language_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Omejitve za tabelo `municipality`
--
ALTER TABLE `municipality`
  ADD CONSTRAINT `municipality_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Omejitve za tabelo `profiles`
--
ALTER TABLE `profiles`
  ADD CONSTRAINT `profiles_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `user_profile_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;

--
-- Omejitve za tabelo `question`
--
ALTER TABLE `question`
  ADD CONSTRAINT `question_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Omejitve za tabelo `question_answer`
--
ALTER TABLE `question_answer`
  ADD CONSTRAINT `question_answer_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `question` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Omejitve za tabelo `question_answer_translation`
--
ALTER TABLE `question_answer_translation`
  ADD CONSTRAINT `question_answer_translation_ibfk_3` FOREIGN KEY (`question_answer_id`) REFERENCES `question_answer` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `question_answer_translation_ibfk_2` FOREIGN KEY (`language_id`) REFERENCES `language` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Omejitve za tabelo `question_resource`
--
ALTER TABLE `question_resource`
  ADD CONSTRAINT `question_resource_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `question` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Omejitve za tabelo `question_translation`
--
ALTER TABLE `question_translation`
  ADD CONSTRAINT `question_translation_ibfk_2` FOREIGN KEY (`language_id`) REFERENCES `language` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `question_translation_ibfk_3` FOREIGN KEY (`question_id`) REFERENCES `question` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Omejitve za tabelo `region`
--
ALTER TABLE `region`
  ADD CONSTRAINT `region_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Omejitve za tabelo `school`
--
ALTER TABLE `school`
  ADD CONSTRAINT `school_ibfk_1` FOREIGN KEY (`school_category_id`) REFERENCES `school_category` (`id`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `school_ibfk_2` FOREIGN KEY (`municipality_id`) REFERENCES `municipality` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `school_ibfk_3` FOREIGN KEY (`region_id`) REFERENCES `region` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `school_ibfk_4` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Omejitve za tabelo `school_mentor`
--
ALTER TABLE `school_mentor`
  ADD CONSTRAINT `school_mentor_ibfk_1` FOREIGN KEY (`school_id`) REFERENCES `school` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `school_mentor_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `school_mentor_ibfk_3` FOREIGN KEY (`activated_by`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION;
SET FOREIGN_KEY_CHECKS=1;