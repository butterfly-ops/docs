# Swagger API Documentation Generator

This document provides guidelines for creating API documentation using PHPDoc comments. These comments help generate API documentation automatically. Below are the formats and examples for various types of API actions.

## PHPDoc Comment Structure

### Required Annotations
- `@title`: A brief title of the API action.
- `@description`: A detailed description of the API action.
- `@defaultMethod`: The HTTP method used (GET, POST, etc.).
- `@route`: The endpoint route of the API action.
- `@responseExample`: An example of the response returned by the API action.

### Optional Annotations
- `@parametereter`: Parameters for the API action.
- `@header`: Headers required for the API action.

## Examples

### Example 1: GET Request to Get All People

```php
/**
 * Handle GET request to get all people.
 *
 * @title Get People
 * @description This action gets all people.
 * @defaultMethod GET
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

You can use optional parameters in the `@parameter` or `@header` annotations to indicate whether a parameter is required or optional. For example, `@parameter string $cookies The cookies of the user (optional)` specifies that the cookies parameter is optional.

Additionally, you can set a default value for a parameter using the `| default:value` syntax. For instance, `@parameter string $source The source of the user | default:web` means that if the source parameter is not provided, it defaults to web.

```php
/**
 * Handle POST request for user login.
 *
 * @title User Login
 * @description This action handles user login with a username and password.
 * @defaultMethod POST
 * @route /api/test/someLogin
 * @parameter string $username The username of the user
 * @parameter string $password The password of the user
 * @parameter string $cookies The cookies of the user (optional)
 * @parameter string $source The source of the user | default:web
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

The `@tags` annotation allows you to categorize your API actions for better organization and navigation in your documentation. For instance, using `@tags` Auth, User will classify an action under both the Auth and User categories. This grouping makes it easier to locate and understand different API actions within the documentation.

```php
/**
 * Handle POST request for user login with a token.
 *
 * @title User Login with Token
 * @description This action handles user login using a token from the Authorization header.
 * @defaultMethod POST
 * @route /api/test/someLoginWithToken
 * @header Authorization string Bearer token for authentication
 * @tags Auth, User
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
2. **Add required and optional annotations**: Make sure to include all required annotations (`@title`, `@description`, `@defaultMethod`, `@route` and `@responseExample`). Add optional annotations (`@parameter`, `@header`) where necessary.
3. **Create Documentation**: Use your document generation tool to automatically generate API documentation from these comments. If set, this deployment is also automatic.

By following these instructions, you can ensure that your API documentation is generated without any problems.
