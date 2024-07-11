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

Via URL

## W3C CSS Validator

The Lonely House website passed all tests using the W3C CSS Validator tool

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

<img src="../../media//testing/desktop-lighthouse.png">
<img src="../../media//testing/mobile-lighthouse.png"> 


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
