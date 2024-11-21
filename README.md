
Таблицы из базы данных supermarket по просьбам трудящихся:<br>
```product```<br>
```users```<br>
```sell_report```<br>
```report```<br>
```user_order```<br>
```order_product```<br>



| prod_id | prod_name | prod_measure | prod_price | prod_category |
|----|----|----|----|----|
| INT | VARCHAR | VARCHAR | FLOAT | INT |


| id | login | password | user_role |
| ---- | ---- | ---- | ---- |
| INT | VARCHAR | VARCHAR | VARCHAR |


| date_of_sale | prod_id | amount | selling_price |
| ---- | ---- | ---- | ---- |
| DATE | INT | FLOAT | FLOAT |


| year | month | prod_id | sum_price | value |
| ---- | ---- | ---- | ---- | ---- |
| INT | INT | INT | FLOAT | FLOAT |


| order_id | user_id | order_date | state |
| ---- | ---- | ---- | ---- |
| INT | INT | DATE | VARCHAR(1) |


| order_id | prod_id | amount |
| ---- | ---- | ---- |
| INT | INT | FLOAT |



    




