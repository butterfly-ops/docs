# Admin Panel

One of the most important features of Butterfly is it's Admin Panel. 
- You can create new Objects,
- Create / Update Object Fields
- Create / Edit your Content Sources,
- Create / Edit your API's,
- Manage your Content
- Manage Search Engine Settings,
- Change Look & Feel of your Applications
- Drag & Drop new Widgets to your Applications

and many more ...    

## Layout

Admin Panel layout is the generic layout which includes all container information. You can customize admin panel layout 
publishing admin panel layout to `app/Views/Cms/layout.tpl` file path.

Run the following command to publish admin template:

```bash
bin/butterfly publish:admin:layout
```

Blank template will look like the following code.

```smarty
{include_tpl file="admin_layout"}
```

Congrats! You now have an admin layout file, works as is but now, you can make customizations.

> [!WARNING]
> This command will not overwrite file in `app/Views/Cms/layout.tpl`. It fails and displays the following error and stops.
> 
> `File already exists, operation is canceled /Users/ozanakcora/Sites/butterfly-app/app/Views/Cms/layout.tpl
   You can check file content
   File should contain the following content:
   {include_tpl file="admin_layout"}
` 

## Objects

Every created object comes with special management screens. You can list, add, edit, 
from it's auto-generated admin panel. You can even bulk edit, import or export your data. Besides having many unique features, 
Management Screens can be customized easily.

### Customizations

Let's think that you have an Object named: `Articles`. Fields in Users object are: `title`, `introduction` and `content`. Admin panel link
of this page will be: `/admin/article/list`.

#### Controller

You can extend behaviour of a Object Controller. In order to extend, you can run the following command to publish Cms Controller.

##### List / Add / Edit Actions

```bash
bin/butterfly publish:admin:controller articles
```

will create a file named `Article.php` under `app/Controller/Cms` directory with the following content:

```php
<?php

namespace App\Controller\Cms;

use Butterfly\Library\ObjectController;

class Article extends ObjectController
{
    public function addAction($id = "", $extra = "")
    {
        parent::addAction($id, $extra);
    }

    public function editAction($id, $extra = '')
    {
        parent::editAction($id, $extra);
    }

    public function listAction($id, $extra)
    {
        parent::listAction($id, $extra);
    }
}
```

Now you can update behaviours of the page by updating each function or you can add a new action to the current Controller.

##### Limit Per Page Options

By default, butterfly has the following options for limit per page on admin panel: `20, 100, 250, 1000`. Sometimes, you may need to 
change this options. You can do the following steps to change limit per page options:

1) Run `bin/butterfly publish:admin:controller` command to publish the controller if it is not already.

Example:

```bash
bin/butterfly publish:admin:controller articles
```

2) Add `$_limit_per_page` and `$_page_limit_options` parameters to published class.

Example:

```php
<?php

namespace App\Controller\Cms;

use Butterfly\Library\ObjectController;

class Article extends ObjectController
{
    protected $_limit_per_page = 5;
    protected $_page_limit_options = [5, 10, 100];
}
```

# Custom Checkbox

However Butterfly automatically creates filters on Admin Panel, sometimes you may need additional logical checkboxes.

For example:
You may want to filter Stocks lower than 5 as Critical Stock when Critical Stock checkbox is selected.

You can use addFilter function to add customized filters to your Listing Page.

First you need to publish Controller for that Data Type.

Example:
```bash
bin/butterfly publish:admin:controller articles
```

Example:
```php
function listAction($id, $extra)
{
    $this->addFilter('checkbox', 'Get Valid Records', [
        'join' => [
            'INNER JOIN child_object_tests ON child_object_tests.article_id = articles.id'
        ],
        'where' => 'child_object_tests.is_valid = 1'
    ]);

    parent::listAction($id, $extra);
}
```


#### Listing Page

##### Full Layout

If you want to customize listing page, you can create a file called `list.tpl` as `app/Views/Cms/article/list.tpl`

> [!TIP]
> You can use `bin/butterfly publish:admin:template articles list` command to generate customization template.

When you create an empty file, you can see that, listing page will also change to a blank page. If you want your custom 
page to work just like it was, you can place the following code to your template file.

```twig
{{ include_file("Data/List") }}
```

Now, you have a listing page, just working as it was but now, you can add new code blocks to top or bottom of the page.

##### Action Buttons

You can add a new button to listing page for row specific actions. New button will be added to left or right of the default buttons.

Add Action button to left:

```smarty
{$action_buttons.left[] = '<a href="/admin/order/list?customer_id=<id>" title="" class="btn14 mr5 topDir" original-title="Customer Orders"><img src="/assets/core/admin/images/icons/dark/cart.png" alt=""></a>'}
```

Add Action button to right:

```smarty
{$action_buttons.right[] = '<a href="/admin/order/list?customer_id=<id>" title="" class="btn14 mr5 topDir" original-title="Customer Orders"><img src="/assets/core/admin/images/icons/dark/cart.png" alt=""></a>'}
```

> [!TIP]
> As you see in the examples above, you can reach columns by using `<field_name>` syntax. `<id>` will be translated into `id` of the row.  


You can also hide default action buttons if you would like to add them manually.

Example template for hiding default action buttons (View / Edit / Delete)

```twig
{{ include_file("Data/List", {
    hide_action_buttons: true
}) }}
```

> [!WARNING]
> hide_action_buttons parameter doesn't revoke user permissions. It just removes buttons from admin panel visually. If you want 
> to limit access for user, please check [permissions](https://thebutterfly.io/docs/#/object?id=permissions) page.

##### Field Based

You may want to change look & feel or functionality of a specific Object Field.

> [!TIP]
> You can use `bin/butterfly publish:admin:template articles list title` command to generate customization template for specific field.

Example:

If you want to change look & feel of `title` column of `articles` object, then you can create a file in `app/Views/Cms/Article/List/Title.twig`

When you create an empty template, you can see that the field will be empty in listing page. You have a variable named `$l` in the template.

If you want to display of your field you can use the following code:

```twig
{{ record[field.column_name] }}
```

or, you can use the field name instead

```twig
{{ record.title }}
```

##### Hiearchical Lists

When you have an object with Self Child > Parent relationship, you may want to display main records in the first page with a button.
For example: You may have an object of multiple depth category having a column named `parent_id` which means that, Main records will 
have parent_id = `0` and others will have the `id` of the parent record.

By default, all records including parent and child ones will be listed together.

Apply following steps to make admin panel hiearchical:

Let's think that, you have object with table name: `categories` and `parent_id` hiearchical column.

```bash
bin/butterfly publish:admin:controller categories
```

will create (if not exists)

```bash
app/Controller/Cms/Category.php
```

Add `$list_hierarchy_column_name` variable to the class

```php
<?php

namespace App\Controller\Cms;

use Butterfly\Library\ObjectController;

class Category extends ObjectController
{
    public $list_hierarchy_column_name = 'parent_id';

    public function addAction($id = "", $extra = "")
    {
        parent::addAction($id, $extra);
    }

    public function editAction($id, $extra = '')
    {
        parent::editAction($id, $extra);
    }

    public function listAction($id, $extra)
    {
        parent::listAction($id, $extra);
    }
}
```

#### Add Page

If you want to customize add page, you can create a file called Add.twig as `app/Views/Cms/Article/Add.twig`

When you create an empty file, you can see that, add form page will also change to a blank page. If you want your custom 
page to work just like it was, you can place the following code to your template file.

```twig
{{ include_file('Data/Add') }}
``` 

Now, you have a add form page, just working as it was but now, you can add new code blocks to top or bottom of the page.

> [!TIP]
> You can use `bin/butterfly publish:admin:template articles add` command to generate customization template.

#### Edit Page

If you want to customize add page, you can create a file called edit.tpl as `app/Views/Cms/Article/Edit.twig`

When you create an empty file, you can see that, edit form page will also change to a blank page. If you want your custom 
page to work just like it was, you can place the following code to your template file.

```twig
{{ include_tpl("Data/Edit") }}
``` 

Now, you have a edit form page, just working as it was but now, you can add new code blocks to top or bottom of the page.

> [!TIP]
> You can use `bin/butterfly publish:admin:template articles edit` command to generate customization template.

#### Behaviour Customisation with Javascript

Butterfly makes it easy to input data for most cases but you may want to extend behaviours independently. You can do this by editing
JS Code of the element.

There are some special keywords to reach current element's DOM.

keyword | description | example
--- | --- | ---
%element% | will reach the element in jQuery syntax | `%element%` will be replaced by `$('#button_type4')` if the column_name is button_type and the element is the 4th element in that page.
%id% | will reach the id of the current element | `%id%` will be replaced by ``button_type4` if the column_name is button_type and the element is the 4th element in that page
%container% | will reach the container of the element in jQuery syntax | `%container%' will be replaced by `$('#button_type4').parent().parent()` if the column_name is button_type and the element is the 4th element in that page.

**Example Usages:**

```javascript
var value = %element%.val();
alert(value);
```

will alert the value of the current element.

##### Conditional Show/Hide

When you need to show / hide other elements based on value of an Object Spec's value, you can use Conditional Show/Hide helper.
`.condition` function is used for this purpose.

**Example Usage:**

```javascript
%element%.condition({
    "FirstValue": ["image", "title", "label"],
    "SecondValue": ["image"],
    "ThirdValue": ["subtitle"] 
});
```

will hide Object Specs with column name: `image`, `title`, `label`, `subtitle` and will show the Object Specs based on the 
value of the current Object Spec. For example: if the value is `ThirdValue` it will show Object Spec with column name: `subtitle`.