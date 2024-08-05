# Usage of Validator

This document provides a detailed guide on how to use the `Validator` feature.

## Using the `Validator` Trait

### 1. Include the Trait in Your Class

First, you need to include the `Validator` trait in the class where you want to use it.

```php
use Butterfly\Core\Trait\Validator;

class SomeClass
{
    use Validator;

    ...
}
```

### 2. Using Validation

#### Example 1: Checking for Validation Errors

In the following example, the `someAction` method validates incoming data and checks for validation errors.

```php
public function someAction()
{
    // Validate incoming data
    if ($response = $this->validate([
        'filter' => [
            new Assert\Required(),
            new Assert\NotBlank(),
        ],
        'sort' => new Assert\Optional()
    ])) {
        // If there are errors, return the response containing the errors
        return $response;
    }

    // Get validated data
    $filter = \Input::get('filter');
    $sort = \Input::get('sort');

    // Return a successful response
    return [
        'status' => 'success',
        'message' => 'Hello World'
    ];
}
```

#### Example 2: Using Validation Without Checking the Result

In this example, the result of the `validate` method is not checked directly. However, make sure to handle validation errors properly.

```php
public function someAction()
{
    // Validate incoming data
    $this->validate([
        'filter' => [
            new Assert\Required(),
            new Assert\NotBlank(),
        ],
        'sort' => new Assert\Optional()
    ]);

    // Get validated data
    $filter = \Input::get('filter');
    $sort = \Input::get('sort');

    // Return a successful response
    return [
        'status' => 'success',
        'message' => 'Hello World'
    ];
}
```

## Defining Validation Rules

With Symfony Validator, you can define various validation rules. Here are some examples:

```php
use Symfony\Component\Validator\Constraints as Assert;

$rules = [
    'name' => [
        new Assert\Required(),
        new Assert\NotBlank(),
        new Assert\Length(['min' => 3, 'max' => 50])
    ],
    'email' => [
        new Assert\Required(),
        new Assert\Email()
    ],
    'age' => [
        new Assert\Optional(),
        new Assert\Type('integer'),
        new Assert\Range(['min' => 18, 'max' => 99])
    ]
];
```

You can pass these rules as a parameter to the `validate` method.

```php
public function someAction()
{
    $rules = [
        'name' => [
            new Assert\Required(),
            new Assert\NotBlank(),
            new Assert\Length(['min' => 3, 'max' => 50])
        ],
        'email' => [
            new Assert\Required(),
            new Assert\Email()
        ],
        'age' => [
            new Assert\Optional(),
            new Assert\Type('integer'),
            new Assert\Range(['min' => 18, 'max' => 99])
        ]
    ];

    if ($response = $this->validate($rules)) {
        return $response;
    }

    // Process validated data
    $name = \Input::get('name');
    $email = \Input::get('email');
    $age = \Input::get('age');

    return [
        'status' => 'success',
        'message' => 'Data validated successfully'
    ];
}
```

These examples demonstrate how to use the `validate` method and define validation rules. With the flexibility of Symfony Validator, you can easily define and use validation rules that suit your needs.

## Customised Language

Customize language for validation messages.

To override the default language file, we need to open the `Langs/validations` folders under the `app` folder. Then we create the file for the language we want. `Ex. (lang.en.php)`

It will be enough to add the text we want to translate. You can find an example below.

```php
return [
    'This value should be blank.' => 'This place can\'t be left empty.',
    ...
    ...
];
```