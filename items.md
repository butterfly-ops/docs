# Items

## Introduction

Butterfly really cares about `Clean Data`. When you create a `Data Type` from Admin Panel, it creates a table with name
you define from Admin or Migration Code.

Items have multiple usages:

- When you want your records to have Globally Unique ID in your system
- When you want your records to be synced to ElasticSearch automatically
- If you want to have your records to have a Design in Frontend and have a Generated Link

Items also have a dynamic many - to - many relation with each other. Let's say that you have Products Data Type and Photo Galleries
Data Type. If both are items, you can relate records right from Admin Panel.

## Sync

When you make an operation from the Butterfly Admin Panel, Sync operation is handled automatically. If you are importing some data
programatically, you should call some functions to sync data to `items` table.

### itemRefreshByItemIds

If you have itemIds on hand, you can use following function to update those items.

```php
$mCmsObject = new \Butterfly\Core\Model\CmsObject();
$mCmsObject->itemRefreshByItemIds([1,2,3], false);
```

> [!TIP]
> If `forceSeoUpdate` parameter is false, then the link of the item won't be changed if it already exists.
> If true, it automatically update links and inserts redirection record to `redirect_map` if the link is changed.

> [!TIP]
> If you have missing items that's not created yet, you can use `itemRefreshByEntityIds`

### itemRefreshByEntityIds

If you have only the ID in the table, you can use `refreshItemsByEntityIds` method.

```php
$mCmsObject = new \Butterfly\Core\Model\CmsObject();
$mCmsObject->itemRefreshByEntityIds([1,2,3], Butterfly\Core\Model\Objects::getObjectId('TABLE_NAME'), false);
```

> [!TIP]
> If `forceSeoUpdate` parameter is false, then the link of the item won't be changed if it already exists.
> If true, it automatically update links and inserts redirection record to `redirect_map` if the link is changed.

### itemFix

You can use this function to create missing items or update seo columns for all or specific Data Types.

```php
$mCmsObject = new \Butterfly\Core\Model\CmsObject();
$mCmsObject->itemFix(); // You can also define Data Type Ids here.
```

> [!TIP]
> If you want Label and Title columns in `items` table. You can use `itemRefresh` method.

### itemRefresh

You can use this function to refresh all items for all or specific Data Type.

```php
$mCmsObject = new \Butterfly\Core\Model\CmsObject();
$mCmsObject->itemRefresh(); // You can also define Data Type Ids here.
```

## Commands

You can also use commands to sync items.

### `cron:garbage-collector`

Cleans up items table for not used items

Usage:

```bash
bin/butterfly cron:garbage-collector
```

### `cron:refresh-items`

Updates items table with the entity table information

Usage:

```bash
bin/butterfly cron:refresh-items 72 ## Will refresh all records for Data Type #72
```