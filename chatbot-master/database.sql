-- MySQL dump 10.13  Distrib 5.7.12, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: web_customer_service
-- ------------------------------------------------------
-- Server version	5.7.15-log

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
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer` (
  `Namez` varchar(100) NOT NULL,
  `Phone` varchar(45) NOT NULL,
  PRIMARY KEY (`Phone`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES ('tanish','9582025804'),('dhruv babbar','9818314184');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `policydetails`
--

DROP TABLE IF EXISTS `policydetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `policydetails` (
  `policyNumber` varchar(100) NOT NULL,
  `policyName` varchar(100) NOT NULL,
  `policyStatus` varchar(100) NOT NULL,
  `surrenderValue` varchar(100) DEFAULT NULL,
  `fundValue` varchar(100) DEFAULT NULL,
  `neftStatus` varchar(100) NOT NULL,
  `renewalStatus` varchar(100) DEFAULT NULL,
  `maturityBenefit` varchar(100) DEFAULT NULL,
  `revivalAmount` varchar(100) DEFAULT NULL,
  `premiumDiff` varchar(100) DEFAULT NULL,
  `premiumStatus` varchar(100) DEFAULT NULL,
  `prevPremium` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`policyNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `policydetails`
--

LOCK TABLES `policydetails` WRITE;
/*!40000 ALTER TABLE `policydetails` DISABLE KEYS */;
INSERT INTO `policydetails` VALUES ('12345678','Raksha','Active','20000','10000','Enabled','Lapsed','100000','10000','2000','Due/Not Recieved','4000'),('12345679','Cancer Shield','Not Active','50000','30000','Disabled','Renewed','50000','10000','4000','Received','2000');
/*!40000 ALTER TABLE `policydetails` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-04-06 11:27:53
