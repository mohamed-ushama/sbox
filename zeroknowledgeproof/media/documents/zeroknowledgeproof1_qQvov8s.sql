-- phpMyAdmin SQL Dump
-- version 4.0.4
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 30, 2024 at 05:07 AM
-- Server version: 5.6.12-log
-- PHP Version: 5.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `zeroknowledgeproof1`
--
CREATE DATABASE IF NOT EXISTS `zeroknowledgeproof1` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `zeroknowledgeproof1`;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=49 ;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add compregistration', 7, 'add_compregistration'),
(26, 'Can change compregistration', 7, 'change_compregistration'),
(27, 'Can delete compregistration', 7, 'delete_compregistration'),
(28, 'Can view compregistration', 7, 'view_compregistration'),
(29, 'Can add comprequirement', 8, 'add_comprequirement'),
(30, 'Can change comprequirement', 8, 'change_comprequirement'),
(31, 'Can delete comprequirement', 8, 'delete_comprequirement'),
(32, 'Can view comprequirement', 8, 'view_comprequirement'),
(33, 'Can add myresource', 9, 'add_myresource'),
(34, 'Can change myresource', 9, 'change_myresource'),
(35, 'Can delete myresource', 9, 'delete_myresource'),
(36, 'Can view myresource', 9, 'view_myresource'),
(37, 'Can add s pregistration', 10, 'add_spregistration'),
(38, 'Can change s pregistration', 10, 'change_spregistration'),
(39, 'Can delete s pregistration', 10, 'delete_spregistration'),
(40, 'Can view s pregistration', 10, 'view_spregistration'),
(41, 'Can add outsourceesregistration', 11, 'add_outsourceesregistration'),
(42, 'Can change outsourceesregistration', 11, 'change_outsourceesregistration'),
(43, 'Can delete outsourceesregistration', 11, 'delete_outsourceesregistration'),
(44, 'Can view outsourceesregistration', 11, 'view_outsourceesregistration'),
(45, 'Can add zkpregistration', 12, 'add_zkpregistration'),
(46, 'Can change zkpregistration', 12, 'change_zkpregistration'),
(47, 'Can delete zkpregistration', 12, 'delete_zkpregistration'),
(48, 'Can view zkpregistration', 12, 'view_zkpregistration');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `clientupload`
--

CREATE TABLE IF NOT EXISTS `clientupload` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `companyname` varchar(50) NOT NULL,
  `serviceprovider` varchar(25) NOT NULL,
  `file_upload` varchar(800) NOT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `complaint`
--

CREATE TABLE IF NOT EXISTS `complaint` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `type` varchar(20) NOT NULL,
  `querry` varchar(800) NOT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=13 ;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(11, 'outsourcees', 'outsourceesregistration'),
(7, 'outsourcingportal', 'compregistration'),
(8, 'outsourcingportal', 'comprequirement'),
(9, 'outsourcingportal', 'myresource'),
(10, 'serviceproviders', 'spregistration'),
(6, 'sessions', 'session'),
(12, 'ZKPprotocols', 'zkpregistration');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=53 ;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'ZKPprotocols', '0001_initial', '2023-12-14 07:41:57.031838'),
(2, 'ZKPprotocols', '0002_rename_spregistration_zkpregistration', '2023-12-14 07:41:57.198825'),
(3, 'ZKPprotocols', '0003_alter_zkpregistration_knowledge', '2023-12-14 07:41:58.064722'),
(4, 'contenttypes', '0001_initial', '2023-12-14 07:41:58.660710'),
(5, 'auth', '0001_initial', '2023-12-14 07:42:06.493228'),
(6, 'admin', '0001_initial', '2023-12-14 07:42:08.137122'),
(7, 'admin', '0002_logentry_remove_auto_add', '2023-12-14 07:42:08.187164'),
(8, 'admin', '0003_logentry_add_action_flag_choices', '2023-12-14 07:42:08.224115'),
(9, 'contenttypes', '0002_remove_content_type_name', '2023-12-14 07:42:09.626036'),
(10, 'auth', '0002_alter_permission_name_max_length', '2023-12-14 07:42:10.379044'),
(11, 'auth', '0003_alter_user_email_max_length', '2023-12-14 07:42:11.115946'),
(12, 'auth', '0004_alter_user_username_opts', '2023-12-14 07:42:11.156974'),
(13, 'auth', '0005_alter_user_last_login_null', '2023-12-14 07:42:11.702935'),
(14, 'auth', '0006_require_contenttypes_0002', '2023-12-14 07:42:11.737907'),
(15, 'auth', '0007_alter_validators_add_error_messages', '2023-12-14 07:42:11.787903'),
(16, 'auth', '0008_alter_user_username_max_length', '2023-12-14 07:42:12.432889'),
(17, 'auth', '0009_alter_user_last_name_max_length', '2023-12-14 07:42:13.031834'),
(18, 'auth', '0010_alter_group_name_max_length', '2023-12-14 07:42:13.678790'),
(19, 'auth', '0011_update_proxy_permissions', '2023-12-14 07:42:13.720788'),
(20, 'auth', '0012_alter_user_first_name_max_length', '2023-12-14 07:42:14.455746'),
(21, 'outsourcees', '0001_initial', '2023-12-14 07:42:14.815723'),
(22, 'outsourcees', '0002_outsourceesregistration_ntime', '2023-12-14 07:42:15.367690'),
(23, 'outsourcees', '0003_alter_outsourceesregistration_ntime', '2023-12-14 07:42:16.105648'),
(24, 'outsourcees', '0004_alter_outsourceesregistration_ntime', '2023-12-14 07:42:16.146643'),
(25, 'outsourcees', '0005_alter_outsourceesregistration_ntime', '2023-12-14 07:42:16.578637'),
(26, 'outsourcingportal', '0001_initial', '2023-12-14 07:42:17.701552'),
(27, 'serviceproviders', '0001_initial', '2023-12-14 07:42:18.067535'),
(28, 'serviceproviders', '0002_remove_spregistration_phoneno', '2023-12-14 07:42:18.624498'),
(29, 'serviceproviders', '0003_spregistration_accept_spregistration_request', '2023-12-14 07:42:19.758453'),
(30, 'serviceproviders', '0004_remove_spregistration_accept_and_more', '2023-12-14 07:42:20.784370'),
(31, 'serviceproviders', '0005_spregistration_contract_spregistration_negotiation', '2023-12-14 07:42:22.008294'),
(32, 'serviceproviders', '0006_spregistration_accept_spregistration_request', '2023-12-14 07:42:23.107231'),
(33, 'serviceproviders', '0007_spregistration_clauserational_and_more', '2023-12-14 07:42:33.532610'),
(34, 'serviceproviders', '0008_spregistration_companyemailid', '2023-12-14 07:42:34.273566'),
(35, 'serviceproviders', '0009_alter_spregistration_industry', '2023-12-14 07:42:35.904473'),
(36, 'serviceproviders', '0010_spregistration_contractlength', '2023-12-14 07:42:36.597425'),
(37, 'serviceproviders', '0011_spregistration_sendntimeoutsourcees', '2023-12-14 07:42:37.273391'),
(38, 'serviceproviders', '0012_spregistration_zkpprotocol', '2023-12-14 07:42:37.906356'),
(39, 'serviceproviders', '0013_spregistration_outscomply_spregistration_spcomply', '2023-12-14 07:42:39.179294'),
(40, 'serviceproviders', '0014_spregistration_contractapprov_and_more', '2023-12-14 07:42:41.815115'),
(41, 'sessions', '0001_initial', '2023-12-14 07:42:42.503080'),
(42, 'serviceproviders', '0015_spregistration_zkpidentifier', '2023-12-15 09:52:27.807412'),
(43, 'serviceproviders', '0016_spregistration_fileupload1', '2023-12-15 12:26:08.501773'),
(44, 'serviceproviders', '0017_spregistration_leakdata', '2023-12-16 04:15:37.867217'),
(45, 'serviceproviders', '0018_spregistration_sendtooutsoucees', '2023-12-16 04:52:58.350141'),
(46, 'serviceproviders', '0019_spregistration_complaint_spregistration_solution', '2023-12-16 07:55:57.174935'),
(47, 'serviceproviders', '0020_spregistration_leakcontent', '2023-12-16 09:05:31.216751'),
(48, 'serviceproviders', '0021_spregistration_sendsolution', '2023-12-16 12:33:06.163600'),
(49, 'serviceproviders', '0022_alter_spregistration_complaint', '2023-12-16 12:46:13.126410'),
(50, 'serviceproviders', '0023_spregistration_inspect', '2023-12-16 12:56:19.611683'),
(51, 'outsourcingportal', '0002_comprequirement_fileupload1', '2023-12-19 06:00:54.918917'),
(52, 'serviceproviders', '0024_alter_spregistration_complaint', '2023-12-19 09:20:50.775536');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('vgcg88kjxby707p5bmeqqxdg7f6ud58a', 'e30:1rFoZ5:7ntpQayonvflulnx7V0RAtnX4I5Sru8ZiyQFatV_kpY', '2024-01-03 04:52:15.923070'),
('ybpeqproou4dh6hnrkwt1virbqle55ao', 'eyJ1c2VyX2lkIjoxfQ:1rFZSO:5iFqPyyzMIOvYUOrAjPpV6_U-AY0gHkUp5q_gginYuE', '2024-01-02 12:44:20.864826');

-- --------------------------------------------------------

--
-- Table structure for table `outsourcees_outsourceesregistration`
--

CREATE TABLE IF NOT EXISTS `outsourcees_outsourceesregistration` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `companyname` varchar(20) NOT NULL,
  `companyemailid` varchar(254) NOT NULL,
  `contactperson` varchar(20) NOT NULL,
  `phoneno` int(10) unsigned NOT NULL,
  `country` varchar(10) NOT NULL,
  `password` varchar(20) NOT NULL,
  `approve` tinyint(1) NOT NULL,
  `reject` tinyint(1) NOT NULL,
  `login` tinyint(1) NOT NULL,
  `logout` tinyint(1) NOT NULL,
  `Ntime` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `companyemailid` (`companyemailid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `outsourcees_outsourceesregistration`
--

INSERT INTO `outsourcees_outsourceesregistration` (`id`, `companyname`, `companyemailid`, `contactperson`, `phoneno`, `country`, `password`, `approve`, `reject`, `login`, `logout`, `Ntime`) VALUES
(4, 'google', 'john@google.com', 'john', 4294967295, 'india', '123', 1, 0, 1, 0, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `outsourcingportal_compregistration`
--

CREATE TABLE IF NOT EXISTS `outsourcingportal_compregistration` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `companyname` varchar(20) NOT NULL,
  `companyemailid` varchar(254) NOT NULL,
  `contactperson` varchar(20) NOT NULL,
  `phoneno` int(10) unsigned NOT NULL,
  `country` varchar(10) NOT NULL,
  `password` varchar(20) NOT NULL,
  `approve` tinyint(1) NOT NULL,
  `reject` tinyint(1) NOT NULL,
  `login` tinyint(1) NOT NULL,
  `logout` tinyint(1) NOT NULL,
  `process` tinyint(1) NOT NULL,
  `upload` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `companyemailid` (`companyemailid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `outsourcingportal_compregistration`
--

INSERT INTO `outsourcingportal_compregistration` (`id`, `companyname`, `companyemailid`, `contactperson`, `phoneno`, `country`, `password`, `approve`, `reject`, `login`, `logout`, `process`, `upload`) VALUES
(3, 'google', 'john@google.com', 'john', 4294967295, 'india', '123', 1, 0, 1, 0, 0, 1);

-- --------------------------------------------------------

--
-- Table structure for table `outsourcingportal_comprequirement`
--

CREATE TABLE IF NOT EXISTS `outsourcingportal_comprequirement` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `companyname` varchar(20) NOT NULL,
  `contactperson` varchar(20) NOT NULL,
  `companyemailid` varchar(254) DEFAULT NULL,
  `location` varchar(10) NOT NULL,
  `industry` varchar(20) DEFAULT NULL,
  `serviceneed` varchar(200) NOT NULL,
  `duration` varchar(20) DEFAULT NULL,
  `budget` varchar(20) DEFAULT NULL,
  `accept` tinyint(1) NOT NULL,
  `request` tinyint(1) NOT NULL,
  `fileupload1` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `companyemailid` (`companyemailid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `outsourcingportal_comprequirement`
--

INSERT INTO `outsourcingportal_comprequirement` (`id`, `companyname`, `contactperson`, `companyemailid`, `location`, `industry`, `serviceneed`, `duration`, `budget`, `accept`, `request`, `fileupload1`) VALUES
(4, 'google', 'john', 'john@google.com', 'bangalore', 'Healthcare', 'Medical billing and coding service', '3 Month', '1-3 Laks', 0, 0, 'D:\\project(ZKP)\\zeroknowledgeproof\\media\\documents\\patient_dataset.csv.encrypted');

-- --------------------------------------------------------

--
-- Table structure for table `outsourcingportal_myresource`
--

CREATE TABLE IF NOT EXISTS `outsourcingportal_myresource` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `companyname` varchar(20) DEFAULT NULL,
  `contactperson` varchar(20) DEFAULT NULL,
  `companyemailid` varchar(254) DEFAULT NULL,
  `fileupload1` varchar(100) NOT NULL,
  `FullName` varchar(20) DEFAULT NULL,
  `DateofBirth` varchar(20) DEFAULT NULL,
  `Gender` varchar(254) DEFAULT NULL,
  `Address` varchar(10) DEFAULT NULL,
  `Phone` varchar(20) DEFAULT NULL,
  `Insurance` varchar(200) DEFAULT NULL,
  `DiagnosisName` varchar(20) DEFAULT NULL,
  `ProcedureName` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `companyemailid` (`companyemailid`),
  UNIQUE KEY `Gender` (`Gender`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

-- --------------------------------------------------------

--
-- Table structure for table `serviceproviders_spregistration`
--

CREATE TABLE IF NOT EXISTS `serviceproviders_spregistration` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `companyname` varchar(200) DEFAULT NULL,
  `contactperson` varchar(20) DEFAULT NULL,
  `emailid` varchar(254) NOT NULL,
  `industry` varchar(200) DEFAULT NULL,
  `serviceoffer` varchar(100) DEFAULT NULL,
  `location` varchar(10) DEFAULT NULL,
  `password` varchar(20) NOT NULL,
  `approve` tinyint(1) NOT NULL,
  `reject` tinyint(1) NOT NULL,
  `login` tinyint(1) NOT NULL,
  `logout` tinyint(1) NOT NULL,
  `contract` tinyint(1) NOT NULL,
  `negotiation` tinyint(1) NOT NULL,
  `accept` tinyint(1) NOT NULL,
  `request` tinyint(1) NOT NULL,
  `ClauseRational` varchar(200) DEFAULT NULL,
  `DataSecurity` varchar(200) DEFAULT NULL,
  `DesiredOutcomes` varchar(200) DEFAULT NULL,
  `DisputeResolution` varchar(200) DEFAULT NULL,
  `IPownership` varchar(200) DEFAULT NULL,
  `NegotiationPoints` varchar(200) DEFAULT NULL,
  `Ntime` varchar(200) DEFAULT NULL,
  `SLA` varchar(200) DEFAULT NULL,
  `TerminationClauses` varchar(200) DEFAULT NULL,
  `agree` tinyint(1) NOT NULL,
  `budget` varchar(20) DEFAULT NULL,
  `duration` varchar(200) DEFAULT NULL,
  `serviceneeded` varchar(100) DEFAULT NULL,
  `companyemailid` varchar(254) DEFAULT NULL,
  `contractlength` varchar(200) DEFAULT NULL,
  `sendntimeoutsourcees` tinyint(1) NOT NULL,
  `zkpprotocol` varchar(200) DEFAULT NULL,
  `Outscomply` tinyint(1) NOT NULL,
  `spcomply` tinyint(1) NOT NULL,
  `contractapprov` tinyint(1) NOT NULL,
  `contractreject` tinyint(1) NOT NULL,
  `zkpadminapprove` tinyint(1) NOT NULL,
  `zkpadminreject` tinyint(1) NOT NULL,
  `zkpidentifier` varchar(20) DEFAULT NULL,
  `fileupload1` varchar(100) NOT NULL,
  `leakdata` tinyint(1) DEFAULT NULL,
  `sendtooutsoucees` tinyint(1) DEFAULT NULL,
  `complaint` varchar(200) DEFAULT NULL,
  `solution` varchar(200) DEFAULT NULL,
  `leakcontent` varchar(200) DEFAULT NULL,
  `sendsolution` tinyint(1) NOT NULL,
  `inspect` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `emailid` (`emailid`),
  UNIQUE KEY `companyemailid` (`companyemailid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `serviceproviders_spregistration`
--

INSERT INTO `serviceproviders_spregistration` (`id`, `companyname`, `contactperson`, `emailid`, `industry`, `serviceoffer`, `location`, `password`, `approve`, `reject`, `login`, `logout`, `contract`, `negotiation`, `accept`, `request`, `ClauseRational`, `DataSecurity`, `DesiredOutcomes`, `DisputeResolution`, `IPownership`, `NegotiationPoints`, `Ntime`, `SLA`, `TerminationClauses`, `agree`, `budget`, `duration`, `serviceneeded`, `companyemailid`, `contractlength`, `sendntimeoutsourcees`, `zkpprotocol`, `Outscomply`, `spcomply`, `contractapprov`, `contractreject`, `zkpadminapprove`, `zkpadminreject`, `zkpidentifier`, `fileupload1`, `leakdata`, `sendtooutsoucees`, `complaint`, `solution`, `leakcontent`, `sendsolution`, `inspect`) VALUES
(8, 'medbilling experts', 'jessica', 'jessica@mebilling.com', 'Healthcare', 'medical coding and billing service ', 'chennai', '123', 1, 0, 1, 0, 1, 1, 1, 0, 'Data security, patient privacy guaranteed', 'Blockchain-based data storage, encryption at rest and in transit', 'Streamlined claims processing, reduced costs', 'Binding arbitration', 'Client retains ownership', 'Scalability, compliance expertise, privacy-preserving solutions', '4 weeks', '99.9% data availability, HIPAA compliance', 'Misuse of patient data, security breaches', 1, '1-3 Laks', '3 Month', 'Medical billing and coding service', 'john@google.com', '1 year', 1, 'Homomorphic Encryption', 1, 1, 1, 0, 1, 0, 'zkp-12475', 'documents/spdataset_zOY0iRm.csv', 1, 1, 'Unintended exposure of diagnoses, medications, and personal health information', 'Report the leak to the data privacy regulator(HIPAA) and consider legal action for potential harm to patient privacy and disruption of healthcare services.', 'Data breach at a scheduling platform; unauthorized access by third-party.', 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `spupload`
--

CREATE TABLE IF NOT EXISTS `spupload` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `spname` varchar(25) NOT NULL,
  `companyname` varchar(50) NOT NULL,
  `file_upload` varchar(800) NOT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `zkpprotocols_zkpregistration`
--

CREATE TABLE IF NOT EXISTS `zkpprotocols_zkpregistration` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `companyname` varchar(20) NOT NULL,
  `companyemailid` varchar(254) NOT NULL,
  `contactperson` varchar(20) NOT NULL,
  `phoneno` int(10) unsigned NOT NULL,
  `country` varchar(10) NOT NULL,
  `knowledge` varchar(200) NOT NULL,
  `password` varchar(20) NOT NULL,
  `approve` tinyint(1) NOT NULL,
  `reject` tinyint(1) NOT NULL,
  `login` tinyint(1) NOT NULL,
  `logout` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `companyemailid` (`companyemailid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `zkpprotocols_zkpregistration`
--

INSERT INTO `zkpprotocols_zkpregistration` (`id`, `companyname`, `companyemailid`, `contactperson`, `phoneno`, `country`, `knowledge`, `password`, `approve`, `reject`, `login`, `logout`) VALUES
(3, '', 'john@gmail.com', 'john', 4294967295, 'india', 'i have 2+years of experience in ZKP implementation.', '123', 1, 0, 1, 0);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
