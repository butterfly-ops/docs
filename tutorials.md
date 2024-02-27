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

### Creating AMP Version of the Design

First of all, you need to Create seperate Layout and Designs for AMP:

- Step 1 - Create Layout under app/Views/LayoutAmp.twig and Create Admin Record from /admin/cms_layout/add
- Step 2 - Create Design from (/admin/cms_design/add) and chose special layout you have created for AMP.
- Step 3 - Create new Widgets specialized for AMP using bin/butterfly make:widget or make:content-widget commands.
- Step 4 - Run `bin/butterfly widget:refresh` Command and add widgets to AMP Designs.

>[!TIP]
> You can use `info` variable to access content details in `Widgets`

>[!TIP]
> You should repeat the previous steps for each Object Type you want to specialize for AMP.

Now you have special designs, widgets and a layout for AMP. We need to define a new URL Format that will render the same 
page as AMP.

We have two different way of defining the new page format:

### Strategy - 1 - Using Object Subpages Feature

Butterfly Subpages feature helps you add multiple url's for a specific Content Item. To add AMP Support for a Content Type, 
you can follow these steps:

Now we will create Object Subpage Record for the Object:

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

### Strategy 2 - Add a new URL Format and Design Prefix using Hooks

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

## How to Integrate Login Mechanism to LDAP

### Step 1 - Install LDAP Extension

First of all, you need to install LDAP Extension to your server. You can install it using the following command:

```bash
sudo apt-get install php8.2-ldap
```

### Step 2 - Configure LDAP Settings

You need to configure LDAP Settings in your `app/Config/integration.php` file.

```php
<?php

$integrationConfig = [];

if (isset($_ENV['LDAP_SERVER'])) {
    $integrationConfig['ldap'] = [
        'adapter' => 'Ldap',
        'server' => $_ENV['LDAP_SERVER'],
        'base_dn' => $_ENV['LDAP_BASEDN'],
        'domain' => $_ENV['LDAP_DOMAIN']
    ];
}

return $integrationConfig;
```

```env
LDAP_SERVER=10.0.0.1
LDAP_BASEDN=DC=butterfly,DC=devops
LDAP_DOMAIN=butterfly.dev
```

### Step 3 - Create Login Mechanism

You need to create a new Login Mechanism to authenticate users using LDAP.

app/Event/AdminUser.php
```php
<?php

namespace App\Event;

use App\Library\Identity\Ldap;
use Butterfly\Library\Event;

class AdminUser extends Event
{
    public function before_login($params)
    {
        // LDAP
        $config = \Config::get('integration.ldap');
        if (empty($config)) {
            return;
        }

        $username = $params['email'];
        $password = $params['password'];

        $ldap = new Ldap();
        $response = $ldap->login($username, $password);

        if (! $response['success']) {
            return [];
            
            // Enable this code block if you want to restrict login to LDAP Users
//            return [
//                'success' => false,
//                'error_message' => 'Please enter your Company LDAP Credentials'
//            ];
        }

        $email = $response['email'];
        $phone = $response['phone'];

        $id = db()->table('users')->where('email', $email)
            ->one('id');

        if($id) {
            db()->table('users')
                ->where('id', $id)
                ->update([
                    'username' => $username,
                    'phone_number' => $phone
                ])
            ;

            // If you return a user_id; it will bypass username / password and log the user in. 
            return [
                'user_id' => $id
            ];
        } else {
            $tmp = explode('@', $email);

            // Insert as Image Uploader
            $id = db()->table('users')
                ->insert([
                    'name' => $tmp[0],
                    'username' => $username,
                    'email' => $email,
                    'password' => 'LoggedInUsingLDAP',
                    'status' => 2,
                    'role_id' => 10,
                    'phone_number' => $phone
                ])
            ;

            // If you return a user_id; it will bypass username / password and log the user in.
            return [
                'user_id' => $id
            ];

            // Send E-mail to responsibles
        }
    }
}
```

### Step 4 - Create Ldap Library

app/Library/Identity/Ldap.php
```php
<?php
namespace App\Library\Identity;

class Ldap
{
    public function login($username, $password)
    {
        $config = \Config::get('integration.ldap');
        if(empty($config))
        {
            return [
                'success' => false
            ];
        }

        $ldap = ldap_connect("ldap://{$config['server']}");

        ldap_set_option($ldap, LDAP_OPT_PROTOCOL_VERSION, 3);
        ldap_set_option($ldap, LDAP_OPT_REFERRALS, 0);
        ldap_set_option(null, LDAP_OPT_X_TLS_REQUIRE_CERT, 0);

        @ldap_start_tls($ldap);

        if(! @ldap_bind($ldap, "{$username}@{$config['domain']}", $password))
        {
            return [
                'success' => false
            ];
        }

        $attributes = array('mail', 'mobile');
        $result = @ldap_search($ldap, $config['base_dn'], "(samaccountname={$username})", $attributes);

        if ($result === false) {
            return [
                'success' => false
            ];
        }

        $entries = @ldap_get_entries($ldap, $result);
        if ($entries['count'] > 0) {
            return [
                'success' => true,
                'email' => $entries[0]['mail'][0],
                'phone' => $entries[0]['mobile'][0]
            ];
        } else {
            return [
                'success' => false
            ];
        }
    }
}
```
