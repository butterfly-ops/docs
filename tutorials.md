# Tutorials

## How to Create an Articles Page

### Create Object Type

- Go to Objects page
- Click on Add New Record
- Fill out the form as follows

Name: Articles (User Friendly name of the Object Type)
Table Name: articles (Table name of the Object (lower case, no psecial characters))
SEO: article/%name% (which will automatically create links using the `name` field from article)
Menu: Main Menu (which will create a main level menu for the new Object Type)
Has Item: Checked
Design: (to be defined after creating new design) /* TODO: Add create new design button */

- Click save and it will redirect automatically to add new Object Spec Page.
- Fill out the form as follows to add a new field to Object Type:

Name: Name (User Friendly name of the field)
Type: string (It will be a text field)
Listed: Checked (To be listed in Listing Page)
Required: Checked
Searchable: Checked
Menu: Main Menu (to Create a link on Admin Panel)

- Click save and it will reload to add a new field.

- Now we have a table named `articles` in our database,
- We have an Admin Panel that we can search, add, edit or delete contents.