# Helpers

## Server

Server Helpers are used to access system informations.

### `isWindows`

Returns `true` if the operating system of Server is Windows, returns `false` otherwise.

Example:

```php
$helper = new \Butterfly\Framework\Helper\Server();
$isWindows = $helper->isWindows();
```
