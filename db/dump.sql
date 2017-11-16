-- MySQL dump 10.14  Distrib 5.5.56-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: myblog
-- ------------------------------------------------------
-- Server version	5.5.56-MariaDB

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
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('dbe109a894cb');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) DEFAULT NULL,
  `link` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_category_name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (1,'About','/about'),(2,'Flask','/flask'),(3,'Scraper','/scraper');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `post`
--

DROP TABLE IF EXISTS `post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `post` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(256) DEFAULT NULL,
  `link` varchar(256) DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL,
  `tags` varchar(256) DEFAULT NULL,
  `viewed` int(11) DEFAULT NULL,
  `content` text,
  `content_html` text,
  `category_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `category_id` (`category_id`),
  KEY `ix_post_title` (`title`(255)),
  CONSTRAINT `post_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post`
--

LOCK TABLES `post` WRITE;
/*!40000 ALTER TABLE `post` DISABLE KEYS */;
INSERT INTO `post` VALUES (1,'关于本站','/post/1','2017-11-03 10:32:01','关于',0,'本站分享了一些教程：\r\n1、Flask，讲述零基础到搭建个人网站的最短路径，在不久之前，我也对Web前后端一无所知；\r\n2、爬虫，学会爬虫技能，就可以赚外快了；\r\n3、英文文献翻译和其他；\r\n<hr>\r\n本站演示代码都可以在<a href=\"https://github.com/sylar1015\">这里</a>找到；\r\n特别的，本站源码可以在<a href=\"https://github.com/sylar1015/myblog\">这里</a>找到；\r\n如在本站使用过程中有任何反馈，请在<a href=\"https://github.com/sylar1015/myblog/issues\">这里</a>留言；\r\n\r\n<pre class=\"hljs python\">\r\n<code class=\"python\">\r\ndef about_me():\r\n    me = Programmer()\r\n    me.experience = [\'流媒体\', \'分布式系统\', \'云计算\', \'爬虫\', \'Web应用\']\r\n    me.language = [\'C\',\'C++\', \'Python\', \'Javascript\']\r\n    me.contact = [\'邮箱\', \'留言系统开发中\']\r\n    print(me)\r\n</code>\r\n</pre>\r\n','<p>本站分享了一些教程：\n1、Flask，讲述零基础到搭建个人网站的最短路径，在不久之前，我也对Web前后端一无所知；\n2、爬虫，学会爬虫技能，就可以赚外快了；\n3、英文文献翻译和其他；\n</p><hr>\n本站演示代码都可以在<a href=\"https://github.com/sylar1015\" rel=\"nofollow\">这里</a>找到；\n特别的，本站源码可以在<a href=\"https://github.com/sylar1015/myblog\" rel=\"nofollow\">这里</a>找到；\n如在本站使用过程中有任何反馈，请在<a href=\"https://github.com/sylar1015/myblog/issues\" rel=\"nofollow\">这里</a>留言；<p></p>\n<pre class=\"hljs python\"><code class=\"python\">\ndef about_me():\n    me = Programmer()\n    me.experience = [\'流媒体\', \'分布式系统\', \'云计算\', \'爬虫\', \'Web应用\']\n    me.language = [\'C\',\'C++\', \'Python\', \'Javascript\']\n    me.contact = [\'邮箱\', \'留言系统开发中\']\n    print(me)\n</code>\n</pre>',1),(2,'Flask搭建个人网站(FAQ)','/post/2','2017-11-05 19:50:31','Flask，FAQ',0,'在开始之前，先回答几个问题：\r\n<p>Q、学习<em>Flask</em>需要什么基础？</p>\r\n<p>Q、为什么要花时间学习<em>Flask</em>？</p>\r\n<p>Q、为什么是<em>Flask</em>，不是其他？</p>\r\n<p>Q、要学多久才能搭建自己的个人网站？</p>\r\n<hr>\r\n<p>Q、学习<em>Flask</em>需要什么基础？</p>\r\n<p>A、<em>Python</em>；你不需要<strong>任何</strong>Web前台后台基础；也不需要<strong>任何</strong>python框架基础；</p>\r\n<p>Q、为什么要花时间学习<em>Flask</em>？</p>\r\n<p>A、假定你已经掌握了<em>Python</em>，通过学习<em>Flask</em>，你不但可以提升你的<em>Python</em>熟练度，而且通过<em>Flask</em>，你可以扩展你的技术栈，因为你会接触到<em>Bootstrap</em>/<em>JQuery</em>等框架；<em>Javascript</em>/<em>HTML5</em>等语言；以及<em>NoSQL</em>/<em>Cache</em>/<em>Nginx</em>...即使除了<em>Flask</em>，你并不想接触其他，你也已经向<em>全栈</em>迈了一大步，而且你也已经可以用<em>Flask</em>搭建你的Web应用了；</p>\r\n<p>即使你在其他平台有技术博客，也很有必要搭建自己的个人网站，因为如果你的Web应用有流量，你也有可能将它变现...</p>\r\n<p>Q、为什么是<em>Flask</em>，不是其他？</p>\r\n<p>A、<em>Flask</em>是个小而美的框架、学习曲线平滑也更短；零基础就可以学习；另外、个人更倾向于轻框架，可以清楚的知道自己做了什么、怎么做到的；</p>\r\n<p>Q、要学多久才能搭建自己的个人网站？</p>\r\n<p>A、以我这样一个零基础、资质中等的过来人的经验告诉你，几周足矣；而如果你希望自己制作出精美的页面，则需要更长的时间(在不侵权的情况下，<kbd>CTRL</kbd>+<kbd>C</kbd>, <kbd>CTRL</kbd>+<kbd>V</kbd>...)；</p>\r\n<p>好了，让我们开始吧！<p>\r\n','<p>在开始之前，先回答几个问题：\n</p><p>Q、学习<em>Flask</em>需要什么基础？</p>\n<p>Q、为什么要花时间学习<em>Flask</em>？</p>\n<p>Q、为什么是<em>Flask</em>，不是其他？</p>\n<p>Q、要学多久才能搭建自己的个人网站？</p>\n<hr>\n<p>Q、学习<em>Flask</em>需要什么基础？</p>\n<p>A、<em>Python</em>；你不需要<strong>任何</strong>Web前台后台基础；也不需要<strong>任何</strong>python框架基础；</p>\n<p>Q、为什么要花时间学习<em>Flask</em>？</p>\n<p>A、假定你已经掌握了<em>Python</em>，通过学习<em>Flask</em>，你不但可以提升你的<em>Python</em>熟练度，而且通过<em>Flask</em>，你可以扩展你的技术栈，因为你会接触到<em>Bootstrap</em>/<em>JQuery</em>等框架；<em>Javascript</em>/<em>HTML5</em>等语言；以及<em>NoSQL</em>/<em>Cache</em>/<em>Nginx</em>...即使除了<em>Flask</em>，你并不想接触其他，你也已经向<em>全栈</em>迈了一大步，而且你也已经可以用<em>Flask</em>搭建你的Web应用了；</p>\n<p>即使你在其他平台有技术博客，也很有必要搭建自己的个人网站，因为如果你的Web应用有流量，你也有可能将它变现...</p>\n<p>Q、为什么是<em>Flask</em>，不是其他？</p>\n<p>A、<em>Flask</em>是个小而美的框架、学习曲线平滑也更短；零基础就可以学习；另外、个人更倾向于轻框架，可以清楚的知道自己做了什么、怎么做到的；</p>\n<p>Q、要学多久才能搭建自己的个人网站？</p>\n<p>A、以我这样一个零基础、资质中等的过来人的经验告诉你，几周足矣；而如果你希望自己制作出精美的页面，则需要更长的时间(在不侵权的情况下，CTRL+C, CTRL+V...)；</p>\n<p>好了，让我们开始吧！</p><p></p>',2);
/*!40000 ALTER TABLE `post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(128) DEFAULT NULL,
  `password_hash` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_user_username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'admin','pbkdf2:sha256:50000$CIRdikW7$062f85d636be4a803c9b8691481bd50297e44a959135328d913294d95bf73aab');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-11-16 19:05:28
