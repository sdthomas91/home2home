# Testing

The Gather recipe website has been tested using the following methods:
- [Code Validation](#code-validation)
    - [W3C HTML Validator](#w3c-html-validator) 
    - [W3C CSS Validator](#w3c-css-validator)
    - [JSHINT Javascript Code Quality Tool](#jshint-javascript-code-quality-tool)
    - [Python Validation using Gitpod](python-validation-using-gitpod)
    
- [Accessibility](#accessibility)
    - [Colour Contrast](#colour-contrast)
    - [Wave Webaim Accessibility Checker](#wave-webaim-accessibility-checker)
- [Lighthouse](#lighthouse)
- [Responsiveness](#responsiveness)
- [Browser Compatibility](#browser-compatibility)
- [Testing User Stories](#testing-user-stories)
    - [First Time User](#first-time-user)
    - [Returning User](#returning-user)
    - [Business Owner](#business-owner)
- [Manual Testing](#manual-testing)
- [Automated Testing](#automated-testing)
- [Peer Review](#peer-review)
- [Bugs](#bugs)
    - [Resolved](#resolved)
    - [Unresolved](#unresolved)

# Code Validation

## W3C HTML Validator

Home2Home site HTML faced a couple of issues due to dynamic templating including the action for the search remaining empty until used - details below

<h2 align="center"><img src="../../media/testing/html-error.png"></h2>
<h2 align="center"><img src="../../media/testing/html-error-2.png"></h2>

Faced a continued issue with the filter setup - when no filters are applied, certain elements are hidden and so they cause an error. Will be addressed in future releases.

## W3C CSS Validator

Home2Home passed all tests using the W3C CSS Validator tool

<h2 align="center"><img src="../../media//testing//core-css-valid.png"></h2>

<h2 align="center"><img src="../../media//testing/checkout-css-valid.png"></h2>

## JSHINT Javascript Code Quality Tool

- Home2Home site Javascript was all validated using JSHint - had to include $ as a global to resolve some JQuery related errors

| core.js | properties.js | stripe_elements.js | property_details.js |
| -------- | -------- | ------- | ---- |
| <img src="../../media//testing/core-js.png"> | <img src="../../media//testing/properties-pep8.png"> | <img src="../../media//testing/stripe-elements-js.png"> | <img src="../../media//testing/property-detail-js.png"> | 

## Python Validation using Gitpod

* Used pycodestyle in gitpod to verify PEP8 compliance accross all py files - no exceptions

| Bookings | Checkout | Contact | Home |
| -------- | -------- | ------- | ---- |
| <img src="../../media//testing/bookings-pep8.png"> | <img src="../../media//testing/checkout-pep8.png"> | <img src="../../media//testing/contact-pep8.png"> | <img src="../../media//testing/home-pep8.png"> | 

| Main Files | Properties | Reviews | Users |
| -------- | -------- | ------- | ---- |
| <img src="../../media//testing/main-files-pep8.png"> | <img src="../../media//testing/properties-pep8.png"> | <img src="../../media//testing/reviews-pep8.png"> | <img src="../../media//testing/users-pep8.png"> | 

# Accessibility 

## Colour Contrast

* I used WebAim contrast checker to ensure chosen colours were accessible - all passed

| main on white | white on main | white on accent |
| -------- | -------- | ------- |
| <img src="../../media//testing/main-white.png"> | <img src="../../media//testing/white-main.png"> | <img src="../../media//testing/white-accent.png"> |

## Wave Webaim Accessibility Checker

* I used WAVE Web Accessibility Evaluation Tools to help me check the A11y compliance of my code. The only errors faced were empty buttons where icons were used. There are still some improvements that could perhaps be made such as heading hierarchy, but otherwise high acceissbility

| Home | Properties | Property Detail |
| -------- | -------- | ------- |
| <img src="../../media//testing/home-wave.png"> | <img src="../../media//testing/property-wave.png"> | <img src="../../media//testing/detail-wave.png"> |


# Lighthouse

I used the Lighthouse reports in Google Developer Tools to examine the pages of the website for the following
- Performance
- Accessibility
- Best Practices 
- SEO

There were some less than optimum scores for performance and Best Practices - though these were caused largely by the stripe library. Could be resolved by :
Using next gen image formats for faster load time
Refining and streamlining script embeds so they are not required on every page when redundant

<img src="../../media/testing/desktop-lighthouse.png">
<img src="../../media/testing/mobile-lighthouse.png"> 


# Browser Compatibility

# Responsiveness

Responsivity tests were carried out using Google Chrome DevTools. Device screen sizes covered include:
- iPhone SE
- iPhone XR
- iPhone 12 Pro
- Pixel 5
- Samsung Galaxy S8+
- Samsung Galaxy S20 Ultra
- iPad Mini
- iPad Air
- Surface Pro 7
- Surface Duo
- Galaxy Fold
- Samsung Galaxy A51/71
- Nest Hub
- Nest Hub Max

I also personally tested the website on iPhone 14 pro, Honor Pad Pro, MacBook Pro 13inch.

# Testing User Stories

## User stories

### Viewing and Navigation
#### Guest

1. I want to be able to view a list of available properties to find one that suits my needs.
    - Multiple CTA buttons and easy navigation items to find full property list
2. I want to view individual property details to see the price, description, images, amenities, and reviews.
    - Dedicated property detail page including price per night, booking functionality, amenities list, reviews and bed/bath count
3. I want to use filters to narrow down property options by location, price range, number of bedrooms, and other criteria.
    - User friendly collapsible filter button allowing for multiple filters to be selected and applied
4. I want to easily navigate the site to find and compare properties.
    - User friendly navigations allowing access to properties and their details

### Registration and User Accounts
#### User

1. I want to easily register for an account to access personalized features.
    - Custom signup allows user to select whether they are a guest or a host and customises their experience accordingly
2. I want to log in and out securely to access my account information.
    - Users can login and view their profile including their name, address and bio
3. I want to recover my password if I forget it to regain access to my account.
    - Password recovery managed with DjangoAllauth and customised pages to fit branding
4. I want a personalized user profile to view my booking history, manage my listings (if I'm a host), and update my information.
    - Customised profile and navigation views allow all users to view past and upcoming bookings, as well as allowing hosts the ability to view and manage their properties

### Property Listings and Management
#### Host

1. I want to add a new property listing to the platform to make it available for booking.
    - Navigation menu option to add new property for hosts only
2. I want to edit and update my property listings to keep the information accurate and up to date
    - Full crud functionality implemented for hosts and superusers to add, view, edit and delete property listings
3. I want to upload images for my property listings to attract potential guests.
    - Image upload functionality available in add and edit property pages
5. I want to delete a property listing if it is no longer available for booking.
    - Both hosts and superusers have the ability to delete a property from within the edit property page - prompts confirm deletion before action is completed

### Booking and Checkout
#### Guest

1. I want to easily select check-in and check-out dates to book a property.
    - Property detail page includes checkin checkout fields for booking
2. I want to view the total cost of my booking to avoid any surprises at checkout.
    - Basket calculates price per night and total nights to provide a total booking cost before checkout
3. I want to enter my payment information securely to complete my booking.
    - Stripe payment system securely manages payment details 
4. I want to receive an order confirmation after booking to verify my booking details.
    - Stripe webhook provides order confirmation email to users upon booking completion

### Administration and Platform Management
#### Admin

1. I want to manage user accounts to maintain the integrity and safety of the platform.
    - Full django admin availabilty to update and remove users 
2. I want to monitor property listings to ensure they comply with platform guidelines.
    - superusers can manage properties from within the web app to edit and delete as appropriate
3. I want to manage site content and updates to keep the platform running smoothly.
    - Django admin and superuser allowances on the site allow for full control over the site

# Automated Testing

* Due to time constraints I had to keep to key tests utilising Django/Python unittest framework. It covers key views that ensure operational function. 

* Issues identified but rectified fairly easily - details below : 

| Bookings | Checkout | Home | Properties |
| ------- | -------- | -------- | -------- |
| <img src="../../media/testing/bookings-pass-py.png"> | <img src="../../media/testing/checkout-pass-py.png"> | <img src="../../media/testing/home-pass-py.png"> | <img src="../../media/testing/properties-pass-py.png"> |

* Faced biggest issue with reviews test - identified a large bug that had failed to identify in user testing as had no past boookings to test user specific reviewing on : 

| Review Test Fail | Review Frontend Fail | Review Fixed | Review Passed |
| ------- | -------- | -------- | -------- |
| <img src="../../media/testing/reviews-fail-py.png"> | <img src="../../media/testing/review-error-set.png"> | <img src="../../media/testing/write-review.png"> | <img src="../../media/testing/reviews-ok-py.png"> |

## All tests passing

* In total I wrote 11 tests. They all passed.

<h2 align="center"><img src="../../media/testing/final-tests.png"></h2>

## Coverage

* I have used coverage to calculate the percentage of my code which is covered by unittests. The result even with time constraints and limited testing is 78%.

* You can see a breakdown by app below:

| <img src="../../media/testing/coverage-1.png"> | <img src="../../media/testing/coverage-2.png"> |
| ------ | ------- |

# Manual Testing

## Navigation

- The main navigation buttons have been tested and proven to work
- User permissions have been tested and proven to work

| <img src="../../media/testing/navbar-host.png"> | <img src="../../media/testing/navbar-superuser.png"> |
|----- | ------ |

<h2 align="center"><img src="../../media/testing/navbar-logged-in.png"></h2>
<h2 align="center"><img src="../../media/testing/navbar-logged-out.png"></h2>
<h2 align="center"><img src="../../media/testing/navbar.png"></h2>

## Footer

- Social links in the footer have been tested and proven to work
- Back to top button functioning well

<h2 align="center"><img src="../../media/testing/footer.png"></h2>

## Homepage

- Buttons have been tested and proven to work
- Links have been tested and proven to work

<h2 align="center"><img src="../../media/testing/home-1.png"></h2>

<h2 align="center"><img src="../../media/testing/home-2.png"></h2>

<h2 align="center"><img src="../../media/testing/home-3.png"></h2>

<h2 align="center"><img src="../../media/testing/home-4.png"></h2>

## All Properties & Filters

- Filters have been tested and proven to work as desired
- Reset Filters button has been tested and proven to work
- Links have been tested and proven to work

<h2 align="center"><img src="../../media/testing/all-props.png"></h2>


| <img src="../../media/testing/filter-modal.png"> | <img src="../../media/testing/filter-selected.png">|
| ---- | ---- |

<h2 align="center"><img src="../../media/testing/filter-btns.png"></h2>

## Search

- Applied search criteria works as expected
- Empty search works as expected

<h2 align="center"><img src="../../media/testing/search-result.png"></h2>
<h2 align="center"><img src="../../media/testing/search-empty.png"></h2>

## Propert Details Page

- Image carousel renders images and controls work as expected

- Date range picker works as expected. Allows user to select a range with previous dates unavailable

### Key Features & Amenities

- Key features and amenities appear as expected

<h2 align="center"><img src="../../media/testing/property-detail.png"></h2>

### Google Map

- Map renders as expected

<h2 align="center"><img src="../../media/testing/map-load.png"></h2>

### Average Rating

- Average rating renders as expected

<h2 align="center"><img src="../../media/testing/avg-rating.png"></h2>

### Reviews

- Reviews appear as expected and allow previous stays to leave review
- No reviews leaves message prompting booking

<h2 align="center"><img src="../../media/testing/leave-review.png"></h2>
<h2 align="center"><img src="../../media/testing/no-reviews.png"></h2>

## Cart

- Cart renders as expected with booking in cart
- Buttons have been tested and proven to work
- Cart renders as expected with no booking in cart
- Booking can be deleted from cart
- Only one booking per checkout - messages render as expected

<h2 align="center"><img src="../../media/testing/cart-full.png"></h2>
<h2 align="center"><img src="../../media/testing/cart-empty.png"></h2>
<h2 align="center"><img src="../../media/testing/cart-delete.png"></h2>
<h2 align="center"><img src="../../media/testing/cart-add.png"></h2>
<h2 align="center"><img src="../../media/testing/cart-too-many.png"></h2>

## Checkout

- Cart contents load correctly
- Signed in user can save information to profile
- Invalid card details error messages appear

<h2 align="center"><img src="../../media/testing/checkout-details.png"></h2>
<h2 align="center"><img src="../../media/testing/checkout-payment-form.png"></h2>
<h2 align="center"><img src="../../media/testing/card-error.png"></h2>

## Order Success

- Order success page renders as expected

<h2 align="center"><img src="../../media/testing/booking-success.png"></h2>

## User authentification

- Register, log in and log out pages render as expected
- Non-authenticated users cannot access user profile, they are redirected to log in
- Password reset renders correctly

<h2 align="center"><img src="../../media/testing/sign-in.png"></h2>
<h2 align="center"><img src="../../media/testing/sign-out.png"></h2>
<h2 align="center"><img src="../../media/testing/sign-up.png"></h2>
<h2 align="center"><img src="../../media/testing/signed-out.png"></h2>
<h2 align="center"><img src="../../media/testing/password-reset.png"></h2>

## User Profile

- User profile renders as expected on small and large screens
- Links are tested and proven to work
- Users can update their information from the form.

<h2 align="center"><img src="../../media/testing/profile-lg.png"></h2>
<h2 align="center"><img src="../../media/testing/profile-mobile.png"></h2>
<h2 align="center"><img src="../../media/testing/edit-profile.png"></h2>

## My Properties

- Users can view their properties and edit via the link
- Buttons and links tested and work

<h2 align="center"><img src="../../media/testing/my-props.png"></h2>
<h2 align="center"><img src="../../media/testing/edit-props.png"></h2>

## Reviews

- Reviews displayed as expected
- Write review form renders correctly

<h2 align="center"><img src="../../media/testing/my-book-leave-review.png"></h2>
<h2 align="center"><img src="../../media/testing/write-review-form.png"></h2>
<h2 align="center"><img src="../../media/testing/review-display.png"></h2>
<h2 align="center"><img src="../../media/testing/edit-review.png"></h2>
<h2 align="center"><img src="../../media/testing/leave-review-btn.png"></h2>

# Peer Review

- I submitted my project for peer review shortly before submission. The feedback was positive and no bugs were highlighted.

# Bugs

## Resolved

### Users

#### Could not get signup form to display custom field to select user or host
- Added profile_setup to views but still threw the same issue
- identified incorrect path being used thanks to DEBUG - accounts/signup.html instead of "account"
- corrected and form displayed with additional field

#### Crispy Forms issues
- could not get crispy forms to load to the system correctly - installed using pip
- added to installed apps already, hadn't loaded correctly in signup.html {% load i18n crispy_forms_tags %}
- still had issues - added CRISPY_TEMPLATE_PACK = Boostrap4 to settings and installed crispy_bootstrap4 using pip
- not working still, realised I hadn't added crispy_bootstrap4 to installed apps
- correct installed apps and now functioning correctly

#### Profile viewing 
- could not get profile page to load 
- amended urls in project level urls.py (changed '' to 'users/') but this caused more errors
- changed back to ('') and confirmed views were setup correctly - was missing the view for the profile page
- updated views and urls and now loads correctly - good to add editing capabilities

#### Profile editing 
- Tried having a profile page that was editable, however it made for a clumsy look so will have a profile page and and edit profile page separate
- edit page was showing the location of the current profile pic, which I didn't like - tried using Django widgets to get around this but kept getting bootstrap errors as I hid the checkbox for clear. 
- Decided to leave it on for functionality but it will be a future feature

#### Admin View
- Wanted a way to distinguish between guests and hosts in the admin view
- Constructed custom admin.py but had issues loading the page - followed [django documentation](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/filters/) to implement the filter view. Functions as hoped
    <img src="../../media/testing/django-filter.png">

### Properties
#### Issues migrating the properties/models.py file
- When migrating forgot I had previously migrated a properties model and so had to run through some overrides.
- In doing so, I provided a default date/time and mis formatted - used decimal instead of hyphen.
- Caused many migration issues, tried using methods such as updating the database with the shell, to no avail as the table hadn't been created, data hadn't migrated so couldn't be altered. 
- Manually amended the migration file in properties/migrations and this did the trick 
#### Issue with uploading properties.JSON - primary key issue
- remembered I had to start host PK from 3 due to existing users on the system - amended host foreign key reference in the properties JSON.
- foreign key constraints was not resolved and couldn't use loaddata - reverse engineered by adding property manually, dumping data into a JSON and comparing. After scanning all JSON data again realise there was a typo. Issue was not with hosts foreign key but amenities as had used 18 and there are only 17 pk's for amenities. 
- amended to 1 instead of 18 and data uploaded 
#### Sorting in property admin not completely acccurate as it is going off host PK (integer) rather than username (alphabetical)
- amended admin.py for properties to include custom sorting and ordering - now functions okay
#### Struggling with filtering form displaying well across all screens - got the JS working and the hide and display was perfect. However, when opened the filter options were all over the place
- tried replacing amenities with a dropdown list, but the form itself wouldn't conform to screen width, and was cluttering the html with bootstrap classes
- used the col method and was okay for the most part but still looked clumsy
- changed plan and decided to go with Bootstrap modal for the filtering options, inspired by AirBnb interface. It is clean, easy to use and works responsively. 
#### Amenities ordering 
- wanted most popular amenities to be listed at the top - should have consideredd this when loading JSON data. Used django documentation and stack overflow to implement manual ordering within the admin interface. This worked nicely and now 8 top amenities show with a "show more" button
#### Map
- Tried adding diferent sized maps but it actually made UI worse - only medium screens where it looks like too much white space. Will stick with 1 size map below all info

### User Profiles
#### Profiles
- difficulty choosing how to properly setup, as I wanted separate profiles for hosts and guests
- Went with separation at signup stage by having a signup selection field - override standard allauth signup form
- Couldn't get my form to load, realised I hadn't provided custom URL to override the allauth redirect
#### Profile setup
- Had issues separating profile setup - couldn't get separate forms to load depending on host or guest
- Realised I was overcomplicating the process. Decided to amalgamate the two and have one profile setup form. No fields were explicitly for host or guest anyway. 
#### Profile edit
- Submitting profile edit worked to an extent but it would not update the name on the profile when you submitted first and last name
- Identified the issue was with the user model - I had not added or migrated the first name and last name to the user model so there was nothing to update
- Still not displaying - realised I also needed to update the django templating in the HTML as it was trying to pull a full name, but that isn't a specific field. Changed to first and last and works okay now


### Bookings
#### Booking form
- Issues incorporating the booking form on the property_detail page - throwing a url error 
- Had added booking URL's but not added to main URL's - easy fix
- New issue thrown "Cannot assign "<Profile: mrHost>": "Booking.user" must be a "User" instance."
- Fixed by amending view to include user instead of profile - another easy fix but generated a type error to address which was fixed by updating the booking model
- Final issue was an operational one as I hadn't migrated the updated booking model - resolved and now need to proceed with checkout and basket to be able to fully test

### Basket
#### Adding to basket
- Tried adding items to basket, had a few minor issues such as redirects to checkout (not created yet) but nothing major. 
- Line items were missing values so could not generate a total value for the basket. Added in the fields and refreshed but kept populating with £0.00 
- Tried a number of things including rebuilding the views and forms and reformatting template, but nothing was working.
- Foolish mistake, existing bookings in the cart were created before model was updated and so had no values for total price etc. 
- Created new booking and now displays correctly - need to add delete functionality to remove line items or clear basket

### Reviews
#### Displaying star rating
- Tried displaying a star rating or "No Reviews Yet" on property page, but discovered [Django Star Rating](https://medium.com/geekculture/django-implementing-star-rating-e1deff03bb1c)
- Implemented but want to replace the No Ratings Yet with 5 empty stars
- Had to utilised some custom JS to add a star rating element to the write_review template - this worked with the fontawesome classes to provide a filled or empty star
- Stars were remaining solid, reformatted JS to include an initial empty state, but this didn't show as empty
- Realised I was using incorrect fontawesome - outdated from previous projects - needed to use fa-solid instead of fas
- Once rectified classes and amended JS accordingly the star widget now works - need to ensure it uploads the rating to the database
- Rating not populating on property_detail page and not displaying stars in carousels - need to revise property model I think to get an average rating, rather than just the single rating
- Stars_rating actually seemed to make things more complex, unnecessarily, especially when it came to displaying the average rating of a property - instead decided to try modifying the property model. It kept bugging but settled on calculating the average rating, and then adding a custom star generation within the model itself. The logic in html was too cluttered and clumsy and made for a messy UI. 
- Settled on the model logic, clean and works well. Means I can display it across multiple areas such as reviews carousels etc. if needed
#### Reviews
- Managed to amend logic similar to star ratings in order to get stars to appear correctly on user reviews. 
- Cannot get the edit button to be clickable - have corrected urls etc. but no luck
- Think the issue may be down to carousel style - think the carousel controls overlap the button - will try center aligning button
- rectified issue, for now will stick with loading the latest reviews - possibly the latest 2 for styling purposes
- Tested functionality and now the review can be edited and when edited it affects the property average rating. Seaside Haven is best for viewing as it has reviews loaded on - will load more via JSON.

### Contact

#### Error with form loading displaying None value

- Contact form was loading "None" values on page load
- Amended form setup but did not help and included placeholders. 
- issue was with the view, passing empty date on load. Amended and now loads with placeholder text - submits successfully

### Checkout 
#### Errors with checkout loading
- resolved issue with checkout total nights error due to model setup :
<h2 align="center"><img src="../../media/testing/checkout-total-error.png"></h2>

- ongoing issue with checkout easily resolved - simpoly forgot to import Sum in py file 
<h2 align="center"><img src="../../media/testing/checkout-sum-error.png"></h2>

- had amended model for bookings but forgot to update for checkout so couldn't pull price properly - now resolved and all elements are pulled from basket correctly 
<h2 align="center"><img src="../../media/testing/checkout-price-error.png"></h2>

- issue with API setup for Stripe on checkout - resolved by referring to Stripe documentation for updated integration 
<h2 align="center"><img src="../../media/testing/checkout-api-error.png"></h2>

## Unresolved

### Datepicker

- Issues with datepicker display on mobile. Visually great, but continued issues with iOS mobile devices - the native datepicker seems to overwrite any and all JS so min/max date doesn't work
- Seems a regular issue according to forums as linked in README - tried reformatting JS and tried several different libraries and plugins but still no luck.
- Cannot find a remedy on forums - even tried copying some code across from another project but had the same issue - will leave unresolved for now but will be a future development - completely custom built booking system. 
- Perhaps adding availability to listings would enhance the experience - could automatically mark past dates as unavailable and then cannot be booked on calendar. 

Back to [README.md](/README.md#testing)