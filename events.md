# Introduction

Events are designed to make changes in behaviours of Butterfly or run custom codes inside of `Butterfly Core`. 

## Frontend

Frontend events are triggered while startup of the Application.

### `bootstrap`

To create a Bootstrap hook, you can run the following command:

```bash
bin/butterfly make:event Frontend Bootstrap
```

> [!TIP]
> Frontend>Bootstrap event doesnt have any parameters. You can use this event to run codes which should be ran for all requests.

> [!WARNING]
> Don't forget that, the code written inside of Frontend>Bootstrap event will run for each request which means that it may decrease 
> performance of your website.