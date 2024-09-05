# Restaurant Sakura 

Restaurant Sakura is a fine dining restaurant focusing on the south east asian cuisine. On the webpage the site users can make a reservation at the restaurant, view the menu, get in contact with the restaurant and pretty much find all the information they need about this specific restaurant - including how to find it. It is a Full Stack website build with the help of the Django framework and offers the users full CRUD functionality to create, read/view, update and delete their reservation at the restaurant.

The live website can be seen [here](https://restaurant-sakura-5d42605299d1.herokuapp.com/)

## Table of content
- [UX/UI Design](#uxui-design)
  - [User Stories](#user-stories)
  - [Wireframes](#wireframes)
  - [Colour scheme](#colour-scheme)
  - [Project Planning](#project-planning)
    - [Agile methodologies](#agile-methodologies)
    - [Database design](#database-design)
- [Features](#features)
  - [Existing features](#existing-features)
  - [Header](#header)
  - [Navigation menu](#navigation-menu)
  - [Landing page](#landing-page)
  - [Location page](#location-page)
  - [Contact page](#contact-page)
  - [Book a table page](#book-a-table-page)
  - [Register account/login page](#register-accountlogin-page)
  - [Footer](#footer)
  - [Potential future features](#potential-future-features)
- [Technologies used](#technologies-used)
  - [Languages](#languages)
  - [Database](#database)
  - [Frameworks](#frameworks)
  - [Libraries & Additional Programs/Software/Tools](#libraries--additional-programssoftwaretools)
- [Manual Testing](#manual-testing)
  - [Responsivness](#responsivness)
  - [Browser compability](#browser-compability)
  - [Validator testing](#validator-testing)
  - [User Story testing](#user-story-testing)
  - [Bugs](#bugs)
- [Deployment](#deployment)
  - [Forking](#forking)
  - [Cloning](#cloning)
  - [Deployment to GitHub](#deployment-to-github)
  - [Deployment to Heroku](#deployment-to-heroku)
- [References/credit](#referencescredit)
  - [Content](#content)
  - [Media](#media)


## UX/UI Design

I went for a quite clean design on the webpage itself - a minimal colour scheme to let the images and functions do the talking, and to give a airy feel - quite like I imagine the restaurant itself feels when you visit it! I set out with really high ambitions when it came to designing nice looking menues, responsive modals and beautiful forms to fill out - all with the help of a perfect Bootstrap grid system. Some things I managed to do - the design and visual effects on menues and modals that I imagined jsut didn't cut it into the short window of time I had for the project. The main focus was to add functionality to the different pages and make sure that the CRUD-functionality for reservations work, that the authentication part works as it should and tht everything connects to the back-end and updates the Django Admin panel the way it should. To summarise - there si so much more I want to do with this webpage! But my ambition was a wee bit to high and the time a wee bit to short, as my mentor pointed out to me a couple of times. 


### User Stories

An agile approach was used to initialize the project - with Epics to draw out the structure for the user stories that needed to be written, and mainly to give me the bigger picture of the project. After the epics were set and the first round of user stories had been written, all the user stories were given labels to identify the must-haves, the should-haves, the could-haves and the wont-have - all in line with the MoSCoW prioritazion method.

When it was time to start building the project and write all the code I had about 15 User Stories to work with. Somewhere half way through the project I realised that there was not nearly enough of them to cover all the parts of the project , and even more so I came to the conclusion that I had not put enough effort into the Acceptance Criterias and Tasks belonging to each User Story to accually simplify the work process ... Lesson learned I went back to my User Story Kanban board and pretty much started from scratch - some stories were updated and a lot more were added. I put the effort in the second time and got User Stories that really helped me in the coding process and gave me a lot of testing tools to validate teh functions on the webpage. As you can imagine this process  took a lot of time that I didn't really have that far into the project - so I learned the lesson the hard way to really take the time at the beginning of the project. But it also meant that I am really comfortable with the process of writing User Stories now, whick hopefully will help me in my next project. 

I ended up with a total of 24 User Stories to work with in the end, the majority o them made it into the "Done" coloumn on my Project Board, while some simply didn't make it into the project at this point due to the short amount of time at my disposal. Those stories will on the other hand be great to use if I want to continue work on the project and create a really good portfolio piece for the future. 

![printscreen user story]()

I do belienve some of the stories could have been split up into even smaller parts and tasks, but if I were t do that the process would be even longer - so hopefully they are enough to give a general feel for the project and its purpose for the users. There are also a lot of Stories regarding the Admin that could have been drawn out, but since my project doesn't focus on operation and andministration of an actual restaurants webpage but at this point mainly focus on the User and their interaction with the back-end and front-end of the website - I leave those stories for the future.  

Below are the epics and the Stories I ended up with. If they made it all the way or need more work I will discuss further down in the [User Story testing](#user-story-testing) section. 


__EPIC: Book a table__

- As a __Site User__ I can book a table at the restaurant online so that I can easily reserve a table at a time that it fits me.

- As a __Site User__ I want the booking process to be as simple as possible so that I can make a reservation and be at ease in the process while doing it.

- As a __Site User__ I can specify special requests or needs when making my booking so that the restaurant can accommodate me.

- As a __Site User__ I can receive an email confirmation of my reservation so that I can find the information about my reservation later.

- As a __Site User__ I can view the restaurants booking policy before completing the form so that I know what to expect before I book a table.

- As a __Site Admin__ I can view all bookings for the day/week/month online so that I can make sure we don't overbook and are capable of giving the customers excellent service.


__EPIC: Manage reservations__
 
- As a __Site User__ I can register an account so that I can view a list of my reservations and modify my reservations online.

- As a __Site User__ I can login to my account from any device so that I can view, edit or delete my reservation.

- As a __Site User__ I can edit or cancel my reservation online so that I can adjust my booking if my plans change.

- As a __Site User__ I can delete my own reservation online so that I don't have to contact the restaurant via phone or email to do so.

- As a __Site Admin__ I can view the total number of already booked seats at a given time/date so that we can prevent overbooking the restaurant.


__EPIC: Contact the restaurant__

As a __Site User__ I can easily find the restaurants contact information so that I can contact them if I have any questions or requests.

As a __Site User__ I can find the restaurants opening hours so that I know when I can contact them with possible questions or inquiries.

As a __Site User__ I can fill out a contact form so that I can send inquiries without having to call the restaurant or send a separate email.

As a __Site Admin__ I can view all incoming messages from the Contact form so that I can respond to the user.


__EPIC: Locate the restaurant__

As a Site User I can find information about the restaurants psycial location so that I can find my way there.

As a Site User I can view a map of the restaurants location so that I can navigater there by car, public transport or on foot.

__EPIC: View the menu__

As a Site User I can view the restaurants menu so that I can decide if this is a restaurant for me.

As a Site Admin I can easily update the menues ans prices so that the customers always have the latest info about what's avaliable at the restaurant.

__EPIC: Reviews__

As a Site User I can write a review of the restaurant so that other people will know if the restaurant is worth a visit.

As a Site User I can read reviews from earlier customers so that I can get a feeling for the restaurants food and quality.

As a Site Admin I can moderate and respons to reviews so that all feedback is handled in the right way.


### Wireframes

Wireframes for both the mobile design and larger devices such as tablets and computers were made using [Balsamique](https://balsamiq.com/). The apporach was quite a simple but straight forward design and almost every view got its own wireframe to make the code process as simple and effective as possible, since the design was already drawn out. I really loved the process and even though I made some changes to some pages along the way, due to it not looking as I imagined when for example responsivness came into the picture - I kept all of the wireframes in its original state as a reference.

Below are some examples:

The first example shows the landing page viewed in a browser on a computer or larger tablet - featuring the navigation bar with all its content visible, the header image/jumbotron and what I believe to be the two most important buttons on a restaurants webpage from a users perspective.

![printscreen](/static/images/wireframes/main_landing_page.png)

Below is a wireframe for the landing page on a computer or larger tablet when the visitor scrolls down a bit, it shows a feature with an image gallery that would be a nice feature, but unfortunately it did not make it into the project at this point due to other functions with a higher priority that needed to be in place first. 

![printscreen](/static/images/wireframes/third_view_landing_page.png)

Next up are some of the wireframes for the mobile view, I wanted the main view on mobile screens to be quite simple and straight forward. A drop down menu instead of a navigation bar to save som space, and focus on the jumbotron plus booking and menues. Below is also an example of one of the projects other pages in mobile view - the Contact page where site visitors can find all of the information the need to get in contact with the restaurant, or fill out a form if they wish.

![printscreen](/static/images/wireframes/mobile_landing_first_view.png)![printscreen](/static/images/wireframes/mobile_contact_page.png)

Here you can view the same Contact page, but designed for a web browser instead. Here Bootstraps grid system came in really handy to simplify the process of making every page responsive for all screen sizes. Although the Contact page was one of the pages that changed its look during the coding process due to a better visual solution, but here is the original idea. 

![printscreen](/static/images/wireframes/contact_page.png)

There were 13 wireframes made in total, which can all be found [here](/static/images/wireframes/).


### Colour scheme

Since Sakura means Cherry Blossom, I let cherry blossoms set the colour scheme for the page. The soft pink is in focus, accompanied by a mid tone grey on buttons and other details. I think the use of not to many colours allows the images and text to take the center stage, which is exactly my goal and what I imagine a restaurant like this would want. 



### Project planning


### Agile methodologies

- Kanban board - I used the Project Board in GitHub for the planning of the Project. Issues were created as User Stories with Acceptance Criterias belonging to each User Story. The User Stories were also assigned with some tasks, to clarify for myself what each User Story demanded of me. As discussed above I had to come back to my Project board and redo plus add some stories, but this just meant that I learned the value of a good Agile approach even more. 

As I love working on the design of a web page it's easy to put way to much time on that part, so the User Stories really helped me to focus on the functionality of the project first and foremost.

- Epics - I really understand the value of Epics for larger projects, to give a better overview of the projects user stories and further prioritize the work process. But they seem a little over-ambitious for a project of this size, although they work well with my brain.

- MoSCoW Prioritization - The User Stories are labeled with one of the following four categories, all according to the MoSCow prioritization methodology:

  - Must Have: Features and requirements that are absolutely neccessary for the product to function and for the website to fulfill its purpose. These User Stories have the highest priority. 

  - Should Have: Important features that should be included if possible, but they are not critical for the website to function.

  - Could Have: Desirable features that can be added if there is enough time and resources.

  - Won’t Have: Features that will not be included in the project at this point, but might be a desirable feature in future development. 


Important to note in this project is that some features which I believe are essential to a restaurants webpage and management system (and are therefor labeled with must-have) also got a wont'have label at this stage of the development - since my focus in this project isn't on the administration and management of a restaurants website but mainly on the user experience. I would love to work with those components in the future though!

![printscreen MoSCoW label prioritization]()



### Database Design

Looking in the rearview mirror I set out to design a project that was a little to big to handle for little ol me - every page on the site got its on app in the root directory, because I had an idea that every page would have features that demanded its own models, views and so on ... Turns out that pages on the site like menues, location and contact could have consisted of just plain html-files placed in the projects root templates folder accompanied by some custom css. On the other hand the project is prepped for a majority of functions and cool add-ons on every page in the future since they are all structured as apps. Below is the root directory of my project, with "sakura" being the projects name, and the "booking"-app unfolded to show the content of one of the apps that fulfilles its purpose as an app at the moment. 

![printscreen root directory](/static/images/printscreen/root_directory.png)


__Entity Relationship Diagrams(ERD)__

Two custom models were made for the project, one to handle the "Book a table" form in the booking-app, and one to handle the "Contact"-form in the contact-app. Below is the original ERD's that were drawn out before the models were made. The User model is handled by the Django Framework. The ERD shows that the User model has a one-to-many relationship with my custom BookATable model - a User can make many bookings and many fields in the User model can be associated with the BookATable model, while only one field in the BookATable model is associated with one exact line in the User model.

![printscreen entity relationship diagram](/static/images/erd_diagram.png)


I ended up making some adjustments to both my custom models later on in the development, some time after the ERD's were made. the ContactRestaurant model has been updated with a CharField for "Subject", for easier administration of the incoming questions from user. The BookATable got a CharField to be able to handle timeslots - instead of a TimeField(courtesy of my mentor).


![printscreen bookatable model](/static/images/printscreen/bookatable_model.png) ![printscreen contactrestaurant model](/static/images/printscreen/contact_restaurant_model.png)


My BookATable model got some extra features to deal with form valiation that I would not have sorted out without the help of my mentor Spencer Barriball. 

![printscreen additional features bookatable model](/static/images/printscreen/additional_functions_bookatable_model.png)


Spencer also supported me in creating a BookingManager that checks to se if the model does the trick in the database, besides from what I can see in the Django admin panel. I can run a command like the one below to be able to see all of todays booking in the terminal and make sure the database si running as it should:
"todays_bookings = BookATable.objects.todays_bookings()
print(todays_bookings)"



## Features

### Existing features


### Header

The main page/landing page is primarily made up of a header image/jumbotron with the restaurants name, a short tagline below to give the site visitor a quick understanding of what the place is all about, and two buttons leading the site visitor to either Book a table, or give them the possibility to view the menues - two features which to me are the primary functions on a restaurants webpage. Below the header image is some short text to give some more context to the page, along with the restaurants Opening hours - which I think a lot of visitors search for when visiting a wepage such as this. 

![printscreen header and info section](/static/images/printscreen/header_info_section.png)

The mobile version containts pretty much the same features but presented in a responsive way, fitting into different screen sizes. I think some adjustmet of font sizes on smaller devices should have been made, but that wasn't a priority at the moment. 

![printscreen header mobile version](/static/images/printscreen/mobile_header.png)


### Navigation menu

The navigation menu consist of links to various other pages - such as a Contact page, a Location page, a page to view the menues and a highlighted button redirecting the visitor to the page where they can book a table. It also consist of links to the restaurants social media pages, which at the moment all lead to the various landing pages of the social media platforms. At the far right of the navigation menu are two links leading to a page for Registration or Sign In - so that the visitor have the option to register an acoount and then Sign in to be able to view, edit or delete their reservation - all in line with the __CRUD__ functionality. 

![printscreen web page navigation menu](/static/images/printscreen/nav-bar.png)

With the help of Bootstrap and some custom CSS styling the navigation menu becomes a drop down feature on smaller devices. On smaller screens the social media icons aren't visible to the visitor in the navigation menu - so that the menu doesn't take up to much space. Instead they are only visible in the footer area on smaller screens. 

![printscreen drop down navigation menu](/static/images/printscreen/nav_bar_dropdown.png)


### Landing page & Footer

When scrolling on the main page the next section consists of some hopefully tempting images and another Book a table-button to once again remind the user that they really need to do so! Here they can also find some contact information to the restaurant, alon with a link to the restaurants Contact form. 

![printscreen second view landing page](/static/images/printscreen/landing_page_second_view.png)

The last view on the main page consists of another appealing image and a button that leads the site user to the menu page. Here you can also view the webpage footer with the restaurants address, copyright info and links to social media.  

![printscreen third view landing page and footer](/static/images/printscreen/landing_page_third_view_footer.png)

On mobile devices one of the images dissappear, along with the repeating Book a table-buttons as to not stack to much stuff on top of each other. Below this content is just a responsive version of the footer.

![printscreen mobile second view landing page](/static/images/printscreen/mobile_second_view.png)


### Location page

The location page is pretty straight forward - information about where the restaurant is located and a interactive embedded map that the site user can zoom in and out on, maximize and get directions from.

![printscreen restaurants location page](/static/images/printscreen/location_page.png)

The mobile version of the location page is just a responsive version with the same content. 

![printscreen mobile restaurants location page](/static/images/printscreen/mobile_location_page.png)


### Contact page

On the Contact page the user can find all the information they can possibly need if the wan't to get in touch with the restaurant. Phone number, email adress and the restaurants adress is all there, in case somebody want's to send them a letter. There you also find the information about the restaurants opening hours, in the same style as on the main page. 

![printscreen contact information](/static/images/printscreen/contact_page.png)

Below the contact info is a handy form that the user can choose to fill out if they do not want to call or email the restaurant. The contact form is connencted to the Django admin panel for the administrator to view incoming questions and inquiries from site user and reply to them. 

![printscreen contact form](/static/images/printscreen/contact_form.png)

Mobile versions of the contact page - same contact but responsive layout. 

![printscreen contact information](/static/images/printscreen/mobile_contact_page.png) ![printscreen contact form](/static/images/printscreen/mobile_contact_form.png)

In line with a user friedly interface the site user gets an immediate respons valiadating that their message has been sent succesfully, or if there is any errors with the way they filled out the form. 

![printscreen user respons from contact form]()


### Book a table page

On the page called "Book a table" the user has the option to fill out a form to make a reservation at the restaurant, without having to contact the restaurant via email or phone. All with the goal of making it as simple for the site user as possible to make the excellent decision to visit the restaurant. The mobile version of the page looks and feels the same, but responsive to different devices of course.

The form contains a Timeslot function for the site users to choose from when making a reservation and validation functions that prevent users from picking a date back in time. There is also the option to add a message to the restaurant - all in line with the user story about being able to make special requests when making a reservation at the restaurant. 

plus cant book more than 30 days in advance, 
avaliable seats limit to 100

![printscreen book a tabel form](/static/images/printscreen/booking_page.png)

The site user will get a direct respons on the webpage confirming a successful booking, or different validation error messages if something is filled in incorrectly.They will also recieve an email confirmation containing the booking information. 

![printscreen user respons from booking form]()


### Register account/sign in and view reservations page



![printscreen]()

![printscreen]()

![printscreen]()

![printscreen]()



### Potential future features

The project became bigger than my skills 

a lot of functionality that needs to be added

but see the value in the functions that are actually there

closed dates

## Technologies used

### Languages
- HTML5
- CSS3
- JavaScript
- Python


### Database
- CI Database URL - used to store all data
Postgres


### Frameworks
Django - main framework for a secure and resuable development process


### Libraries & Additional Programs/Software/Tools
- Bootstrap - used for some of the front-end design. Mainly to make the page responsive and make use of Bootstraps grid system. It was accompanied by some custom CSS since I'm not all that familiar with Bootstraps many fuctions and add ons just yet. 
- Balsamique - used to create all wireframes for the project
- Cloudinary - 
- Django All Auth - used for user registration and authentication
- Django Crispy Forms - used for all forms on the page, mainly to control their behaviour and give them the same look.
- Django Summernote - used as the editor for the Admin panel
- dj-database-url - used to connect Django to database via URL
- Favicon - used for finding a tab icon, which also became part of the logo for the restaruant project
- Font Awesome - used for social media icons 
- GitHub - used to store all the code and the Projects Kanban board
- GitPod - used as the IDE during development
- Google Fonts - used for custom fonts on the entire page
- Gunicorn - used as the server to run Python code/Django on Heroku platform
- Heroku - used as the platform to deploy the project
- Lucidchart - used to create the Entity Relationship Diagrams, also known as ERD
- Pexels - used to find suiting images for all pages of the site
- Psycopg - 
- Whitenoice - used to handle the static files for deployment



## Manual testing


### Responsivness 

Mainly thanks to Bootstrap the page is responsive on all devices, from mobile phones to tablets, laptops and larger screens. It reaches a max-width on larger devices as to not look to stretched out. 

### Browser compability

The project has been tested on different browsers, such as: Google Chrome, Safari, Microsoft Edge and Mozilla Firefox. It looks and functions pretty much the same on all browsers. 

### Validator testing

HTML - through the official W3C validator.

![printscreen html validator]()

CSS -  the official Jigsaw validator.

![printscreen css validator](/static/images/printscreen/css_validation.png)

JavaScript - the JavaScript check in JSHint came back 

![printscreen javascript validator]()

Python - PEP8 Python Validator

There were quite a few files to run throught the PEP8 validator, many of them with too long lines and some trailing whitespace, but all have been corrected and hopefully no errors remain. 

![printscreen python validator](/static/images/printscreen/python_validator.png)

When testing the accessibility using Lighthouse for Chrome,

![printscreen lighthouse]()


### User Story testing

Acceptance criterias regarding cancellation 
The system prevents modifications or cancellations within a certain timeframe (e.g., 24 hours before the booking), if applicable.

Unique booking numer for reference, reminder of booking
boka bord för special event
upptagent tidsslot

The booking policy is included in the confirmation email sent to the visitor.

mailto:link i contact, phonenumber clickable

Special hours (e.g., holidays or special events) can be displayed and updated easily by the administrator.


 - Create an interface for administrators to update the hours without needing to modify code.

 interface for adminstrating bookings - here is were the user stories cannot be teested since such functions are above my ... great functions to build in the future if
 but for now the goal was to focus on an crud function for the user and authentication functions

 recover password

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

Datetime picker to work I turned to ChatGPT in the end since my Bootstrap one didn't work as intended

### Media

Favicon

Images were taken from Pixels.com

