Introduction
============

This is a full-blown functional test. The emphasis here is on testing what
the user may input and see, and the system is largely tested as a black box.
We use PloneTestCase to set up this test as well, so we have a full Plone site
to play with. We *can* inspect the state of the portal, e.g. using 
self.portal and self.folder, but it is often frowned upon since you are not
treating the system as a black box. Also, if you, for example, log in or set
roles using calls like self.setRoles(), these are not reflected in the test
browser, which runs as a separate session.

Being a doctest, we can tell a story here.

First, we must perform some setup. We use the testbrowser that is shipped
with Five, as this provides proper Zope 2 integration. Most of the 
documentation, though, is in the underlying zope.testbrower package.

    >>> from Products.Five.testbrowser import Browser
    >>> browser = Browser()
    >>> portal_url = self.portal.absolute_url()

The following is useful when writing and debugging testbrowser tests. It lets
us see all error messages in the error_log.

    >>> self.portal.error_log._ignored_exceptions = ()

With that in place, we can go to the portal front page and log in. We will
do this using the default user from PloneTestCase:

    >>> from Products.PloneTestCase.setup import portal_owner, default_password

Because add-on themes or products may remove or hide the login portlet, this test will use the login form that comes with plone.  

    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()

Here, we set the value of the fields on the login form and then simulate a
submit click.  We then ensure that we get the friendly logged-in message:

    >>> "You are now logged in" in browser.contents
    True

Finally, let's return to the front page of our site before continuing

    >>> browser.open(portal_url)

-*- extra stuff goes here -*-
The Publication content type
===============================

In this section we are tesing the Publication content type by performing
basic operations like adding, updadating and deleting Publication content
items.

Adding a new Publication content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Publication' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Publication').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Publication' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Publication Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Publication' content item to the portal.

Updating an existing Publication content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Publication Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Publication Sample' in browser.contents
    True

Removing a/an Publication content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Publication
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Publication Sample' in browser.contents
    True

Now we are going to delete the 'New Publication Sample' object. First we
go to the contents tab and select the 'New Publication Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Publication Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Publication
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Publication Sample' in browser.contents
    False

Adding a new Publication content item as contributor
------------------------------------------------

Not only site managers are allowed to add Publication content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Publication' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Publication').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Publication' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Publication Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Publication content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Gallery content type
===============================

In this section we are tesing the Gallery content type by performing
basic operations like adding, updadating and deleting Gallery content
items.

Adding a new Gallery content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Gallery' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Gallery').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Gallery' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Gallery Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Gallery' content item to the portal.

Updating an existing Gallery content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Gallery Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Gallery Sample' in browser.contents
    True

Removing a/an Gallery content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Gallery
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Gallery Sample' in browser.contents
    True

Now we are going to delete the 'New Gallery Sample' object. First we
go to the contents tab and select the 'New Gallery Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Gallery Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Gallery
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Gallery Sample' in browser.contents
    False

Adding a new Gallery content item as contributor
------------------------------------------------

Not only site managers are allowed to add Gallery content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Gallery' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Gallery').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Gallery' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Gallery Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Gallery content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Seminar content type
===============================

In this section we are tesing the Seminar content type by performing
basic operations like adding, updadating and deleting Seminar content
items.

Adding a new Seminar content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Seminar' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Seminar').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Seminar' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Seminar Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Seminar' content item to the portal.

Updating an existing Seminar content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Seminar Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Seminar Sample' in browser.contents
    True

Removing a/an Seminar content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Seminar
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Seminar Sample' in browser.contents
    True

Now we are going to delete the 'New Seminar Sample' object. First we
go to the contents tab and select the 'New Seminar Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Seminar Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Seminar
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Seminar Sample' in browser.contents
    False

Adding a new Seminar content item as contributor
------------------------------------------------

Not only site managers are allowed to add Seminar content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Seminar' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Seminar').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Seminar' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Seminar Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Seminar content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The FAQ content type
===============================

In this section we are tesing the FAQ content type by performing
basic operations like adding, updadating and deleting FAQ content
items.

Adding a new FAQ content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'FAQ' and click the 'Add' button to get to the add form.

    >>> browser.getControl('FAQ').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'FAQ' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'FAQ Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'FAQ' content item to the portal.

Updating an existing FAQ content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New FAQ Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New FAQ Sample' in browser.contents
    True

Removing a/an FAQ content item
--------------------------------

If we go to the home page, we can see a tab with the 'New FAQ
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New FAQ Sample' in browser.contents
    True

Now we are going to delete the 'New FAQ Sample' object. First we
go to the contents tab and select the 'New FAQ Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New FAQ Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New FAQ
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New FAQ Sample' in browser.contents
    False

Adding a new FAQ content item as contributor
------------------------------------------------

Not only site managers are allowed to add FAQ content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'FAQ' and click the 'Add' button to get to the add form.

    >>> browser.getControl('FAQ').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'FAQ' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'FAQ Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new FAQ content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Career content type
===============================

In this section we are tesing the Career content type by performing
basic operations like adding, updadating and deleting Career content
items.

Adding a new Career content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Career' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Career').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Career' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Career Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Career' content item to the portal.

Updating an existing Career content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Career Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Career Sample' in browser.contents
    True

Removing a/an Career content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Career
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Career Sample' in browser.contents
    True

Now we are going to delete the 'New Career Sample' object. First we
go to the contents tab and select the 'New Career Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Career Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Career
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Career Sample' in browser.contents
    False

Adding a new Career content item as contributor
------------------------------------------------

Not only site managers are allowed to add Career content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Career' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Career').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Career' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Career Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Career content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The CIP in the News content type
===============================

In this section we are tesing the CIP in the News content type by performing
basic operations like adding, updadating and deleting CIP in the News content
items.

Adding a new CIP in the News content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'CIP in the News' and click the 'Add' button to get to the add form.

    >>> browser.getControl('CIP in the News').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'CIP in the News' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'CIP in the News Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'CIP in the News' content item to the portal.

Updating an existing CIP in the News content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New CIP in the News Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New CIP in the News Sample' in browser.contents
    True

Removing a/an CIP in the News content item
--------------------------------

If we go to the home page, we can see a tab with the 'New CIP in the News
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New CIP in the News Sample' in browser.contents
    True

Now we are going to delete the 'New CIP in the News Sample' object. First we
go to the contents tab and select the 'New CIP in the News Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New CIP in the News Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New CIP in the News
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New CIP in the News Sample' in browser.contents
    False

Adding a new CIP in the News content item as contributor
------------------------------------------------

Not only site managers are allowed to add CIP in the News content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'CIP in the News' and click the 'Add' button to get to the add form.

    >>> browser.getControl('CIP in the News').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'CIP in the News' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'CIP in the News Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new CIP in the News content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


