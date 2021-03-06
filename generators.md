# Generators

Generators make it easy to create new files like Controller, Model, Widget, Hook etc. You can use generators by various make commands.

> [!TIP]
> You can reach list of generators by running `bin/butterfly list make` command.

Command | Description
--- | ---
controller | Generates new Controller
hook | Generates new Hook for creating hooks
model | Generates new Model
widget | Generates new Widget
content-widget | Generates new Content Listing Widget

## Controller 

Parameters:

Parameter Name | Description | Required
--- | --- | ---
controller | Controller Name | Yes
folder | Folder Name | No

```bash
 bin/butterfly make:controller Detail Commerce/Product
```

```bash
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

## Command 

Parameters:

Parameter Name | Description | Required
--- | --- | ---
class | Class Name | Yes

Parameter Name | Description | Required
--- | --- | ---
name | Function Name | Yes

Parameter Name | Description | Required
--- | --- | ---
description | Description | No (Optional)

```bash
 bin/butterfly make:command User user:login:update 'User login update'
```

```bash
File created in "app/Command/User.php";
```
```php
<?php
namespace App\Command;

use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;

class User extends Command
{
    public function configure()
    {
        $this->setName("user:login:update")->setDescription("User login update");
        parent::configure();
    }

    public function execute(InputInterface $input, OutputInterface $output)
    {
    }
}
```

## `twig-filter`

Parameters:

Parameter Name | Description | Required
--- | --- | ---
name | Filter Name | Yes

```bash
bin/butterfly make:twig:filter test_filter
```

```bash
Filter created in "app/View/TwigFilter/TestFilter.php
```

```php
<?php

namespace App\View\TwigFilter;

class TestFilter
{
    public function filter($parameter)
    {
        return $parameter;
    }
}
```

## `twig-function`

Parameters:

Parameter Name | Description | Required
--- | --- | ---
name | Function Name | Yes

```bash
bin/butterfly make:twig:function test_function
```

```bash
Filter created in "app/View/TwigFunction/TestFunction.php
```

```php
<?php

namespace App\View\TwigFunction;

class TestFunction
{
    public function execute($params)
    {

        return print_r($params, true);
    }
}
```

## Model 

Parameters:

Parameter Name | Description | Required
--- | --- | ---
model | Model Name | Yes
folder | Folder Name | No

```bash
 bin/butterfly make:model Detail Commerce/Product
```

```bash
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

## Hook 

Parameters:

Parameter Name | Description | Required
--- | --- | ---
hook | Hook Name | Yes

```bash
 bin/butterfly make:hook User
```

```bash
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


## Event

Parameters:

Parameter Name | Description | Required
--- | --- | ---
class | Class Name | Yes

Parameter Name | Description | Required
--- | --- | ---
func | Function Name | Yes

```bash
 bin/butterfly make:event User login
```

```bash
File created in "app/Event/User.php";
```
```php
<?php

namespace App\Event;

use Butterfly\Library\Hook;

class User extends Hook
{
    public function login()
    {
    
    }
}
```

## Widget 

Parameters:

Parameter Name | Description | Required
--- | --- | ---
widget | Widget Name | Yes
folder | Folder Name | No


### Without Folder

If you are creating a general widget, which you need it directly in `app/Widget/`, you can use command without a folder.

Example: 

```bash
bin/butterfly make:widget Product
```

```bash
File successfully created in app/Widget/Product/Product.php
File successfully created in app/Widget/Product/Product.tpl
File successfully created in app/Widget/Product/parameters.yaml

```

Php file:
```php
<?php
namespace App\Widget\Product;

class Product extends \Butterfly\Library\Widget
{
    protected $_friendly_name = "Product";

    public function init() {

        return $this->render();
    }
}
```
### With Sub Folders

If you want to group your widgets, you can use second parameter to create your widget in a sub folder. Sub folder will be located in `app/Widget/`, you can use deeper folders.

Example: 

```bash
bin/butterfly make:content-widget ProductDetail General/Products
```

```bash
File successfully created in app/Widget/General/Products/ProductDetail/ProductDetail.php
File successfully created in app/Widget/General/Products/ProductDetail/ProductDetail.tpl
File successfully created in app/Widget/General/Products/ProductDetail/parameters.yaml
```

Php file:
```php
<?php
namespace App\Widget\General\Products\ProductDetail;

class ProductDetail extends \Butterfly\Library\Widget
{
    protected $_friendly_name = "Product Detail";

    public function init() {

        return $this->render();
    }
}
```

## Content Widget 

Parameters:

Parameter Name | Description | Required
--- | --- | ---
widget | Widget Name | Yes
folder | Folder Name | No

Content Widget is a type of Widget which aims to display your contents. Content Widgets accepts Content Pool parameter to 
determine data that will be displayed.

Content Pools make it easy to make your display layer content agnostic. Which means that, you can change the data to be displayed without changing your code.

You can get more details from Content Pools Section.

### Without Folder

If you are creating a general widget, which you need it directly in `app/Widget/`, you can use command without a folder.

Example: 

```bash
bin/butterfly make:content-widget Product
```

```bash
File successfully created in app/Widget/Product/Product.php
File successfully created in app/Widget/Product/Product.tpl
File successfully created in app/Widget/Product/parameters.yaml

```

Php file:
```php
<?php
namespace App\Widget\Product;

class Product extends \Butterfly\Framework\Widget\ContentPool
{
    protected $_friendly_name = "Product";
    protected $content_pools = ['content_pool_id'];

    public function init() {
        parent::init();

        return $this->render();
    }
}
```

Template file:
```smarty
<ul>
{foreach $contents.content_pool_id.item as $item}
    <li>
        <a href="/{$item.seo}" title="{$item.label} - {$item.title}">
            {$item.label}
        </a>
    </li>
{/foreach}
</ul>
```

Yaml file:
```yaml
content_pool_id:
    name: 'Content Pool'
    column_name: content_pool_id
    type: content_pool
```

### With Sub folders

If you want to group your widgets, you can use second parameter to create your widget in sub folder. Sub folder will be located in `app/Widget/`, you can use deeper folders.

Example: 

```bash
bin/butterfly make:content-widget ProductDetail General/Products
```

```bash
File successfully created in app/Widget/General/Products/ProductDetail/ProductDetail.php
File successfully created in app/Widget/General/Products/ProductDetail/ProductDetail.tpl
File successfully created in app/Widget/General/Products/ProductDetail/parameters.yaml
```

Php file:
```php
<?php
namespace App\Widget\General\Products\ProductDetail;

class ProductDetail extends \Butterfly\Framework\Widget\ContentPool
{
    protected $_friendly_name = "Product Detail";
    protected $content_pools = ['content_pool_id'];

    public function init() {
        parent::init();

        return $this->render();
    }
}
```

Template file:
```smarty
<ul>
{foreach $contents.content_pool_id.item as $item}
    <li>
        <a href="/{$item.seo}" title="{$item.label} - {$item.title}">
            {$item.label}
        </a>
    </li>
{/foreach}
</ul>
```

Yaml file:
```yaml
content_pool_id:
    name: 'Content Pool'
    column_name: content_pool_id
    type: content_pool
```