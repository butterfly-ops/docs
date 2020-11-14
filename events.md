# Introduction

Events are designed to make changes in behaviours of Butterfly or run custom codes inside of `Butterfly Core`. 

## Frontend

Frontend events are triggered while startup of the Application.

### `bootstrap`

To create a Bootstrap hook, you can run the following command:

```bash
bin/butterfly make:event Frontend Bootstrap
```

> [!TIP]
> Frontend>Bootstrap event doesnt have any parameters. You can use this event to run codes which should be ran for all requests.

> [!WARNING]
> Don't forget that, the code written inside of Frontend>Bootstrap event will run for each request which means that it may decrease 
> performance of your website.

### `object::detail`

```bash
bin/butterfly make:event:object:detail campaigns
```

will create 

```php
<?php

namespace App\Event;

use Butterfly\Core\Controller\Frontend\Item;
use Butterfly\Library\Event;

class Campaigns extends Event
{
    public function detail($params)
    {
        $info = $params['info'];
        /** @var Item $controller */
        $controller = $params['class'];

        /**
         * TODO: Make info variable manipulations
         */

        /**
         * TODO: Make meta title, meta description manipulations
         *
         * Example:
         * $info['meta_title'] = '';
         * $info['meta_description'] = '';
         */


        // Assign info to detail controller
        $controller->info = $info;

        // Reload Info to make manipulations effective.
        $controller->reloadInfo();
    }
}
```
