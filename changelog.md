# Changelog

## 1.5.179

- app/Widget/Cms/ directory is added for overriding Butterfly Core Widget Templates
- Added Pagination widget to Butterfly Core

## 1.5.178

- `bin/butterfly health-check` command is added to check environment configs.
- CmsObject->refreshItemsByEntityIds function is added.
- refreshItem methods automatically add redirections now.

## 1.5.174
- File upload endpoint added for Butterfly Api.

## 1.5.173
- Sms integration updated.

## 1.5.172
- Webp support added to manipulated images.

## 1.5.171

- Please check [Upgrade Notes](https://thebutterfly.io/docs/#/upgrade?id=_15179)
- design widgets - drag & drop fix for nested fields
- design widgets - new line character fix for textarea_with_editor in nested fields
- fixed a bug causing elastic search queries with boolean value not working as expected

## 1.5.170

- HTTPS Redirection to outside domains support is added for Redirect Maps.
- Fixed a bug causing false security errors on Login

## 1.5.165

- Fixed a bug causing object duplication while updating existing Objects
- Updated Object Import to allow imports if column exists but doesn't show in Admin

## 1.5.164

- Rest API Module is added
- Cms Image Upload API is added
- Cms Login API is added
- Fixed bug on Designs Permissions for Non-Administrator Users.
- Passive Method is added for FTP Connections
- Fixed a bug on Bulk Edits that prevents data's to be set from Hooks.
- Fixed a bug causing URL's to be redirected when there is a `.` in the URL.
- Ignore Unmapped parameter is added for Sorting on ElasticSearch.
- Widget Parameters now supports Nested Field Type.
- Added additional class name to Frontend Renders.
- Improved design rendering to prevent errors when target Widget doesn't exist.
- Added support for passwordless auth for SMTP Servers.

## 1.5.159

- Registry is cleared after each test-run

## 1.5.157

- Optional Sub Folder parameter is added to File and Image Upload Handlers [Details](https://thebutterfly.io/docs/#/file-storage?id=handling-file-uploads)

## 1.5.154

- Refresh button is added to Dropdown Field Type
- `twig` support is added to `Code` Field Type.
- Elastic Search query improvements.
- Fixed Elastic Search Index mapping for `label` and `title`
- Migration functions for FileUpload Field Type and DropdownFromClass are added
- Fixed a bug prevents the system to start when Turkish Locale is installed to Web Server.
- Security Improvement: Additional security checks are added to image and file uploads.

## 1.5.151

- `cron:refresh-items` command and refresh items operation in admin panel is speeded up 100x times.
- Data Pool improvements. (It has 3 different types: manual, automatic, advanced)
- You can now add elastic search query string to Data Pools (Advanced Mode)
- Customer and Design Segmentations are added

## 1.5.149

- Added `make:event:object:detail` Command [Details](https://thebutterfly.io/docs/#/events?id=objectdetail)

## 1.5.145
   
- New Admin Panel Customization for Objects with Parent / Child Record relationship is added. [Details](https://thebutterfly.io/docs/#/adminpanel?id=hiearchical-lists) 

## 1.5.144

- `Nested Clause with Multiple Depth` is added. [Details](https://thebutterfly.io/docs/#/database?id=nested-clause-with-multiple-depth)
- Added language option to Elastic Search Integration
- Improved Data Pool page. It now lists contents of Data Pool in edit page.

## 1.5.139

- Added `make:twig:function` and `make:twig:filter` [Details](https://thebutterfly.io/docs/#/generators?id=twig-filter) 

## 1.5.133

- Fixed a bug in ImageManipulations

## 1.5.132

- Symlink support for Windows is added for `bin/butterfly folders:create` command.
- `isWindows` function is added to Server Helpers [Details](https://thebutterfly.io/docs/#/helpers?id=iswindows)

## 1.5.130

- ColorPicker Field Type is fixed to use in NestedField

## 1.5.129

- Block field type is added [Details](https://thebutterfly.io/docs/#/objects?id=block)

## 1.5.128
   
- Fixed a bug causing Cms Widget Refresh not to update Widget Parameters.

## 1.5.127

- Object Import and Multi Image upload bugs are fixed.
- `make:hook` and `make:event` commands are added. 

## 1.5.124

- Multiple Replacement support for Object Listing customizations action buttons.
- Game Changer `:)` Elastic Search Integration for Database Layer. [Details](https://thebutterfly.io/docs/#/database?id=elasticsearch)
- Fixed a bug causing auto_increment feature removal on duplicate runs for migrations.
- Frontend>Bootstrap event is added. [Details](https://thebutterfly.io/docs/#/events?id=bootstrap)

## 1.5.123

- `parse` filter is added to TwigFilters. [Details](https://thebutterfly.io/docs/#/frontend?id=parse)

## 1.5.122

- `json_decode` filter is added to TwigFilters. [Details](https://thebutterfly.io/docs/#/frontend?id=json_decode)

## 1.5.120

- New Function to access image full paths is added. [Details](https://thebutterfly.io/docs/#/file-storage?id=getting-full-path)
- New Function to access file full paths is added. [Details](https://thebutterfly.io/docs/#/file-storage?id=getting-full-path-1)

## 1.5.116

- Please check [Upgrade Notes](https://thebutterfly.io/docs/#/upgrade?id=15116)
- Publicly accessible files are moved to `public` folder for enhanced security.

## 1.5.107

- Real IP Access Headers are added to `security` config. [Details](https://thebutterfly.io/docs/#/security?id=accessing-real-ip-address)

## 1.5.106

- Fixed a bug in Bulk Edits. (It was ignoring characters after `&` character in String Fields.)
- Nested Fields Visual Improvements

## 1.5.105

- FTP Support for File Storages is added.
- Flysystem is integrated [Details](https://thebutterfly.io/docs/#/file-storage)
- Upload Handlers are added for easier File and Image Upload through API's [Details](https://thebutterfly.io/docs/#/file-storage)

## 1.5.104

- `nested` field type support is added for `Settings` 

## 1.5.101

- butterfly current installed version information is added to page header in `Settings` page.
- Conditional Show/Hide helpers are added for Object Specs. [Details](https://thebutterfly.io/docs/#/adminpanel?id=conditional-showhide) 

## 1.5.100

- `svg` support is added for Image Upload Types [Details](https://thebutterfly.io/docs/#/objects?id=image-upload)

## 1.5.97

- `setting` function is added to twig functions. [Details](https://thebutterfly.io/docs/#/frontend?id=setting)

## 1.5.96

- Updated code field type to prevent unrelated Doctype syntax errors for HTML type. [Details](https://thebutterfly.io/docs/#/objects?id=code)

## 1.5.95

- AdminTemplateGenerator hotfix
- hide_action_buttons variable is added for custom list pages [Details](https://thebutterfly.io/docs/#/adminpanel?id=action_buttons)

## 1.5.94

- Environment based configuration override is added. [Details](https://thebutterfly.io/docs/#/installation?id=environment-based-override)

## 1.5.91

- `placeAfter` and `placeBefore` positioning is added for `Migrations`. [Details](https://thebutterfly.io/docs/#/migrations?id=removing-object-specs)
- `multicheckbox` update for `Nested Field Type`. You can use multicheckbox's with `Nested Field Type` 

## 1.5.90

- `config` filter is added to twig filters. [Details](https://thebutterfly.io/docs/#/frontend?id=config)

## 1.5.88

- Fixed a bug causing [Checkbox Field Type](https://thebutterfly.io/docs/#/objects?id=checkbox) not to be able to unchecked.  

## 1.5.85

- `git_version` function is added. [Details](https://thebutterfly.io/docs/#/frontend?id=git_version)
- `datetime` field type is vanilla jsified [Details](https://thebutterfly.io/docs/#/objects?id=datetime)

## 1.5.82

- Nested field supports recursive nested fields. [Details](https://thebutterfly.io/docs/#/objects?id=nested)

## 1.5.80

- Azure Blob Storage integration is added. [Details](https://thebutterfly.io/docs/#/file-storage) 

## 1.5.78

- Please check [Upgrade Notes](https://thebutterfly.io/docs/#/upgrade?id=_1578)
- frontend template engine is moved to twig.
- `bin/butterfly convert:twig` command is added for smarty => twig conversions
- `count`, `registry`, `truncate` filters are added for twig. [Details](https://thebutterfly.io/docs/#/frontend?id=twig-filters)
- `widget`, `file_path`, `image_path`, `include_file` `current_url` functions are added for twig. [Details](https://thebutterfly.io/docs/#/frontend?id=twig-functions) 

## 1.5.74

- Please check [Upgrade Notes](https://thebutterfly.io/docs/#/upgrade?id=_1574)
- `image_upload` Field Type includes data all sizes inside of Elastic Index.

## 1.5.69

- vendor/butterfly/src/Core/Assets folder is symlinked to assets/core folder
- createOrUpdateTable is added to Schema [Details](https://thebutterfly.io/docs/#/database?id=createorupdatetable)
- dropColumns is added to Schema [Details](https://thebutterfly.io/docs/#/database?id=dropcolumns)
- removeObjectSpec is added to Migrations [Details](https://thebutterfly.io/docs/#/migrations?id=removing-object-specs)

## 1.5.65

- Readonly Permission (View Permission is added to system) [Details](https://thebutterfly.io/docs/#/objects?id=generic-permissions)

## 1.5.64

- Table Name and Column Name format check is added. Valid Format: `[a-z]|[A-Z]|_|[0-9])+`
- Hotfix for where clauses with null as second parameter. (Example: ->where('id', null) will run query WHERE id IS NULL)

## 1.5.63

- Hotfix for image manipulation operations. Now, it gets config from File Storages.

## 1.5.62

- IAM Authentication Support for Amazon S3 is added.
- Index support is added for Objects. [Details] 

## 1.5.61

- Security enhancement. X-Frame-Options: SAMEORIGIN header is added to Admin.

## 1.5.59

- Download image filename bugfix.

## 1.5.58

- Performance Improvement for first() and one() database functions
- Image Crop bug is fixed which causes 1 pixel black line after image manipulation. 

## 1.5.57

- Admin Menu Creation is added to Object Migrations. [Details](https://thebutterfly.io/docs/#/migrations?id=creating-admin-menus-for-objects)
- Custom Permission Defitions are added. [Details](https://thebutterfly.io/docs/#/objects?id=custom-permissions)

## 1.5.56

- Fixed - User / List onclick event fix (it opens edit page again)
- Fixed a bug in ObjectSpec Migrations which causes new Object Spec to placed top instead of bottom of the current EditPage.
- CrudHelper - Security Updates // Permission Check is added
- Object Save Handler - Security Updates // Permission Check is added
- Fixed - Object list page excel export error (objects with more then 26 field on list page)

## 1.5.55

- Excel Import Improvement. It now ignores fully empty lines at the end of the file.
- Utils - Storage Type support added for download_image and download_file functions

## 1.5.54

- Overriding Records Per Page options support is added for Admin Panel. [Details](https://thebutterfly.io/docs/#/adminpanel?id=limit-per-page-options)
- Cms Controller Generator Command is added `bin/butterfly publish:admin:controller` for objects. [Details](https://thebutterfly.io/docs/#/adminpanel?id=list-add-edit-actions)

## 1.5.51

- Multiple object export hotfix
- Fixed a bug in Nested Fields occurs when Nested Field is the first field of the Object
- Login As support is added for Users with User Add / Edit Permission.
- Fixed Admin Menu's doesn't show up when Permitted Object is a SubMenu

## 1.5.50

- Money field type fixes

## 1.5.48

- Install / Upgrade support for Core + App is finalized. [Documentation](https://thebutterfly.io/docs/#/migrations)

## 1.5.41

- Admin Left Menu fix for object / detail pages.
- Garbage Collector (`cron:garbage-collector`) performance update.

## 1.5.40

- Hotfix for ObjectController list action display

## 1.5.39
   
- Hotfix for Widget Reload operation

## 1.5.38

- Performance Improvement for Objects - Multi-Database Support

## 1.5.36

- Hotfix for Admin / Reports button display status

## 1.5.34

- Hotfix for custom admin layouts 

## 1.5.33 

- Updated Object Listing for `remote_image` field type. Now displays image in list. 

## 1.5.32

- Added `bin/butterfly publish:admin:layout` command. [Details](https://thebutterfly.io/docs/#/adminpanel?id=layout)

## 1.5.31

- Fixed a bug in `make:content-widget` command.

## 1.5.30

- Removed unnecessary `duration` column from Item->Refresh method

## 1.5.29

- Added `bin/butterfly publish:admin:template` command
- Added `bin/butterfly make:model` command
- Added `bin/butterfly install` command
- `tables` function is added to Schema
- Added `bin/butterfly admin:user:create` command
- Added `bin/butterfly make:hook` command
- Added `bin/butterfly make:controller` command
- Added `bin/butterfly make:widget` command
- Added `bin/butterfly make:content-widget` command
- Added `bin/butterfly upgrade` command for Database Upgrades
- Added `whereNotIn` function 
- Added Object Migrations

## 1.5.28

- Added ability to customize column based views for Objects.