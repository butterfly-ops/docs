# Smarty Helpers

## Email Operations

### Basic email
```twig
{% set subject = 'Important Update' %}
{% set message = 'Your request has been processed' %}
{{ sendEmail(recipient, subject, message) }}
```
### Template email

```twig
{% set template = 'welcome-email' %}
{% set vars = {
"username": "John",
"activation_link": "https://example.com/activate"
} %}
{{ sendEmailWithTemplate(recipient, template, vars) }}`
```

### Approval email

```twig
{% set subject = 'Approval Required' %}
{% set message = 'Please review and approve' %}
{{ sendApprovalEmail(subject, message, 'approval-template', 'email') }}
```

## SMS
```twig
{% set phone = '+905000000' %}
{% set message = 'Your verification code is 123456' %}
{{ sendSms(phone, message) }}
```

## File Operations

### Get file
```twig
{{ getFile(filePath, fileAlias) }}
```

### Get file content
```twig
{{ getFileContent(filePath, fileAlias) }}
```

### Delete file
```twig
{{ unlinkFile(localPath) }}
```

### Save image
```twig
{% set fileContent = getRequest('https://example.com/test.png') %}
{% set fileName = 'profile.png' %}
{% set alias = 'avatars' %}
{% set folder = 'users' %}
{% set response = saveImage(fileContent, fileName, alias, folder) %}
{{ response.success }}
{{ response.full_path }}
```

## Database Operations

### Listing Query
```twig
{% set query = getListingQuery() %}
{{ query
.where('status', 'active')
.orderByDesc('created_at')
.keyToValue('id', 'name')
}}
```

### Matrix Query
```twig
{% set matrix = getListingQuery()
.matrix('category', 'subcategory', 'count')
%}
```

### Vector Query
```twig
{% set vector = getListingQuery()
.vector('id', 'name', 'email')
%}
```

### Basic query

```twig
{% set users = db()
.from('users')
.where('status', 'active')
.get()
%}
```

### Complex query
```twig
{% set orders = db()
.from('orders')
.join('users', 'users.id', '=', 'orders.user_id')
.where('orders.status', 'pending')
.whereIn('orders.type', ['retail', 'wholesale'])
.whereBetween('orders.created_at', [startDate, endDate])
.orderByDesc('orders.created_at')
.groupBy('orders.user_id')
.paginate(20, 1)
%}
```

## CRUD operations
```twig
{% set result = crud('default')
.table('products')
.insert({
'name': 'New Product',
'price': 99.99,
'status': 'active'
})
%}
```

## Value management
```twig
{% set columnName = 'status' %}
{% set value = 'active' %}
{{ setValue(columnName, value) }}
{% set currentValue = getValue(columnName) %}
```

## Excel Operations
```twig
{% set excel = excel('Sales Report') %}
{{ excel
.sheet('Overview')
.fromArray(data)
.cell('A1', 'Sales Data')
.merge('A1:D1')
.bold('A1:D1')
.width('A', 15)
.alignText('A1', 'center', 'center')
.formatNumber('B2:B10', 2)
.formatCurrency('C2:C10', '$')
.freeze('A2')
.border('A1:D10')
.download('report.xlsx')
}}
```

## Filters

### Array operations
```twig
{% set items = ['apple', 'banana'] %}
{{ items|add('orange') }}
{{ items|push('grape') }}
{{ items|count }}
{{ items|chunk(2) }}
```

## String operations
```twig
{{ 'Hello World'|truncate(5) }}
{{ 'Product Name'|slug }}
{{ '42.5'|floatVal }}
{{ '42'|intVal }}
{{ 'a,b,c'|explode(',') }}
```

## Data visualization
```twig
{% set chartData = {
'January': {'sales': 100, 'costs': 80},
'February': {'sales': 150, 'costs': 100},
'March': {'sales': 200, 'costs': 150}
} %}
{{ chartData|dataset({'January': 'Jan', 'February': 'Feb'})|chart('line') }}
```

## Table view
```twig
{% set tableData = [
{'id': 1, 'name': 'John', 'email': 'john@example.com'},
{'id': 2, 'name': 'Jane', 'email': 'jane@example.com'}
] %}
{{ tableData|table({
'id': 'ID',
'name': 'Name',
'email': 'Email'
}, [
'<a href="/edit/<id>" class="btn">Edit</a>',
'<a href="/delete/<id>" class="btn">Delete</a>'
]) }}
```

## Configuration and Registry
```twig
{{ 'app.debug'|config }}
{{ 'cache_key'|registry }}
{{ 'user_preferences'|registry(userPrefs) }}
```

## Path handling
```twig
{{ path({'alias': 'uploads', 'type': 'file', 'full': true}) }}
{{ imagePath('avatars') }}
{{ filePath('documents') }}
```

## State Management
```twig
{{ error_message('Validation failed') }}
{{ confirm('Are you sure?') }}
{{ notValid() }}
{{ validHidden() }}
{{ validRequire('Please fill required fields') }}
```

### HTTP Requests
```twig
{{ getRequest(endpoint, options) }}
{{ postRequest(endpoint, vars, options) }}
```

## User and Permissions
```twig
{{ currentUser('role_id') }}
{{ hasPermission('edit') }}
```

## GPT Integration
```twig
{% set gptClient = gpt('gpt-4-mini') %}
```

## URL and Parameters
```twig
{{ currentUrl() }}
{{ getParameter('page', 1) }}
{{ getAllParameters() }}
```

## Header
```twig
{% block header %}
{% endblock %}
```

## Footer
```twig
{% block footer %}
{% endblock %}
```