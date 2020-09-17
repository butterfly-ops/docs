# Installation

## Server Requirements

Butterfly has minimum requirements on server side. 

**Required:**

* PHP >= 7.1
* MySQL 5.7+
* JSON PHP Extension
* Mbstring PHP Extension
* OpenSSL PHP Extension
* PDO PHP Extension 
* GD2 PHP Extension
* Exif PHP Extension
* Zip PHP Extension

**Recommended:**

* Imagick  

*Optional:*

* XML PHP Extension
* Soap PHP Extension

>For Ubuntu 18.04, you can use the following command to install extensions

```bash
apt-get install php7.4 php7.4-json php7.4-xml php7.4-exif php7.4-gd2
```

## Installing Butterfly

Butterfly uses [Composer](https://getcomposer.org/) to manage dependencies and packages. You can easily install packages using the following command:

```bash
/usr/local/bin/composer create-project butterfly/butterfly my_new_project --repository-url=https://repo.rglabs.co/
```

> [!NOTE]
> You we need access token to access repo.rglabs.co and git repository.

### Running installation

After changing to butterfly directory, you need to run installation script:

```bash
bin/butterfly install
```

> [!WARNING]
> You should create MySQL Database, Grant permission to user before running installation script. 
> Even for root users, you need to create database.

> [!TIP]
> ***Recommended Database Encoding:*** utf8mb4, Collation: utf8mb4_general_ci. You can choose the collation suits to your language.

You will be prompt to enter environment variables. You will need the following information:

Parameter | Description
--- | ---
Domain | This is the domain which butterfly will run on without schema. Example: butterfly.rg 
Database Server Host | Hostname of the database server
Database Server Username | Username for the database server
Database Server Password | Password for the database server
Database Name | Database name that is created.

!> **Caution:** In order to finish installation, there should be no tables in the database.

- Admin E-mail
- Admin Username
- Password (Auto generated if empty)

After the installation, you will see the admin information in shell.

```bash
Butterfly is successfully installed ! You can use the following information to access your panel:

https://butterfly.test/admin

Username: info@thebutterfly.io
Password: aji1854843!@Xsz
```

If you already created the tables, you can skip the database installation `--skip-database` option. Following command will check for the needed folders, will create a user.

```bash
bin/butterfly install --skip-database 1
```

### Folder Creation

Butterfly needs the following folders to be owned by web server user. (Or chmod 777).

> [!NOTE]
> install command automatically calls this command after checking database. You don't need to run this command if you
> run install command. 

```
- var
    |- cache
    |- log
    |- tmp
- static
```

If you don't have the folders, you can run the following command to check or create folders:

```bash
bin/butterfly folders:create
```

If script cannot create or chmod folders, it will print the commands that should be run. You can also run the 
following commands if you need in the root directory of the project.

```bash
cd $PROJECT_DIRECTORY; ## Please change directory to project root.
mkdir static var var/tmp var/cache var/log;
chmod -R 777 var static;
```

### Configurations

Config files are located in `app/Config` folder. When there are more than one environment, it is possible to override configuration.

#### Environment Based Override

Sometimes, you may have multiple domains in the same server / folder with same configuration. For this case, you can have a folder for that environment. Butterfly prioritize `app/Config/ENVIRONMENT` for configurations. Environment is set from your Web Server. For example, if the environment is set to `production`, it will first check 
`app/Config/production/` folder for configurations. Files in the root folder will be appended to configurations.

>[!TIP]
> You can add generic configs which are valid for all environments to `app/Config` folder, then you can only put environment specific configurations 
> like database to domain folders.

Apache Example for setting Environment:
```apacheconfig
SetEnv ENVIRONMENT production
```

Nginx Example for setting Environment:
```nginx
fastcgi_param  ENVIRONMENT "production";
```

#### Domain Based Override

`Butterfly` prioritize `app/Config/DOMAIN_NAME` for configurations. For example, if the domain name is thebutterfly.io, it will first check 
`app/Config/thebutterfly.io/` folder for configurations. Files in the root folder will be appended to configurations.

>[!TIP]
> You can add generic configs which are valid for all environments to `app/Config` folder, then you can only put environment specific configurations 
> like database to domain folders.

### Admin User Creation

You may need to create new users when you initiated an empty project or you need another account. You can run the 
following command to create a new user:

```bash
bin/butterfly admin:user:create
```

The command will prompt for e-mail, password and name of the user. Name is optional.