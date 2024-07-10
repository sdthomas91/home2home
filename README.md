# Home2Home

## Milestone Project 4 - Full Stack Development

<h2 align="center"><img src="media/readme/home2home-mockup.jpg"></h2>

Welcome,

This project is a property rental platform utilizing Django for the backend and HTML, CSS, and JavaScript for the frontend. The platform allows users to register as guests or hosts, list and book properties, and communicate through an integrated messaging system. It also includes Google Maps integration for searching and viewing properties on a map.

* Key features include:
  - Dynamic Filtering : Users can filter properties using a variety of filters for quicker property searching.
  - Active search : Users can search by keyword or phrase to find their ideal property
  - Cart & Stripe Checkout: Users may book one stay per checkout, and proceed to checkout with Stripe. See [Stripe's testing card details](https://stripe.com/docs/testing?testing-method=card-numbers#visa) to place an order on the website.
  - Authentication: Users can create an account to save their contact information and view their bookings (past and future)
  - Reviews: Users can leave reviews only for properties at which they have stayed to ensure verified reviews. 

## Live Project

[View the live project here.](https://home-2-home-534807be7c72.herokuapp.com/)

## Repository

[Find the project repository here.](https://github.com/sdthomas91/home2home)

## Contents
   - [User experience](#user-experience)
      * [User Stories](#user-stories)
         + [Viewing and Navigation](#viewing-and-navigation)
         + [Registration and User Accounts](#registration-and-user-accounts)
         + [Property Listings and Management](#property-listings-and-management)
         + [Booking and Checkout](#booking-and-checkout)
         + [Messaging](#messaging)
         + [Administration and Platform Management](#administration-and-platform-management)
   - [Design](#design)
      + [Colour Scheme](#colour-scheme)
      + [Typography](#typography)
      + [Imagery](#imagery)
      + [Icons](#icons)
      + [Cards](#cards)

# User Experience

## User stories

### Viewing and Navigation
#### Guest

1. I want to be able to view a list of available properties to find one that suits my needs.
2. I want to view individual property details to see the price, description, images, amenities, and reviews.
3. I want to use filters to narrow down property options by location, price range, number of bedrooms, and other criteria.
4. I want to view properties on a map to understand their locations relative to points of interest.
5. I want to easily navigate the site to find and compare properties.

### Registration and User Accounts
#### User

1. I want to easily register for an account to access personalized features.
2. I want to log in and out securely to access my account information.
3. I want to recover my password if I forget it to regain access to my account.
4. I want to receive an email confirmation after registration to verify my account.
5. I want a personalized user profile to view my booking history, manage my listings (if I'm a host), and update my information.

### Property Listings and Management
#### Host

1. I want to add a new property listing to the platform to make it available for booking.
2. I want to edit and update my property listings to keep the information accurate and up to date.
3. I want to upload images for my property listings to attract potential guests.
4. I want to manage the availability of my properties to accurately reflect when they can be booked.
5. I want to delete a property listing if it is no longer available for booking.

### Booking and Checkout
#### Guest

1. I want to easily select check-in and check-out dates to book a property.
2. I want to view the total cost of my booking to avoid any surprises at checkout.
3. I want to enter my payment information securely to complete my booking.
4. I want to receive an order confirmation after booking to verify my reservation details.
5. I want to receive an email confirmation of my booking to keep a record of my reservation.

### Administration and Platform Management
#### Admin

1. I want to manage user accounts to maintain the integrity and safety of the platform.
2. I want to monitor property listings to ensure they comply with platform guidelines.
3. I want to handle booking disputes and issues to provide customer support.
4. I want to manage site content and updates to keep the platform running smoothly.
5. I want to view site analytics to understand user behavior and improve the platform.


# Design

## Colour Scheme
 - The Colour scheme was generally kept simple and in line with best practices, with high WebAim contrast compatibilit as outlined in the [test document](docs/readme/TESTING.md)

### Main Colour
- #008080 - This teal is a revitalizing and rejuvenating color that also represents open communication and clarity of thought.

### Accent Colour
- #004747 - This maintains the teal but darkens the colour to provide user feedback with elements such as hover and active buttons

### Supporting Colours
- #fff & #000 - Used black and white for high contrast, increased accessibility nad user experience. 

<img src="media/readme/file-design.jpg">

## Tyography
- Logo Font : Playwrite ES Deco was used as the main font for the logo/brand of the site. It could not be used for general headings due to readability but for a brand identity it worked nicely as a decorative piece
- Title Font : Montserrat was used as the title font due to high readability, compatability and versatility with differing font weights. 
- Body Font : Body was left as Arial/System font as it pairs well with Montserrat, is universal and highly readable. 

## Imagery
- Little imagery was required for the body of the site due to the population of space with property images. The same image was used for both desktop and mobile hero/body images, though it was scaled accordingly for different viewport sizes. 
- Property images were largely from pexels and all credits will be included in a separate [CREDITS.md](docs/readme/credits.md)

## Icons
- All icons used come from the [FontAwesome library](https://www.fontawesome.com) - they were used to provide information without the need for excess text, though often times they are supported by text for optimum UX. Used across amenities, navbar and search bars.

## Cards
- Used bootstrap cards for visual heirarchy and easy design for properties, profiles and contact forms. These worked especially well for organising content such as property listings when more than one occurs. 

# Wireframes

- Please find all core wireframes [here](docs/readme/wireframes.md)

## Wireframe Deviations
 - There were little to no deviations from the original wireframe. I had a clear idea of how I wanted the User Interface to look and the general navigation of the pages. 
 - One element missed on the wireframe is the location of the filter element on the all properties page. Located below the page title for easy access and maximum UX. 
 - Added "view details" button below properties for easy navigation and kept property cards fairly minimal
 - Introduced additional interface pages such as my properties (for hosts), manage properties (for super users) and my bookings (for all users)

# Database Schema

## Considerations

Thins I had to take into account when compiling the DB models were:
- How a user could be listed as a host or a guest and the different actions that would allow
- How I could pass multiple amenities to a property whilst maintaining a clean model
- How bookings would be marked as pending/confirmed for users viewing them in the basket or their my bookings page
- How could I allow different levels of editing for guests, hosts and superusers
- How to allow multi image capacity to property model
- How reviews would link to specific properties as well as the hosts

## Diagram 
 - The following image represents the database models and relevant relationships as utilised within the project

 <img src="media/readme/home2home-db-diagram.png">

### DB Models
- A list of database models used in the project can be found below :
   * **User** - stores user information including username, email, password, first name, last name, whether the user is a host or guest, and the date they joined.
   * **Profile** - stores additional information about the user such as bio, profile picture, address and phone number. Relates to the User model.
   * **Property** - stores information for each property including host ID, title, description, address, city, state, country, postal code, latitude, longitude, price per night, maximum guests, number of bedrooms, number of bathrooms, availability, creation date, and update date.
   * **PropertyImage** - stores multiple images for each property. Relates to the Property model.
   * **Booking** - stores booking information including guest ID, property ID, check-in date, check-out date, total price, booking status, creation date, and update date. Relates to the User and Property models.
   * **Review** - stores rating and review information including guest ID, property ID, rating, comment, creation date, and update date. Relates to the User and Property models.
   * **Amenity** - stores information about property amenities including the name and font awesome class for the amenity icon.
   * **PropertyAmenity** - stores the relationship between properties and amenities. Relates to the Property and Amenity models.

# Features - Inc. in final project

## All Pages

- Responsive design using Bootstrap columns
- Semantic HTML
- Custom CSS to give the website a cohesive and user-friendly appearance
- Back to top button for easy page navigation
- Toasts/JS for clearer messaging
- Footer - to clarify end of page and provide business information

### Header & Navigation

- Logo consisting of text in Logo Font
- Top navigation including:
   - Search bar (to search all properties)
   - My Account (depicted by profile icon) with dropdown for all profile navigations
      - Conditional logic to display differently dependant on user status (guest, host, superuser)
   - Cart including cart contents counter for user feedback on whether the cart has a live booking in or not
- Secondary navigation:
   - Home link - for easy navigation to home page at any time
   - All properties for an easier browsing experience
   - Contact - leading to contact form

### Footer

- Company information
- Social media Links 

### Flash Messages
- Styled and located for increased UI/UX and includes messages for:
   - Success message
   - Info message
   - Error message
   - Warning message

## Homepage

- Jumbotron - includes CTA and high contrast for readability
- Featured Properties - another CTA
- Become a Home2Home host - CTA to join the platform as a host
- Featured Reviews - increase user trust with a final CTA to book a stay

## All Properties Page

- Clear title
- Filter toggle button with clear indicator using fontawesome slider icon including functions such as:
  - Collapse for better UI
  - Dropdowns for bed/bath/price/city selection
  - Multiple choice checkbox for amenity filtering (includes show more button to keep UI clean)
  - Filters update dynamically and display results immediately
  - Filters can be edited/updated dynamically any time
  - Clear filters button to reset filters
- Property Cards with bootstrap card structure and custom css:
  - First property image with carousel if property has mutliple images
  - Price per night
  - View details button to go through to property detail / booking
- Pagination - allows users to easily navigate through pages to view more properties

## Propert Details Page
- Property Title
- Property averge rating
- First property image with carousel if property has mutliple images
- Date range picker allowing for booking date selection which includes:
   - inability to book prior to the present day
   - inability to book checkout prior to checkin date selected
   - select a date range that dynamically adds to booking details when added to cart
- Number of guests selector dropdown (maximum selection) with link to contact if need to book extra guests
- Book now button, adds to cart with dates and guest number
- Bed/Bathroom count with icons
- Top amenity list (currently limited to 8)
- Google Map with pin locator
- Property reviews

## Cart Page
- Dynamic cart allowing for only one propery booking at a time for host convenience
- Dynamic cart with delete/clear buttons to remove booking
- Line item details including 
   - price per night
   - total nights
   - subtotal
- Cart Total
- Secure Checkout button

## Checkout Page
- Order summary including : 
   - property image
   - booking details including check in and out
   - total nights
- Checkout form that includes:
  - Contact detaisl and address
  - Option to save to profile
  - Auto populates with content saved to user profile
  - Stripe payment with warning to notify of final charge amount

## Checkout Confirmation Page
- Checkout success page includes booking details 
- Marks booking as completed and adds to "My Bookings"
- Sends booking confirmation email

## Authentification Pages
- Register/ Log In/ Log Out/ Reset Password Pages all styled to match theme
- Custom signup form using DJango Allauth template allowing users to select whether they are signing up as a host or a guest

## User Profile Page
- Customised profile page including:
   - profile picture
   - name
   - address
   - bio
   - edit profile button
- Users must be logged in
- Users can only access their own User Profile

## Edit Profile page
- Allow logged in users to edit their own profile including all personal information
- No authentication info can be edited here

## My Bookings page
- Logged in users can access a page displaying their bookings including:
   - Upcoming stays - future bookings allocated using checkin date
   - Previous Stays - past bookings allocated using checkout date
- Displayed inline multi-column on larger screens and as a sinlge column per booking on smaller screens

## My Properties Page
- Logged in hosts can access a "my properties" page that includes:
   - List containing cards (same styling as other properties pages for consistency)
   - Edit property button

## Manage Properties Page
- Superusers can access all properties with the same styling as the my properties page and same edit property button

## Edit property page
- Allow hosts and superusers to edit the property details in full including:
   - All property information
   - Confirm Edit button
   - Delet button - opening deletion confirmation modal


# Future Features

## UX Features

### Datepicker

#### Datepicker displays dynamic availability

* The datepicker as present doesn't draw from an existing "availability" database and so a property could get double booked. Would like to implement the availability model/view within the booking app to allow for a more dynamic booking experience.

#### Datepicker UX improvements/optimisation on mobile

* Mobile devices default override of the datepicker is frustrating. Seems a common issue and tried multiple workarounds found on a variety of forums. Would consider updating the datepicker to a more versatile open source library such as MobiScroll.

### Property Pages

#### Interactive Map

* Implement a "search by map" function, would need additional page space likely incorporated into the search results page

#### Sort By

* Allow for property sorting in addition to standard filtering such as "Sort by Price (Low to High)"

#### Categorise properties

* Allow hosts to add a category to their listing to allow for a more robust and precise search experience for users. This could include categories such as Luxury Stays, Seasid retreats etc. 

### Hosts/Guests

#### View host 

* Allow guests/users to view the hosts profile including property reviews/average rating for trust building

#### Review guests/hosts

* Allow guests and hosts to rate eachother accordingly following a stay allowed only after checkout is complete

### Cart & Checkout

#### Dynamic editing of booking

* Allow the user to edit details such as checkin/checkout dates within the cart view and have it update cart total

### Bookings

* Allow for users to "rebook" a stay from their my bookings page if they enjoyed it

### Additional Apps

#### Blog

* Incorporate a site blog for increased SEO and user interaction

#### Custom admin interface

* Utilise something like Jazzmin to customise the user interface in django easily allow for a custom admin experience and keeping admin/user experiences separate

#### Newsletter 

* Include a newsletter signup opportunity for future promotions and communications

#### Favourites

* Allow users to "favourite" a property and add it to the navigation under a heading such as "My Favourites"

# Technologies Used

## Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)

- [CSS3](https://en.wikipedia.org/wiki/CSS)

- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

## Frameworks & Libraries

- [Django](https://www.djangoproject.com/)
  - This website is built using Django, a high-level Python web framework. Home2Home features multiple apps with model, view and template layers. I have also used Django to provide an admin view, create forms and test my website. Further features used include [Django Allauth](https://django-allauth.readthedocs.io/en/latest/index.html) for user authentification, Pillow for uploading images, and Crispy Forms for better form styling.

- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)
  - Templating language I've used with Python to add logic to my html templates.

- [jQuery](https://jquery.com/)
  - I used jQuery to add functionality to Bootstrap components and within my scripts.

- [Bootstrap 4](https://getbootstrap.com/) 
  - I used bootstrap throughout the site to make it responsive. The website uses Bootstrap's Containers, Grid System, Flexbox and Spacing utilities. I sourced code from the Bootstrap documentation when building the Navbar, Image Carousels, Cards and Buttons.

- [Google Fonts](https://fonts.google.com/)
  - Fonts are imported from google fonts.
  
- [Font awesome](https://fontawesome.com/)
  - I used icons from font awesome across the website

- [FlatPickr Date Picker](https://flatpickr.js.org/options/)
  - I used this CDN to display the datepicker on the property detail page

## Storage & Hosting

- [Heroku](https://id.heroku.com/login)
  - Heroku is the deployment source I used for this project.

- [Github](https://github.com/)
  - Github was used to create and store the project repository.

- [Amazon Web Services](https://aws.amazon.com/)
  - AWS is used to host and store static files and media.

- [ElephantSQL](https://www.elephantsql.com/)
  - ElephantSQL is used to host the website's PostgreSQL database.

## Payments

- [Stripe](https://stripe.com/gb)
  - Stripe is used to handle website payments.

## APIs

- [Google Maps API](https://developers.google.com/maps/)
  - I used Google MAPS API to show the property location on a google map via coordinates.

## IDE & Version Control

- [Git](https://git-scm.com/)
  - Git was used as a version control in the terminal.

- [Gitpod](https://gitpod.io/)
  - Gitpod was used to create my files and where I wrote the code.

## Other Tools

- [Figma](https://figma.com/)
  - Figma was used to create Wireframes for the project during the initial planning stage.

- [Adobe Illustrator](https://www.adobe.com/ie/products/illustrator.html)
  - Photoshop was used to resize images for the website as well as create multi-device mockup

- [TinyJPG](https://tinyjpg.com/)
  - TinyJPG was used to compress images for a faster loading time.

- [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)
  - Google Chrome's Dev Tools were used while building the project to test responsiveness and for debugging.

- [DBDiagram.io](https://dbdiagram.io/)
  - Tool used to mock up database structure diagram.

- [Pexels](https://pexels.com/)
  - Pexels was used to source the profile pic imagery.

- [Freepik](https://freepik.com/)
   - Freepik was used to source property imagery

- [ChatGPT](https://openai.com/blog/chatgpt/)
  - OpenAI's ChatGPT was used in part to generate amenities lists, fake host bios and random addresses for properties.

## Testing & Code Validation

The following tools were used for testing and code validation. You can see results in the Testing section of this README.

- [W3C Markup Validation Service](https://validator.w3.org/)
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
- [JSHint](https://jshint.com/)
- [Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk?hl=en)
- [Python Linting on Gitpod](https://open-vsx.org/extension/ms-python/python)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [WAVE Web Accessibility Evaluation Tools](https://wave.webaim.org/)

# Testing

- Please refer [here](docs/TESTING.md) for more information on tests conducted on the Home2Home site

# Deployment

- Please refer [here](docs/DEPLOYMENT.md) for more information on the deployment of the Home2Home site

# Credits

## Code

### Code Institute:
  - I used the CodeInstitue github repo template and also utilised multiple elements from the Boutique Ado Walkthrough, though the site is largely custom built with similarities only being drawn in the navbar and the checkout (including Stripe Functionality)

### Django:
- I referred to the Django documentation whilst building my project. I used the docs a number of times including :
   - [Static files](https://docs.djangoproject.com/en/5.0/howto/static-files/)
   - [Built-In Template Tags](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/)
   - [Model Admin Filters](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/filters/)
   - [Widgets](https://docs.djangoproject.com/en/5.0/ref/forms/widgets/)
   - [Forms API](https://docs.djangoproject.com/en/5.0/ref/forms/api/)

### Bootstrap:
  - I have used Bootstrap classes throughout my project, including for layout utilities and cards. I sourced code from the Bootstrap documentation when building the navbar, image carousels, modals, dropdowns and cards. These were sourced through the [Bootstrap documentation](https://getbootstrap.com/docs/4.6/getting-started/introduction/)


### Stack Overflow: 
  I used and/ or referenced code from the following Stack Overflow articles as listed below:
- Datepicker
   - https://stackoverflow.com/questions/74649032/uidatepicker-max-and-min-date-range
   - https://stackoverflow.com/questions/62300321/mobile-ios-input-type-date-min-and-max-not-working-on-chrome-and-safari
   - https://stackoverflow.com/questions/54982031/flatpickr-mobile-format
- dateTime issues
   - https://stackoverflow.com/questions/19934248/nameerror-name-datetime-is-not-defined
- Custom filters
   -https://stackoverflow.com/questions/12102697/creating-custom-filters-for-list-filter-in-django-admin
  
### GeeksForGeeks:
  - I used [GeeksforGeeks](https://www.geeksforgeeks.org/python-datetime-timedelta-function/) for datetime functionality

## Content

- The images used are stock images sourced from FreePik and Pexels - more details can be found in the [CREDITS.md](docs/readme/credits.md)

- The host information and property details were ficitious and largely generated using Open AI's chatGPT

- I took a lot of inspiration for the booking model from [AirBnb](https://www.airbnb.com/)

## Acknowledgements

- Thank you to the tutors and staff at Code Institute for their support.

- Thank you to Ben Smith and Pasquale Fasulo at City of Bristol College for their support.

Please note this is a personal project. This website is purely for the sake of the developer's portfolio and not for public consumption.

Samuel Thomas, 2024.