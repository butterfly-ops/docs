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

Usage

```
use League\Flysystem\Filesystem;
use League\Flysystem\Adapter\Local;

$adapter = new Local(__DIR__.'/path/to/root');
$filesystem = new Filesystem($adapter);
```

### Amazon S3

Installation

```composer require league/flysystem-aws-s3-v3```

Usage

```
use Aws\S3\S3Client;
use League\Flysystem\AwsS3v3\AwsS3Adapter;
use League\Flysystem\Filesystem;

$client = new S3Client([
    'credentials' => [
        'key'    => 'your-key',
        'secret' => 'your-secret',
    ],
    'region' => 'your-region',
    'version' => 'latest|version',
]);

$adapter = new AwsS3Adapter($client, 'your-bucket-name', 'optional/path/prefix');

$filesystem = new Filesystem($adapter);
```

### Azure Blob Storage

Installation

```composer require league/flysystem-azure-blob-storage```

Usage

```
use League\Flysystem\AzureBlobStorage\AzureBlobStorageAdapter;
use League\Flysystem\Filesystem;
use MicrosoftAzure\Storage\Blob\BlobRestProxy;

include __DIR__.'/vendor/autoload.php';

$client = BlobRestProxy::createBlobService('DefaultEndpointsProtocol=https;AccountName={YOUR_ACCOUNT_NAME};AccountKey={YOUR_ACCOUNT_KEY};');
$adapter = new AzureBlobStorageAdapter($client, 'container_name');
$filesystem = new Filesystem($adapter);
var_dump($filesystem->listContents());
```

### SFTP

Installation

```composer require league/flysystem-sftp```

Usage 

```
use League\Flysystem\Filesystem;
use League\Flysystem\Sftp\SftpAdapter;

$filesystem = new Filesystem(new SftpAdapter([
    'host' => 'example.com',
    'port' => 22,
    'username' => 'username',
    'password' => 'password',
    'privateKey' => 'path/to/or/contents/of/privatekey',
    'root' => '/path/to/root',
    'timeout' => 10,
]));
```

### FTP

This adapter ships with Butterfly by default.

Usage 

```
use League\Flysystem\Filesystem;
use League\Flysystem\Adapter\Ftp as Adapter;

$filesystem = new Filesystem(new Adapter([
    'host' => 'ftp.example.com',
    'username' => 'username',
    'password' => 'password',

    /** optional config settings */
    'port' => 21,
    'root' => '/path/to/root',
    'passive' => true,
    'ssl' => true,
    'timeout' => 30,
    'ignorePassiveAddress' => false,
]));
```

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