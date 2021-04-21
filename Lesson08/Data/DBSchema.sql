-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: localhost    Database: lesson8
-- ------------------------------------------------------
-- Server version	8.0.18

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `items`
--

DROP TABLE IF EXISTS `items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `items` (
  `iditems` int(11) NOT NULL AUTO_INCREMENT,
  `item_name` varchar(45) DEFAULT NULL,
  `papa_id` int(10) unsigned zerofill NOT NULL,
  `order_id` int(11) NOT NULL DEFAULT '5',
  `is_checked` int(11) NOT NULL DEFAULT '0',
  `idusers` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`iditems`),
  UNIQUE KEY `iditems_UNIQUE` (`iditems`) /*!80000 INVISIBLE */,
  KEY `idusers` (`idusers`),
  KEY `papa_id` (`papa_id`),
  KEY `order_id` (`order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `idusers` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(45) NOT NULL,
  PRIMARY KEY (`idusers`),
  UNIQUE KEY `idusers_UNIQUE` (`idusers`) /*!80000 INVISIBLE */,
  KEY `user_name` (`user_name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary view structure for view `view_items`
--

DROP TABLE IF EXISTS `view_items`;
/*!50001 DROP VIEW IF EXISTS `view_items`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_items` AS SELECT 
 1 AS `idusers`,
 1 AS `user_name`,
 1 AS `iditems`,
 1 AS `item_name`,
 1 AS `papa_id`,
 1 AS `order_id`,
 1 AS `is_checked`*/;
SET character_set_client = @saved_cs_client;

--
-- Dumping events for database 'lesson8'
--

--
-- Dumping routines for database 'lesson8'
--

--
-- Final view structure for view `view_items`
--

/*!50001 DROP VIEW IF EXISTS `view_items`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`Doron`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `view_items` AS select `users`.`idusers` AS `idusers`,`users`.`user_name` AS `user_name`,`items`.`iditems` AS `iditems`,`items`.`item_name` AS `item_name`,`items`.`papa_id` AS `papa_id`,`items`.`order_id` AS `order_id`,`items`.`is_checked` AS `is_checked` from (`users` join `items` on((`users`.`idusers` = `items`.`idusers`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-21 18:01:46
