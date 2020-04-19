# Introduction
Butterfly uses multi-layer database management. It's possible to use multiple databases at the same time. You can configure multiple databases and use it. Butterfly uses MySQL as the primary database.
All Butterfly related data is stored in MySQL but you can use the following database drivers: 

- MySQL 5.6+
- ElasticSearch 7.X
- Redis (Coming soon)
- MongoDB (Coming soon)

# Configuration
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

## Slave Database

Butterfly uses slave database if it's defined. If not, it uses default database for the SELECT operations.

## Using The Database Client

Database client can be reached using `db()` helper. You can also reach defined databases using the database alias as the first parameter.
 
```php
db(); // Database Alias defaults to default database.
```

Following function call will return a database client connected to database external defined in configuration.

```php
db('external');
```

# Transactions

You can begin, rollback or commit a transaction.

## Begin

```php
db()->transaction();
```

## Commit

```php
db()->commit();
````

## Rollback

```php
db()->rollback();
```

## Example Usage

```php
db()->transaction();
try {
    $id = db()->table('orders')->insert([
        'customer_id' => 1
    ]);
    
    db()->table('order_items')->insert([
        'order_id' => $id
    ]);

    db()->commit();
} catch(\Exception $e)
{
    db()->rollback();
}
```

# Running Queries

## Select Queries

```php
$users = db()
   ->from('users')
    ->get();
```

will run the query:

```sql
SELECT * FROM users;
``` 

and return all results as associative array.

### Specifying Columns

You may want to return specific columns:

```php
$users = db()->from('users', ['id', 'name'])
    ->get();
```

### Where

You can write where clauses in many ways. Examples are the following:

```php
$user = db()->from('users')
    ->where('id', 5)
    ->first();
```

will run the query:

```sql
SELECT * FROM users WHERE id = 5;
``` 

and return one row as associative array.

will run query:

```sql
SELECT id, name FROM users;
```

You can use parameter binding, and bind parameters:

```php
$user = db()->from('users')
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
$users = db()->from('users')
    ->where('id = ? OR id = ?', [5, 10])
    ->get()
;
```

will run:

```sql
SELECT * FROM users WHERE id = 5 OR id = 10
```

!> **Caution:** Question mark style binding, doesn't work with associative arrays.

**Following code will generate error:**

```php
$users = db()->from('users')
    ->where('id = ?', ['id' => 5])
    ->get()
;
```

Nested SQL Queries can be generated using callback functions.

```php
$users = db()->from('users')
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

You can also use operators in where clauses. If you pass where clauses as an array, all clauses in the array will be joined using `AND` operator.

```php
$users = db()->from('users')
    ->where('id', 3)
    ->orWhere([
        ['votes', '<', '500'],
        ['status', 3]
    ])
    ->get()
;
```

will run:

```sql
SELECT * FROM users WHERE id = 3 OR (votes < 500 AND status = 3)
```


As you can see below, queries inside of the function will be evaluated seperately inside of braces and it will run:

```sql
SELECT * FROM users 
    WHERE id = 5 OR status = 2 
        OR (votes < 500 AND status = 3) 
    ORDER BY id DESC
```

### Join

You can join tables:

```php
$users = db()->from('users')
    ->join('INNER JOIN user_permissions ON user_permissions.id = users.id')
    ->where('id', 1)
    ->get()
;
```

You can left join tables:

```php
$users = db()->from('users')
    ->joinLeft('user_permissions ON user_permissions.id = users.id')
    ->where('id', 1)
    ->get()
;
```

### Order By

You can order by column ascending or descending order:

```php
$users = db()->from('users')
    ->orderBy('id')
    ->get()
;
```

```php
$users = db()->from('users')
    ->orderByDesc('id')
    ->get()
;
```

### Group By

You can group by column:

```php
$users = db()->from('users')
    ->groupBy('id')
    ->get()
;
```

For multiple columns, you can use comma seperator:

```php
$users = db()->from('users')
    ->groupBy('status,votes')
    ->get()
;
```

### Find

You can use `find` function to return one row using identifier

```php
$user = db()->from('users')
    ->find(1)
;
```

will return one row with id = 1

### Die 

For debugging purposes, you can use `die` function to output the SQL Query that will run.

```php
db()->from('users')
    ->where('id', 5)
    ->die()
;
```

will output the query that will be executed. 

!> Please note that, die function will not run the query, just outputs it and **terminates the script**.

### Returning Functions

Function  | Description
------------- | -------------
get | will return all rows as associative array.
first | will just return the first row as associative array
count | Will return the number of rows for the query without any Group By statement.
one($column_name) | will return only one column value. 
column($column_name) | will return the values of specific column as an array list.
keyToValue($key_column) | will return result indexed by key_column. Value will be the row as the associative array.
keyToValue($key_column, $value_column) | will return result indexed by key_column. Value will be value of the specified column.
keyToValues($key_column) | when key_column is not unique, you can use this function to group results by key_column (e.g. status). Value will be the row as the associative array. 
keyToValues($key_column, $value_column) | when key_column is not unique, you can use this function to group results by key_column (e.g. status). Value will be value of the specified column.
max($column_name) | Will return maximum value of the specific column as a single value.
min($column_name) | Will return minimum value of the specific column as a single value.
average($column_name) | Will return average value of the specific column as a single value.

## Insert Queries

You can run insert queries using database client.

### Insert

Single insert statement can be run as the following example: 

```php
$userId = db()->table('users')->insert([
    'name' => 'John Doe'
]);
```

will return the auto increment id of the created row.

### InsertOrUpdate

Inserts or updates single record. First parameter is used to find if the row already exist,
- There are two options:
    * If the record doesn't exist:\
    Both parameters will be merged and inserted into database.

    * If the record exists:\
    Since first parameters doesn't change, it will update the record with the values in $data array (Second Parameter)

Function returns auto increment value for the record for both cases.

> Note: This function doesn't use unique indexes. It's recommended to use indexed columns for better performance.

```php
$attribute = [
    'id' => 1
];

$data = [
    'name' => 'foo'
];

db()->table('users')
    ->insertOrUpdate($attribute, $data);
```
It will check if there is a record having id => 1,\
if it doesnt exist, then this will become an insert statement.\
If it exist, then, the call become an update statement.

### InsertOrIgnore

When inserting a record to database, if there is a unique index, you may get an error. When this function is used, it ignores insert errors and returns without inserting the record on error. Which means that, the record will not be inserted if it already exist.

```php
db()->table('users')->insertOrIgnore([
    'id' => 1,
    'name' => 'John Doe'
]);
```

will not insert record if there is already a record with id = 1

### BulkInsert

Bulk inserts can improve performance since multiple records will be inserted in a single query.
