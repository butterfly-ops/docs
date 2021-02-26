# Commands

You can see list of commands by running `bin/butterfly` command.

## Listing Commands

`bin/butterfly list`

will return:

```
Available commands:
  health-check              Checks system resources and connections
  help                      Displays help for a command
  install                   Installs the Butterfly
  list                      Lists commands
  upgrade                   Upgrades database schema
 admin
  admin:user:create         Creates admin user
 convert
  convert:twig              Convert Smarty templates to Twig
 cron
  cron:garbage-collector    Cleans up items table for not used items
  cron:refresh-items        Updates items table with the entity table information
 folders
  folders:create            Creates needed folders for Butterfly
 image
  image:webp:generate       Regenerates all aliases with webp support
 make
  make:command              Generates new Command for creating Command
  make:content-widget       Generates new Content Widget
  make:controller           Generates new Controller
  make:event                Generates new Event code
  make:event:object:detail  Generates new Event code
  make:hook                 Generates new Hook for creating hooks
  make:model                Generates new Model
  make:twig:filter          Generates new Twig Filter
  make:twig:function        Generates new Twig Function
  make:widget               Generates new Widget
 object
  object:migration:create   Generates Migration For Existing Objects
 publish
  publish:admin:controller  Publishes custom controller for admin panel controller customizations
  publish:admin:layout      Publishes admin layout for customizations
  publish:admin:template    Publishes templates for admin panel template customizations
  publish:layout            Publishes frontend layout for customizations
  publish:template          Publishes frontend templates for customizations
 queue
  queue:worker:kill         Kill Queue Workers
  queue:worker:start        Runs Queue Workers
 search
  search:reindex            Creates a new Search index and populates with items
 set
  set:domain                Sets the Domain Name
 widget
  widget:refresh            Refreshes Widgets
```

## `health-check`

Checks system resources and connections

Example:

```bash
bin/butterfly health-check
```

will return:

```
✓ app/.domain file exists
Current Domain: butterfly.rg

Checking for folders in var folder
✓ Folders in var folder exists and writable

Found 5 database configs
Checking connection for default
✓ Successfully connected

Checking connection for default-test
✓ Successfully connected

Checking connection for elastic-search
✓ Successfully connected

Checking connection for slave
✓ Successfully connected

Checking connection for reports
✓ Successfully connected
```
