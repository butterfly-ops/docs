# Security

Butterfly has security features out of box. We follow the guides of OWASP regularly and since Butterfly is used by enterprise companies, we run regular security tests to ensure it's as secure as possible.

Altough it has security features, developers should follow this guide:

## CSRF Token

CSRF Tokens are composed of two parts:

- Token Generation
- Token Validation

### Token Generation

In order to generate a token (to use on client side) you can use the following code:

```php
$csrf = new \Butterfly\Framework\Security\Csrf();
$csrf->token();
```

this function will return a token with generated timestamp on it.

### Token Validation

For validation, you can use the following code on controller:

```php
$token = \Input::get('csrf_token');
$csrf = new \Butterfly\Framework\Security\Csrf();

try {
    $csrf->check($token);
} catch (\Exception $e)
{
    // Error case.
}
```

## SQL Queries

Using User Input Parameters in SQL Queries is most common pitfall which causes SQL Injection attacks. You should 
consider using parameter binding instead of using un-safe user input in SQL Queries.

All database functions in Butterfly uses parameter binding by default. You can leverage these functions to write secure code.

Wrong Usage Example:

```php
$userIdInput = \Input::get('userIdInput');
db()->where('id = ' . $userIdInput);
```

Correct Usage Example:

```php
$userIdInput = \Input::get('userIdInput');
db()->where('id', $userIdInput);
```

in the correct usage, user parameter is sent to MySQL Server using PDO Parameter Binding, which means that, an attacker 
can not manipulate query by just manipulating the input data itself. 

You can check [database](#database) documentation for more usage examples.

## Accessing Real IP Address

Logging user activities and ip addresses is important for a secure system. Butterfly Admin Panel automatically logs this information 
for your security.

If you're using a Load Balancer, there may be a confusion about IP Address since IP Address of the Load Balancer may replace the user's Real IP Address.

You can set the correct IP Header from `app/security.php`.

Example:
```php
[
    'ip_header' => 'HTTP_X_FORWARDED_FOR'    
];
``` 

will use the X-Forwarded-For Header set from Load Balancer.

If you need to access IP Address from `app` directory, you can use the following function:

```php
    $helper = new \Butterfly\Framework\Helper\Request();
    $ip = $helper->getIpAddress();
```

> [!TIP]
> You can check from Admin Panel > Settings screen if your IP Address is set correctly or not. On the right top corner, IP Address is shown.

> [!WARNING]
> Ask your Devops team before setting this parameter since setting a not-existing header may cause a security leak since hackers may set 
> override a non-existing parameter.