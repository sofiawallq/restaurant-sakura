## Table of content
- UX Design
  - Wireframes
  - Database design
- Features
  - Header
  - Navigation menu
  - Landing page
  - Location page
  - Contact page
  - Book a table page
  - Register account/login page
  - Footer
  - Potential future features
- Technologies
- Manual Testing
  - Responsivness
  - Browser compability
  - Validator testing
  - User Story testing
  - Bugs
- Deployment
  - Forking
  - Cloning
  - Deployment to GitHub
  - Deployment to Heroku
- References/credit
  - Content
  - Media


## UX Design

### User Stories

An agile approach was used to initialize the project, with Epics to draw out the structure for the user stories a give me as a developer the bigger picture of the project. After the user stories and epics were finished they were given labels to identify the must-haves, the should-haves and the wont-have - all in line with ...


EPIC: Book a table

EPIC: Change or delete a reservation

EPIC: Contact the restaurant

EPIC: Locate the restaurant

EPIC: Look at the menu

EPIC: Handle bookings(administrator)



### Wireframes

Wireframes for both the mobile design and larger devices such as tablets and computers were made using Balsamique(LÄNK). The apporach was quite a simple but straight forward design and every view got its own wireframe to make the code process as simple and effective as possible, since the design was already drawn out. Below are some examples:

The first example shows the landing page viewed in a browser on a computer or larger tablet - featuring the navigation bar with all its content visible, the header image/jumbotron and the two most important buttons to focus on.

![printscreen](/wireframes/Main%20landing%20page.png)



![printscreen]()

![printscreen]()

![printscreen]()

All wireframes can be found [here](/wireframes/)


### Database Design


## Features


### Existing features


### Header

The main page is primarily made up of a header image/jumbotron with the restaurants name, a short tagline below to give the site visitor a quick understanding of what the place is all about, and two buttons leading the site visitor to either Book a table, or give them the possibility to view the menues - two features which to me are the primary functions on a restaurant web page. 

![printscreen]()


### Navigation menu

The navigation menu consist of links to various other pages - such as a Contact page, a Location page, a page to view the menues and a highlighted button redirecting the visitor to the page where they can book a table. It also consist of links to the restaurants social media pages, which at the moment all lead to the various landing pages of the social media platforms. At the far right of the navigation menu are two links leading to a page for Registration or Login - so that the visitor can have the option to Login and view, edit or delete their reservation - all in line with the __CRUD__ functionality. 

![printscreen web page navigation menu]()

With the help of Bootstrap and some custom CSS styling the navigation menu becomes a drop down feature on smaller devices. On smaller screen the social media icons aren't visible to the visitor in the navigation menu - so that it doesn't take up to much space. Instead they are only visible in the footer area on smaller screens. 

![printscreen drop down navigation menu]()


### Landing page

![printscreen]()


### Location page

![printscreen]()


### Contact page

On the Contact page the user can find all the information they can possibly need if the wan't to get in touch with the restaurant. Phone number, email adress and the restaurants adress is all there, in case somebody want's to send them a letter. 

![printscreen contact information]()

To make things even easier for the user there is a contact form on this page that the user can fill out to get in contact with the restaurant. 

![printscreen contact form]()

In line with a user friedly interface the user gets an immediate respons valiadationg that their message has been sent succesfully, or if there is any errors with the way they filled out the form. 

![printscreen user respons from contact form]()



### Book a table page

On the page called "Book a table" the user has the option to fill out a form to make a reservation at the restaurant, without having to contact them via email or phone. All with the goal of making it as simple for the user as possible to make the decision to visit the restaurant. 

![printscreen book a tabel form]()

![printscreen user respons from form]()


### Register account/login page


![printscreen]()

### Footer


![printscreen]()

### Potential future features


## Technologies


## Manual testing


### Responsivness 


### Browser compability


### Validator testing

HTML - through the official W3C validator.

![printscreen html validator]()

CSS -  the official Jigsaw validator.

![printscreen css validator]()

JavaScript - the JavaScript check in JSHint came back 

![printscreen javascript validator]()

Python - PEP8 Python Validator

![printscreen python validator]()

When testing the accessibility using Lighthouse for Chrome,

![printscreen lighthouse]()


### User Story testing


### Bugs



## Deployment


### Forking


### Cloning


### Deployment to GitHub

The website was deployed using a hosting platform in the form of GitHub. The steps to deploy are as follows:

In the GitHub repository of the project, navigate to the "Settings"-tab
Select "Pages" in the left-hand menu and in the "Source" drop-down menu select "Deploy from a branch"
In the "Branch" section below chose the main branch
When the main branch is selected the GitHub repository will automatically refresh and after a little while you will find the Deployed page on the right-hand side with a detailed list of every updated deployment going forward.
The link to the live project-site can be found here:


### Deployment to Heroku

This project was deployed using Heroku

Steps for deployment in Heroku:

Create a new app in Heroku
Under "Settings" add "Create Var" containing the key PORT and the value 8000.
Further down (still under the "Settings"-tab), add Buildpacks "Python" and "Node.js" - in that order.
Under the "Deploy"-tab choose Deployment method GitHub and connect to the right repository.
Manually deploy the project via main-branch.
The link to the mock terminal in Heroku can be found here:


## References/credit


### Content

Inspiration for the food and drink menues I borrowed from two of my favourite restaurants here in Gothenburg, Sweden: [Toso](https://toso.nu/) and [Cheri-Lee](https://www.cheri-lee.se/).




### Media

Favicon

Images were taken from Pixels.com

