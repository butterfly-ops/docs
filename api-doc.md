# Swagger API Documentation Generator

This document provides guidelines for creating API documentation using PHPDoc comments. These comments help generate API documentation automatically. Below are the formats and examples for various types of API actions.

## PHPDoc Comment Structure

### Required Annotations
- `@title`: A brief title of the API action.
- `@description`: A detailed description of the API action.
- `@method`: The HTTP method used (GET, POST, etc.).
- `@route`: The endpoint route of the API action.
- `@responseExample`: An example of the response returned by the API action.

### Optional Annotations
- `@param`: Parameters for the API action.
- `@header`: Headers required for the API action.

## Examples

### Example 1: GET Request to Get All People

```php
/**
 * Handle GET request to get all people.
 *
 * @title Get People
 * @description This action gets all people.
 * @method GET
 * @route /api/test/some
 * @responseExample { "status": "success", "message": "Hello World" }
 *
 * @return array
 */
public function someAction()
{
    $filter = \Input::get('filter');
    $sort = \Input::get('sort');

    return [
        'status' => 'success',
        'message' => 'Hello World'
    ];
}
```

### Example 2: POST Request for User Login

```php
/**
 * Handle POST request for user login.
 *
 * @title User Login
 * @description This action handles user login with a username and password.
 * @method POST
 * @route /api/test/someLogin
 * @param string $username The username of the user
 * @param string $password The password of the user
 * @responseExample { "status": "success", "message": "Hello World" }
 *
 * @return array
 */
public function someLoginAction($username, $password)
{
    return [
        'status' => 'success',
        'message' => 'Hello World'
    ];
}
```

### Example 3: POST Request for User Login with Token

```php
/**
 * Handle POST request for user login with a token.
 *
 * @title User Login with Token
 * @description This action handles user login using a token from the Authorization header.
 * @method POST
 * @route /api/test/someLoginWithToken
 * @header Authorization string Bearer token for authentication
 * @responseExample { "status": "success", "message": "Hello World" }
 *
 * @return array
 */
public function someLoginWithTokenAction()
{
    $header = \Request::header('Authorization');
    $token = str_replace('Bearer ', '', $header);

    return [
        'status' => 'success',
        'message' => 'Hello World'
    ];
}
```

## How to Use

1. **Define the PHPDoc comment**: Before each API action method, define the PHPDoc comment block with appropriate annotations.
2. **Add required and optional annotations**: Make sure to include all required annotations (`@title`, `@description`, `@method`, `@route` and `@responseExample`). Add optional annotations (`@param`, `@header`) where necessary.
3. **Create Documentation**: Use your document generation tool to automatically generate API documentation from these comments. If set, this deployment is also automatic.

By following these instructions, you can ensure that your API documentation is generated without any problems.