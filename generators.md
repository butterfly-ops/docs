# Generators

Generators make it easy to create new files like Controller, Model, Widget, Hook etc. You can use generators by various make commands.

> [!TIP]
> You can reach list of generators by running `bin/butterfly list make` command.

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

### Model 

Parameters:

Parameter Name | Description | Required
--- | --- | ---
model | Model Name | Yes
folder | Folder Name | No

```shell script
 bin/butterfly make:model Detail Commerce/Product
```

```shell script
File created in "app/Model/Commerce/Product/Detail.php";
```

```php
<?php

namespace App\Model\Commerce\Product;

use Butterfly\Library\Model;

class Detail extends Model
{
    public $_name = "Detail";
}
```

### Hook 

Parameters:

Parameter Name | Description | Required
--- | --- | ---
hook | Hook Name | Yes

```shell script
 bin/butterfly make:hook User
```

```shell script
File created in "app/Hook/User.php";
```
```php
<?php

namespace App\Hook;

use Butterfly\Library\Hook;

class User extends Hook
{

}
```

### Widget 

Parameters:

Parameter Name | Description | Required
--- | --- | ---
widget | Widget Name | Yes
folder | Fodler Name | No

```shell script
 bin/butterfly make:widget basket product (optional folder)
```

```shell script
File successfully created in 'app/Widget/product/basket/basket.php'
File successfully created in 'app/Widget/product/basket/basket.tpl'
File successfully created in 'app/Widget/product/basket/parameters.yaml'

```
```php
<?php
namespace App\Widget\product\basket;

class basket extends \Butterfly\Library\Widget
{
    protected $_friendly_name = "Basket";

    public function init() {
        return $this->render();
    }
}
```

### Content Widget 

Parameters:

Parameter Name | Description | Required
--- | --- | ---
widget | Widget Name | Yes
folder | Fodler Name | No

```shell script
 bin/butterfly make:content-widget basket product (optional folder)
```

```shell script
File successfully created in 'app/Widget/product/basket/basket.php'
File successfully created in 'app/Widget/product/basket/basket.tpl'
File successfully created in 'app/Widget/product/basket/parameters.yaml'

```
```php
<?php
namespace App\Widget\product\basket;

class basket extends \Butterfly\Library\Widget
{
    protected $_friendly_name = "Basket";

    public function init() {
        return $this->render();
    }
}
```
```yaml
content_pool_id:
    name: 'Content Pool'
    column_name: content_pool_id
    type: content_pool
```