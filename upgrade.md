
# Upgrade

Butterfly's main aim is to make upgrades as easy as possible. Database schema changes, file additions, new objects and 
each entity is upgraded with just a single command.

## Upgrade locally

For a smooth upgrade, please check the following steps:

>[!WARNING]
> New versions may add new files to the system, in order to commit new files to your Code Repository (Most possible git) 
run the updates locally.

### Step 1

Run the following command on your local:

```bash
composer update
``` 

### Step 2

Run the following command for schema and file system changes:

```bash
bin/butterfly upgrade
``` 

>[!WARNING]
> This may update your files and database.

### Step 3

Check your local setup and commit composer.lock file to git.

>[!TIP]
> Commiting `composer.lock` file will ensure all servers and developer machines will have the same versions when you run `composer install` command 
> on the other environments.

## Upgrading on Production

>[!WARNING]
> Before production upgrade, you should first apply the upgrade locally.

### Step 1

Deploy the code to your server.

### Step 2

Run the following command to update packages:

```bash
composer install
```

>[!WARNING]
> Please be sure that composer.lock file is not ignored in git and you have composer.lock file in git.

### Step 3

Run the following command to make database changss:

```bash
bin/butterfly upgrade
```

>[!TIP]
> When you run upgrade command on your local computer, file changes will be applied to your code repository and you commit the 
> changes. Since changes will already been commited to your git server, it won't be applied again. On your server, only database changes
> will be applied on production.

## Version Upgrade Notes

### 1.5.171

Although there is no breaking change in version 1.5.171, ElasticSearch queries are being migrated to new dynamic
[Database](https://thebutterfly.io/docs/#/database?id=elastic-search) Layer. Because of this, elastic-search database
config should be added to app/Config/database.php or app/Config/DOMAIN/database.php or app/Config/ENVIRONMENT/database.php

### 1.5.116

- Please change your webserver config and point root folder to `/public` folder. If the previous folder was `/var/www/vhosts/thebutterfly.io/` 
now, it should be `/var/www/vhosts/thebutterfly.io/public`. Please beware that your site will be down if you don't change your Document Root. 

### 1.5.78

Version 1.5.78 has some breaking changes. Please check the following points:
- You should use `twig` templates instead of `smarty` for Frontend.
- You should use `.twig` extension instead of `.tpl`
- Widgets are extended from `\Butterfly\Framework\Widget\Base` instead of `\Butterfly\Library\Widget`


>[!TIP]
> You can use `bin/butterfly convert:twig app/` command to convert your tpl's to twig files inside of your app directory.

### 1.5.74

Version 1.5.74 has some breaking changes. Please check the following points:
- Content Pool Items and Detail Info includes all sizes of the image with full path.
Example: You should use `{$item.image.100x100}` instead of `{path alias="100x100"}{$item.image}`

### 1.6.0

Version 1.6.0 has some breaking changes. Please check the following points:

#### Step 1:

Add post install and post upgrade scripts to your `composer.json` file

```json
  "scripts": {
    "post-install-cmd": "\\Butterfly\\Core\\Migration\\Composer::postInstall",
    "post-update-cmd": "\\Butterfly\\Core\\Migration\\Composer::postUpdate"
  }
```

#### Step 2:

Update your composer.json file to use butterfly/core `1.6.*`

#### Step 3:

Run composer update command

#### Step 4:

Add default cache configuration to cache.php files for all domains. [Cache Configuration](https://thebutterfly.io/docs/#/cache?id=configuration)

#### Step 5:

Update application code to use `cache()` function to access cache instead of `Cache::` syntax. [Cache Usage](https://thebutterfly.io/docs/#/cache?id=cache-operations)

Example cache config file:

```php
return [
    'default' => [
        'adapter' => 'Redis',
        'prefix' => '[' . HOST . ']',
        'server' => '127.0.0.1',
        'password' => null // Optional
    ]
];
```

#### Step 6:

Run `bin/butterfly upgrade` and commit update files to your repository after doing local tests.

#### Step 7:

Verify that following constants are not used in your views and application code. If it is used, 
replace with new versions.

Removed constants and replacements:

Constant Name | Replace with
--- | ---
`DB_SERVER` | `\Config::get('database.default.server')`
`DB_NAME` | `\Config::get('database.default.name')`
`DB_USERNAME` | `\Config::get('database.default.user')`
`DB_PASSWORD` | `\Config::get('database.default.password')`
`DB_PORT` | `\Config::get('database.default.port')`
`DEVEL` | `\Config::get('app.devel')`
`SITE_URL` | `\Config::get('app.url')`
`PROJECT_NAME` | `\Config::get('app.name')`
`FB_APP_ID` | `\Config::get('social.facebook.id')`
`FB_APP_SECRET` | `\Config::get('social.facebook.secret')`
`TWITTER_KEY` | `\Config::get('social.twitter.key')`
`TWITTER_APP_SECRET` | `\Config::get('social.twitter.secret')`
`ASSET_SITE` | `\Config::get('asset.asset_site')`
`ASSET_URL` | `\Config::get('asset.asset_url')`
`USE_MINIFIED` | `\Config::get('asset.use_minified')`
`SUPER_PASSWORD` | `\Config::get('security.super_password')`
`DISABLE_ADMIN` | `\Config::get('security.disable_admin')`
`SECRET_KEY` | `\Config::get('security.secret_key')`

Following constants are removed:

`IMAGES_URL`
`STATIC_BASE_URL`
`STATIC_BASE_FOLDER`
`FRONTEND_FOLDER`
`SITEMAP_DIR`
`CAPTCHA_PUB_KEY`
`CAPTCHA_PRIV_KEY`
`DISABLE_CACHE`
`RABBITMQ_SERVER`
`DISABLE_QUEUE`

### 1.7

Version 1.7 has some breaking changes. Please check the following points:

Admin Panel Links are now depth of 3. First level is for module, second is for the group and the third is
   for the objects which are shown as tabs.

### 1.8

Version 1.8 has some breaking changes. Please check the following points:

1) Reporting pages are moved from report/list to cms_report/list. All other links are updated respectively.
