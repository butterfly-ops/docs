# Migrations

## Introduction

Butterfly is extensible. You can extend system by using Migrations.

## Migrations of Butterfly

Controller  => make:controller
Model       => make:model
Hook        => make:hook


### Butterfly - Make Controller 

Example Controller Create

User -- Controller (Required)
User/Auth -- Folder (Optional)

```shell script
 bin/butterfly make:controller User User/Auth
```
- Output
File created this path "/app/Controller/User/Auth/User.php";

```php
<?php

namespace App\Controller\User\Auth;

use Butterfly\Framework\Controller\Action;

class User extends Action
{
    public function UserAction() {

    }
}
```
### Butterfly - Make Model 

Example Model Create

User -- Model (Required)
User/Auth -- Folder (Optional)

```shell script
 bin/butterfly make:model User User/Auth
```
- Output
File created this path "/app/Model/User/Auth/User.php";

```php
<?php

namespace App\Model\User\Auth;

use Butterfly\Library\Model;

class User extends Model
{
    public $_name = "User";
}
```
### Butterfly - Make Hook 

Example Hook Create

User -- Hook (Required)

```shell script
 bin/butterfly make:hook Users
```
- Output
File created this path "/app/Hook/Users.php";

```php
<?php

namespace App\Hook;

use Butterfly\Library\Hook;

class User extends Hook
{

}
```