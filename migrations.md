# Migrations

When you are maintaining a software with database, it's obvious that you may need database changes.

- You may create new tables
- You may add new columns to existing tables
- You may create new Objects
- You may create new Object Specs for existing Objects
- You may update Objects
- You may update Object Specs

Migrations are placed in `Migration` folder for each Module. If you need Migrations for your App, than you can use Migrations
in `app/Migration` folder.

There are two types of Migrations

- [Install](#Install)
- [Upgrade](#Upgrade)

## Install

Install migrations run when the system is installed to a new database. Which means that, you can assume that, target database is empty
when you add a new migration.

> [!TIP]
> As an example: If you want to change name of a table, you can directly rename it if it already exists in Install script. 
> Since Installation only runs for empty databases, it will not have a table with the previous name.

You can use the following command to run migrations:

```bash
bin/butterfly install
```

## Generator

Install script aims to install an application from scratch. You may want to generate or update Install script with the following command:

```bash
bin/butterfly object:migration:create
```

This command will update app/Migration/Install.php with the migrations of all Data Types in the active database.

You can also filter table names

```bash
bin/butterfly object:migration:create --tables=users,faqs
```

will generate migration for Data Type: users and faqs tables.

You may also use wildcards for table names

```bash
bin/butterfly object:migration:create --tables=user%
```

will generate a single migration file with tables starting with user*.

## Upgrade

Upgrade migrations should run after each deployment. Upgrade migrations make it easy to maintain structure of your Database. Besides creating new Tables, Objects, Indexes, you can also delete or update 
existing ones using Upgrades.

You can use the following command to run migrations:

```bash
bin/butterfly upgrade
```

For migrations not to run more than once, you can use version numbers. Butterfly uses [semantic versioning](https://semver.org/) to version the Modules. Version numbers are written in module.yaml files. For more information about Modules 
you can check [Modules documentation](https://thebutterfly.io/docs/#/modules)

Example:

```php
namespace App\Migration;

use Butterfly\Framework\Migration\Base;

class Upgrade extends Base
{
    public function run()
    {
        if($this->currentVersionIsOlderThan('1.0.1'))
        {
            // Put some Migration Script code here
        }
    }
}
```

## Indexes

You can add Unique or Normal index to the Objects you have created.

### Index

```php
$response = db()->schema('my_new_table')->object(function(\Butterfly\Framework\Data\ButterflyObject $object) {
    $object->string('name');
    $object->dropdown('user_id', 'User')
        ->parameters('users', 'name', 'id', '-')
        ->searchable()
        ->listColumn()
        ->readonly()
        ->index() // This will add index to column user_id
        ->required()
    ;

    return $object;
});
```

### Unique Index

```php
$response = db()->schema('my_new_table')->object(function(\Butterfly\Framework\Data\ButterflyObject $object) {
    $object->string('name');
    
    $object->string('remote_user_id')->unique(); // This will add unique index to remote_user_id column

    return $object;
});
```

### Multiple Columns

```php
$response = db()->schema('my_new_table')->object(function(\Butterfly\Framework\Data\ButterflyObject $object) {
    $object->string('title');
    $object->string('sub_title');
    
    $object->unique(['title', 'sub_title']); // This will add unique index to title and sub_title columns together. 
    
    $object->index(['title', 'sub_title']); // This will add normal index to title and sub_title columns together.

    return $object;
});
```

## App Specific Migrations

You can also use Migrations in `app` Folder. `app` is considered as a Module inside of the System. Which means that, you can 
update your modules version from `app/module.yaml` and you can write down Migration scripts in `app/Migration/Install.php` and 
`app/Migration/Upgrade.php` files.

## Migration Scripts

### Objects

#### Create or Update

Object Migrations works with upsert strategy. Which means that, when you write down a migration, if the target Object already exist, it will update the existing Object. If it doesn't exist, it will insert new Object.

> [!WARNING]
> If you create a migration for an existing object and you don't define all of the existing Specs, it `won't` delete existing Object Specs.

> [!WARNING]
> Objects check existence with `table_name`. If you want to rename an existing Object, then you can check Renaming Object Table Names section.

Example:

```php
$response = db()->schema('my_new_table')->object(function(\Butterfly\Framework\Data\ButterflyObject $object) {
    $object->setDescription('Sample Description for Object');
    $object->hasItem();
    $object->hasTrash();
    $object->hasOrder();
    $object->setDatabaseAlias('test');
    $object->setAutoIncrementColumnName('entity_id');
    $object->setLinkFormat('%name%');
    $object->string('name');

    $object->integer('votes');
    $object->integer('vote_count')->defaultValue(100);
    $object->dropdown('user_id', 'User')
        ->parameters('users', 'name', 'id', '-')
        ->searchable()
        ->listColumn()
        ->readonly()
        ->required()
    ;
    
    $object->datetimeMysql('created_at')->defaultValue(db()->raw('CURRENT_TIMESTAMP()'));

    return $object;
});
```

#### Defining Object Spec Position (Placement)

When creating additional Object Specs, you can choose the relative position of the newly created Object Spec.

Example:

```php
db()->schema('my_new_table')->objectSpecs(function(\Butterfly\Framework\Data\ButterflyObject $object) {
            $object->integer('votes')->placeAfter('test');
            $object->integer('vote_count')->defaultValue(100)->placeBefore('test_2');

            return $object;
        });
```

will place `votes` Object Spec, after `test` column and will place `vote_count` Object Spec, before `test_2` column. 

>[!WARNING]
> By default, new Object Specs are placed Left Side Bottom. If target Column Name is not found, Default rules are applied. 

#### Creating Admin Menus for Objects

You can create admin menus while creating an Object using Migrations.

##### With Parent Menu

Example:
```php
$response = db()->schema('my_new_table')->object(function(\Butterfly\Framework\Data\ButterflyObject $object) {
    
    // This will create System Settings > Sub System Settings > My New Table    
    $object->setAdminParentMenu('System Settings', 'Sub System Settings');
    
    // You can update Menu Title. If you don't call this function it will default to Object Name
    $object->setAdminMenuTitle('My Menu Title');
       
    return $object;
});
```

##### Without Parent Menu

If you want to create a Main Menu to link to Object Listing Page, you can use the following example:

Example:
```php
$response = db()->schema('my_new_table')->object(function(\Butterfly\Framework\Data\ButterflyObject $object) {
    // This will create a Main Menu with title: My Menu Title  
    $object->setAdminMenuTitle('My Menu Title');
    
    // If you don't set the first argument, it will default to Object Name  
    $object->setAdminMenuTitle(); // will create a menu with title: My New Table
       
    return $object;
});
``` 

#### Renaming Table Names

You can rename table names of existing Objects.

```php
db()->schema('old_table_name')->object(function (\Butterfly\Framework\Data\ButterflyObject $butterflyObject) {
    $butterflyObject->setName('Desired Object Name');
    $butterflyObject->renameTable('new_table_name');
});
```

> [!TIP]
> Renaming table name will change the name of Object. You may use `setName` function to override auto-generated object name 

#### Creating new Object Specs

You can create new Object Specs for existing Objects using Migrations.

Example:

```php
$response = db()->schema('my_existing_table')->objectSpecs(function(\Butterfly\Framework\Data\ButterflyObject $object) {
    $object->integer('votes');
    $object->integer('vote_count')->defaultValue(100);

    return $object;
});
```

> [!TIP]
> You can also check Create or Update Object section for adding new Specs to existing Objects. It will also upsert Object Specs.  

#### Removing Object Specs

You can remove an existing Object Specs using Migrations.

Example:

```php
$cmsObjectModel = new \Butterfly\Core\Model\CmsObject();
$cmsObjectModel->removeObjectSpec('test_table_name', 'test_column_name');
```

will remove Object Spec with column name: `test_column_name` of the Object with table name: `test_table_name`

> [!WARNING]
> This function removes column from database. Please beware that all data in the column will be destroyed.

#### Overriding Column Type

Sometimes you may need different column types in database, for example: default column type for integers is `int(11)` but
you may want to increase the limit and update it to `bigint(20)`. You can use `columnType` function to update column type.

Example:
```php
$response = db()->schema('my_existing_table')->objectSpecs(function(\Butterfly\Framework\Data\ButterflyObject $object) {
    $object->integer('votes');
    $object->integer('vote_count')->columnType('bigint(20)');

    return $object;
});
```