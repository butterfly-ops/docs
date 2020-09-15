# Objects

## Introduction

Objects are one of the most special component of Butterfly. Objects are tables with detailed definition.
While defining your object, you can define Url, Table Name, User Friendly Name etc. After defining your objects, you can
start editing your contents from your admin panel, without writing a single line of code.

When you create an Object from `butterfly panel` or `upgrade migration`, `table` (for SQL) or `collection` (for MongoDB) or `index` (for ElasticSearch) is automatically generator
which means that, you don't need to make Database creations manually.  

## Object Specs

All data types have their names and specifications. For example: If you have object named `blog_posts`, you would possibly need a 
Object Spec named `title` with a type of `String`.

When you create an admin panel or using a migration script, `columns` (for SQL), `fields` (for MongoDB), `mapping` for Elastic Search is automatically created.

In other words, Object Specs is equavilant to `columns` in SQL.

### String

Strings are data types which have a short text (maximum length: 255).

Parameters:

Name | Column Name | Description
--- | --- | ---
Limit| val_1 | Limits the number of characters in string. 

### Datetime

Datetime Field type is used to store Date & Time information in [Unix Timestamp format](https://en.wikipedia.org/wiki/Unix_time).
When you use this field type, it will create a column with type integer, since Unix Timestamp format designates the number of seconds 
have passed since 1th of January 1970.

This field type is suitable for Release Date's, Expiry Date's, Event Dates etc. Since it includes time and starts from 1970, we don't recommend this field type to be used 
for birth dates.

>[!TIP]
> When you need a content to be disappear from site before Release Date or Expiry Date automatically, you can use the following special column names:
> `release_date` for Publication Dates and `expiry_date` for auto Expiration.

### Checkbox

Checkbox Field type displays a checkbox as it's name describes. It will create a column with type tinyint.

It will save value "1" if field is checked and "0" if it's not checked. 

### Nested

When you want to store your multiple rows / fields in a single field as JSON, you can use Nested Field Type.

As it's name explains, in nested fields, you can build your JSON using other field types.

Parameters:

Name | Column Name | Description
--- | --- |---
Configuration | val_1 | Field Configuration of the field as YAML (Example is below)
Sortable | val_2 | Whether sub-fields can be sorted or not.
Multiple | val_3 | If yes, you can add multiple rows

Example Configuration:

```yaml
title:
    name: 'Title'
    type: 'string'
image:
    name: 'Image'
    type: 'image_upload'
    val_1: 'content'
```

will save the data in Database like follows:

```json
[
  {
    "title": "Test Title",
    "image": "content/12-10/01/test.png"
  }   
]
```

will output:

![Nested Field Type](images/nested-field-1.png "Nested Field Type")

>[!TIP]
> You can use nested field recursively, which means that, you can build endlessly deep JSON using the following example.

More complex example:

```yaml
test:
    name: 'Test'
    type: string
people:
    name: 'People'
    type: nested
    val_1:
        name:
            name: 'Name'
            type: string
        surname:
            name: 'Surname'
            type: string
        images:
            name: 'Images'
            type: nested
            val_1:
                title:
                    name: 'Title'
                    type: string
                image:
                    name: 'Image'
                    type: image_upload
                    val_1: content
                people:
                    name: 'Credits'
                    type: 'nested'
                    val_1:
                        name:
                            name: 'Name'
                            type: 'string'
            val_2: 1
            val_3: 1
    val_2: 1
    val_3: 1
```

will save the data in Database like follows:

```json
[
  {
    "test": "Test",
    "people": [
       {
        "name": "Test",
        "surname": "Surname",
        "images": [
          {
            "title": "Test",
            "image": "20-09/01/test.png",
            "credits": [
              {
                "name": "Name - 1"
              },
              {
                "name": "Name - 2"
              }     
            ]   
          }   
        ]
       }  
    ]
  },
  {
      "test": "Test - 2",
      "people": [
         {
          "name": "Test - 2",
          "surname": "Surname",
          "images": [
            {
              "title": "Test - 2",
              "image": "20-09/01/test-2.png",
              "credits": [
                {
                  "name": "Name - 3"
                },
                {
                  "name": "Name - 4"
                }     
              ]   
            }   
          ]
         }  
      ]
    }  
]
```

will output:

![Complex Example for Nested Field Type](images/nested-field-2.png "Complex Example for Nested Field Type")

## Permissions

You can define permissions per Object / per User Group in Butterfly Panel.

There are three main types of permissions:

- [Generic Permissions](#generic-permissions)
- [Permission Exceptions](#permission-exceptions)
- [Custom Permissions](#custom-permissions)

### Generic Permissions

Using Generic Permissions, you can define permissions for each Object / Object Spec.

>[!TIP]
> You can define permission exceptions to limit the User's permission to the defined Record Set. For example: You may want to 
> grant user to edit Products in a specific Category. Or you may want your Junior Editor's to create Articles in a Pending State.
> This definitions are handled in [Permission Exceptions](#permission-exceptions).

#### Add Permission:

This permission grants user to add a new Record to the Object.  

#### Edit

This permission grants user to edit an existing Record of the Object.

#### View

This permission grants user read only view access for existing Records of the Object 

#### Delete

This permission grants user delete permission for Records of the Object.

### Permission Exceptions

You may want to grant user to edit Products in a specific Category. Or you may want your Junior Editor's to create Articles in a Pending State.

### Custom Permissions

Custom Permissions are used for the Custom Permission checks. Permissions are saved in Permission Defitions Object in `cms_permissions`. You should also
define Permission Groups to group permissions.

#### Check Permission

You can check defined permissions for the logged in user using the following example:

```php
$mUser = new \Butterfly\Core\Model\User();
$mUser->checkCustomPermission('sales-order', 'approve');
```

```smarty
{'sales_order::approve'|custom_permission}
```

#### Grant Permission

Grant permission is used to Log Custom Permission granted to user.

> [!WARNING]
> Grant Permission Work In Progress. You can start using function calls for the future reference.

```php
$mUser = new \Butterfly\Core\Model\User();
$mUser->grantCustomPermission('sales-order', 'approve', [
        'entity_id' => 1234, 
        'object_id' => \Butterfly\Core\Model\Objects::getObjectId('orders'),
        'comment' => 'Testing' 
    ]
);
```

## Hooks

You can intercept operations like Insert, Update or Delete on Panel. For example, you may want to check an external service 
before a new entry is added to database, or you may want to send data to an external service.

### Hook Creation

You can create a hook using the following command:

```bash
bin/butterfly make:hook users
```  

this will create a file in app/Hook/Users.php.

Then, when a new entry is saved in admin panel, it will run related function in this hook.

### Event Functions

Hook functions are as follows:

#### before_add

This function is triggered before adding new entry. You can stop the operation by calling error function, or 
you can use confirm function to alert user before doing the operation.

> When you use before_ functions, since the operation is not done yet, you can run error function; you should use before function if you want to stop operation.

> [!DANGER]
> We don't have an id yet when before_add operation is triggered.

Following Hook will halt to operation and display an error on screen:

```php
<?php

namespace App\Hook;

use Butterfly\Framework\Data\Crud;
use Butterfly\Library\Hook;

class Users extends Hook
{
    public function before_add(Crud &$crud)
    {
        $crud->error('No way !');
    }
}
```

#### after_add

This function is triggered after adding new entry. You can use this function if you want to run your trigger
 when entry is actually added.
 
 ```php
<?php

namespace App\Hook;
 
use Butterfly\Framework\Data\Crud;
use Butterfly\Library\Hook;
 
class Users extends Hook
{
    public function after_add(Crud &$crud)
    {
        $data = $crud->getData();
        $newId = $crud->getDataId();
    
        // You can call external service with $data variable here
    }
}
```

#### before_edit

This function is triggered before updating an entry. You can also check if there is a difference with previous state using 
[`isChanged`](#isChanged) function. You can also get the old info using [`getOldData`](#getOldData) function.

```php
<?php

namespace App\Hook;
 
use Butterfly\Framework\Data\Crud;
use Butterfly\Library\Hook;
 
class Users extends Hook
{
    public function before_edit(Crud &$crud)
    {
        // Following if block will ask user confirmation.
        if($crud->isChanged('name'))
        {
            $oldData = $crud->getOldData('name');
            $newData = $crud->get('name');
                
            $crud::confirm('You are changing name from ' . $oldData . ' to ' . $newData . '. Are you sure?');
        }
    }
}
```

#### after_edit

This function is triggered after updating an entry.

> [!WARNING]
> You cannot use `isChanged` and `getOldData` functions on after_edit section because the data is already updated. Because
> of that, `isChanged` will always return `false` and `getOldData` will return the new data.

> [!TIP]
> You can use `before_edit` hook to check `isChanged` and `getOldData` and set the data to a variable in `$this` context. Then,
> you can use variables you've created to access this information.   

```php
<?php

namespace App\Hook;
 
use Butterfly\Framework\Data\Crud;
use Butterfly\Library\Hook;
 
class Users extends Hook
{
    private $nameIsChanged;
    private $oldName;

    public function before_edit(Crud &$crud)
        {
            $this->nameIsChanged = $crud->isChanged('name');
            $this->oldName = $crud->getOldData('name');
        }

    public function after_edit(Crud &$crud)
    {
        // Now, you can use $this->nameIsChanged or $this->oldName variables to access this information.
    }
}
```

#### before_delete

This function is triggered before deleting an entry. You can access the data to be deleted by using `$crud->getDataId()` function.
It will retrieve the id that will be deleted. Since the operation is not done yet, you can also access the data.

#### after_delete

This function is triggered after deleting an entry. Only parameter you can access is the ID `$crud->getDataId()` of the entry, since it's deleted from
the database. 
 
### Crud Functions

#### get

You can use `get` function to get value of a specific field.

Example:

```php
<?php

namespace App\Hook;

use Butterfly\Framework\Data\Crud;
use Butterfly\Library\Hook;

class Users extends Hook
{
    public function before_add(Crud &$crud)
    {
        $name = $crud->get('name');

        // Now we have name value in `$name` variable. You can use it for further operations.
    }
}
``` 

#### error

You can trigger error and stop the operation using this function.

> [!WARNING]
> You should use `error` function with before_ events, since the operation is not done when before_ events are triggered.

Example:

```php
<?php

namespace App\Hook;

use Butterfly\Framework\Data\Crud;
use Butterfly\Library\Hook;

class Users extends Hook
{
    public function before_add(Crud &$crud)
    {
        $crud->error('No way !');
    }
}
```

#### confirm

You can use confirm function when you want to get yes / no confirmation from user. If user clicks to no, it will cancel 
the operation. If user clicks OK, then the operation will continue. 

```php
<?php

namespace App\Hook;

use Butterfly\Framework\Data\Crud;
use Butterfly\Library\Hook;

class Users extends Hook
{
    public function before_add(Crud &$crud)
    {
        // The following should not be placed before calling confirm function
        // Because this code will run twice after user confirms the dialog. You can move this function
        // call after confirm function.
        db()->table('test')->update([
            'test' => 5
        ]);

        $crud->confirm('Are you sure?');
    }
}
```

!> When you use confirm function, Hook code which is written before confirmation runs twice. You should not write code that 
should not be called more than once before calling confirm function.

#### getDataId

You can use getDataId function to retrieve the id of relevant column.

> [!DANGER]
> You cannot use this function inside of before_add since record is not created yet which means there is no id.

```php
<?php

namespace App\Hook;

use Butterfly\Framework\Data\Crud;
use Butterfly\Library\Hook;

class Users extends Hook
{
    public function after_add(Crud &$crud)
    {
        $newId = $crud->getDataId();

        // We have the id of new record, so you can use it for further operations.
    }
}
```

#### getOldData

When user saves data from Butterfly Panel, you can get it's previous state using getOldData function.

```php
<?php

namespace App\Hook;

use Butterfly\Framework\Data\Crud;
use Butterfly\Library\Hook;

class Articles extends Hook
{
    public function before_edit(Crud &$crud)
    {
        $oldTitle = $crud->getOldData('title');

        // You have the title of the article you can use it for further operations.
    }
}
```

> [!NOTE]
> `getOldData` function gets data from Database when it's called. Since database is updated before calling after_ events, if you call this function in after function, it will not work properly and return the latest data. If you need old data in after_ events, then, you can call it in before function and set it to another property.

#### isChanged

When user saves data in Butterfly Panel, you may want to check if a specific field is changed or not.  

> [!WARNING]
> `isChanged` function returns if the field is changed or not. Since database is updated before calling after_ events, if you call this function in after function, it will not work properly and return the latest data. If you need old data in after_ events, then, you can call it in before function and set it to another property.

In the following example, confirmation dialog will be displayed if the user changed `title`:

```php
<?php

namespace App\Hook;

use Butterfly\Framework\Data\Crud;
use Butterfly\Library\Hook;

class Articles extends Hook
{
    public function before_edit(Crud &$crud)
    {
        if($crud->isChanged('title'))
        {
            $oldTitle = $crud->getOldData('title');
            $newTitle = $crud->get('title');
        
            $crud->confirm('You have changed title from : ' . $oldTitle . ' to ' . $newTitle 
                . '. Are you sure?');
        }

        // You have the title of the article you can use it for further operations.
    }
}
```