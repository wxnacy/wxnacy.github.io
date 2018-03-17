DROP TABLE IF EXISTS `auto_id`;
CREATE TABLE `auto_id` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `shard_id` int(11) NOT NULL DEFAULT '0' COMMENT '占位字段',
  `item_id` int(11) NOT NULL DEFAULT '0' COMMENT '占位字段',
  `create_ts` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '记录创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `auto_shard_item_id_uindex` (`shard_id`, `item_id`)
) ENGINE=InnoDB CHARSET=utf8mb4 COMMENT='自动生成 id';

DROP FUNCTION IF EXISTS `func_auto_id`;
DELIMITER $$
CREATE FUNCTION `func_auto_id`(shard_seed INT, item_seed INT) RETURNS BIGINT(20)
BEGIN
    DECLARE shard_offset    INT;
    DECLARE item_offset     INT;
    DECLARE final_id        BIGINT;
    DECLARE shard_id        BIGINT;
    DECLARE item_type       BIGINT;
    DECLARE last_insert_id  BIGINT;

    SET shard_offset = 44;
    SET item_offset  = 36;

    SET shard_id  = (SELECT shard_seed << shard_offset);
    SET item_type = (SELECT item_seed  << item_offset);


    replace INTO auto_id  (`shard_id`, `item_id`) VALUES (shard_seed, item_seed);
    SET last_insert_id = (SELECT last_insert_id());
    SET final_id = (SELECT shard_id + item_type + last_insert_id);
    RETURN final_id;
END $$
DELIMITER ;
