# Migrations

Migrations make it easy to create new files like Controller, Model, Widget, Hook etc. You can use migrations by various make commands.

> [!TIP]
> You can reach list of migrations by running `bin/butterfly list make` command.

## Commands

Command | Description
--- | ---
controller | Generates new Controller
hook | Generates new Hook for creating hooks
model | Generates new Model
widget | Generates new Widget
content-widget | Generates new Content Listing Widget

### Controller 

Parameters:

Parameter Name | Description | Required
--- | --- | ---
controller | Controller Name | Yes
folder | Folder Name | No

```shell script
 bin/butterfly make:controller Detail Commerce/Product
```

```shell script
File created in "app/Controller/Commerce/Product/Detail.php";
```

```php
<?php

namespace App\Controller\Commerce\Product;

use Butterfly\Framework\Controller\Action;

class Detail extends Action
{
    public function indexAction() {

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

class Users extends Hook
{

}
```