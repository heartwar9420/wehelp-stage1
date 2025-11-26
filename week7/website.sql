-- MySQL dump 10.13  Distrib 8.0.44, for Win64 (x86_64)
--
-- Host: localhost    Database: website
-- ------------------------------------------------------
-- Server version	8.0.44

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
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `follower_count` int unsigned NOT NULL DEFAULT '0',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (1,'test2','test@test.com','test',0,'2025-11-13 08:54:59'),(2,'test11','test11@test11.com','test11',0,'2025-11-13 08:54:59'),(3,'test22','test22@test22.com','test22',0,'2025-11-13 08:54:59'),(4,'test33','test33@test33.com','test33',0,'2025-11-13 08:54:59'),(5,'test44','test44@test44.com','test44',0,'2025-11-13 08:54:59'),(6,'','','',0,'2025-11-22 09:11:18'),(7,'丁丁','aaa@aaa.com','aaa',0,'2025-11-22 09:24:08'),(8,'bbb','bbb@bbb.com','bbb',0,'2025-11-22 20:21:01');
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `message` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `member_id` int unsigned NOT NULL,
  `content` text NOT NULL,
  `like_count` int unsigned NOT NULL DEFAULT '0',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `message_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `member` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (1,8,'測試測試',0,'2025-11-22 20:39:43'),(2,8,'123456',0,'2025-11-22 20:39:50'),(3,7,'好了啦',0,'2025-11-22 20:40:14'),(5,7,'可以了嗎',0,'2025-11-22 21:02:02'),(6,7,'測試一下',0,'2025-11-22 21:02:06'),(7,1,'789789',0,'2025-11-22 21:02:27'),(8,7,'可以測試一下嗎',0,'2025-11-25 22:12:59');
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `query_log`
--

DROP TABLE IF EXISTS `query_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `query_log` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `target_id` bigint NOT NULL,
  `searcher_id` bigint NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `query_log`
--

LOCK TABLES `query_log` WRITE;
/*!40000 ALTER TABLE `query_log` DISABLE KEYS */;
INSERT INTO `query_log` VALUES (1,2,3,'2025-11-25 22:46:56'),(2,3,2,'2025-11-25 22:48:08'),(3,1,2,'2025-11-25 22:48:13'),(4,4,2,'2025-11-25 22:48:15'),(5,2,8,'2025-11-25 23:16:13'),(6,1,7,'2025-11-25 23:16:27'),(7,2,7,'2025-11-25 23:16:29'),(8,3,7,'2025-11-25 23:16:30'),(9,8,7,'2025-11-25 23:16:32'),(10,8,7,'2025-11-25 23:26:44'),(11,8,7,'2025-11-25 23:26:46'),(12,8,7,'2025-11-25 23:26:47'),(13,8,7,'2025-11-25 23:26:47'),(14,8,7,'2025-11-25 23:26:47'),(15,8,7,'2025-11-25 23:26:47'),(16,8,7,'2025-11-25 23:26:47'),(17,8,7,'2025-11-25 23:26:47'),(18,8,7,'2025-11-25 23:26:48'),(19,8,7,'2025-11-25 23:26:48'),(20,8,7,'2025-11-25 23:26:48');
/*!40000 ALTER TABLE `query_log` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-11-26 20:52:27
