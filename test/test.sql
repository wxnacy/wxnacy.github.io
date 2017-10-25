select * from shop limit 1\G;

select * from tmddev.screen where shop_id in (
    select id from tmddev.shop where id = 566
)\G;

select * from config ;

select * from config where `key` = 'shop_login_short_url';
