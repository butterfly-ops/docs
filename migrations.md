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

## Upgrade

Upgrade migrations should run after each deployment. Upgrade migrations make it easy to maintain structure of your Database. Besides creating new Tables, Objects, Indexes, you can also delete or update 
existing ones using Upgrades.

You can use the following command to run migrations:

```bash
bin/butterfly upgrade
```

For migrations not to run more than once, you can use version numbers. Butterfly uses [semantic versioning](https://semver.org/) to version the Modules. Version numbers are written in module.yaml files. For more information about Modules 
you can check [Modules documentation](https://thebutterfly.io/docs/#/modules)

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

    return $object;
});
```

#### Renaming Table Names

You cao rename table names of existing Tables.

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