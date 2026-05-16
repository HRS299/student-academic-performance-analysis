-- MySQL dump 10.13  Distrib 8.0.46, for Win64 (x86_64)
--
-- Host: localhost    Database: student_performance
-- ------------------------------------------------------
-- Server version	8.0.46

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
-- Temporary view structure for view `student_performance_view`
--

DROP TABLE IF EXISTS `student_performance_view`;
/*!50001 DROP VIEW IF EXISTS `student_performance_view`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `student_performance_view` AS SELECT 
 1 AS `student_id`,
 1 AS `student_name`,
 1 AS `department_name`,
 1 AS `semester`,
 1 AS `gpa`,
 1 AS `avg_attendance`,
 1 AS `risk_level`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `student_performance_view`
--

/*!50001 DROP VIEW IF EXISTS `student_performance_view`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `student_performance_view` AS select `s`.`student_id` AS `student_id`,`s`.`student_name` AS `student_name`,`d`.`department_name` AS `department_name`,`pr`.`semester` AS `semester`,`pr`.`gpa` AS `gpa`,round(avg(`a`.`attendance_percentage`),2) AS `avg_attendance`,(case when ((`pr`.`gpa` < 5) or (avg(`a`.`attendance_percentage`) < 50)) then 'High Risk' when ((`pr`.`gpa` < 7) or (avg(`a`.`attendance_percentage`) < 70)) then 'Medium Risk' else 'Low Risk' end) AS `risk_level` from (((`student` `s` join `department` `d` on((`s`.`department_id` = `d`.`department_id`))) join `performance_report` `pr` on((`s`.`student_id` = `pr`.`student_id`))) join `attendance` `a` on((`s`.`student_id` = `a`.`student_id`))) group by `s`.`student_id`,`s`.`student_name`,`d`.`department_name`,`pr`.`semester`,`pr`.`gpa` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Dumping events for database 'student_performance'
--

--
-- Dumping routines for database 'student_performance'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-05-16 16:39:04
