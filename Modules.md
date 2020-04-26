# Modules

## Introduction

Butterfly is extensible. You can extend system by using Modules.

!> ***Caution:*** Purpose of Modules is make reusable code. Which means that, if your code is project specific, you can just keep it
 in project repository within app directory. If you are developing a new feature that can be used in other projects, than you can develop it as a Module.

## Modules of Butterfly

Butterfly has 3 Modules out of box:

### Butterfly\Core:

Butterfly Core module handles admin panel operations. It has API access for all operations.

### Butterfly\Framework

Butterfly Framework module has Base Classes for integrations like Database, Cache, Search etc.

### Butterfly\Library

Butterfly Framework module has utility classes and functions like StringHelper, Utils. This is a legacy which will merge into Butterfly\Framework Module.    

## Module Structure

Every module has the following pieces:

- module.yaml

Example yaml file content as follows: 

```yaml
name: 'Butterfly Framework Module'
namespace: 'Butterfly\Framework'
version: '1.0.0'
```

- VendorName\ModuleName\Module class: This is an empty class extended from `Butterfly\Framework\Module\Base`

Example file:

```php
<?php


namespace Butterfly\Framework;

use Butterfly\Framework\Module\Base;

class Module extends Base
{

}
```

 
## Enabling Modules

In order to enable modules, first, you need to require the composer package from composer.

```shell script
composer require vendorname\packagename;
```

In order to enable the Module, you need to add Module class reference to modules.php.

> You can enable different modules in different domains. For example: You can enable your development module only in development domain.
> Please check `config` section for more details.

Example modules config file:

```php
return [
    \Butterfly\Core\Module::class,
    \Butterfly\Framework\Module::class,
    \Butterfly\Library\Module::class
];
```

> ***Note:*** Modules are initiated in the order of config array. You can change order in the array to manage dependencies.  