## ЧИТАЙТЕ ПОЖАЛУЙСТА ПРИМЕЧАНИЯ К КОММИТАМ
ну пожалуйста.

## Таблицы
Таблицы из базы данных supermarket по просьбам трудящихся:<br>

```product```<br>

| prod_id | prod_name | prod_measure | prod_price | prod_category |
|----|----|----|----|----|
| INT | VARCHAR | VARCHAR | FLOAT | INT |
| PK |  |  |  |  |


```users```<br>

| id | login | password | user_role |
| ---- | ---- | ---- | ---- |
| INT | VARCHAR | VARCHAR | VARCHAR |
| PK |  |  |   |

```sell_report```<br>

| date_of_sale | prod_id | amount | selling_price |
| ---- | ---- | ---- | ---- |
| DATE | INT | FLOAT | FLOAT |
|  | FK |  |  |

```report```<br>

| year | month | prod_id | sum_price | value |
| ---- | ---- | ---- | ---- | ---- |
| INT | INT | INT | FLOAT | FLOAT |
|  |  | FK |  |  |

```user_order```<br>

| order_id | user_id | order_date | state |
| ---- | ---- | ---- | ---- |
| INT | INT | DATE | VARCHAR(1) |
| PK | FK |  |  |

```order_product```<br>

| order_id | prod_id | amount |
| ---- | ---- | ---- |
| INT | INT | FLOAT |
| FK | FK |    |


При желании можно сделать в таблицах без PK композитные PK, но зачем...


    




