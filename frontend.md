# Frontend

Butterfly uses `twig` as the main frontend template engine. Although it's possible to use Smarty, we strongly recommend using 
`twig` since `smarty` support will be dropped in the upcoming releases.

## Twig Filters

### count

`count` filter returns number of elements in an array.

Example:

```twig
{% if array_variable|count > 1 %}
    this text will be shown if the array_variable has more then 1 elements. 
{% endif %}
``` 

### registry

`registry` filter is used to get a variable in the butterfly registry or set a variable to butterfly registry.

to get a variable:
```twig
{{ 'registry-key'|registry }}
```

to set a variable:
```twig
{{ 'registry-key'|registry('value') }}
```

### truncate

`truncate` filter is used to shorten strings. It returns the first X characters of the string. 

Example:
```twig
{{ 'Test String'|truncate(4) }}
```

will output

```text
Test
```

## Twig Functions

### image_path

`image_path` function is used to access the full path of image or file aliases.

```twig
image_path('original')
``` 

will return the full path to access original image alias.

### file_path

`file_path` function is used to access the full path of image or file aliases.

```twig
image_path('excel')
``` 

will return the full path to access excel file alias.

### widget

`widget` function is used to render a widget with given parameters.

Example:

```twig
{{ widget({name: 'Banner', 'title': 'Hello World'}) }}
``` 

to render admin widgets, you can set admin: true

```twig
{{ widget({name: 'FrontendAdmin', 'admin': true}) }}
```

### include_file

`include_file` function is used to include twig files. It automatically checks include directories to find the twig templates.
Default frontend folders are: `app/Views`, `app/Widgets`, `Core/View/Frontend`.

Following example will check for `app/Views/test.twig`, `app/Widget/test.twig' ... and if it finds the file, it will stop.

```twig
include_file('test.twig')
```

>[!TIP]
> If you want to extend Frontend Folders, you can use `$this->getView()->addViewPath('FOLDER_NAME');` from any controller. 

### current_url

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