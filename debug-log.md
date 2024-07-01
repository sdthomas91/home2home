# Bugs

## Users

 - Could not get signup form to display custom field to select user or host
    * Added profile_setup to views but still threw the same issue
    * identified incorrect path being used thanks to DEBUG - accounts/signup.html instead of "account"
    * corrected and form displayed with additional field

 - Cirspy Forms issues
    * could not get crispy forms to load to the system correctly - installed using pip
    * added to installed apps already, hadn't loaded correctly in signup.html {% load i18n crispy_forms_tags %}
    * still had issues - added CRISPY_TEMPLATE_PACK = Boostrap4 to settings and installed crispy_bootstrap4 using pip
    * not working still, realised I hadn't added crispy_bootstrap4 to installed apps
    * correct installed apps and now functioning correctly

- Profile viewing 
    * could not get profile page to load 
    * amended urls in project level urls.py (changed '' to 'users/') but this caused more errors
    * changed back to ('') and confirmed views were setup correctly - was missing the view for the profile page
    * updated views and urls and now loads correctly - good to add editing capabilities

- Profile editing 
    * Tried having a profile page that was editable, however it made for a clumsy look so will have a profile page and and edit profile page separate
    * edit page was showing the location of the current profile pic, which I didn't like - tried using Django widgets to get around this but kept getting bootstrap errors as I hid the checkbox for clear. 
    * Decided to leave it on for functionality but it will be a future feature

- Admin View
    * Wanted a way to distinguish between guests and hosts in the admin view
    * Constructed custom admin.py but had issues loading the page - followed [django documentation](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/filters/) to implement the filter view. Functions as hoped
    <img src="media/testing/django-filter.png">

- Properties
    * Issues migrating the properties/models.py file
        * When migrating forgot I had previously migrated a properties model and so had to run through some overrides.
        * In doing so, I provided a default date/time and mis formatted - used decimal instead of hyphen.
        * Caused many migration issues, tried using methods such as updating the database with the shell, to no avail as the table hadn't been created, data hadn't migrated so couldn't be altered. 
        * Manually amended the migration file in properties/migrations and this did the trick 
    * Issue with uploading properties.JSON - primary key issue
        * remembered I had to start host PK from 3 due to existing users on the system - amended host foreign key reference in the properties JSON.
        * foreign key constraints was not resolved and couldn't use loaddata - reverse engineered by adding property manually, dumping data into a JSON and comparing. After scanning all JSON data again realise there was a typo. Issue was not with hosts foreign key but amenities as had used 18 and there are only 17 pk's for amenities. 
        * amended to 1 instead of 18 and data uploaded 
    * Sorting in property admin not completely acccurate as it is going off host PK (integer) rather than username (alphabetical)
        * amended admin.py for properties to include custom sorting and ordering - now functions okay
    * Struggling with filtering form displaying well across all screens - got the JS working and the hide and display was perfect. However, when opened the filter options were all over the place
        * tried replacing amenities with a dropdown list, but the form itself wouldn't conform to screen width, and was cluttering the html with bootstrap classes
        * used the col method and was okay for the most part but still looked clumsy
        * changed plan and decided to go with Bootstrap modal for the filtering options, inspired by AirBnb interface. It is clean, easy to use and works responsively. 
    * Amenities ordering - wanted most popular amenities to be listed at the top - should have consideredd this when loading JSON data. Used django documentation and stack overflow to implement manual ordering within the admin interface. This worked nicely and now 8 top amenities show with a "show more" button
    * Map
        - Tried adding diferent sized maps but it actually made UI worse - only medium screens where it looks like too much white space. Will stick with 1 size map below all info

- Users
    * Profiles
        - difficulty choosing how to properly setup, as I wanted separate profiles for hosts and guests
        - Went with separation at signup stage by having a signup selection field - override standard allauth signup form
        - Couldn't get my form to load, realised I hadn't provided custom URL to override the allauth redirect
    * Profile setup
        - Had issues separating profile setup - couldn't get separate forms to load depending on host or guest
        - Realised I was overcomplicating the process. Decided to amalgamate the two and have one profile setup form. No fields were explicitly for host or guest anyway. 
    * Profile edit
        - Submitting profile edit worked to an extent but it would not update the name on the profile when you submitted first and last name
        - Identified the issue was with the user model - I had not added or migrated the first name and last name to the user model so there was nothing to update
        - Still not displaying - realised I also needed to update the django templating in the HTML as it was trying to pull a full name, but that isn't a specific field. Changed to first and last and works okay now
    
- Bookings
    * Booking form
        - Issues incorporating the booking form on the property_detail page - throwing a url error 
        - Had added booking URL's but not added to main URL's - easy fix
        - New issue thrown "Cannot assign "<Profile: mrHost>": "Booking.user" must be a "User" instance."
        - Fixed by amending view to include user instead of profile - another easy fix but generated a type error to address which was fixed by updating the booking model
        - Final issue was an operational one as I hadn't migrated the updated booking model - resolved and now need to proceed with checkout and basket to be able to fully test
        
- Basket
    * Adding to basket
        - Tried adding items to basket, had a few minor issues such as redirects to checkout (not created yet) but nothing major. 
        - Line items were missing values so could not generate a total value for the basket. Added in the fields and refreshed but kept populating with £0.00 
        - Tried a number of things including rebuilding the views and forms and reformatting template, but nothing was working.
        - Foolish mistake, existing bookings in the cart were created before model was updated and so had no values for total price etc. 
        - Created new booking and now displays correctly - need to add delete functionality to remove line items or clear basket

- Reviews
    * Displaying star rating
        - Tried displaying a star rating or "No Reviews Yet" on property page, but discovered [Django Star Rating](https://medium.com/geekculture/django-implementing-star-rating-e1deff03bb1c)
        - Implemented but want to replace the No Ratings Yet with 5 empty stars
        - Had to utilised some custom JS to add a star rating element to the write_review template - this worked with the fontawesome classes to provide a filled or empty star
        - Stars were remaining solid, reformatted JS to include an initial empty state, but this didn't show as empty
        - Realised I was using incorrect fontawesome - outdated from previous projects - needed to use fa-solid instead of fas
        - Once rectified classes and amended JS accordingly the star widget now works - need to ensure it uploads the rating to the database
        - Rating not populating on property_detail page and not displaying stars in carousels - need to revise property model I think to get an average rating, rather than just the single rating
        - Stars_rating actually seemed to make things more complex, unnecessarily, especially when it came to displaying the average rating of a property - instead decided to try modifying the property model. It kept bugging but settled on calculating the average rating, and then adding a custom star generation within the model itself. The logic in html was too cluttered and clumsy and made for a messy UI. 
        - Settled on the model logic, clean and works well. Means I can display it across multiple areas such as reviews carousels etc. if needed
    * Review carousel
        - Managed to amend logic similar to star ratings in order to get stars to appear correctly on user reviews. 
        - Cannot get the edit button to be clickable - have corrected urls etc. but no luck
        - Think the issue may be down to carousel style - think the carousel controls overlap the button - will try center aligning button
        - rectified issue, for now will stick with loading the latest reviews - possibly the latest 2 for styling purposes
        - Tested functionality and now the review can be edited and when edited it affects the property average rating. Seaside Haven is best for viewing as it has reviews loaded on - will load more via JSON.
        
