/*
Navicat MySQL Data Transfer

Source Server         : localhost MySql5.6
Source Server Version : 50610
Source Host           : localhost:3306
Source Database       : imc

Target Server Type    : MYSQL
Target Server Version : 50610
File Encoding         : 65001

Date: 2021-12-08 09:23:23
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `paciente`
-- ----------------------------
DROP TABLE IF EXISTS `paciente`;
CREATE TABLE `paciente` (
  `id_paciente` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `nome_paciente` varchar(25) NOT NULL,
  `altura_paciente` int(3) NOT NULL,
  `peso_paciente` int(3) NOT NULL,
  `imc_paciente` float(5,0) NOT NULL,
  `descricao_imc_paciente` varchar(25) NOT NULL,
  PRIMARY KEY (`id_paciente`),
  KEY `id_paciente` (`id_paciente`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of paciente
-- ----------------------------
INSERT INTO `paciente` VALUES ('1', 'Vinicius', '166', '60', '22', 'Peso normal');
INSERT INTO `paciente` VALUES ('2', 'Vinicius', '166', '63', '24', 'Peso normal');
