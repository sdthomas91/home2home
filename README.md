# Home2Home

## Milestone Project 4 - Full Stack Development

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

### Messaging
#### User (Guest or Host)

1. I want to send messages to the host to ask questions about a property before booking.
2. I want to receive messages from guests inquiring about my property.
3. I want to keep all communication within the platform for ease of access and tracking.
4. I want to be notified when I receive a new message to respond promptly.
5. I want to view the entire message thread to follow the conversation easily.

### Administration and Platform Management
#### Admin

1. I want to manage user accounts to maintain the integrity and safety of the platform.
2. I want to monitor property listings to ensure they comply with platform guidelines.
3. I want to handle booking disputes and issues to provide customer support.
4. I want to manage site content and updates to keep the platform running smoothly.
5. I want to view site analytics to understand user behavior and improve the platform.
