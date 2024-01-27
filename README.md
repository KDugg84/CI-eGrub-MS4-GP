![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# eGrub

For my fourth and last project (MS4) I decided to create a fast food delivery site/application that allows users to make fast food orders by selecting from a set menu of items and inputting their address details for delivery. The site includes the use of an ecommerce payment gate to allow users to pay for their orders before they are dispatched. There is also a staff login area where staff can view the total number of orders for the day and the total revenue generated for that particular day and the ability to sign-off an order as completed for dispatch.

![AmIResponsive]

[View the live site here]

## CONTENTS

* [Site Objectives](#site-objectives)

* [User Experience](#user-experience-ux)
  * [Target Audience](#target-audience)
  * [User Stories](#user-stories)
  
* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)

* [Features](#features)
  * [Database Schema](#database-schema)
  * [General Features Across The Site](#general-features-on-each-page)
  * [Accessibility](#accessibility)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
  * [Local Development](#local-development)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)

* [Testing](#testing)
  * [Manual Testing](#manual-testing)
  * [User](#user)
  * [Bugs](#bugs)
  * [Lighthouse](#lighthouse)
  * [Validation Testing](#validation-testing)
    * [HTML \& CSS](#html--css)
    * [Python Testing](#python-testing)

* [Credits](#credits)
  * [Code Used](#code-used)
  * [Acknowledgments](#acknowledgments)

## Site Objectives

Design and create a food delivery website to demonstrate an increasing understanding of the libraries and frameworks available to developers.

My main objectives are:

* I wanted to make the site easily accessible and intuitively navigated for the users.

* Allow users to search the menu and then decide what they would like to order.

* Allow users to pay for their orders with the use of a payment gate.

* The use of the backend framework which allows staff to login to the restuarant to check and sign-off on orders.

* I used ElephantSQL to store the SQLite3 database for this project.

## User Experience (UX) 

The best (intuitive) UX creates single-use learning.

### Target Audience

* Users who frequently order food online and use similar applications such as Uber Eats, Deliveroo etc.

### User Stories

* First Time Visitor Goals:

    * To understand how the site works and what its about.

    * How to navigate the site.

    * Search the menu for what's available to order.

* Returning Visitor Goals:

    * Be able to place an order by selecting items from the menu.

    * Be able to add delivery details such as name, email, address etc.

    * Be able to pay for that order using a payment gate. 

    * Allow staff to login to the restaurant side to view current orders.

    * Allow staff to update and sign-off on orders as completed for dispatch.

    * Allow staff to tally both orders and revenue for that particular day.

    * Allow staff to logout of the restaurant side of the site.

## Design

### Colour Scheme

The colour scheme used throughout the project was intended to be consistant with most if not all pages and consisted of bootstrap colour classes and other CSS colour classes:

Bootstrap:

* bg-success, text-success: #28a745, a shade of green used for the navigation bar and the footer.

* text-white: #fff, a shade of white used on the navigation and footer links as well as page headers.

* text-danger: #dc3545, a shade of red (ruby) used with the font awesome cross icons.

* btn-outline-primary: a shade of cyan-blue used to style all buttons used in placing orders and marking the orders as dispatched.

CSS: 

* Gray: #777777, a shade of gray used as the default in the body element in conjunction with the bootstrap card class used to create a more subtle font style.

### Typography

The main font style used throughout the project was the Lato font, which is a type of sans-serif, this was imported into the project from Google Fonts by imbedding their links into the head element of the base project page which included all of the various font weights avaliable. This font style has become popular due to its unique balance of originality and transparency when used in body text. 

### Imagery

The landing page includes the use of a hero image which is extended across all pages of the website. The hero image is a fast food collage displaying the various food items which are for order via the menu and the place order page. The hero image was taken from an [Uder Eats page](https://www.ubereats.com/gb/store/low-cost-fast-food/kETrDPZwSrG0LUrZ3EK9rw), the photos used to display the food items also came from the same page.

### Wireframes

The wireframes were created using Balsamiq desktop for Windows 10:

## Features

### Database Schema 

* The 'MenuItems' model within the customer app is used to store information relating to the menu items.

* The 'Category' model within the customer app is used to group all the various menu items based on the many-to-many relationship.

* The 'OrderModel' model within the customer app is used to store information relating to a customer's address details, payment information and the price, when the order was created and the MenuItems many-to-many relationship.

### General Features Across The Site

* The general features of most the website's pages include:

  * A navigation bar which is responsive across all device screens.

  * A logo which directs the user back to the home page when clicked.

  * A footer with a link to the restaurant login for staff members.

* Responsive on all device screen sizes:

  * Mobile-first layout, responsive on all devices using the Bootstrap grid system.

* User-friendly interface with easy navigation across the site:

  * Minimalistic design with visuals and information presented clearly and concisely.

  * Easily readable fonts and simple navigation throughout the site.

  * Fixed navigation bar visible on every page including links to all other pages with a brand logo linking the user back to the home page.

* Buttons:

  * Clear interactive buttons using Bootstrap responsive button classes used for starting an order, placing an order and marking an order as been dispatched.

* Forms:

  * Forms used to submit order delivery details and confirm delivery.

* Modal:

  * Used to confirm that the user wishes to place the order.

* Search bar:

  * Used to search the menu page by keywords.

### Accessibility

Whilst coding the site I have ensured that the site is accesible for all. This is achieve by using:

* Google Dev Tools to check contrast of items.

* Semantic HTML.

* Aria Labels to hightlight areas for users who require the use of a screen reader.

## Technologies Used

### Languages Used

* HTML5

* CSS3

* JavaScript ES6

* Python

### Frameworks, Libraries & Programs Used

* [Django](https://www.djangoproject.com/) the main Python framework used throughout the project.
* [Gitpod](https://www.gitpod.io/) the vast majority of my time was spent inside GitPod's VSCode Cloud IDE.
* Google Dev Tools was used to identify and resolve problems related to responsiveness and appearance.
* [Github](https://github.com/) was used to store my project in a repository.
* [Git](https://git-scm.com/) was used for version control.
* [Google](https://google.com) for research and problem solving.
* [Stack Overflow](https://stackoverflow.com/) for research and problem solving.
* [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/) used to assist with the responsiveness and styling of the website using design templates.
* [Django Allauth](https://docs.allauth.org/en/latest/introduction/index.html) used for form validation and user authentication.
* [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) used to control the rendering behaviour of Django forms in a very elegant and DRY way.
* [Pillow](https://pypi.org/project/pillow/2.2.1/) used to add support for opening, manipulating, and saving images.
* [AWS](https://aws.amazon.com/) cloud-based storage service used to store static and, media files.
* [Paypal](https://developer.paypal.com/docs/archive/checkout/integrate/) was used to deal with payments. 
* [PEP8 Validator](https://pep8ci.herokuapp.com/) was used to check python code for errors
* [ElephandSQL](https://www.elephantsql.com/) was used to store PostgreSQL database.
* [Heroku](https://id.heroku.com/) was used to deploy the project.
* [Balsamiq](https://balsamiq.com/wireframes/) was used to create the wireframes for the website.
* [Am I Responsive](https://ui.dev/amiresponsive) To create the responsive banner of devices.
* [Google Fonts](https://fonts.google.com/) was used to import the Lato font into the base template head tags which is used on all pages throughout the project.
* [Font Awesome 6.5.1](https://fontawesome.com/) was used to add icons for aesthetic and UX purposes.
* [W3C Validator](https://validator.w3.org/) & [W3C CCS Validator](https://jigsaw.w3.org/css-validator/) used to validate my HTML and CSS files.
* [JShint](https://jshint.com/) used to validate JS code.