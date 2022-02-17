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

### `not_found`

Not Found Event is triggered when a page is not found. Dynamic redirections can be handled in this event. To create a Not Found hook, you can run the following command:

```bash
bin/butterfly make:event Frontend not_found
```

Example:
```php
<?php

namespace App\Event;

use App\Controller\Item;
use App\Model\Article;
use Butterfly\Framework\Registry\Registry;
use Butterfly\Library\Hook;

class Frontend extends Hook
{
    public function not_found($params)
    {
        $url = $params['url'];
        if(preg_match('~en/(.+)~', $url, $tmp))
        {
            $mArticle = new Article();
            $article = $mArticle->getByCustom_seo_en($tmp[1]);

            if(! empty($article))
            {
                Registry::set('url', $article['seo']);
                Registry::set('language', 'en');

                $controller = new Item();
                $controller->designPrefix = 'en-';
                $controller->detailAction();
                echo $controller->renderLayout();
                exit;
            }
        }
    }
}
```

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

### BulkImageUpload::before_add

When you are using one-to-many relations with Multi Upload option. You can use this feature to manipulate Bulk Image Uploads.
Since this trigger is common for all Bulk Image Uploads, you need to narrow it's scope like the following example.

You can also change one-to-many import behaviour, for example you can define unique_keys to override existing records.

Example:

```php
<?php
namespace App\Hook;

use Butterfly\Core\Model\Objects;
use Butterfly\Core\View\TwigFunction\ImagePath;

class BulkImageUpload
{
    public function before_add($params)
    {
        $object_id = $params['object_id'];
        $table_name = Objects::getTableName($object_id);

        if($table_name != 'banner_images_bulk_upload')
        {
            return $params;
        }

        $entity_id = $params['data']['banner_images_bulk_upload_id'];

        $imageUpload = db()
            ->table('banner_images_bulk_upload')
            ->find($entity_id)
        ;

        $path = new ImagePath();
        $imageBasePath = $path->execute('content');

        $filename = $params['db_filename'];

        $params['data']['title'] = $imageUpload['title'];
        $params['data']['link'] = $imageBasePath . $filename;
        $params['data']['link_webp'] = $imageBasePath . $filename . '.webp';

        // If you want to override existing records, you can define unique_keys
        $params['unique_keys'] = [
            'sku', 'position', 'image_type'
        ];

        return $params;
    }
}
```