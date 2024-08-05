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

#### Example: Checking for Validation Errors

In the following example, the `someAction` method validates incoming data and checks for validation errors.

```php
use Symfony\Component\Validator\Constraints as Assert;

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
use Symfony\Component\Validator\Constraints as Assert;

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

## Custom Rule

This section explains how to create and use a custom validation rule in Validator. We will use the example of validating an American phone number format.

## Step-by-Step Guide to Creating a Custom Rule

### Create Folder Structure

Create the following folder structure in your project:

```
Project Path

├── app
│   ├── Validator
│   │   ├── AmericanNumber.php
│   │   └── AmericanNumberValidator.php
```

### 1. Create the Constraint Class

First, create a constraint class that defines the validation message and the validator class it uses.

```php
<?php

namespace App\Validator;

use Symfony\Component\Validator\Constraint;

/**
 * @Annotation
 */
class AmericanNumber extends Constraint
{
    public string $message = 'The string "{{ string }}" is not a valid American number.';

    public function validatedBy(): string
    {
        return 'App\Validator\AmericanNumberValidator';
    }
}
```

### 2. Create the Validator Class

Next, create the validator class that contains the logic for validating the value.

```php
<?php

namespace App\Validator;

use Symfony\Component\Validator\Constraint;
use Symfony\Component\Validator\ConstraintValidator;
use Symfony\Component\Validator\Exception\UnexpectedTypeException;
use Symfony\Component\Validator\Exception\UnexpectedValueException;

class AmericanNumberValidator extends ConstraintValidator
{
    public function validate($value, Constraint $constraint): void
    {
        if (!$constraint instanceof AmericanNumber) {
            throw new UnexpectedTypeException($constraint, AmericanNumber::class);
        }

        if (null === $value || '' === $value) {
            return;
        }

        if (!is_string($value)) {
            throw new UnexpectedValueException($value, 'string');
        }

        if (preg_match('/^\d{3}-\d{3}-\d{4}$/', $value)) {
            return;
        }

        $this->context->buildViolation($constraint->message)
            ->setParameter('{{ string }}', $value)
            ->addViolation();
    }
}
```

### 3. Use the Custom Rule

Finally, use the custom validation rule in your code.

```php
use App\Validator\AmericanNumber;

if ($response = $this->validate([
    'phone_number' => [
        new AmericanNumber(),
    ],
])) {
    return $response;
}
```

### Summary Custom Rule

To create a custom validation rule in Symfony Validator:

1. Create folder structure.
2. **Create the Constraint Class**: Define the validation message and the validator class.
3. **Create the Validator Class**: Implement the validation logic.
4. **Use the Custom Rule**: Apply the custom rule in your validation logic.

By following these steps, you can create custom validation rules tailored to your specific requirements.

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