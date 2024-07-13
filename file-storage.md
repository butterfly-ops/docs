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
- Google Cloud Storage
- SFTP
- FTP

### Local Folder 

This adapter ships with Butterfly by default.

### Amazon S3

Installation

```bash
composer require league/flysystem-aws-s3-v3
```

### Google Cloud

```bash
composer require superbalist/flysystem-google-storage:* google/cloud-storage:* -W
```

Usage
Google Cloud Storage requires Service Account Credentials, which can be generated in the Cloud Console. Read more in the official documentation.

The credentials will be auto-loaded by the Google Cloud Client.
1. The client will first look at the GOOGLE_APPLICATION_CREDENTIALS env var.
   You can use ```putenv('GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json');``` to set the location of your credentials file.

2. The client will look for the credentials file at the following paths:
- windows: %APPDATA%/gcloud/application_default_credentials.json
- others: $HOME/.config/gcloud/application_default_credentials.json

If running in Google App Engine, the built-in service account associated with the application will be used.
If running in Google Compute Engine, the built-in service account associated with the virtual machine instance will be used.

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

// Subfolder parameter is optional, it defaults to current year and month
$mImageHelper->downloadImage('https://www.example.com/example.png', 'image_alias', 'sub_folder/');
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

// Subfolder parameter is optional, it defaults to current year and month
$mImageHelper->processUpload('UPLOAD_KEY', 'image_alias', 'sub_folder/');
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

### Uploading Images Via API

You can upload images using Butterfly REST Api.

For ```api/upload/image``` endpoint, available options:

- alias: Butterfly image upload alias, default: content
- sub_folder: Image upload path, default: null 
- files: Array of Images

Sample request:
```
curl --location --request POST 'http://domain.tld/api/upload/image' \
--form 'files[0]=@"/path/image1.png"' \
--form 'files[1]=@"/path/image2.png"'
```

> Note: Response includes webp params only when it was enabled.

Sample success response:
```
{
    "success": true,
    "result": [
        {
            "full_path": "https://cdn.url/static/img/content/21-01/24/image1.png",
            "webp": "https://cdn.url/static/img/content/21-01/24/image1.png.webp",
            "filename": "image.png"
        },
        {
            "full_path": "https://cdn.url/static/img/content/21-01/24/image2.png",
            "webp": "https://cdn.url/static/img/content/21-01/24/image2.png.webp",
            "filename": "image.png"
        }
    ]
}
```

Sample error response:
```
{
    "success": false,
    "errors": [
        {
            "message": "error message",
            "filename": "image1.png"
        },
        {
            "message": "error message",
            "filename": "image2.png"
        }
    ]
}
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

// Subfolder parameter is optional, it defaults to current year and month
$mFileHelper->downloadFile('https://www.example.com/example.xlsx', 'file_alias', 'sub_folder/');
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

// Subfolder parameter is optional, it defaults to current year and month
$mFileHelper->processUpload('UPLOAD_KEY', 'file_alias', 'sub_folder/');
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

### Uploading Files Via API

You can upload files using Butterfly REST Api.

For ```api/upload/file``` endpoint, available options:

- alias: Butterfly file upload alias, default: content
- sub_folder: File upload path, default: null 
- files: Array of Files

Sample request:
```
curl --location --request POST 'http://domain.tld/api/upload/file' \
--form 'files[0]=@"/path/file.mp4"' \
--form 'files[1]=@"/path/file2.pdf"'
```

Sample success response:
```
{
    "success": true,
    "result": [
        {
            "full_path": "https://cdn.url/static/file/content/21-01/24/file.mp4",
            "filename": "file.mp4"
        },
        {
            "full_path": "https://cdn.url/static/file/content/21-01/24/file2.pdf",
            "filename": "file2.pdf"
        }
    ]
}
```

Sample error response:
```
{
    "success": false,
    "errors": [
        {
            "message": "error message",
            "filename": "file.mp4"
        },
        {
            "message": "error message",
            "filename": "file2.pdf"
        }
    ]
}
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
{{ file_path('file_alias') }}
```

### Updating Sub Folder for Uploads

By default, `butterfly` creates subfolders in year-month/day format. Which means that, when you upload a file named `x.jpg`
your file will be uploaded to 21-05/01/x.jpg if date is 1th of May in 2021.

You can change this behaviour by updating Sub Folder Format on File Storage Admin. If you leave this field empty, it will default to
default behaviour.

If you set `/` to this setting, it will upload file to the root.

If you want to use different dates, you can use strftime function format. You can checkout [https://www.php.net/strftime](this link)

### File Overwrite Strategy

When you let users to upload files or images, files with same filename is always something you need to consider. You can set Overwrite Strategy
option under `File Storages` for uploaded files with same name.
 
#### Append Time:

If you choose this option, unix time will be added to filename if there is already a file with same name.

For example: Let's say that you uploaded a file named `test.png`. If you upload another file with the same name, it will be saved as 
`test-1624119416.png`.

Advantages:
- Existing files with the same name used by other records will not be affected.
- Since the name of the file is changed, CDN Caches automatically becomes invalid for updated images.

#### Overwrite:

Simple: It will replace the old file if a file with same name is added.

> [!WARNING]
> Don't choose `overwrite` option if you really don't need it. It may lead data loss since old files with same name is 
> overridden. And if you need this option just for some Upload Config, create additional File Storage for these Upload Configs.

### Filename Sanitization for Uploads

When you upload a file or image to Butterfly, it's a good practice to replace white-spaces and special characters in the filename to 
prevent errors on browsers etc, but sometimes you may want to leave filename as-is.

Sanitize Option is enabled by default in `File Storage` settings, but if you uncheck this box, then it will leave the filename and spaces 
as-is.

Example:

If you upload a file named `Test Filename ÇÖĞ.jpg`

Sanitized version will be
`test-filename-cog.jpg`

Not Sanitized version
`Test Filename ÇÖĞ.jpg`