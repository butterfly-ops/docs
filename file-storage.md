# File Storage

When dealing with scalable Cloud Systems, everyone needs different File Storages. butterfly provides an abstraction layer for you 
to upload your static images / files.

Butterfly uses [Flysystem](https://flysystem.thephpleague.com/v1/docs/) for abstracting file systems. 

## Storage Drivers

You can use multiple storages at the same time. Storages are managed under `System Settings > CMS - File Storages` page. You
can add / edit / remove storages.

File Storage Drivers are:

- Local Folder
- Amazon S3
- Azure Blob Storage
- SFTP
- FTP

### Local Folder 

This adapter ships with Butterfly by default.

### Amazon S3

Installation

```bash
composer require league/flysystem-aws-s3-v3
```

### Azure Blob Storage

Installation

```bash
composer require league/flysystem-azure-blob-storage
```

### SFTP

Installation

```bash
composer require league/flysystem-sftp
```

### FTP

This adapter ships with Butterfly by default.

## Images

Allowed extensions for images: `jpg, jpeg, gif, svg, png`

### Downloading an Image

You can upload / crop an image from Admin Panel if it's defined as Widget Spec, Setting or Object Spec; but you may need to download 
an image programatically.

When you need to download an image, you can use the following code example:

```php
$mImageHelper = new \Butterfly\Framework\Helper\Image();
$mImageHelper->downloadImage('https://www.example.com/example.png', 'image_alias');
```

You can define Image Aliases from `System Settings` > `Image Uploads`.

successful response:

```php
[
    'success' => true,
    'full_path' => 'https://thebutterfly.io/static/2020-01/01/test.png',
    'filename' => '2020-01/01/test.png'
];
```

failed response:

```php
[
    'success' => false,
    'message' => 'Error message'
];
```

### Handling Image Uploads

If you need to upload an image programatically else than Admin Panel, you can do it easily using the following example:

```php
$mImageHelper = new \Butterfly\Framework\Helper\Image();
$mImageHelper->processUpload('UPLOAD_KEY', 'image_alias');
```

UPLOAD_KEY designates the key in $_FILES array which means the input name of the Upload. You can define Image Aliases from `System Settings` > `Image Uploads`.

successful response:

```php
[
    'success' => true,
    'full_path' => 'https://thebutterfly.io/static/2020-01/01/test.png',
    'filename' => '2020-01/01/test.png'
];
```

failed response:

```php
[
    'success' => false,
    'message' => 'Error message'
];
```

### Getting Full Path

When you use image uploads, only filenames are kept in the Database. Although full paths of the images for all possible sizes are 
saved in Elastic Search Index (Data Pools), you may want to get data from Database.

You can get the full path of an image alias like the following:

- Getting image full path by alias from PHP Code:

```php
$mCmsImageUpload = new \Butterfly\Core\Model\CmsImageUpload();
$mCmsImageUpload->getFullPathByAlias('original'); // `original` is the alias of image upload
```

- Getting image full path by alias from Twig Templates:

```twig
{{ image_path('image_alias') }}
```


## Files

Allowed file upload extensions are defined from Admin panel.

Restricted File Types: `php, php5, sh`

### Downloading a File

You can upload / crop an image from Admin Panel if it's defined as Widget Spec, Setting or Object Spec; but you may need to download 
an image programatically.

When you need to download an image, you can use the following code example:

```php
$mFileHelper = new \Butterfly\Framework\Helper\File();
$mFileHelper->downloadFile('https://www.example.com/example.xlsx', 'file_alias');
```

You can define Image Aliases from `System Settings` > `Image Uploads`.

successful response:

```php
[
    'success' => true,
    'full_path' => 'https://thebutterfly.io/static/2020-01/01/test.xlsx',
    'filename' => '2020-01/01/test.xlsx'
];
```

failed response:

```php
[
    'success' => false,
    'message' => 'Error message'
];
```

### Handling File Uploads

If you need to upload an image programatically else than Admin Panel, you can do it easily using the following example:

```php
$mFileHelper = new \Butterfly\Framework\Helper\File();
$mFileHelper->processUpload('UPLOAD_KEY', 'file_alias');
```

UPLOAD_KEY designates the key in $_FILES array which means the input name of the Upload. You can define Image Aliases from `System Settings` > `Image Uploads`.

successful response:

```php
[
    'success' => true,
    'full_path' => 'https://thebutterfly.io/static/2020-01/01/test.xlsx',
    'filename' => '2020-01/01/test.xlsx'
];
```

failed response:

```php
[
    'success' => false,
    'message' => 'Error message'
];
```

### Getting Full Path

When you use file uploads, only filenames are kept in the Database. Although full path of the file upload 
saved in Elastic Search Index (Data Pools), you may want to get data from Database.

You can get the full path of an file alias like the following:

- Getting file full path by alias from PHP Code:

```php
$mCmsFileUpload = new \Butterfly\Core\Model\CmsFileUpload();
$mCmsFileUpload->getFullPathByAlias('file_upload_alias'); // `original` is the alias of image upload
```

- Getting image full path by alias from Twig Templates:

```twig
{{ image_path('image_alias') }}
```