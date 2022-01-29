# Tutorials

## How to Create an Articles Page

### Create Object Type

- Go to Objects page
- Click on Add New Record
- Fill out the form as follows

Name: Articles (User Friendly name of the Object Type)
Table Name: articles (Table name of the Object (lower case, no psecial characters))
SEO: article/%name% (which will automatically create links using the `name` field from article)
Menu: Main Menu (which will create a main level menu for the new Object Type)
Has Item: Checked
Design: (to be defined after creating new design) /* TODO: Add create new design button */

- Click save and it will redirect automatically to add new Object Spec Page.
- Fill out the form as follows to add a new field to Object Type:

Name: Name (User Friendly name of the field)
Type: string (It will be a text field)
Listed: Checked (To be listed in Listing Page)
Required: Checked
Searchable: Checked
Menu: Main Menu (to Create a link on Admin Panel)

- Click save and it will reload to add a new field.

- Now we have a table named `articles` in our database,
- We have an Admin Panel that we can search, add, edit or delete contents.

## Adding AMP (Accelerated Mobile Pages) Support to a Website

Accelerated Mobile Pages are lightweight version of a website that aims Mobile Pages to be cached on Google. You can get 
detailed information about AMP from Google's [AMP Website](https://amp.dev/)

Technically if you would like to add AMP Support for your website, you need to create AMP Versions of the pages. Most 
platforms suffers from managing content of these pages seperately which causes additional effort to maintain content of 
AMP Pages.

### Creating AMP Version of the Design:

First of all, you need to Create seperate Layout and Designs for AMP:

- Step 1 - Create Layout under app/Views/LayoutAmp.twig and Create Admin Record from /admin/cms_layout/add
- Step 2 - Create Design from (/admin/cms_design/add) and chose special layout you have created for AMP.
- Step 3 - Create new Widgets specialized for AMP using bin/butterfly make:widget or make:content-widget commands.
- Step 4 - Run `bin/butterfly widget:refresh` Command and add widgets to AMP Designs.

>[!TIP]
> You should repeat the previous steps for each Object Type you want to specialize for AMP.

Now you have special designs, widgets and a layout for AMP. We need to define a new URL Format that will render the same 
page as AMP.

We have two different way of defining the new page format:

### Strategy - 1

Butterfly Subpages feature helps you add multiple url's for a specific Content Item. To add AMP Support for a Content Type, 
you can follow these steps:

#### Step 1 - Create Object Subpage Record for the Object

- On Admin Panel, go to Object Subpages
- Choose Object to create AMP Version
- Enter amp/%seo% to create a new URL Format that will prepend amp/ to a URL.
- Choose AMP Version of the Design you have created in the [previous step](https://thebutterfly.io/docs/#/design?id=creating-amp-version-of-the-design)
- Save

Now, every time a new content (Item) is created, amp/*** version of the page which will be rendered for AMP will automatically created.

>[!WARNING]
> This strategy creates a record for each item in `item_subpages` table which means that if you have millions of records in a table,
> this will create same amount of record under this table.
> If you have more than 10.000 record in a table, we suggest second strategy.

#### Step 2 - Add a new URL Format and Design Prefix using Hooks

- Create Frontend / Bootstrap Hook to detect url's starting with amp/

Run `bin/butterfly make:event Frontend Bootstrap`

Update `app/Event/Frontend.php` file with the following:

```php
<?php

namespace App\Event;

use Butterfly\Framework\Registry\Registry;
use Butterfly\Library\Hook;

class Frontend extends Hook
{
    public function Bootstrap()
    {
        $url = Registry::get('url');

        if(substr($url, 0, 4) == 'amp/')
        {
            Registry::set('amp', true);
            Registry::set('url', substr($url, 4));
        }
    }
}
```

this code will remove `amp/` from URL and set amp -> true to Registry.

- Update `app/Controller/Item.php` as the following:

```php
<?php
namespace App\Controller;

use Butterfly\Framework\Registry\Registry;

class Item extends \Butterfly\Core\Controller\Frontend\Item
{
    public function getDetails()
    {
        if(Registry::get('amp'))
        {
            $this->designPrefix = 'amp-';
        }

        parent::getDetails();
    }
}
```

this code will set design prefix check if amp key in the registry is set to true.

Now you can create AMP versions of the Designs by adding `amp-` prefix to existing design aliases.

For example:
If your article page Design's alias is: `article-detail`, then you should set `amp-article-detail` as alias in the AMP 
Version.