SELECT prod_name, sum_price,`value`, prod_measure FROM report JOIN product USING (prod_id) WHERE `year` = '$e_year' AND `month` = '$e_month';