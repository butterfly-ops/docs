# Introduction

Butterfly uses multi-layer cache management. It's possible to use multiple caches at the same time. You can configure multiple caches and use it. Butterfly uses APC as the primary cache for the configuration files.

Default cache driver is registry on application cycle but you can use the following cache drivers: 

- Redis
- Memcached
- Apc
- Database

When you check Redis and other cache implementations you will see that it's written to make developer comfortable whether you 
are using Redis or Memcached. We have built a system with same behaviours independent from which driver you use. 

## Configuration

Butterfly Cache Implementation usages are similar to Butterfly Database implementation.   

The cache configurations are stored in `app/config/cache.php`. Configurations can be customized by domain name with subfolders.

## Redis

Before enable redis cache, please check [predis/predis package](https://github.com/predis/predis) installed.

Example configuration:

```php
<?php

return [
    'default' => 'backend', // default cache
    
    'backend' => [
        'driver' => 'Redis',
        'parameters' => [
            'scheme' => 'tcp',
            'host'   => '10.0.0.1',
            'port'   => 6379,
        ],
        'options' => [
            'prefix' => 'be:',
            'parameters' => [
                'password' => 'SECRET_PASSWORD',
                'database' => 10,
            ],
        ]    
    ],
    
    'frontend' => [
        'driver' => 'Redis',
        'parameters' => [
            'scheme' => 'tcp',
            'host'   => '10.0.0.1',
            'port'   => 6379,
        ],
        'options' => [
            'prefix' => 'fe:',
            'parameters' => [
                'password' => 'SECRET_PASSWORD',
                'database' => 10, 
            ],
        ]    
    ],
    
    'external' => [
        'driver' => 'Redis',
        'parameters' => [
            'scheme' => 'tcp',
            'host'   => '1.1.1.1',
            'port'   => 6379,
        ],
        'options' => [
            'prefix' => null,
            'parameters' => [
                'password' => 'SECRET_PASSWORD',
                'database' => 0, 
            ],
        ]    
    ],
];
```

> [!TIP]
> Further information for parameters and options, please read [predis/predis](https://github.com/predis/predis) documentation

## Database

Database cache needs to `database_cache` table. 
You can use following migration to create the table.

```
db()->schema('database_cache')->object(function(\Butterfly\Framework\Data\ButterflyObject $object) {
    $object->setDescription('Butterfly Database Cache');
    $object->string('cache_key', 'Cache Key');
    $object->textarea('value', 'Value');
    $object->integer('expire', 'Expire In Seconds');
    $object->datetimeMysql('created_at');
    $object->unique(['cache_key']);
    return $object;
});
```

Example configuration for database:

```
return [
    // other cache configurations in cache.php

    'foo' => [ 
        'driver' => 'Database',
        'prefix' => 'docs:'
    ]
];
```

Sample usage for the configuration:

```
cache('foo');
```


## Memcached

Before enable memcached cache, please check [memcached pecl package](https://pecl.php.net/package/memcached) installed and enabled.

Example configuration for memcached:

```
return [
    // other cache configurations in cache.php

    'bar' => [ 
        'driver' => 'Memcached',
        'servers' => [
            ['127.0.0.1', 11211]
        ],
        'prefix' => 'docs:'
    ]
];
```

Sample usage for the configuration:

```
cache('bar');
```


## Apc

Before enable apc cache, please check [apc pecl package](https://pecl.php.net/package/apc) installed and enabled.

Example configuration for apc:

```
return [
    // other cache configurations in cache.php

    'baz' => [ 
        'driver' => 'Apc',
        'prefix' => 'docs:'
    ]
];
```

Sample usage for the configuration:

```
cache('baz');
```

### Using The Cache Client

Cache client can be reached using `cache()` helper. You can also reach defined cache drivers using the cache alias as the first parameter.
 
```php
cache(); // Cache Driver defaults to default cache configuration.
```

Following function call will return a cache client connected to cache external defined in configuration.

```php
cache('external');
```

## Cache Operations

### GET

```php
$foo = cache()
    ->get('foo');
```

### SET

```php
$value = 'bar';
cache()
    ->set('foo', 'bar');
```

### DELETE

```php
cache()
    ->delete('foo');
```

### INCREMENT

Increment cached values with optional step amount.

```php
cache()
    ->increment('foo', 1);
```

### DECREMENT

Decrement cached values with optional step amount.

```php
cache()
    ->decrement('foo', 1);
```

### FLUSH

To clear all cache, use flush method to flush related cache source.

```php
cache()
    ->flush();
```
