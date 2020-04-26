# Objects

## Introduction

Objects are one of the most special component of Butterfly. Objects are tables with detailed definition.
While defining your object, you can define Url, Table Name, User Friendly Name etc. After defining your objects, you can
start editing your contents from your admin panel, without writing a single line of code. 

## Hooks

You can intercept operations like Insert, Update or Delete on Panel. For example, you may want to check an external service 
before a new entry is added to database, or you may want to send data to an external service.

### Hook Creation

You can create a hook using the following command:

```shell script
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

!> We don't have an id yet when before_add operation is triggered.

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

!> You should use `error` function with before_ events, since the operation is not done when before_ events are triggered.

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

!> ***Caution:*** You cannot use this function inside of before_add since record is not created yet which means there is no id.

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

!> ***Caution:*** getOldData function gets data from Database when it's called. Since database is updated before calling after_ events, if you call this function in after function, it will not work properly and return the latest data. If you need old data in after_ events, then, you can call it in before function and set it to another property.

#### isChanged

When user saves data in Butterfly Panel, you may want to check if a specific field is changed or not.  

!> ***Caution:*** isChanged function returns if the field is changed or not. Since database is updated before calling after_ events, if you call this function in after function, it will not work properly and return the latest data. If you need old data in after_ events, then, you can call it in before function and set it to another property.

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