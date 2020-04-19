# Introduction
Butterfly uses multi-layer database management. It's possible to use multiple databases at the same time. You can configure multiple databases and use it. Butterfly uses MySQL as the primary database.
All Butterfly related data is stored in MySQL but you can use the following database drivers: 

MySQL 5.6+
ElasticSearch 7.X
Redis (Coming soon)
MongoDB (Coming soon)

# Configuration:
The database configurations are stored in `app/config/database.php`. Configurations can be customized by domain name with subfolders.
Example configuration:

```php
<?php

return [
    'default' => [
        'server' => 'localhost',
        'adapter' => 'MySQL',
        'name' => 'DB_NAME',
        'user' => 'DB_USERNAME',
        'password' => 'DB_PASSWORD',
        'port' => 3306 // Optional
    ],
    
    'external' => [
        'server' => 'EXTERNAL_SERVER_IP',
        'adapter' => 'MySQL',
        'name' => 'DB_NAME',
        'user' => 'DB_USERNAME',
        'password' => 'DB_PASSWORD',
        'port' => 3306 // Optional 
    ]
];
```

## Slave Database:

Butterfly uses slave database if it's defined. If not, it uses default database for the SELECT operations.

## Running Queries:

### Running a select query:

```php
db()
   ->from('users')
    ->get();
```

will run the query:

```sql
SELECT * FROM users;
``` 

and return all results as associative array.

#### WHERE Clause:

You can write where clauses in many ways. Examples are the following:

```php
db()->from('users')
    ->where('id', 5)
    ->first();
```

will run the query:

```mysql
SELECT * FROM users WHERE id = 5;
``` 

and return one row as associative array.

You can use parameter binding, and bind parameters:

```php
db()->from('users')
    ->where('id = :id')
    ->bind('id', 5)
    ->first()
;
```

will run the query:

```sql
SELECT * FROM users WHERE id = 5;
``` 

You can bind parameters using question marks (?)

```php
db()->from('users')
    ->where('id = ? OR id = ?', [5, 10])
    ->get()
;
```

Will run:

```sql
SELECT * FROM users WHERE id = 5 OR id = 10
```

```text
Caution:

Question mark style binding, doesn't work with associative arrays.

Following code will generate error:
```
```php
db()->from('users')
    ->where('id = ?', ['id' => 5])
    ->get()
;
```

Nested SQL Queries can be generated using callback functions.

```php
db()->from('users')
    ->where('id', 5)
    ->orWhere('status', 2)
    ->orWhere(function($query) {
        return $query->where('votes', '<', '500')
            ->where('status', 3);
    })
    ->orderByDesc('id')
    ->get()
;
``` 

As you can see below, queries inside of the function will be evaluated seperately inside of braces and it will run:

```sql
SELECT * FROM users 
    WHERE id = 5 OR status = 2 
        OR (votes < 500 AND status = 3) 
    ORDER BY id DESC
```

Returning function:

Function  | Description
------------- | -------------
get | will return all rows as associative array.
first | will just return the first row as associative array
one($column_name) | will return only one column value. 
column($column_name) | will return the values of specific column as an array list.
keyToValue($key_column) | will return result indexed by key_column. Value will be the row as the associative array.
keyToValue($key_column, $value_column) | will return result indexed by key_column. Value will be value of the specified column.
keyToValues($key_column) | when key_column is not unique, you can use this function to group results by key_column (e.g. status). Value will be the row as the associative array. 
keyToValues($key_column, $value_column) | when key_column is not unique, you can use this function to group results by key_column (e.g. status). Value will be value of the specified column.
max($column_name) | Will return maximum value of the specific column as a single value.
min($column_name) | Will return minimum value of the specific column as a single value.
average($column_name) | Will return average value of the specific column as a single value.

