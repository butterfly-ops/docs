# Frontend

Butterfly uses `twig` as the main frontend template engine. Although it's possible to use Smarty, we strongly recommend using 
`twig` since `smarty` support will be dropped in the upcoming releases.

## Layout

Butterfly displays pages using [Designs](https://thebutterfly.io/docs/#/design). When you define a Design, you need to create a Layout and choose 
Layout file from butterfly Admin.

While creating a Layout, you can use the following predefined variables:

Variable | Variable Type | Description
--- | --- | ---
page_title | string | Includes the Page Title rendered from settings defined on Cms Design
page_description | string | Includes the Page Description rendered from settings defined on Cms Design
widgets | array | Includes the widget renders. Detailed example below.

### `widgets`

```twig
{% for render in widgets.content.renders %}
    {{ render|raw }}
{% endfor %}
```
 

## Twig Filters

### `count`

`count` filter returns number of elements in an array.

Example:

```twig
{% if array_variable|count > 1 %}
    this text will be shown if the array_variable has more then 1 elements. 
{% endif %}
``` 

### `registry`

`registry` filter is used to get a variable in the butterfly registry or set a variable to butterfly registry.

to get a variable:
```twig
{{ 'registry-key'|registry }}
```

to set a variable:
```twig
{{ 'registry-key'|registry('value') }}
```

### `truncate`

`truncate` filter is used to shorten strings. It returns the first X characters of the string. 

Example:
```twig
{{ 'Test String'|truncate(4) }}
```

will output

```text
Test
```

### `json_decode`

Twig doesn't come with a `json_decode` filter by default. You can use `json_decode` filter to return json encoded string to array.

>[!TIP]
>
> `json_decode` filter converts to array by default (calls the following function: json_decode('JSON_STRING', true);

### `parse`

`parse` filter is used to process strings and replaces dynamic values into strings. This filter is used to process dynamic strings specially entered from Admin Panel. 
For example: In Item Detail page, you can enter string `%name%` from admin, and parse filter will replace `%name%` to name value of the array.

Example:

```twig
{{ "%name% %title%"|parse(info) }}
```

will replace values between `%` from info variable. For example if the column name is name, then, it will search for info.name and replace %name% with info.name

### `config`

`config` filter is used to return specific config set in `app/Config` directory.

Example:

```twig
{{ 'app.url'|config }}
```

will return the url of the butterfly setup, which is set in `app/Config/app.php` with key: `url`.

>[!TIP]
> You can retrieve inner keys of the config. Example: `app.testkey.innerkey` will return the `testkey->innerkey`
> inside `app/Config/app.php`  

## Twig Functions

### `image_path`

`image_path` function is used to access the full path of image or file aliases.

```twig
image_path('original')
``` 

will return the full path to access original image alias.

### `file_path`

`file_path` function is used to access the full path of image or file aliases.

```twig
file_path('excel')
``` 

will return the full path to access excel file alias.

### `widget`

`widget` function is used to render a widget with given parameters.

Example:

```twig
{{ widget({name: 'Banner', 'title': 'Hello World'}) }}
``` 

to render admin widgets, you can set admin: true

```twig
{{ widget({name: 'FrontendAdmin', 'admin': true}) }}
```

### `image`

`image` function is used to generate an img tag with support of Lazy Loading and Webp.

Example:

```twig
image({item:item,alias:"content",field:"field_name", "class":"test"})
```

will return

```html
<img class="test" src="https://xxx.com/test.png.webp" />
```

if browser doesn't support webp or if webp not enabled for that image it will return:

```html
<img class="test" src="https://xxx.com/test.png" />
```

It has the following parameters:

Parameter | Description | Default | Required
--- | --- | --- | ---
`item` | Variable including all item data | - | Yes
`alias` | Image Config Alias | `content` | No
`field` | Image Field Name | `image` | No
`class` | Class Name | - | No

### `image_source`

`image_source` function returns just the image url based on `webp` and other configurations.

It has the following parameters:

Parameter | Description | Default | Required
--- | --- | --- | ---
`item` | Variable including all item data | - | Yes
`alias` | Image Config Alias | `content` | No
`field` | Image Field Name | `image` | No

will return

```html
https://xxx.com/test.png.webp
```

if browser doesn't support webp or if webp not enabled for that image it will return:

```html
https://xxx.com/test.png
```

### `include_file`

`include_file` function is used to include twig files. It automatically checks include directories to find the twig templates.
Default frontend folders are: `app/Views`, `app/Widgets`, `Core/View/Frontend`.

Following example will check for `app/Views/test.twig`, `app/Widget/test.twig' ... and if it finds the file, it will stop.

```twig
include_file('test.twig')
```

>[!TIP]
> If you want to extend Frontend Folders, you can use `$this->getView()->addViewPath('FOLDER_NAME');` from any controller. 

### `current_url`

`current_url` function returns the contents of `$_SERVER['REQUEST_URI']` [Details](https://www.php.net/manual/tr/reserved.variables.server.php)

Example:

When active page is thebutterfly.io/test.html

```twig
{{ current_url() }}
```

will return

```text
/test.html
```

### `setting`

`setting` function is used to return specific setting defined in Admin Panel. 

Example:

```twig
{{ setting('site-settings', 'description') }}
```

will return the Setting with alias `description` defined in Setting Group with alias: `site-settings`

### `git_version`

`git_version` returns hash of current git version for invalidating asset caches etc.

You may use git_version function after static files to invalidate browser, cdn or output caches.

Example usage:
```twig
<script src="/assets/test.js?v={{ git_version() }}"></script>
```  

>[!TIP]
> In production, we recommend removing .git folder. This function checks for .git-version file in the root directory. Which means that, 
> you may put a textfile including your git version or timestamp which will change in each release.
> If your webserver root folder is `/var/www/vhosts/thebutterfly.io/public/` you can dump current git version to `/var/www/vhosts/thebutterfly.io/.git-version`.
> This file won't be publicly accessible but `git_version()` function will read this file priorly.  