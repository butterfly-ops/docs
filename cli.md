# Butterfly CLI Commands Documentation

## help

### Description

Display help for a command

### Usage

```bash
help [--format FORMAT] [--raw] [--] [<command_name>]
```

### Arguments

* `command_name`
  * The command name
  * Default: `help`

### Options

* `--format` (Required)
  * The output format (txt, xml, json, or md)
  * Default: `txt`

* `--raw`
  * To output raw command help

### Help

The <info>%command.name%</info> command displays help for a given command:

  <info>%command.full_name% list</info>

You can also output the help in other formats by using the <comment>--format</comment> option:

  <info>%command.full_name% --format=xml list</info>

To display the list of available commands, please use the <info>list</info> command.

---

## list

### Description

List commands

### Usage

```bash
list [--raw] [--format FORMAT] [--short] [--] [<namespace>]
```

### Arguments

* `namespace`
  * The namespace name

### Options

* `--raw`
  * To output raw command list

* `--format` (Required)
  * The output format (txt, xml, json, or md)
  * Default: `txt`

* `--short`
  * To skip describing commands' arguments

### Help

The <info>%command.name%</info> command lists all commands:

  <info>%command.full_name%</info>

You can also display the commands for a specific namespace:

  <info>%command.full_name% test</info>

You can also output the information in other formats by using the <comment>--format</comment> option:

  <info>%command.full_name% --format=xml</info>

It's also possible to get raw list of commands (useful for embedding command runner):

  <info>%command.full_name% --raw</info>

---

## _complete

### Description

Internal command to provide shell completion suggestions

### Usage

```bash
_complete [-s|--shell SHELL] [-i|--input INPUT] [-c|--current CURRENT] [-a|--api-version API-VERSION] [-S|--symfony SYMFONY]
```

### Options

* `--shell` (`-s`) (Required)
  * The shell type ("bash", "fish", "zsh")

* `--input` (`-i`) (Required)
  * An array of input tokens (e.g. COMP_WORDS or argv)

* `--current` (`-c`) (Required)
  * The index of the "input" array that the cursor is in (e.g. COMP_CWORD)

* `--api-version` (`-a`) (Required)
  * The API version of the completion script

* `--symfony` (`-S`) (Required)
  * deprecated

---

## completion

### Description

Dump the shell completion script

### Usage

```bash
completion [--debug] [--] [<shell>]
```

### Arguments

* `shell`
  * The shell type (e.g. "bash"), the value of the "$SHELL" env var will be used if this is not given

### Options

* `--debug`
  * Tail the completion debug log

### Help

The <info>%command.name%</> command dumps the shell completion script required
to use shell autocompletion (currently, bash, fish, zsh completion are supported).

<comment>Static installation
-------------------</>

Dump the script to a global completion file and restart your shell:

    <info>%command.full_name% zsh | sudo tee $fpath[1]/_butterfly</>

Or dump the script to a local file and source it:

    <info>%command.full_name% zsh > completion.sh</>

    <comment># source the file whenever you use the project</>
    <info>source completion.sh</>

    <comment># or add this line at the end of your "~/.zshrc" file:</>
    <info>source /path/to/completion.sh</>

<comment>Dynamic installation
--------------------</>

Add this to the end of your shell configuration file (e.g. <info>"~/.zshrc"</>):

    <info>eval "$(/Users/efendi/Sites/butterfly/bin/butterfly completion zsh)"</>

---

## make:twig:filter

### Description

Generates new Twig Filter

### Usage

```bash
make:twig:filter <name>
```

### Arguments

* `name` (Required)
  * Filter Name Lowercase

### Help

This command allows you to generate Twig Filter

---

## make:hook

### Description

Generates new Hook for creating hooks

### Usage

```bash
make:hook <table>
```

### Arguments

* `table` (Required)
  * Table Name

### Help

This command allows you to generate hook codes.

---

## folders:create

### Description

Creates needed folders for Butterfly

### Usage

```bash
folders:create
```

### Help

This command creates folders in the home directory. Folders: var, static, var/tmp var/cache var/log.

---

## cron:refresh-items

### Description

Updates items table with the entity table information

### Usage

```bash
cron:refresh-items [--force-update-seo [FORCE-UPDATE-SEO]] [--] [<types> [<table_names>]]
```

### Arguments

* `types`
  * Type ID of the Object

* `table_names`
  * Table Names of the Object

### Options

* `--force-update-seo`
  * Force updating the existing links

### Help

This command allows you to refresh items table, should be called when manual database delete operations are done.

---

## make:event

### Description

Generates new Event code

### Usage

```bash
make:event <class_name> <function_name>
```

### Arguments

* `class_name` (Required)
  * Class Name

* `function_name` (Required)
  * Function Name

### Help

This command allows you to generate event codes.

---

## install

### Description

Installs the Butterfly

### Usage

```bash
install [-s|--skip-database [SKIP-DATABASE]] [-sa|--skip-admin-user [SKIP-ADMIN-USER]] [--] <domain> [<database_server> [<database_name> [<database_username> [<database_password> [<database_port>]]]]]
```

### Arguments

* `domain` (Required)
  * Domain Name

* `database_server`
  * Database Server

* `database_name`
  * Database Name

* `database_username`
  * Database Username

* `database_password`
  * Database Password

* `database_port`
  * Database Port

### Options

* `--skip-database` (`-s`)
  * 1 for skipping database installation

* `--skip-admin-user` (`-sa`)
  * 1 for skipping admin user creation

### Help

This command allows you to initiate the Butterfly, create database entries, creates the first admin user.

---

## widget:refresh

### Description

Refreshes Widgets

### Usage

```bash
widget:refresh [-d|--delete [DELETE]]
```

### Options

* `--delete` (`-d`)
  * Delete not Existing Widgets

### Help

This command allows you to update widget informations in Admin Panel

---

## publish:layout

### Description

Publishes frontend layout for customizations

### Usage

```bash
publish:layout
```

### Help

This command generates default frontend layout under app/Views/Layout.twig

---

## object:migration:create

### Description

Generates Migration For Existing Objects

### Usage

```bash
object:migration:create [--tables [TABLES]]
```

### Options

* `--tables`
  * Table names comma separated or search like query for table_name. Example 1: users,user_groups Example 2: user%

### Help

This command helps you to generate migrations for existing objects.

---

## excel:convert-to-twig

### Description

Converts an Excel file to Twig code

### Usage

```bash
excel:convert-to-twig <filePath>
```

### Arguments

* `filePath` (Required)
  * Path to the Excel file

### Help

This command creates folders in the home directory. Folders: var, static, var/tmp var/cache var/log.

---

## connection:test

### Description

Send a GET request to an external service

### Usage

```bash
connection:test [-a|--address [ADDRESS]] [-o|--output [OUTPUT]]
```

### Options

* `--address` (`-a`)
  * Address (Default: https://www.google.com)

* `--output` (`-o`)
  * Print Output

### Help

This command allows you to test connectivity

---

## convert:twig

### Description

Convert Smarty templates to Twig

### Usage

```bash
convert:twig <file>
```

### Arguments

* `file` (Required)
  * File

### Help

This command allows you to convert smarty templates to twig

---

## make:model

### Description

Generates new Model

### Usage

```bash
make:model <table> [<folder>]
```

### Arguments

* `table` (Required)
  * Table Name

* `folder`
  * Folder Name

### Help

This command allows you to generate model codes.

---

## publish:admin:layout

### Description

Publishes admin layout for customizations

### Usage

```bash
publish:admin:layout
```

### Help

This command generates admin layout under app/Views/Cms/layout.tpl

---

## admin:user:create

### Description

Creates admin user

### Usage

```bash
admin:user:create [-r|--random-password RANDOM-PASSWORD] [--] <email> [<password> [<name>]]
```

### Arguments

* `email` (Required)
  * Admin User E-mail

* `password`
  * Password

* `name`
  * Admin Name

### Options

* `--random-password` (`-r`) (Required)
  * Generate Random Password

### Help

This command allows you to create super user for admin panel.

---

## cron:execute

### Description

Executes crons scheduled using Cronjobs

### Usage

```bash
cron:execute
```

### Help

This command allows you to run scheduled jobs, should be added to crontab of a server

---

## image:webp:generate

### Description

Regenerates all aliases with webp support

### Usage

```bash
image:webp:generate
```

### Help

This command downloads all images with webp support enabled and uploads to remote

---

## admin:menus:check

### Description

Cleans up relations for Admin Menus and Objects

### Usage

```bash
admin:menus:check
```

### Help

This is a temporary fix command for broken admin menu <> object relations which causes not displayed menus on Admin.

---

## make:twig:function

### Description

Generates new Twig Function

### Usage

```bash
make:twig:function <name>
```

### Arguments

* `name` (Required)
  * Function Name Lowercase

### Help

This command allows you to generate Twig Function

---

## upgrade

### Description

Upgrades database schema

### Usage

```bash
upgrade
```

### Help

This command allows you to run upgrade to run migrations.

---

## publish:admin:controller

### Description

Publishes custom controller for admin panel controller customizations

### Usage

```bash
publish:admin:controller <table>
```

### Arguments

* `table` (Required)
  * Table Name

### Help

This command generates admin controller under app/Controller/Cms folder for given objects.

---

## console

### Description

Starts an interactive terminal using psysh

### Usage

```bash
console [--execute [EXECUTE]]
```

### Options

* `--execute`
  * Execute given code

### Help

This command starts a new interactive terminal to interact with your application through terminal

---

## make:event:object:detail

### Description

Generates new Event code

### Usage

```bash
make:event:object:detail <table_name>
```

### Arguments

* `table_name` (Required)
  * Table Name

### Help

This command allows you to generate event codes.

---

## cron:garbage-collector

### Description

Cleans up items table for not used items

### Usage

```bash
cron:garbage-collector
```

### Help

This command allows you to clean-up items table, should be called when manual database delete operations are done.

---

## publish:admin:template

### Description

Publishes templates for admin panel template customizations

### Usage

```bash
publish:admin:template <table> <action> [<column>]
```

### Arguments

* `table` (Required)
  * Table Name

* `action` (Required)
  * Action to be customized. Possible values: add / edit / bulkedit

* `column`
  * Column Name

### Help

This command generates admin templates under app/Views/Cms folder for given objects / object fields.

---

## make:api-doc

### Description



### Usage

```bash
make:api-doc [-d|--directory DIRECTORY]
```

### Options

* `--directory` (`-d`) (Required)
  * Base directory for the controllers. Default is "Api" under app/Controller folder. Use comma to seperate multiple locations like Api,Ajax,V2 etc.
  * Default: `Api`

---

## publish:template

### Description

Publishes frontend templates for customizations

### Usage

```bash
publish:template <file>
```

### Arguments

* `file` (Required)
  * File name of the Frontend Template

### Help

This command generates specified templates under app/Views/ directory

---

## queue:worker:start

### Description

Runs Queue Workers

### Usage

```bash
queue:worker:start <queue_name> <worker_count> [<logging>]
```

### Arguments

* `queue_name` (Required)
  * Name of the Queue

* `worker_count` (Required)
  * Number of workers to be started

* `logging`
  * Enable logging

### Help

This command starts queues using configuration from app/config/queue.php.

---

## queue:worker:kill

### Description

Kill Queue Workers

### Usage

```bash
queue:worker:kill
```

### Help

This command kills workers.

---

## cron:sitemap

### Description

Create sitemaps using objects with SEO links. Include or exclude objects by marking the 'include_in_sitemap' field.

### Usage

```bash
cron:sitemap [-g|--group-objects GROUP-OBJECTS] [-l|--link-format-groups LINK-FORMAT-GROUPS] [-o|--objects OBJECTS] [-c|--custom-fields CUSTOM-FIELDS] [-e|--exceptions EXCEPTIONS] [-u|--base-url BASE-URL] [-p|--base-path BASE-PATH] [-t|--test TEST] [-s|--chunk-size CHUNK-SIZE]
```

### Options

* `--group-objects` (`-g`) (Required)
  * Grouped Object Table Names like "articles,blog_posts" etc. into single sitemap file. To set a name to file execute with prefix like --group-objects=posts-sitemap:articles,blog_posts\;stores-sitemap:stores,cities,regions. This command will output two sitemap with names posts-sitemap.xml and stores-sitemap.xml

* `--link-format-groups` (`-l`) (Required)
  * Grouped Urls By Link Formats like "/ButterflyBusiness/*" etc. into single sitemap file. To set a name to file execute with prefix like --link-format-groups=business:\ButterflyBusiness\\;news:\ButterflyNews\. This command will output two sitemap with names business-sitemap.xml and news-sitemap.xml

* `--objects` (`-o`) (Required)
  * Object Table Names like "articles,blog_posts" etc.

* `--custom-fields` (`-c`) (Required)
  * Custom link fields like "url,link,no_index" etc

* `--exceptions` (`-e`) (Required)
  * Custom link field exceptions like "pages:link" excludes page link checks

* `--base-url` (`-u`) (Required)
  * Base url for links. Example: https://thebutterfly.io

* `--base-path` (`-p`) (Required)
  * Base path for links. Example: /sitemap/current/{file}

* `--test` (`-t`) (Required)
  * Skip upload operation, write only tmp folders.

* `--chunk-size` (`-s`) (Required)
  * Chunk size for grouped objects. Default: 0 without chunking.

### Help

Use the --objects option to set multiple objects for multiple websites. Each object will create a new sitemap, while all remaining items will be included in a single sitemap file. An example usage would be bin/butterfly cron:sitemap --objects=articles,blog_posts.

---

## make:command

### Description

Generates new Command for creating Command

### Usage

```bash
make:command <class_name> <name> [<description>]
```

### Arguments

* `class_name` (Required)
  * Class Name

* `name` (Required)
  * Name

* `description`
  * Description

### Help

This command allows you to generate command codes.

---

## make:widget

### Description

Generates new Widget

### Usage

```bash
make:widget <widget> [<folder>]
```

### Arguments

* `widget` (Required)
  * Widget Name

* `folder`
  * Folder Name

### Help

This command allows you to generate widgets

---

## mailer:test

### Description

Send a test mail

### Usage

```bash
mailer:test <to> [<attached_file>]
```

### Arguments

* `to` (Required)
  * To

* `attached_file`
  * Attached File in var/tmp folder

### Help

This command allows you to test mail settings

---

## config:cache:clear

### Description

Clears config cache

### Usage

```bash
config:cache:clear
```

### Help

This command allows you to clean config cache after deployment on production

---

## data:migrate

### Description

Migrates data between databases

### Usage

```bash
data:migrate [-l|--limit LIMIT] [--] <source-db> <target-db> <tables>
```

### Arguments

* `source-db` (Required)
  * Source Database

* `target-db` (Required)
  * Target Database

* `tables` (Required)
  * Tables to migrate

### Options

* `--limit` (`-l`) (Required)
  * Limit

### Help

This command allows you migrate tables from a database to other.

---

## make:content-widget

### Description

Generates new Content Widget

### Usage

```bash
make:content-widget <widget> [<folder>]
```

### Arguments

* `widget` (Required)
  * Widget Name

* `folder`
  * Folder Name

### Help

This command allows you to generate content widgets which have Content Pools as Parameter

---

## notification:test

### Description

Send a test notification

### Usage

```bash
notification:test <to> [<alias> [<attached_file>]]
```

### Arguments

* `to` (Required)
  * To

* `alias`
  * Notification Alias
  * Default: `email`

* `attached_file`
  * Attached File in var/tmp folder

### Help

This command allows you to test notification settings

---

## search:reindex

### Description

Creates a new Search index and populates with items

### Usage

```bash
search:reindex
```

### Help

This command creates a new search index on Elastic Search. After it finishes, current ElasticSearch alias is changed with the new index without any downtime.

---

## search:update

### Description

Updates Elastic Search Index for specific types

### Usage

```bash
search:update <table_name> [<item_ids>]
```

### Arguments

* `table_name` (Required)
  * Table Name

* `item_ids`
  * Item IDs to update (comma separated)

### Help

This command updates elastic search for a specific type. It directly updates current index without creating a new index

---

## search:stats

### Description

Updates item stats for index

### Usage

```bash
search:stats [--last-days [LAST-DAYS]]
```

### Options

* `--last-days`
  * Comma seperated last days like 2,3,4 means it will create hit_2_days, hit_3_days, hit_4_days

### Help

This command updates hit, hit_last_X_days fields search index on Elastic Search.

---

## search:health-check

### Description

Elastic Search Index health check

### Usage

```bash
search:health-check [<dry-run>]
```

### Arguments

* `dry-run`
  * Don\t take action, just check and notify

### Help

This command checks elastic search for various problems and tries to fix them automatically

---

## state-machine:publish:hook

### Description

Publishes state machine hook to handle processes.

### Usage

```bash
state-machine:publish:hook
```

### Help

This command publishes state machine hook to handle processes.

---

## health-check

### Description

Checks system resources and connections

### Usage

```bash
health-check
```

### Help

It checks settings for Cache, Database, Search and verifies system has needed components

---

## make:controller

### Description

Generates new Controller

### Usage

```bash
make:controller <controller> [<folder>]
```

### Arguments

* `controller` (Required)
  * Controller Name

* `folder`
  * Folder Name

### Help

This command allows you to generate controller codes.

---


