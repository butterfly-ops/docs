# Changelog

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