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

#### Listing Page

##### Full Layout

If you want to customize listing page, you can create a file called `list.tpl` as `app/Views/Cms/article/list.tpl`

> [!TIP]
> You can use `bin/butterfly publish:admin:template articles list` command to generate customization template.

When you create an empty file, you can see that, listing page will also change to a blank page. If you want your custom 
page to work just like it was, you can place the following code to your template file.

```smarty
{include_tpl file="object/list"}
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

```smarty
{$hide_action_buttons = true}

{include_tpl file="object/list"}
```

> [!WARNING]
> hide_action_buttons parameter doesn't revoke user permissions. It just removes buttons from admin panel visually. If you want 
> to limit access for user, please check [permissions](https://thebutterfly.io/docs/#/object?id=permissions) page.

##### Field Based

You may want to change look & feel or functionality of a specific Object Field.

> [!TIP]
> You can use `bin/butterfly publish:admin:template articles list title` command to generate customization template for specific field.

Example:

If you want to change look & feel of `title` column of `articles` object, then you can create a file in `app/Views/Cms/article/list/title.tpl`

When you create an empty template, you can see that the field will be empty in listing page. You have a variable named `$l` in the template.

If you want to display of your field you can use the following code:

```smarty
{$l[$os.column_name]}
```

or, you can use the field name instead

```smarty
{$l.title}
```

#### Add Page

If you want to customize add page, you can create a file called add.tpl as `app/Views/Cms/article/add.tpl`

When you create an empty file, you can see that, add form page will also change to a blank page. If you want your custom 
page to work just like it was, you can place the following code to your template file.

```smarty
{include_tpl file="object/add"}
``` 

Now, you have a add form page, just working as it was but now, you can add new code blocks to top or bottom of the page.

> [!TIP]
> You can use `bin/butterfly publish:admin:template articles add` command to generate customization template.

#### Edit Page

If you want to customize add page, you can create a file called edit.tpl as `app/Views/Cms/article/edit.tpl`

When you create an empty file, you can see that, edit form page will also change to a blank page. If you want your custom 
page to work just like it was, you can place the following code to your template file.

```smarty
{include_tpl file="object/edit"}
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

When you need to show / hide other elements based on value of an Object Spec, you can use Conditional Show/Hide helper.
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
value of the current Object Spec. For example: if the value is equal to `ThirdValue` it will show Object Spec with column name: `subtitle`.