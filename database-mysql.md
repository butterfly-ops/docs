# Introduction

Butterfly MySQL Implementation syntax is inspired from Laravel. Core aim of implementation is to maintain readability besides having performant queries. 
You can generate performant queries easily by using built-in functions.  

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

## SELECT Queries

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

#### Column List

```php
$users = db()
    ->from('users', ['id', 'name'])
    ->get();
```

#### Column List with Alias

You can also use aliases using following example:

```php
$users = db()->from('users', [
    '*',
    'relation_id' => 'object_relations.id'
])
    ->where('id', 5)
    ->orderBy('id DESC')
    ->get();
```

will run the following query:

```sql
SELECT *,object_relations.id AS relation_id FROM users WHERE id = :param_1 ORDER BY id DESC
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

> [!WARNING]
> You don't need bind function for shorthand where clauses. You can use directly bind parameter as second parameter to where clauses.
> For example: `->where('id', 5)` will bind parameters automatically. Don't use `bind` function for non-complex where operations.  

```php
$user = db()->from('users')
    ->join('user_roles', 'user_roles.user_id', '=', 'users_id AND status = :status')
    ->bind('status', 2)
    ->first();
```

will run the query:

```sql
SELECT * FROM users WHERE id = 5;
``` 

You can bind parameters using question marks (?)

```php
$users = db()->from('users')
    ->where('id = ? OR id = ?', [5, 10])
    ->get();
```

will run:

```sql
SELECT * FROM users WHERE id = 5 OR id = 10
```

> [!DANGER]
> Question mark style binding, doesn't work with associative arrays.

**Following code will generate error:**

```php
$users = db()->from('users')
    ->where('id = ?', ['id' => 5])
    ->get();
```

#### whereIn

You can use arrays with where clauses:

```php
$users = db()->from('users')
    ->whereIn('id', [1,2,3])
    ->get();
```

will run the query:

```sql
SELECT * FROM users WHERE id IN (1, 2, 3)
```

#### whereNotIn

You can use arrays with where clauses:

```php
$users = db()->from('users')
    ->whereNotIn('id', [1,2,3])
    ->get();
```

will run the query:

```sql
SELECT * FROM users WHERE id NOT IN (1, 2, 3)
```

#### whereNull

By using **whereNull**, you can easily filter only null values:

```php
$users = db()->from('users')
    ->whereNull('status')
    ->get();
```

will run the query:

```sql
SELECT * FROM users WHERE status IS NULL
```

#### whereNotNull

```php
$users = db()->from('users')
    ->whereNotNull('status')
    ->get();
```

will run the query:

```sql
SELECT * FROM users WHERE status IS NOT NULL
```


#### Nested Clause

Nested SQL Queries can be generated using callback functions.

```php
$users = db()->from('users')
    ->where('id', 5)
    ->orWhere('status', 2)
    ->orWhere(function($query) {
        return $query->where('votes', '<', '500')
            ->orWhere('status', 3);
    })
    ->orderBy('id DESC')
    ->get();
```

As you can see below, queries inside of the function will be evaluated seperately inside of braces and it will run:

```sql
SELECT * FROM users 
    WHERE id = 5 OR status = 2 
        OR (votes < 500 AND status = 3) 
    ORDER BY id DESC
```

#### orWhere

You can also use operators in where clauses. If you pass where clauses as an array, all clauses in the array will be joined using `AND` operator.

```php
$users = db()->from('users')
    ->where('id', 3)
    ->orWhere([
        ['votes', '<', '500'],
        ['status', 3]
    ])
    ->get();
```

will run:

```sql
SELECT * FROM users WHERE id = 3 OR (votes < 500 AND status = 3)
```

#### orWhereIn

```php
$users = db()->from('users')
->where('id', 5)
->orWhereIn('status', [1,2,3])
->get();
```

will run the query:

```mysql
SELECT * FROM users WHERE id = 5 OR status IN (1,2,3)
```

#### orWhereNull

```php
$users = db()->from('users')
->where('id', 5)
->orWhereNull('status')
->get();
```

will run the query:

```mysql
SELECT * FROM users WHERE id = 5 OR status IS NULL
```

#### orWhereNotNull

```php
$users = db()->from('users')
->where('id', 5)
->orWhereNotNull('status')
->get();
```

will run the query:

```mysql
SELECT * FROM users WHERE id = 5 OR status IS NOT NULL
```

#### Distinct

```php
$users = db()
   ->from('users')->distinct(['name', 'phone'])
    ->get();
```

```php
$users = db()
   ->from('users', ['name', 'phone'])->distinct()
    ->get();
```

will run the queris:

```sql
SELECT DISTINCT name,phone FROM users;
``` 

#### Between

```php
$users = db()->from('users')
    ->orWhereBetween('status', [5, 10])
    ->get();
```
will run:

```sql
SELECT * FROM users WHERE status BETWEEN 5 AND 10
```
#### Not Between

```php
$users = db()->from('users')
    ->orWhereNotBetween('status', [5, 10])
    ->get();
```
will run:

```sql
SELECT * FROM users WHERE status NOT BETWEEN 5 AND 10
```

### Join

You can join tables:

#### Inner Join

```php
$users = db()->from('users')
    ->join('user_permissions', 'users.id', '=', 'user_permissions.id')
    ->where('id', 1)
    ->get();
```

will run the query:

```sql
SELECT * FROM users
    INNER JOIN user_permissions ON users.id = user_permissions.id
WHERE id = 1
```

> [!WARNING]
> Join function uses INNER JOIN Statement

#### Left Join

You can left join tables:

```php
$users = db()->from('users')
    ->joinLeft('user_permissions', 'users.id', '=', 'user_permissions.id')
    ->where('id', 1)
    ->get();
```

will run the query:

```sql
SELECT * FROM users
    LEFT JOIN user_permissions ON users.id = user_permissions.id
WHERE id = 1
```

#### Right Join

You can right join tables:

```php
$users = db()->from('users')
    ->joinRight('user_permissions', 'users.id', '=', 'user_permissions.id')
    ->where('id', 1)
    ->get();
```

will run the query:

```sql
SELECT * FROM users
    RIGHT JOIN user_permissions ON users.id = user_permissions.id
WHERE id = 1
```

### Use Index

```php
$users = db()
   ->from('users')->useIndex('name, phone')
    ->get();
```

will run the query:

```sql
SELECT * FROM users USE INDEX (name, phone);
``` 

### Force Index

```php
$users = db()
   ->from('users')->forceIndex('name, phone')
    ->get();
```

will run the query:

```sql
SELECT * FROM users FORCE INDEX (name, phone);
``` 

### Order By

You can order by column ascending or descending order:

```php
$users = db()->from('users')
    ->orderBy('id')
    ->get();
```

```php
$users = db()->from('users')
    ->orderByDesc('id')
    ->get();
```

### Group By

You can group by column:

```php
$users = db()->from('users')
    ->groupBy('id')
    ->get();
```

For multiple columns, you can use comma seperator:

```php
$users = db()->from('users')
    ->groupBy('status,votes')
    ->get();
```

### Having

```php
db()->from('users', ['users.id'])
    ->groupBy('role_id')
    ->having('a > 5')
->get();
```

will run the following query:

```sql
SELECT users.id FROM users GROUP BY role_id HAVING a > 5
```

### Skip (Offset)

You can add an offset to the result using `skip` function 

```php
db()->from('users')
    ->skip(5);
```

will run the query:

```sql
SELECT * FROM users OFFSET 5
```

> [!TIP]
> You can use skip function with limit or pagination functions. It will basically skip `X` 
> results and limit or paginate after skipped records.

### Limit

Results can be limited using limit function. Only the first number of rows will be returned.

```php
db()->from('users')
    ->limit(10);
```

Will run the query:

```sql
SELECT * FROM users LIMIT 10
```

And will return first 10 rows from `users` table.

### Pagination

You can define paginate results by using `paginate` function.

Parameter | Description | Default Value
--------- | ----------- | ----------- 
`$limit` | Sets the limit per page | 20
`$page_no` | Sets the current page  | 1

```php
db()->from('users')
    ->paginate(5, 2)
    ->get();
```

Will run the following query:

```sql
SELECT * FROM users LIMIT 5, 5
```

And will return the results from 2nd page starting from `6.` to `10.` record. 

### Find

You can use `find` function to return one row using identifier

```php
$user = db()
    ->from('users')
    ->find(1);
```

will return one row with id = 1

### Die 

For debugging purposes, you can use `die` function to output the SQL Query that will run.

```php
db()->from('users')
    ->where('id', 5)
    ->die();
```

will output the query that will be executed. 

> [!NOTE]
> `die` function will not run the query, just outputs it and **terminates the script**.

### Returning Functions

Returning functions are used to execute the query and return the processed result.

Let's think of a virtual `users` table with the following records:

id | name | status
--- | --- | ---
1 | John Doe | waiting
2 | Jane Doe | waiting
3 | Jack Hamel | active
  

#### get

Will return all rows as associative array.

```php
db()->from('users')
    ->get();
```

will return

```php
[
    [
        'id' => 1,
        'name' => 'John Doe',
        'status' => 'waiting'  
    ],
    [
        'id' => 2,
        'name' => 'Jane Doe',
        'status' => 'waiting'  
    ],
    [
        'id' => 3,
        'name' => 'Jack Hamel',
        'status' => 'active'  
    ]
];
```

#### first

Will just return the first row as associative array

```php
db()->from('users')
    ->first();
```

will return

```php
[
    'id' => 1,
    'name' => 'John Doe',
    'status' => 'waiting'  
];
```

#### count

Will return the number of rows for the query without any Group By statement.

```php
db()->from('users')
    ->count();
```

will return:

`(int) 3`

#### one

Will return only one column value

```php
db()->from('users')
    ->one('name');
```

will return the name column value of the first row.

`John Doe`

#### column

Will return the values of specific column as an array list

```php
db()->from('users')
    ->column('name');
```

will return names as an array list.

```php
[
    'John Doe',
    'Jane Doe',
    'Jack Hammel'
];
```

#### keyToValue

Will return result indexed by key_column. Value will be the row as the associative array.

```php
db()->from('users')
    ->keyToValue('id')
;
```

will return:

```php
[
    1 => [ // As you see, id column value is used as the key of the array.
        'id' => 1,
        'name' => 'John Doe',
        'status' => 'waiting'  
    ],
    2 => [
        'id' => 2,
        'name' => 'Jane Doe',
        'status' => 'waiting'  
    ],
    3 => [
        'id' => 3,
        'name' => 'Jack Hamel',
        'status' => 'active'  
    ]
];
```

When you call keyToValue function with two parameters, it will use the column value

```php
db()->from('users')
    ->keyToValue('id', 'name')
;
```

will return result indexed by key_column. Value will be value of the specified column:

```php
[
    1 => 'John Doe',
    2 => 'Jane Doe',
    3 => 'Jack Hamel'
];
```

#### keyToValues

when key_column is not unique, you can use this function to group results by key_column (e.g. status). Value will be the row as the associative array.

```php
db()->from('users')
    ->keyToValues('status')
;
```

will return:

```php
[
    'waiting' => [ // As you see, results are grouped by `status` column.
        [ 
            'id' => 1,
            'name' => 'John Doe',
            'status' => 'waiting'  
        ],
        [
            'id' => 2,
            'name' => 'Jane Doe',
            'status' => 'waiting'  
        ]
    ],
    'active' => [
        [
            'id' => 3,
            'name' => 'Jack Hamel',
            'status' => 'active'  
        ]
    ]
];
```

When key_column is not unique, you can use this function to group results by key_column (e.g. status). Value will be value of the specified column

```php
db()->from('users')
    ->keyToValues('status', 'name')
;
```

will return result indexed by key_column. Value will be array of values of the specified column:

```php
[
    'waiting' => [
        'John Doe',
        'Jane Doe'
    ],
    'active' => [
        'Jack Hamel'
    ]
];
```

#### max

Will return maximum value of the specific column as a single value

```php
db()->from('users')
    ->max('id');
```

will return:

`3`

#### min

Will return minimum value of the specific column as a single value

```php
db()->from('users')
    ->min('id');
```

will return:

`1`

#### average

Will return average value of the specific column as a single value

```php
db()->from('users')
    ->average('id');
```

will return:

`2`

#### transform

Transform function is used to transform the returning rows.

> [!DANGER]
> Transform function should be called before returning functions.

```php
db()->from('users')->transform(function($row) {
    $row['id_with_name'] = $row['id'] . ' - ' . $row['name']; 
    return $row;
})->first();
```

will return

```php
[
    'id' => 1,
    'name' => 'John Doe',
    'status' => 'waiting',
    'id_with_name' => '1 John Doe'  
];
```

### Caching Results

To improve performance of your application, you may want to cache results to use it multiple times. On the other hand,
you may need the same result in the same code (For example: in a background job, you may have a where query in for loop)
For these cases, if you use registry, then you may get rid of `Cache Driver Connection` time.  

#### Cache

You can use cache function to cache results.

##### Without Parameters

Example:

```php
db()->from('users')
    ->where('id', 5)
    ->cache()
->get();
```

will cache the result after first call for 60 seconds by default. 

> [!TIP]
> Result will return result without caching if cache is disabled.

##### With Duration

Example:

```php
db()->from('users')
    ->where('id', 5)
    ->cache(120)
->get();
```

will cache the result after first call for 120 seconds.

> [!TIP]
> Result will return result without caching if cache is disabled.

##### With Duration and Cache Key

Example:

```php
db()->from('users')
    ->where('id', 5)
    ->cache(120, 'test-cache-key')
->get();
```

will cache the result using `test-cache-key` in Cache. Which means that, you can remove cache using following code:

```php
\Cache::delete('test-cache-key');
```

#### Registry

You can use registry to cache results for the running code.

##### Without Registry Key

Example:

```php
db()->from('users')
    ->where('id', 5)
    ->registry()
->get();
```

will save the result to application registry and returned  

##### With Registry Key

Example:

```php
db()->from('users')
    ->where('id', 5)
    ->registry('test-key')
->get();
```

will save the result to application registry using `test-key` as key. Which means that, you can access and manipulate result 
using following code block:

```php
\Butterfly\Framework\Registry\Registry::get('test-key');
```

```php
\Butterfly\Framework\Registry\Registry::set('test-key', [
    'changed-data'
]);
```

> [!TIP]
> Although you may use registry keys while saving results to registry, there is no known use case for this feature :)

## INSERT Queries

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

```php
db()->table('users')
    ->bulkInsert([
        [
            'id' => 1,
            'name' => 'foo',
            'surname' => 'bar'
        ],
        [
            'id' => 2,
            'name' => 'John',
            'surname' => 'Doe'
        ]
    ])
;
```

### BulkInsertOrUpdate

When bulk inserting data, if there is a unique index and new data already exists, than you may want to update the existing data.
There are two options:

- Updating all columns: Following query will update all columns if the records already exist.

```php
db()->table('users')
     ->bulkInsertOrUpdate([
         [
             'id' => 1,
             'name' => 'foo',
             'surname' => 'bar'
         ],
         [
             'id' => 2,
             'name' => 'John',
             'surname' => 'Doe'
         ]
     ])
 ;
```

- Updating specific columns: Following query will only update the name column if the unique key already exist for the records.

```php
db()->table('users')
    ->bulkInsertOrUpdate([
        [
            'id' => 1,
            'name' => 'foo',
            'surname' => 'bar'
        ],
        [
            'id' => 2,
            'name' => 'John',
            'surname' => 'Doe'
        ]
    ], [
        'name'
    ])
;
```

### BulkInsertOrIgnore

When bulk inserting data, if there is a unique index and new data already exists, than you may want to ignore the new data without any error.

```php
db()->table('users')
    ->bulkInsertOrIgnore([
        [
            'id' => 1,
            'name' => 'foo',
            'surname' => 'bar'
        ],
        [
            'id' => 2,
            'name' => 'John',
            'surname' => 'Doe'
        ]
    ])
;
```

## UPDATE Queries

You can run update queries using database client.

### Update

Simple update statement can be run as the following example:

```php
db()->table('users')
    ->where('id', 1)
    ->update([
        'name' => 'foo',
        'surname' => 'bar'
    ]);
```

### Limit

You can limit the number of rows the update query can update by using limit function.

```php
db()->table('users')
    ->where('id', 1)
    ->limit(1)
    ->update([
        'name' => 'foo',
        'surname' => 'bar'
    ]);
```

will run the query:

```sql
UPDATE users SET name = 'foo', surname = 'bar' WHERE id = 1 LIMIT 1;
```

### Where Clause

> **Note:** You can use all type of where clauses with update queries. Please check [WHERE](#where) section for this.

### Join Statement

> **Note:** You can use all type of join clauses with update queries. Please check [JOIN](#join) section for this.

Example Usage:

```php
db()->table('users')
    ->join('user_groups', 'user_groups.id', '=', 'users.user_group_id')
    ->where('users.id', 1)
    ->update([
        'name' => 'foo',
        'user_groups.name' => 'bar'
    ])
;
```

will run the following query:

```sql
UPDATE `users` INNER JOIN user_groups ON user_groups.id = users.user_group_id SET `name` = 'foo',`user_groups`.`name` = 'bar' WHERE users.id = 1
```

## DELETE Queries

You can run delete queries using database client.

### Delete

Simple delete statement can be run as the following example:

```php
$affected = db()->table('users')
    ->where('id', 5)
    ->delete()
;
```

will run the following query and will return `number of rows affected`

```sql
DELETE FROM users WHERE id = 5
```

### Join Statement

Multiple tables may be joined and deleted.

```php
db()->table('user_groups')
    ->join('users', 'user_groups.id', '=', 'users.user_group_id')
    ->whereNull('users.id')
    ->delete(['users'])
;
```

Will run the following query:

```sql
DELETE users FROM user_groups INNER JOIN users ON user_groups.id = users.user_group_id WHERE users.id IS NULL
```

> **Note:** Delete function accepts array of table names, if tables names are not given, then it will only delete the main table which is defined when table function is called. Which is `user_groups` table in the example.

When using join statements, if no delete tables is defined when delete function is called, only main table will be deleted.

Example:

```php
db()->table('user_groups')
    ->join('users', 'user_groups.id', '=', 'users.user_group_id')
    ->whereNull('users.id')
    ->delete() // No table name is defined, user_groups table will be deleted. 
;
```

Will run the following query:

```sql
DELETE user_groups FROM user_groups INNER JOIN users ON user_groups.id = users.user_group_id WHERE users.id IS NULL
```

## Schema

You can run schema operations with `Butterfly\Database`

### tables

Will return the list of tables in the databases.

```php
db()->schema()->tables();
```

will return the list of tables as an array list.

```php
[
    'cms_admin_users', 
    'videos',
    'articles'
];
```

### columns

Will return the list of columns in a table.

```php
db()->schema('users')->columns();
```

will return

```php
[
    [
        'column_name' => 'id',
        'data_type' => 'int',
        'is_primary_key' => true,
        'is_nullable' => false
    ],
    [
        'column_name' => 'name',
        'data_type' => 'varchar',
        'is_primary_key' => false,
        'is_nullable' => false
    ]
];
```

### createTable

will create a table with the specified columns.

```php
db()->createTable('test', [
  [
      'column_name' => 'id',
      'identifier' => true,
      'column_type' => 'int(11)'
  ],
  [
      'column_name' => 'name',
      'column_type' => 'varchar(255)'
  ]
]);
```

will run the following query:

```sql
CREATE TABLE `test` (`id` int(11) NOT NULL AUTO_INCREMENT,`name` varchar(255) NOT NULL, PRIMARY KEY (`id`)) ENGINE = `InnoDB`
```

### createOrUpdateTable

it checks for the table, if the table already exists, it will alter.

> [!TIP]
> This function also checks for columns, if column information is the same, then, it will skip it, if column is not identical, it will modify the column.

> [!WARNING]
> This function doesn't check auto_increment column for altering operations. Which means that, you may not change auto_increment column for existing tables.

```php
db()->schema()->createOrUpdateTable('test', [
  [
      'column_name' => 'id',
      'identifier' => true,
      'column_type' => 'int(11)'
  ],
  [
      'column_name' => 'name',
      'column_type' => 'varchar(255)',
      'column_default' => 'John Doe'
  ]
]);
```

will run the following query if table doesn't exist:

```sql
CREATE TABLE `test` (`id` int(11) NOT NULL AUTO_INCREMENT,`name` varchar(255) NOT NULL DEFAULT 'John Doe', PRIMARY KEY (`id`)) ENGINE = `InnoDB`
```

will run the following query if table exists, id column exists but different then current info, name column is missing.

```sql
ALTER TABLE `test` MODIFY `id` int(11) NOT NULL,ADD `name` varchar(255) NOT NULL DEFAULT 'John Doe'
```

will run the following query if table exists, id column exists and identical, name column is missing.

```sql
ALTER TABLE `test` ADD `name` varchar(255) NOT NULL DEFAULT 'John Doe'
```

### dropColumns

Drop column drops the column from table. If column doesn't exist, then it will just return true

```php
db()->schema('test')->dropColumns(['test_column', 'test_column_2']);
```

will run the following query:

```sql
ALTER TABLE `test` DROP `test_column`,DROP `test_column_2`
```

### dropTable

Drop table removes the table from database. If table doesn't exist, then it will just return true

```php
db()->schema('test')->dropTable();
``` 

will run the following query:

```sql
DROP TABLE `test`;
```

> [!TIP]
> Drop table function checks if table exists before running the query

Alternatively, you can also call function with table name as first parameter.

```php
db()->schema()->dropTable('test');
```

will run the following query:

```sql
DROP TABLE `test`;
```

> [!TIP]
> As you may guess, if you define parameter to the function, it will be used instead of tableName property of the class.