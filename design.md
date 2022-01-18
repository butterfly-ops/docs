# Introduction

Designs are the gateway for Butterfly Presentation Layer. You can manage your outputs using Designs. Designs are composed of Widgets.
If you are building a Webpage, Designs outputs HTML. If you are building a webservice, Designs outputs JSON data.

## Terminologies

### Designs

Let's move on with an example case:

- You want to build an Ecommerce Website.
- You have the following Pages:
    - Homepage
    - Product Detail Page
    - Category Listing Page
    - Cart Page

You can think each of these pages as Designs which means that, Designs are generic Look & Feels of your website. You don't need
to create different Designs for each Category or Product. You may have a single Product Detail Design for all Products.

>[!TIP]
> You can also define Design for a Specific Item or Group of Items. 

### Widgets

Widgets are the minor segments of Designs. For the Ecommerce Website Example, Let's think about Homepage,

- You have a Homepage Design,
- There are Header and Footer in the page,
- There is a Slider under Header.
- Best Selling Products
- Latest Products (with the Same Look & Feel with Best Selling Products)

In this case study, you will have the following Widgets: Header, Footer, Slider, ProductList

As you see, Best Selling Products and Latest Products are displayed using the same Widget with different Parameters.

## Frontend

When you build a website, frontend of the website is the pages that faces end users. (If it's a mobile app, it may be the api's).
All frontend can be managed from Butterfly Admin Panel using Drag and Drop features.

### Layouts

You may have multiple layout places in a Design like Header, Left Content, Right Content, Footer etc. These places are defined in Layout. Layout Places 
are defined with column sizes like 4-4-4-4, 12, 3-3-3, 9-3 etc. If you want to put a full page header, then, you can set the Layout Place size to 12.

### Partial Rendering

Even though you have multiple places on a Design, you may want to render it partially. For example, you may want to omit Header and Footer and render just Content section 
in a page for a specific embed.

You can add `renderPlaces` parameter as a GET parameter at the end of the request to render specific place.

Example:
```
https://butterfly.app/category-page?renderPlaces=content
```

will render just the widgets in layout place aliased as `content`.

You can also add multiple places seperated by comma.

Example:
```
https://butterfly.app/category-page?renderPlaces=header,content
```

will render just the widgets in layout place aliased as `header` and `content`.

## Personalization

## Content Pools

## Customizing Frontend Templates

### Layout

Layout is the default container template for Designs. By default, it outputs all widgets defined in the current design. 
If you want to customize layout, you can run the following command:

```bash
bin/butterfly publish:layout
```

### 404 Not Found

Not Found file is stored in Error404.twig file. By default, it displays Not Found message. If you want to customize 404 file,
you can run the following command:

```bash
bin/butterfly publish:template Error404
```

### 503 Server Error

When an error occurs in the system, it outputs 503 Server Error (Maintenance Page). Error file is stored in Error503.twig. 
If you want to customize 503 file, you can run the following command.

```bash
bin/butterfly publish:template Error503
```