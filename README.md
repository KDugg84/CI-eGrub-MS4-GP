![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# eGrub

For my fourth and last project (MS4) I decided to create a fast food delivery site/application that allows users to make fast food orders by selecting from a set menu of items and inputting their address details for delivery. The site includes the use of an ecommerce payment gate to allow users to pay for their orders before they are dispatched. There is also a staff login area where staff can view the total number of orders for the day and the total revenue generated for that particular day and the ability to sign-off an order as completed for dispatch.

![AmIResponsive]

[View the live site here](https://ci-egrub-app-782b95feee00.herokuapp.com/)

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

* [Testing](#testing)
  * [Testing User Stories](#testing-user-stories)
  * [Manual Testing](#manual-testing)
    * [Further Testing](further-testing)
  * [Bugs \& Errors](#bugs--errors)
  * [Validation Testing](#validation-testing)
    * [HTML \& CSS](#html--css)
    * [Python Testing](#python-testing)
    * [Lighthouse](#lighthouse)
  * [Payments](#payments)  

* [Deployment \& Local Development](#deployment--local-development)
  * [GitHub Deployment](#deployment)
  * [Local Development](#local-development)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)
  * [Deployment to Heroku](#deployment-to-heroku)
    * [Automatic Deployment to Heroku](#automatic-deployment-to-heroku)
    * [AWS Static \& Media Files](#aws-static--media-files)    

* [Credits](#credits)
  * [Code Used](#code-used)
  * [Media](media)
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

    * Allow staff to login to the restaurant side of the website.

    * Allow staff to view orders and sign-off on orders as completed for dispatch.

    * Allow staff to tally both orders and revenue for that particular day.

## Design

### Colour Scheme

The colour scheme used throughout the project was intended to be consistant with most if not all pages and consisted of bootstrap colour classes and other CSS colour classes:

Bootstrap:

* bg-success, text-success: #28a745, a shade of green used for the navigation bar and the footer.

* text-white: #fff, a shade of white used on the navigation and footer links as well as page headers.

* text-danger: #dc3545, a shade of red (ruby) used with the font awesome cross icons.

* btn-outline-primary: #007bff, a shade of cyan-blue used to style all buttons used in placing orders and marking the orders as dispatched.

* btn-info: #17a2b8, a shade of cyan used to style the staff login button.

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
* [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) Python SDK for AWS, used to directly create, update, and delete AWS resources from my Python scripts.
* [psycopg2](https://pypi.org/project/psycopg2/) PostgreSQL database adapter.
* [Gunicorn](https://gunicorn.org/) WSGI server used to take care of everything happening between the web server and web application.
* [AWS](https://aws.amazon.com/) cloud-based storage service used to store static and, media files.
* [Paypal](https://developer.paypal.com/docs/archive/checkout/integrate/) was used to deal with payments. 
* [PEP8 Validator](https://pep8ci.herokuapp.com/) was used to check python code for errors
* [ElephandSQL](https://www.elephantsql.com/) was used to store PostgreSQL database.
* [Heroku](https://id.heroku.com/) was used to deploy the project.
* [Balsamiq](https://balsamiq.com/wireframes/) was used to create the wireframes for the website.
* [Am I Responsive](https://ui.dev/amiresponsive) To create the responsive banner of devices.
* [Google Fonts](https://fonts.google.com/) was used to import the Lato font into the base template head tags which is used on all pages throughout the project.
* [Font Awesome 6.5.1](https://fontawesome.com/) was used to add icons for aesthetic and UX purposes.
* [W3C Validator](https://validator.w3.org/) used to validate my HTML files.
* [JShint](https://jshint.com/) used to validate JS code.

## Testing

### Testing User Stories

* First Time Visitor Goals:

  * To understand how the site works and what its about.

    * Upon entering the home page the user will see the site name/logo in the top left hand corner of the navigation bar, the name indicates to the user what the website/application is and does. The navigation bar links clearly identify what page is which without ambiguity.

  * How to navigate the site.

    * The navigation bar links are clearly visible in the top right hand corner, each link tells the user what page is which.

  * Search the menu for what's available to order.

    * Clicking on the menu link in the navigation bar will direct the user to the menu page where they can either scroll down the page and see all the food items that are for purchase or they can search the menu using the search bar using various keywords.

* Returning Visitor Goals:

  * Be able to place an order by selecting items from the menu.

    * The user has two options by which to place an order, either by clicking on the "order now" button located in the centre of the landing page or in the navigation bar by clicking on the "place order" link, both options will redirect the user to the order page where they can select from a range of fast food items.

  * Be able to add delivery details such as name, email, address etc.

    * Once a user has selected what they would like to order from the menu list on the order page below that there is a form to allow the user to add their name, email address, full address which includes steet name and number, town or city, county and post code. This information is then posted to the database and the user is then redirected to an order confirmation page where they can review their order. 

  * Be able to pay for that order using a payment gate.

    * After the user has placed their order they are redirected to an order confirmation page where they can review their order which includes all items and the total price. At the bottom of the order confirmation page located above the footer there is a Paypal button which allows the user to pay for their order. The payment system used is not real for development purposes but uses Paypal's sandbox which is a self-contained, virtual testing environment that simulates the live Paypal production environment.

  * Allow staff to login to the restaurant side of the website.

    * Located in the footer there is an anchor url styled using bootstrap button clases which when clicked takes you to the restaurant side of the site which would allow a staff member to view current orders for the current day.

  * Allow staff to view orders and sign-off on orders as completed for dispatch.

    * Once a staff member has logged into the restuarant app there are two bootstrap cards at the top of the page, one displaying the total number of orders for that particular day. At the end of each table which displays the various order details there is a button to display the order information in another bootstrap card with a button to signoff an order as dispatched.

  * Allow staff to tally both orders and revenue for that particular day.

    * The restuarant app has two bootstrap cards displaying both total orders and the total revenue for a particular day.

### Manual Testing

* All throughout the development process as previously mentioned each page was consistently checked to make sure that they responded correctly to the various default breakpoints built into Chrome Developer Tools.

* The logo was clicked in each page to make sure that it was correctly linked to the home page.

* Each navigation bar link on each page was clicked to verify that it not only worked but took you to the correct page.

### Further Testing

* All pages that make up the website/application were tested using Chrome Developer Tools to check for responsivness at the various different breakpoints to see how the site would react to being viewed on different devices.

* The website was viewed on various different devices such as Desktop, Laptop, Google Nexus 7 tablet and my Blackview BV6000 Android phone.

* Friends and family members were asked to review the site to highlight any bugs or user experience issues.

### Bugs and Errors

There is a minor issue with the footer, using the bootstrap class of 'fixed-bottom' keeps the footer stuck to the bottom of each page where its featured on the site, the fixed footer unfortunately obscures the order button at the bottom of the order form and the PayPal payment button. Removing the 'fixed-bottom' class will resolve the issue but given the lack on content on the landing page the footer will then sit almost in the middle of the page.

Email comfirmations only appear in the terminal and not as an actual live email confirmation sent to a real email address.

Staff cannot logout of the restaurant side of the website once an order has been placed but are prompted to login when an order has been placed to allow them to sign-off an order as dispatched.

### Validation Testing

The W3C Markup Validation Service was used on all HTML pages, the use of the CSS Jigsaw Validator was omitted from this process due to the lack of external CSS, this would be attributed to the use of bootstrap in the project. The code was entered through direct input.

* HTML Validator:

  * Customers App:

    * The validator flagged the Jinja templating logic as the majority of errors raised, the image elements were flagged for having no alt attributes in the 'order' and 'menu_list' files but this was corrected afterwards.

* Restaurant App:

  * The only error messages raised with the HTML files in the restaurant app were with the Jinja templating logic, these were subsequently ignored as they are not considered major or fatal errors.

JShint was used to check any errors in the Javascript used as part of the PayPal API implementation script in the 'order_confirm' file.

* Undefined Variables:

  * paypal on line 57.

  * $ on line 91.

  * Three missing semicolons missing on lines 95, 99 and 101. These missing semicolons have now been added to the JS script in the 'order_confirm' HTML file. 

### Python Testing

Python PEP8 validation was done via Code Institue's Python Linter.

The files that were tested:

* Customers App: 

  * models.py

  * views.py

* Restaurant App:

  * account_adapter.py

  * views.py

* Root directory:

  * urls.py

The only errors received were some lines of text exceeded the character limit of 79 and some areas of trailing white space where comments are located.

### Lighthouse

Lighthouse was used to run a series of audits to improve the quality of web pages. Overall performance and errors are highlighted below.

Results:

* [Mobile](eGrub/egrub/static/img/Lighthouse-Mobile.PNG)

* [Desktop](eGrub/egrub/static/img/Lighthouse-Desktop.PNG)

The performance score can fluctuate because of changes in underlying conditions.

### Payments

When placing an order the following sandbox credentials are used:

* Email: sb-9oebo29133223@personal.example.com

* Password: D[8PJ1>d

I did not change the password because of one-time password generation the new password is not displayed.

When logging in to the restaurant side via the restaurant staff login button after payment has been processed the following superuser account credentials are used:

* Name: kdugg84

* Password: thisismypassword

With each order table there is a button on the right handside which when clicked will display the order details again and telling a staff member whether that person has paid of not with the option to press another button to mark the order as dispatched.

## Deployment & Local Development

### GitHub Deployment

The website/application is stored using GitHub for data and version control. To do this you follow these steps:

* After each addition, change or removal of code and by utilizing the IDE's terminal commands simply type:

  * git add.

  * git commit -m and include a git commit message with a brief description of what this particular commit envolves.

  * git push.

Following the above process allows you to view the updates made to the projects repository on GitHub.  

### Local Development

#### How to Fork

Forking is the process of creating a copy of the original repository. The process allows a developer to make any changes without affecting the main repo.

To do this:

* Search for the Github repo you want to copy.

* Select the "Fork" button located in the top right corner which is located under your profile icon.

* Once completed, you will now have your own version of that repo to make changes to.

#### How to Clone

To copy a Github repository:

* First navigate to the repository you wish to copy.

* Click on the "Code" button (which has a download icon) and copy the link provided.

* In the Gitpod terminal, navigate to the directory where you want to place the clone. Then, type "git clone" and paste the link you copied earlier and press enter.

* Another way to push a cloned repository to a new Gitpod workspace can be done through the use of a Gitpod extension installed in your prefered browser, in my case Google Chrome. This browser extension will add a green Gitpod button to your Github account and will be visible on every repository created, cloned or searched for.

## Deployment to Heroku

The project was deployed to Heroku with all static and media files stored on Amazon S3. I also set up automatic deployment to ensure my Heroku app was always up to date with my GitPod repository.

* Login to Heroku and from your dashboard click 'new' > 'create new app'.

* Enter your 'app name' and choose the appropriate region, then click 'Create app'.

* To use Postgres, install dj_database_url, and psycopg2 in the project terminal using the following commands;

  * $ pip3 install dj_database_url

  * $ pip3 install psycopg2

* Freeze the requirements to ensure Heroku installs all the apps requirements when deployed.

* To migrate to the Postgres database, go to settings.py and add the following import;

  * import dj_database_url

* Then down in the database's setting comment out the default configuration and replace the default database with a call to dj_database_url.parse and give it the database URL from Heroku.

* Apply all migrations using the following command, after migrations have been applied amend your database configurations.

  * $ python3 manage.py migrate

* Create a superuser to log in with using the following command;

  * $ python3 manage.py createsuperuser

* Go to the Settings tab on Heroku, scroll to the 'Config Vars' section, and click 'Reveal Config Vars' and enter the variables (key and value) contained in your environment settings.

* Install gunicorn using the following command;

  * $ pip3 install gunicorn
  
  * Then freeze into your requirements file.

* Create a Procfile and add the following line;

  * web: gunicorn egrub.wsgi:application

  * This tells Heroku to create a web dyno which will run gunicorn and serve the Django app.

* Last, you need to temporarily disable collectstatic to ensure that Heroku won't try to collect static files when we deploy. This is done by adding the below variable;

  * | DISABLE_COLLECTSTATIC | 1 |

* Add the 'hostname' of your Heroku app to allowed hosts in settings.py as well as 'localhost' so the project can still on on you IDE.

* Now you can commit all the changes and push to GitHub;

  * $ git add . $ git commit -m <'your commit message'> $ git push

  * If you created your app on the website you will need to initialize your Heroku git remote using the following command;

    * $ heroku git:remote -a <'your app name'>

    * Then use the following command to push to Heroku;

      * $ git push heroku master

### Automatic Deployment to Heroku

* From the Heroku deploy tab, select the Deployment method 'GitHub'.

* On the 'Connect to GitHub' section make sure your GitHub profile is displayed then add your repository name and click 'Search'.

  * Your repo should now be displayed below, click 'Connect' to connect to this app.

* Go to the Deploy tab on Heroku and under the Automatic deployment section, click 'Enable Automatic Deploys'. Then under Manual deploy click 'Deploy Branch'. 

  * Heroku will now receive the code from GitHub and start building the app using the required packages.

  * Once built you will receive the message 'Your app was successfully deployed' and you can click 'View' to launch your new app.

### AWS Static & Media Files

* Create an account by navigating to aws.amazon.com and clicking create an AWS account. Fill in your email and password, and a username for your account, and select continue.

* Now on the account type page, select personal and fill out the required information, click create an account and continue.

* Next you will be asked to enter a credit card number which will be used for billing if we go above the free usage limits. Beyond this, you'll be asked a couple more verification questions then once all required information is confirmed your account will be created.

* Now you can navigate back to aws.amazon.com and sign-in to your account.

* Navigate to AWS management console under my account and using the 'find services' search bar, find s3.

* Now open s3 and create a new bucket to store all your files.

  * Enter a name for your bucket (recommend naming your bucket the same as your Keroku app).

  * Select a region (Select the region closest to you like you did when creating your Heroku app).

  * Uncheck block all public access and acknowledge that the bucket will be public.

* Now click into your new bucket and set some settings;

  * On the properties tab and turn on static website hosting.

  * On the permissions tab;

    * Paste in a CORS Configuration to set up the required access between your Heroku app and your s3 bucket. The code is supplied by CodeInstitute.

  * In the Bucket Policy tab, select policy generator;

    * Policy type is 's3 bucket policy'.

    * Allow all principles using a *.

    * Actions is 'GetObject'.

    * Add in your ARN (found on previous page).

    * Click 'Add statement' then 'Generate policy'.

    * Copy the policy code and paste it into the bucket policy editor (To allow access to all resources in this bucket add a slash star onto the end of the resource key).

    * In the Access Control List tab, under the Public Access section, set the list objects permission to everyone.

* Create a user to access the bucket created.

  * Search for a new service 'IAM'.

  * Now open IAM, navigate to 'groups' and click 'Create new group'.

  * Create a policy by navigating to 'policies' and click 'Create policy'.

  * Go JSON tab and click 'import managed policy'.

    * Search for s3 and then import the s3 full access policy.

    * Replace resource value '*' with your bucket ARN from the bucket policy page.

    * Click 'Review policy', give it a name and a description and click 'Create policy'.

* Attach the policy to the group you created.

  * Navigate to 'groups', select the group you created and on permissions tab select 'Attach policy'.

  * Search for the policy you created, select it and click 'Attach policy'.

  * Now to create the user, navigate to 'users' and click 'Add user'

    * Add username, select programmatic access and click 'Next'.

    * Add user to a group by selecting the group you created and click 'Next' then click through to the end and click 'Create user'

    * Now download the CSV file which will contain this users access key and secret access key.

* To connect to Django, head to your project and install two new packages then freeze them into your requirements.txt;

  * $ pip3 install 
  
  * $ pip3 install django-storages

  * $ pip3 freeze > requirements.txt

* In settings, add 'storages' to installed apps.

* To connect Django to s3 add the 'USE_AWS' settings in an 'if' statement to the settings.py which will tell it which bucket it should be communicating with.

* Create a file called custom_storages.py

### Credits

### Code Used

* [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/)

* [Django Allauth](https://docs.allauth.org/en/latest/installation/quickstart.html#post-installation)

* [Django CSRF](https://docs.djangoproject.com/en/3.1/ref/csrf/)

* [PayPal Developer](https://developer.paypal.com/home/)

### Media

[Uber Eats](https://www.ubereats.com/gb/store/low-cost-fast-food/kETrDPZwSrG0LUrZ3EK9rw) Menu images and landing page hero image.

### Acknowledgments

* Jubril Akolade (My stand-in mentor for Chris) - for offering guidence and support for the project from it's inception, development and deployment.

* Code Institute student cohort on Slack - always offering help and solutions.

* Friends and family members for their feedback and support.