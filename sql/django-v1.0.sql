/*
 Navicat Premium Data Transfer

 Source Server         : pyton-django
 Source Server Type    : MySQL
 Source Server Version : 50721
 Source Host           : hqh-study-python.com:33066
 Source Schema         : django

 Target Server Type    : MySQL
 Target Server Version : 50721
 File Encoding         : 65001

 Date: 30/04/2018 15:07:25
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id`, `permission_id`) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id`, `codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 19 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (5, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can add user', 3, 'add_user');
INSERT INTO `auth_permission` VALUES (8, 'Can change user', 3, 'change_user');
INSERT INTO `auth_permission` VALUES (9, 'Can delete user', 3, 'delete_user');
INSERT INTO `auth_permission` VALUES (10, 'Can add group', 4, 'add_group');
INSERT INTO `auth_permission` VALUES (11, 'Can change group', 4, 'change_group');
INSERT INTO `auth_permission` VALUES (12, 'Can delete group', 4, 'delete_group');
INSERT INTO `auth_permission` VALUES (13, 'Can add content type', 5, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (14, 'Can change content type', 5, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (15, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (16, 'Can add session', 6, 'add_session');
INSERT INTO `auth_permission` VALUES (17, 'Can change session', 6, 'change_session');
INSERT INTO `auth_permission` VALUES (18, 'Can delete session', 6, 'delete_session');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `first_name` varchar(30) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `email` varchar(254) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq`(`user_id`, `group_id`) USING BTREE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id`(`group_id`) USING BTREE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq`(`user_id`, `permission_id`) USING BTREE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for d_user
-- ----------------------------
DROP TABLE IF EXISTS `d_user`;
CREATE TABLE `d_user`  (
  `id` int(8) NOT NULL,
  `user` varchar(16) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `passwd` varchar(32) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `valid` tinyint(8) NOT NULL,
  `permission` tinyint(8) NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of d_user
-- ----------------------------
INSERT INTO `d_user` VALUES (1, 'test', 'e10adc3949ba59abbe56e057f20f883e', 0, 0);
INSERT INTO `d_user` VALUES (2, 'python', '4297f44b13955235245b2497399d7a93', 0, 0);

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL,
  `object_repr` varchar(200) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `content_type_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk`(`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `model` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label`, `model`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (4, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'user');
INSERT INTO `django_content_type` VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (6, 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `name` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 15 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2018-04-26 09:32:03.027652');
INSERT INTO `django_migrations` VALUES (2, 'auth', '0001_initial', '2018-04-26 09:32:05.373666');
INSERT INTO `django_migrations` VALUES (3, 'admin', '0001_initial', '2018-04-26 09:32:05.599639');
INSERT INTO `django_migrations` VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2018-04-26 09:32:05.625654');
INSERT INTO `django_migrations` VALUES (5, 'contenttypes', '0002_remove_content_type_name', '2018-04-26 09:32:05.750232');
INSERT INTO `django_migrations` VALUES (6, 'auth', '0002_alter_permission_name_max_length', '2018-04-26 09:32:05.797100');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0003_alter_user_email_max_length', '2018-04-26 09:32:05.832193');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0004_alter_user_username_opts', '2018-04-26 09:32:05.848221');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0005_alter_user_last_login_null', '2018-04-26 09:32:05.938521');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0006_require_contenttypes_0002', '2018-04-26 09:32:05.942524');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0007_alter_validators_add_error_messages', '2018-04-26 09:32:05.955544');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0008_alter_user_username_max_length', '2018-04-26 09:32:06.129732');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0009_alter_user_last_name_max_length', '2018-04-26 09:32:06.170260');
INSERT INTO `django_migrations` VALUES (14, 'sessions', '0001_initial', '2018-04-26 09:32:06.288877');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `session_data` longtext CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('03mf5noqh62pvjr6fc57ncfdoy6vm2nl', 'OTBkNmNjMDY1OTE2OTBkZjBlODQxMzUyNGNlZjRkYmNlMDQxYWM3NTp7InVzZXJuYW1lIjoidGVzdCIsIl9zZXNzaW9uX2V4cGlyeSI6MTgwMH0=', '2018-04-29 04:46:09.318053');
INSERT INTO `django_session` VALUES ('39nqr939v4zs77auglbid1x3fsszna0g', 'MTliYzk0ZGUyNjAyOTZmYjRhZmU2M2Q2NmZlZjc2ODZkODE5MTMzYTp7Il9zZXNzaW9uX2V4cGlyeSI6NjAwfQ==', '2018-04-27 05:42:41.796293');
INSERT INTO `django_session` VALUES ('4c3p6sun95qoz9xr36783gx3nobccbb0', 'N2QzZGM3OGZlZGZmY2U0ZmUyZDNmZGViODViYjQ3ZWI4OTlhNGIwNjp7InVzZXJuYW1lIjoidGVzdCIsIl9zZXNzaW9uX2V4cGlyeSI6NjAwfQ==', '2018-04-27 12:10:07.158758');
INSERT INTO `django_session` VALUES ('4qmc8puwyrwo0ieh13gaoiesh9qwiwk1', 'N2QzZGM3OGZlZGZmY2U0ZmUyZDNmZGViODViYjQ3ZWI4OTlhNGIwNjp7InVzZXJuYW1lIjoidGVzdCIsIl9zZXNzaW9uX2V4cGlyeSI6NjAwfQ==', '2018-04-27 09:19:47.702624');
INSERT INTO `django_session` VALUES ('5ir6ye1u2gb7pxupluj2l780ahyx0zjv', 'OTBkNmNjMDY1OTE2OTBkZjBlODQxMzUyNGNlZjRkYmNlMDQxYWM3NTp7InVzZXJuYW1lIjoidGVzdCIsIl9zZXNzaW9uX2V4cGlyeSI6MTgwMH0=', '2018-04-29 18:09:05.133637');
INSERT INTO `django_session` VALUES ('6ekqgmxre2x7cglj5b4ov8jw386quc04', 'OTBkNmNjMDY1OTE2OTBkZjBlODQxMzUyNGNlZjRkYmNlMDQxYWM3NTp7InVzZXJuYW1lIjoidGVzdCIsIl9zZXNzaW9uX2V4cGlyeSI6MTgwMH0=', '2018-04-29 06:27:25.384739');
INSERT INTO `django_session` VALUES ('8dsdrl7i7kd9rqo7n8t58k4f0jgmb4sa', 'M2JkMzUwMDAyMmJlN2FmMzFlYTQ2MTNmMWU0YmU4ZTZmOWZhNGUxNjp7Il9zZXNzaW9uX2V4cGlyeSI6MTgwMCwidXNlcm5hbWUiOiJ0ZXN0In0=', '2018-04-30 03:53:43.320791');
INSERT INTO `django_session` VALUES ('aq0c0q8jei052eq0nr9u1j7l7sarnfhd', 'ZWFjZGI0N2U1ZTQ2YzJkMTIxMmNlNDc2YzhiOTJjOTE1Mjc5OTI4ZDp7InVzZXJuYW1lIjoidGVzdCIsIl9zZXNzaW9uX2V4cGlyeSI6NjAwfQ==', '2018-04-28 17:43:14.314186');
INSERT INTO `django_session` VALUES ('dgiqk2iuo878u46b8z87ayn7pats8fv8', 'M2JkMzUwMDAyMmJlN2FmMzFlYTQ2MTNmMWU0YmU4ZTZmOWZhNGUxNjp7Il9zZXNzaW9uX2V4cGlyeSI6MTgwMCwidXNlcm5hbWUiOiJ0ZXN0In0=', '2018-04-29 14:54:57.796571');
INSERT INTO `django_session` VALUES ('di1tkfexhp43yplf301yixvd02rh6san', 'M2JkMzUwMDAyMmJlN2FmMzFlYTQ2MTNmMWU0YmU4ZTZmOWZhNGUxNjp7Il9zZXNzaW9uX2V4cGlyeSI6MTgwMCwidXNlcm5hbWUiOiJ0ZXN0In0=', '2018-04-29 17:32:25.610238');
INSERT INTO `django_session` VALUES ('fqeg06b8nlsxap8pwwcswrivkjf614qn', 'ZWFjZGI0N2U1ZTQ2YzJkMTIxMmNlNDc2YzhiOTJjOTE1Mjc5OTI4ZDp7InVzZXJuYW1lIjoidGVzdCIsIl9zZXNzaW9uX2V4cGlyeSI6NjAwfQ==', '2018-04-28 17:05:52.004397');
INSERT INTO `django_session` VALUES ('fzp2txs30o2roni2p3avuvcnk9g08m6o', 'M2JkMzUwMDAyMmJlN2FmMzFlYTQ2MTNmMWU0YmU4ZTZmOWZhNGUxNjp7Il9zZXNzaW9uX2V4cGlyeSI6MTgwMCwidXNlcm5hbWUiOiJ0ZXN0In0=', '2018-04-29 13:22:28.736317');
INSERT INTO `django_session` VALUES ('grxyjskrpvd2f435vpphf1jtz6ku7443', 'N2QzZGM3OGZlZGZmY2U0ZmUyZDNmZGViODViYjQ3ZWI4OTlhNGIwNjp7InVzZXJuYW1lIjoidGVzdCIsIl9zZXNzaW9uX2V4cGlyeSI6NjAwfQ==', '2018-04-27 03:03:35.934699');
INSERT INTO `django_session` VALUES ('ibdy3k6hv7gy6gu68gxywa7c1xmxgtex', 'N2QzZGM3OGZlZGZmY2U0ZmUyZDNmZGViODViYjQ3ZWI4OTlhNGIwNjp7InVzZXJuYW1lIjoidGVzdCIsIl9zZXNzaW9uX2V4cGlyeSI6NjAwfQ==', '2018-04-26 09:42:29.729893');
INSERT INTO `django_session` VALUES ('j6sl51gmyhy6v534x4rjw2o43polgq9k', 'N2QzZGM3OGZlZGZmY2U0ZmUyZDNmZGViODViYjQ3ZWI4OTlhNGIwNjp7InVzZXJuYW1lIjoidGVzdCIsIl9zZXNzaW9uX2V4cGlyeSI6NjAwfQ==', '2018-04-27 06:40:23.688781');
INSERT INTO `django_session` VALUES ('omf4zyy1aaz37v93tfhz66uzii4zr82j', 'YjI1MDhjNDU3ZjVhODY3NmYwODAwNjkyYTQwYTU1ZmYyZjY2MTk0Yjp7Il9zZXNzaW9uX2V4cGlyeSI6NjAwLCJ1c2VybmFtZSI6InRlc3QifQ==', '2018-04-26 10:33:44.669346');
INSERT INTO `django_session` VALUES ('pxopilrubhwy6ob22d2pd0ntlm6borxg', 'N2QzZGM3OGZlZGZmY2U0ZmUyZDNmZGViODViYjQ3ZWI4OTlhNGIwNjp7InVzZXJuYW1lIjoidGVzdCIsIl9zZXNzaW9uX2V4cGlyeSI6NjAwfQ==', '2018-04-27 06:27:05.894054');
INSERT INTO `django_session` VALUES ('q7mbka5ebhgxnlhefvs694lnjng3npy4', 'OTBkNmNjMDY1OTE2OTBkZjBlODQxMzUyNGNlZjRkYmNlMDQxYWM3NTp7InVzZXJuYW1lIjoidGVzdCIsIl9zZXNzaW9uX2V4cGlyeSI6MTgwMH0=', '2018-04-29 08:29:10.793869');
INSERT INTO `django_session` VALUES ('q9re7kb6idl1uvhptkpal07os2ug82qu', 'N2QzZGM3OGZlZGZmY2U0ZmUyZDNmZGViODViYjQ3ZWI4OTlhNGIwNjp7InVzZXJuYW1lIjoidGVzdCIsIl9zZXNzaW9uX2V4cGlyeSI6NjAwfQ==', '2018-04-27 05:57:25.231006');
INSERT INTO `django_session` VALUES ('qx0w7jy4gc1e1rzyh3cvajpec2ywsgqm', 'M2JkMzUwMDAyMmJlN2FmMzFlYTQ2MTNmMWU0YmU4ZTZmOWZhNGUxNjp7Il9zZXNzaW9uX2V4cGlyeSI6MTgwMCwidXNlcm5hbWUiOiJ0ZXN0In0=', '2018-04-29 07:06:25.870129');
INSERT INTO `django_session` VALUES ('rao8lpq1jyx94qp8baqljvpixohqjdx4', 'YjI1MDhjNDU3ZjVhODY3NmYwODAwNjkyYTQwYTU1ZmYyZjY2MTk0Yjp7Il9zZXNzaW9uX2V4cGlyeSI6NjAwLCJ1c2VybmFtZSI6InRlc3QifQ==', '2018-04-26 09:55:45.535764');
INSERT INTO `django_session` VALUES ('rqhejmgjtuhvkacz807b34yowjoe5orj', 'N2QzZGM3OGZlZGZmY2U0ZmUyZDNmZGViODViYjQ3ZWI4OTlhNGIwNjp7InVzZXJuYW1lIjoidGVzdCIsIl9zZXNzaW9uX2V4cGlyeSI6NjAwfQ==', '2018-04-27 05:38:36.422104');
INSERT INTO `django_session` VALUES ('rrgx3wj6symd0dmjhnoxx99j8gfmjxvg', 'OTBkNmNjMDY1OTE2OTBkZjBlODQxMzUyNGNlZjRkYmNlMDQxYWM3NTp7InVzZXJuYW1lIjoidGVzdCIsIl9zZXNzaW9uX2V4cGlyeSI6MTgwMH0=', '2018-04-29 05:33:31.791699');
INSERT INTO `django_session` VALUES ('rxg22c4h24cfra6sya277j4tf4awl5nr', 'M2JkMzUwMDAyMmJlN2FmMzFlYTQ2MTNmMWU0YmU4ZTZmOWZhNGUxNjp7Il9zZXNzaW9uX2V4cGlyeSI6MTgwMCwidXNlcm5hbWUiOiJ0ZXN0In0=', '2018-04-29 09:04:48.360677');
INSERT INTO `django_session` VALUES ('s8w2fau5ld83w2y2moke2me5aobw0q6t', 'OTBkNmNjMDY1OTE2OTBkZjBlODQxMzUyNGNlZjRkYmNlMDQxYWM3NTp7InVzZXJuYW1lIjoidGVzdCIsIl9zZXNzaW9uX2V4cGlyeSI6MTgwMH0=', '2018-04-29 09:44:25.757592');
INSERT INTO `django_session` VALUES ('syd89vvsuezpkuotygblm5k2kx6hbhml', 'OTBkNmNjMDY1OTE2OTBkZjBlODQxMzUyNGNlZjRkYmNlMDQxYWM3NTp7InVzZXJuYW1lIjoidGVzdCIsIl9zZXNzaW9uX2V4cGlyeSI6MTgwMH0=', '2018-04-30 07:33:57.529606');
INSERT INTO `django_session` VALUES ('tm9whuawfih45hageb1830119me7j0wv', 'N2QzZGM3OGZlZGZmY2U0ZmUyZDNmZGViODViYjQ3ZWI4OTlhNGIwNjp7InVzZXJuYW1lIjoidGVzdCIsIl9zZXNzaW9uX2V4cGlyeSI6NjAwfQ==', '2018-04-26 09:50:24.566505');
INSERT INTO `django_session` VALUES ('to8a36mjfii1iqf36ns6igoxk2o00uir', 'N2QzZGM3OGZlZGZmY2U0ZmUyZDNmZGViODViYjQ3ZWI4OTlhNGIwNjp7InVzZXJuYW1lIjoidGVzdCIsIl9zZXNzaW9uX2V4cGlyeSI6NjAwfQ==', '2018-04-27 03:33:54.918146');
INSERT INTO `django_session` VALUES ('trupooz04w12d54adoq8x5tjk4m20172', 'M2JkMzUwMDAyMmJlN2FmMzFlYTQ2MTNmMWU0YmU4ZTZmOWZhNGUxNjp7Il9zZXNzaW9uX2V4cGlyeSI6MTgwMCwidXNlcm5hbWUiOiJ0ZXN0In0=', '2018-04-28 18:30:09.340192');
INSERT INTO `django_session` VALUES ('v5g2q4ysknyr4s4ine1spuczfsdd2c9i', 'ZWFjZGI0N2U1ZTQ2YzJkMTIxMmNlNDc2YzhiOTJjOTE1Mjc5OTI4ZDp7InVzZXJuYW1lIjoidGVzdCIsIl9zZXNzaW9uX2V4cGlyeSI6NjAwfQ==', '2018-04-28 16:47:33.751007');
INSERT INTO `django_session` VALUES ('w18ivv4e728f1xmag52tsd29w4m5z9q5', 'N2QzZGM3OGZlZGZmY2U0ZmUyZDNmZGViODViYjQ3ZWI4OTlhNGIwNjp7InVzZXJuYW1lIjoidGVzdCIsIl9zZXNzaW9uX2V4cGlyeSI6NjAwfQ==', '2018-04-27 05:55:05.672173');
INSERT INTO `django_session` VALUES ('wxoqyxha2k8gwk6pkagrjar7072dci55', 'OTBkNmNjMDY1OTE2OTBkZjBlODQxMzUyNGNlZjRkYmNlMDQxYWM3NTp7InVzZXJuYW1lIjoidGVzdCIsIl9zZXNzaW9uX2V4cGlyeSI6MTgwMH0=', '2018-04-30 05:17:24.359515');
INSERT INTO `django_session` VALUES ('xvhg5x16qqla5y7ai76sp2ncet4kjg5g', 'M2JkMzUwMDAyMmJlN2FmMzFlYTQ2MTNmMWU0YmU4ZTZmOWZhNGUxNjp7Il9zZXNzaW9uX2V4cGlyeSI6MTgwMCwidXNlcm5hbWUiOiJ0ZXN0In0=', '2018-04-29 09:08:24.044769');
INSERT INTO `django_session` VALUES ('zte9wiem6k581mv76cxvvb2v0v19cse3', 'NzM2M2FmYWE1ZjliM2ExYjhkNjRlM2VlNzRhYzAzMGRkMmM2ZjcyZDp7Il9zZXNzaW9uX2V4cGlyeSI6MTgwMH0=', '2018-04-29 06:17:47.044261');

SET FOREIGN_KEY_CHECKS = 1;
