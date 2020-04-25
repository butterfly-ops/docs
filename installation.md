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
* Zip PHP Extension

**Recommended:**

* Imagick  

*Optional:*

* XML PHP Extension
* Soap PHP Extension

>For Ubuntu 18.04, you can use the following command to install extensions

```shell script
apt-get install php7.4 php7.4-json php7.4-xml
```

## Installing Butterfly

Butterfly uses [Composer](https://getcomposer.org/) to manage dependencies and packages. You can easily install packages using the following command:

```shell script
/usr/local/bin/composer create-project butterfly/butterfly my_new_project --repository-url=https://repo.rglabs.co/
```

!> **Caution:** You we need access token to access repo.rglabs.co and git repository.

### Running installation:

After changing to butterfly directory, you need to run installation script:

```shell script
bin/butterfly install
```

You will be prompt to enter environment variables. You will need the following information:

- Domain
- Database Server Host
- Database Server Username
- Database Server Password
- Database Name

!> **Caution:** In order to finish installation, target database should be empty.

- Admin E-mail
- Admin Username
- Password (Auto generated if empty)

After the installation, you will see the admin information in shell.

```shell script
Butterfly is successfully installed ! You can use the following information to access your panel:

https://butterfly.test/admin

Username: info@thebutterfly.io
Password: aji1854843!@Xsz
```