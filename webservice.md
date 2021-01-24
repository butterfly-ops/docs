# Webservice

## Authentication

In order to use webservices, you need to log in to webservice.

Example:

```curl
curl --location --request POST '##BASE_URL##/api/auth/generateToken' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'api_key=##API_KEY##' \
--data-urlencode 'password=##PASSWORD##'
```

Response:

```json
{
    "success": true,
    "token": "600dd1d69983a4.72658127-6ae75bff5b0a4de826de2a93510241a1",
    "expires_at": 1611522022
}
```

Then, you should use token in further requests,

HTTP_BUTTERFLY_API_KEY: Api Key of the authenticating user.
HTTP_BUTTERFLY_ACCESS_TOKEN: Access token received from Authentication

Example:

```curl
curl --location --request POST 'https://vdf.rglabs.co/api/upload/image' \
--header 'HTTP_BUTTERFLY_API_KEY: ##API_KEY##' \
--header 'HTTP_BUTTERFLY_ACCESS_TOKEN: 600dd1d69983a4.72658127-6ae75bff5b0a4de826de2a93510241a1' \
--form 'files[]=@"/Users/butterfly/examples/logos/test.jpeg"' \
--form 'files[]=@"/Users/butterfly/examples/logos/test2.png"'
```