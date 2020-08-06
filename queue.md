# Queue

## Introduction

When you have higher work loads or long running operations; you can use Queue's to send these long running to background 
and respond quickly.

Advantages of using Queue's are:
- You can limit number of jobs running concurrently
- You can postpone long-running operations and respond quicker
- You can split jobs into pieces and parallel process

## Configuration

Queue configurations are in `app/Config/queue.php`. You can use Redis or RabbitMQ as the Queue Manager.

> [!TIP]
> If you want to use different configurations for different domains, you can simply put configuration file in `app/Config/example.domain/queue.php` to differentiate 
> configuration for specific domain.

Example Redis Configuration:

```php
<?php

return [
    'type' => 'redis',
    'resque' => 'localhost:6379'
];
```

Example RabbitMQ Configuration:

```php
<?php

return [
    'type' => 'rabbitmq',
    'server' => 'localhost' // Default port for RabbitMQ is 5672
];
```

## Running Workers

You can run multiple jobs per server. Redis / RabbitMQ Server will handle not to run the same job more than once.

In order to run the jobs, you can run the following command:

```bash
## * is the queue_name and 1 is the worker count. 
bin/butterfly queue:worker:start '*' 1
```

> [!TIP]
> When you start 1 worker, it will stay attached to the screen, you can stop jobs by using CTRL + C.
> If you start more than 1 worker, then you can use `bin/butterfly queue:worker:kill` command to stop workers.

