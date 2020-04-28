# Admin Panel

One of the most important features of Butterfly is it's Admin Panel. 
- You can create new Objects,
- Create / Update Object Fields
- Create / Edit your Content Sources,
- Create / Edit your API's,
- Manage your Content
- Manage Search Engine Settings,
- Change Look & Feel of your Applications
- Drag & Drop new Widgets to your Applications

and many more ...    

## Objects

Every created object comes with special management screens. You can list, add, edit, 
from it's auto-generated admin panel. You can even bulk edit, import or export your data. Besides having many unique features, 
Management Screens can be customized easily.

### Customizations

Let's think that you have an Object named: Articles. Fields in Users object are: title, introduction and content. Admin panel link
of this page will be: `/admin/article/list`.  

#### Listing Page

If you want to customize listing page, you can create a file called list.tpl as `app/Views/Cms/article/list.tpl`

When you create an empty file, you can see that, listing page will also change to a blank page. If you want your custom 
page to work just like it was, you can place the following code to your template file.

```smarty
{include_tpl file="object/list"}
``` 

Now, you have a listing page, just working as it was but now, you can add new code blocks to top or bottom of the page.

> [!TIP]
> You can use `bin/butterfly publish:admin:template articles list` command to generate customization template.

You may want to change look & feel or functionality of a specific Object Field.

Example:

If you want to change look & feel of title column of articles object, then you can create a file in `app/Views/Cms/article/list/title.tpl`

When you create an empty template, you can see that the field will be empty in listing page. You have a variable named `$l` in the template.

If you want to display of your field you can use the following code:

```smarty
{$l[$os.column_name]}
```

or, you can use the field name instead

```smarty
{$l.title}
```

> [!TIP]
> You can use `bin/butterfly publish:admin:template articles list title` command to generate customization template for specific field.

#### Add Page

If you want to customize add page, you can create a file called add.tpl as `app/Views/Cms/article/add.tpl`

When you create an empty file, you can see that, add form page will also change to a blank page. If you want your custom 
page to work just like it was, you can place the following code to your template file.

```smarty
{include_tpl file="object/add"}
``` 

Now, you have a add form page, just working as it was but now, you can add new code blocks to top or bottom of the page.

> [!TIP]
> You can use `bin/butterfly publish:admin:template articles add` command to generate customization template.

#### Edit Page

If you want to customize add page, you can create a file called edit.tpl as `app/Views/Cms/article/edit.tpl`

When you create an empty file, you can see that, edit form page will also change to a blank page. If you want your custom 
page to work just like it was, you can place the following code to your template file.

```smarty
{include_tpl file="object/edit"}
``` 

Now, you have a edit form page, just working as it was but now, you can add new code blocks to top or bottom of the page.

> [!TIP]
> You can use `bin/butterfly publish:admin:template articles edit` command to generate customization template.
   

 