# Restaurant Sakura 

Restaurant Sakura is a fine dining restaurant focusing on the south east asian cuisine. On the webpage the site users can make a reservation at the restaurant, view the menu, get in contact with the restaurant and pretty much find all the information they need about this specific restaurant - including how to find it. It is a Full Stack website build with the help of the Django framework and offers the users full CRUD functionality to create, read/view, update and delete their reservation at the restaurant.

The live website can be seen [here](https://restaurant-sakura-5d42605299d1.herokuapp.com/)

![printscreen responsive website](/static/images/printscreen/responsive_layout.png)

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
  - [Deployment to Heroku](#deployment-to-heroku)
- [References/credit](#referencescredit)
  - [Content](#content)
  - [Media](#media)


## UX/UI Design

I went for a clean design on the webpage itself - a minimal colour scheme to let the images and functions do the talking, and to give a airy feel - quite like I imagine the restaurant itself feels when you visit it! I set out with really high ambitions when it came to designing nice looking menues, responsive modals and beautiful forms to fill out - all with the help of a perfect Bootstrap grid system. Some of the things I managed to do - but the design and visual effects on menues and modals that I imagined, just didn't cut it into the short window of time I had for the project. The main focus was to add functionality to the different pages and make sure that the CRUD-functionality for reservations work, that the authentication part works as it should and that everything connects to the back-end and updates the Django Admin panel the way it should. To summarise - there is so much more I want to do with this webpage! But my ambition was a wee bit to high and the time a wee bit to short, as my oh so wise mentor pointed out to me a couple of times. 


### User Stories

An agile approach was used to initialize the project - Epics to set the main structure for the user stories that needed to be written, and to give me the bigger picture of the project. After the epics were set and the first round of user stories had been written, all the user stories were given labels to identify the must-haves, the should-haves, the could-haves and the wont-have - all in line with the MoSCoW prioritazion method.

When it was time to start building the project and write all the code I had about 15 User Stories to work with. Somewhere half way through the project I realised that there was not nearly enough stories to cover all the parts of the project, and even more so I came to the conclusion that I had not put enough effort into the Acceptance Criterias and Tasks belonging to each User Story to accually simplify my work process ... Lesson learned I went back to my User Story Kanban board and pretty much started all over - some stories I decided to keep and update with new criterias and tasks, and a lot more were added. I put the effort in the second time and got User Stories that really helped me in the coding process, plus they gave me a lot of testing tools to validate the functions on the webpage. As you can imagine this process took a lot of time that I didn't really have that far into the project - so I learned the lesson the hard way to really take the time at the beginning of the project. But it also meant that I am really comfortable with the process of writing User Stories now, whick hopefully will help me in my next project. 

I ended up with a total of 23 User Stories to work with in the end, the majority o them made it into the "Done" coloumn on my Project Board, while some simply didn't make it into the project at all at this point, due to the short amount of time at my disposal. Those stories will on the other hand be great to use if I want to continue work on the project and create a really good portfolio piece for the future. 

![printscreen user story](/static/images/printscreen/user_stories_list.png)

I do belienve some of the stories could have been split up into even smaller parts and tasks, but if I were t do that the process would be even longer - so hopefully they are enough to give a general feel for the project and its purpose for the users. There are also a lot of Stories regarding the Admin that could have been drawn out - but since my project doesn't focus on operation and andministration of an actual restaurants webpage, but at this point mainly focus on the User and their interaction with the back-end and front-end of the website - I leave those stories for the future.  

Below are the epics and the Stories I ended up with. If they made it all the way to the end or need more work I will discuss further down in the [User Story testing](#user-story-testing) section. 


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

- As a __Site Admin__ I can modify bookings in the admin panel so that I can make sure everybody gets seated and we have enough staff to care for every guest.


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

Wireframes for both the mobile design and larger devices such as tablets and computers were made using [Balsamique](https://balsamiq.com/). The apporach was as mentioned a simple but straight forward design and almost every view got its own wireframe to make the code process as simple and effective as possible, since the design was already drawn out. I really loved the process and even though I made some changes to some pages along the way, due to it not looking as I imagined when for example responsivness came into the picture - I kept all of the wireframes in its original state as a reference.

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

![printscreen moscow open issues](/static/images/printscreen/open_issues.png) ![printscreen moscow closed issues](/static/images/printscreen/closed_issues.png)


Important to note in this project is that some features which I believe are essential to a restaurants webpage and management system (and are therefor labeled with must-have) didn't make it into the "Done" column on my Kanban board. In fact they didn't even make it to "In progress" - since my focus in this project isn't on the administration and management of a restaurants website but mainly on the user experience. I would love to work with those components in the future though!



### Database Design

Looking in the rearview mirror I set out to design a project that was a little to big to handle for little ol me - I didn't manage to finish all the things I set out to do, but hopefully I got the important stuff in place. On the other hand the project is perfect to further develop and work with in the future. 
Below is the root directory of my project, with "sakura" being the projects name and the "booking"-app unfolded to show the content of one of the apps. The project consists of one app named landing_page that contains views and paths to html pages/templates such as Contact, Menu etc that dont need their own app structure. Then we have the booking-app and the contact-app which both contains custom models, views and forms.

![printscreen root directory](/static/images/printscreen/root_directory.png)


__Entity Relationship Diagrams(ERD)__

Two custom models were made for the project, one to handle the "Book a table" form in the booking-app, and one to handle the "Contact" form in the contact-app. Below is the original ERD's that were drawn out before the models were made. The User model is handled by the Django Framework. The ERD shows that the User model has a one-to-many relationship with my custom BookATable model - a User can make many bookings and many fields in the User model can be associated with the BookATable model, while only one field in the BookATable model is associated with one exact line in the User model.

![printscreen entity relationship diagram](/static/images/erd_diagram.png)


I ended up making some adjustments to both my custom models later on in the development, some time after the ERD's were made. the ContactRestaurant model has been updated with a CharField for "Subject", for easier administration of the incoming questions from user. The BookATable got a CharField to be able to handle timeslots - instead of a TimeField as was the case from the start (courtesy of my mentor).


![printscreen bookatable model](/static/images/printscreen/bookatable_model.png) ![printscreen contactrestaurant model](/static/images/printscreen/contact_restaurant_model.png)


My BookATable model got some extra features to deal with all the form valiation that I would not have sorted out without the help of my mentor Spencer Barriball. 

![printscreen additional features bookatable model](/static/images/printscreen/additional_functions_bookatable_model.png)


Spencer also supported me in creating a BookingManager that checks to se if the model does the trick in the database, besides from what I can see in the Django admin panel. I can run a command like the one below to be able to see all of todays booking in the terminal and make sure the database is running as it should:
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

The navigation menu consist of links to various other pages - such as a Contact page, a Location page, a page to view the menues and a highlighted button redirecting the visitor to the page where they can book a table. It also consist of links to the restaurants social media pages, which at the moment all lead to the various landing pages of the social media platforms. At the far right of the navigation menu are two links leading to a page for Registration or Sign In - so that the visitor have the option to register an acoount and then Sign in to be able to view, edit or delete their reservation - all in line with the __CRUD__ functionality. When logged in the user will instead see the options of "My reservations" or "Logout" at the far right.

![printscreen web page navigation menu](/static/images/printscreen/nav-bar.png)

With the help of Bootstrap and some custom CSS styling the navigation menu becomes a drop down feature on smaller devices. On smaller screens the social media icons aren't visible to the visitor in the navigation menu - so that the menu doesn't take up to much space. Instead they are only visible in the footer area on smaller screens. 

![printscreen drop down navigation menu](/static/images/printscreen/nav_bar_dropdown.png)


### Landing page & Footer

When scrolling on the main page the next section consists of some hopefully tempting images and another Book a table-button to once again remind the user that they really need to do so! Here they can also find some contact information to the restaurant, alon with a link to the restaurants Contact form. 

![printscreen second view landing page](/static/images/printscreen/landing_page_second_view.png)

The last view on the main page consists of another appealing image and a button that leads the site user to the menu page. Here you can also view the webpage footer with the restaurants address, copyright info and links to social media.  

![printscreen third view landing page and footer](/static/images/printscreen/landing_page_third_view_footer.png)

On mobile devices one of the images dissappear, along with the repeating Book a table-button, as to not stack to much stuff on top of each other. Below this content is just a responsive version of the footer.

![printscreen mobile second view landing page](/static/images/printscreen/mobile_second_view.png)


### Location page

The location page is pretty straight forward - information about where the restaurant is located and a interactive embedded map that the site user can zoom in and out on, maximize and get directions from.

![printscreen restaurants location page](/static/images/printscreen/location_page.png)

The mobile version of the location page is simply a responsive version with the same content. 

![printscreen mobile restaurants location page](/static/images/printscreen/mobile_location_page.png)


### Contact page

On the Contact page the user can find all the information they can possibly need if the wan't to get in touch with the restaurant. Phone number, email adress and the restaurants adress is all there, in case somebody want's to send them a letter. There you also find the information about the restaurants opening hours, in the same style as on the main page. 

![printscreen contact information](/static/images/printscreen/contact_page.png)

Below the contact info is a handy form that the user can choose to fill out if they do not want to call or email the restaurant. The contact form is connencted to the Django admin panel for the administrator to view incoming questions and inquiries from site user and reply to them. 

![printscreen contact form](/static/images/printscreen/contact_form.png)

Mobile versions of the contact page - same content but responsive layout. 

![printscreen contact information](/static/images/printscreen/mobile_contact_page.png) ![printscreen contact form](/static/images/printscreen/mobile_contact_form.png)

In line with a user friedly interface the site user gets an immediate respons valiadating that their message has been sent succesfully, or if there is any errors with the way they filled out the form. The validation is a po-up module created with the help of Bootstrap modules, and some custom js-script that I had to ask ChatGpt to debug in the end since I never got it quite right with redirectiong to the right urls. 

![printscreen user respons from contact form](/static/images/printscreen/contact_confirmation.png)


### Book a table page

On the page called "Book a table" the user has the option to fill out a form to make a reservation at the restaurant, without having to contact the restaurant via email or phone. All with the goal of making it as simple for the site user as possible to make the excellent decision to visit the restaurant. The mobile version of the page looks and feels the same, but responsive to different devices of course.

![printscreen book a tabel form](/static/images/printscreen/booking_page.png)

The form contains a Timeslot function for the site users to choose from when making a reservation and validation functions that prevent users from picking a date back in time. There is also the option to add a message to the restaurant - all in line with the user story about being able to make special requests when making a reservation at the restaurant. There are also some validation features making sure you cannot book a table to far into the future (30 days or more), and no bigger party than 8 guests. 

![printscreen validaton past dates](/static/images/printscreen/error_booking_date.png) ![printscreen validation 30 days](/static/images/printscreen/30_days_validation.png)

The site user will get a direct respons on the webpage confirming a successful booking, or different validation error messages if something is filled in incorrectly.

![printscreen user respons from booking form](/static/images/printscreen/booking_confirmation.png)


### Register account/sign in and view reservations page

The Sign-Up/Register and Sign-in page have the same feel to them and the forms got some styling with the help of Django Crispy forms. They both contain password validation.

![printscreen sign up](/static/images/printscreen/sign-up_page_large.png)

![printscreen sign in](/static/images/printscreen/sign_in_larger_screen.png)

The mobile version contains the same info but in a responsive design. 

![printscreen mobile sign up](/static/images/printscreen/sign-up_page.png) ![printscreen mobile sign in](/static/images/printscreen/sign_in_page.png)

When logged in the user has the option to logut, before they do so they get the question to confirm logging out a second time. 

![printscreen sign out confirmation](/static/images/printscreen/sign_out.png)


When registered and logged in the user has the option to view a list of their reservations (that have been made after they registered for an account) and there they can edit or choose to delte their reservation. The reservations are ordered by date with the closest upcomming one first.

![printscreen reservation list](/static/images/printscreen/list_reservations.png)

When choosing to edit the user is redirected to a form similar to the original Booking form, where they can update all the fields if they want to and then save their changes. 

![printscreen edit reservation](/static/images/printscreen/edit_reservation.png)

Unfortunately I didn't get an confirmation modal working for the edit confirmation and delete confirmation, so to confirm their actions the user is redirected to a new page, and then back to the list of reservations view. 

![printscreen edit confirmation](/static/images/printscreen/edit_confirmation.png)



### Potential future features

There are A LOT of features that can be added to the page. The project became a bit bigger than my current skill set and even though I probably would have worked out a lot of the functions if I had the time for it - I unfortunately do not at this point.

There is still many functions to be added when it comes to the administration of the page - such as a UX friendly interface for the staff to deal with customer inquieres, modify bookings and so on - but that is a whole different project. 

Another part of the project that would add a lot of value to the user would be a page dedicated to reviews. And those user stories I have written regarding reviews would have been a nice place to start to get the CRUD-functionality up and running. Unfortunately I didn't come to that conclusion until way to late into the project - so I decided to stick with the user being able to edit a reservation. If I were to do it again I would have started with a review page and probably be satisfied with that. 

I would also have loved some sort of interactive picture section, with for example images tagged on Instagram taken at the restaurant. 

Another important feature for a restaurant to have would be a function for sending an email to the visitor containing their booking confirmation and the booking policy, in case they make a reservation at the restaurant. I started working on that but quickly gave up the idea due to other functions that were more important to get up and running. 

I would also like to add some Acceptance Criterias and functions regarding cancellations closer than 24 hours before the reservation, a unique booking number for user reference when interacting with the restaurant, the ability to book tables for bigger events, notification of fully booked timeslots and the list goes on. 



## Technologies used

### Languages
- HTML5
- CSS3
- JavaScript
- Python


### Database
- CI Database URL (Postgres) - used to store all data.


### Frameworks
Django - main framework for a secure and resuable development process.


### Libraries & Additional Programs/Software/Tools
- Bootstrap - used for some of the front-end design. Mainly to make the page responsive and make use of Bootstraps grid system. It was accompanied by some custom CSS since I'm not all that familiar with Bootstraps many fuctions and add ons just yet.
- Balsamique - used to create all wireframes for the project
- Django All Auth - used for user registration and authentication
- Django Crispy Forms - used for all forms on the page, mainly to control their behaviour and give them the same look for a good UX
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
- Psycopg - PostgreSQL adapter for Python
- Whitenoice - used to handle the static files for deployment

Images are hosted in the projects static directory for this project, but in the future I want to work Cloudinary.



## Manual testing

The manual testing consisted of not only the things listed below, but the testing also meant asking everybody I know to test the website and all its functions - such as filling out the Contact form, Booking a table via the form, register for an account and then login to see their reservations - and of course try to update/edit or delete a reservation. All while I checked the admin panel for real-time action. 

### Responsivness 

Mainly thanks to Bootstrap the page is responsive on all devices - from mobile phones to tablets, laptops and larger screens. It reaches a max-width on larger devices as to not look to stretched out and looks alright on even the smallest mobile screens. I've asked friends and family to try it out on different devices to get as many opinions in as possible. 

### Browser compability

The project has been tested on different browsers such as: Google Chrome, Safari, Microsoft Edge and Mozilla Firefox. It looks and functions pretty much the same on all browsers. 

### Validator testing

- HTML - through the official W3C validator. There were some issues with buttons and anchor tags being mixed up in the html, so I had some sorting out to do. But now every bit of HTML code is up to standard.

![printscreen html validator](/static/images/printscreen/html_validator.png)

- CSS - through the official Jigsaw validator. No issues came back when i ran the code through the CSS validator. 

![printscreen css validator](/static/images/printscreen/css_validation.png)

- JavaScript - the JavaScript check in JSHint came back with some issues regarding syntax issues in some web browser, but nothing more than that so for now I will leave it at that.

![printscreen javascript validator](/static/images/printscreen/js_validator.png)

- Python - PEP8 Python Validator

There were quite a few files to run throught the PEP8 validator, many of them with too long lines and some trailing whitespace, but all have been corrected and hopefully no errors remain. 

![printscreen python validator](/static/images/printscreen/python_validator.png)

When testing the accessibility using Lighthouse for Chrome, the result didn't really end up where I like them to be, but I'll go with that for now. 

![printscreen lighthouse]()


### User Story testing

The User Story testing has been performed throughout the development. When building the site I moved the Stories I was working on into the "In Progress" column on my Kanban-board, and then checked that every acceptance criteria and task was fulfilled before moving it into the "Done" column. As you can see there are still Stories left in the "In progress" column, due to the fact that some criterias have been met, but not all of them. The project is still functional but I don't want to move them into the Done column until the criterias are fully met. 

For example the User Story about modifying reservations as an administrator have been met on two of the criterias, but the remaining two will not be fulfilled until an admin friendly interface is developed. 

![example user story modifying reservation](/static/images/printscreen/example_not_fulfilled_user_story.png)

Along with the User Stories about a review page that haven't made it out of the "Todo" column yet. These are really good Stories to work with in the future and like I mentioned earlier, they would have been alot easier to start out with. But sometimes the logical thinking goes out the window.

So the focus has been on getting some CRUD-functionality up and running with the User Stories about Booking a table, and authentication to go along with the stories about registration and login to a user account. Which I hope works as it should.

![printscreen kanban board]()


### Bugs

The bugs have been very present. I don't know how many times the url paths have stopped working the way they should and the number of "404 Page Not Found" messages I have caused are beond counting. 

Most of them have been sorted out in the end - mainly thanks to Google and some much needed troubleshooting with ChatGPT. Sometimes the AI made the situation even worse, so its a wonderful tool when you need help, but the brain needs to to the majority of the thinking still. 

Some things I haven't been able to sort out up to date - when a site user first makes a booking as a guest, and then registers for an accound the connection between their email and reservations isn't fully in place. So at the moment only users that have registered and then Make a reservation can view and edit their reservations. I tried to sort it out with adding a signals.py file to my booking app and updating the apps.py but its still not in place. 

Also some alert messages that follow along with the Django Allauth is causing havock on the admin page when you make a lot of successful registrations, sign ins, bookings and so on at the same time. Good thing the messages work though - but not in an optimal way just yet. 

At this point the confirmation messages for signing in and out only show up on the admin panel page, and even though I have tried to redirect the messages, create modules and tried to redirect the Sign-In action to a new page based on a confirmation html-file there were always a new error showing up - so for the being this function does not work as I intended it to. 


## Deployment

This project was deployed using Heroku.

### Forking

- Navigate to the GitHub repository.
- On the top right hand side, click the button named "Fork".
- A new page named "Create new Fork" will open up, where you can choose to edit hte name of the project.
- Click on "Create Fork" at the bottom of the page. 
- Now a copy of the project will appear in your list of repositories.


### Cloning

- Navigate to the GitHub repository.
- Click on the "Code" tab at the top of the repository and copy the URL for web that appears. 
- Open up the terminal in a code editor of your choice and change the current working directory to a new one you will use to clone the repository. 
- Type in "git clone" in the terminal, paste in the copied URL and press "Enter".


### Deployment to Heroku

1. Create and set up the Heroku app
- Login to your Heroku account and navigate to the dashboard.
- Click on the "New"-button to create a new app.
- Give the app a unique name.


2. Ready your code for deployment in your Code Editor.
- Install a production ready webserver for Heroku such as gunicorn by writing the following command in your terminal: pip3 install gunicorn~=20.1.0.
- Add gunicorn==20.1.0 to the requirements.txt file with the following command in your terminal: pip3 freeze --local > requirements.txt.
- Create a file called Procfile in the root directory of your project.
- Inside the Procfile declare that the web process followed by the command to execute your Django project: web: gunicorn yourprojectsname.wsgi
- Open the projects settings.py file an set DEBUG=False
- In settings.py add '.herokuapp.com' to the ALLOWED_HOSTS list.
- Git add, git commit and git push to GitHub so that all files are up to date in your repository.


3. Ready your database for deployment
- Create an env.py file and add the following:
import os
os.environ.setdefault( "DATABASE_URL", "")
os.environ.setdefault("SECRET_KEY", "your__secret_key")
- Check to se that your env.py file is added to the .gitignore file. 
- Make sure your settings.py has this code in it: SECRET_KEY = os.environ.get("SECRET_KEY").
- Click on the "Settings" tab and navigate to the "Reveal Config Vars" section. 
- Add a SECRET_KEY value to Herokus Config Vars.


4. Deployment with static files
- Install Python package for whitenoise with the command: pip3 install whitenoise==6.7.0
- Add whitenoise to your requirements.txt file with the command: pip3 freeze --local > requirements.txt
- Add 'whitenoise.middleware.WhiteNoiseMiddleware' to the list of MIDDLEWARE in settings.py below Django SecurityMiddleware.
- In settings.py add a path to staticfiles in this way: STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
- Run python3 manage.py collectstatic in the terminal to collect the static files and when asked to choose yes or no, type "yes" in the terminal.
- Check what Python version is used in your development environment and look up the supported runtime closest to your Python version. 
- Create a runtime.txt file in your apps root directory and add the Python version from the list of supported runtimes, in a format like this: python-3.12.5.


4. Deploy on Heroku
- Click on the "Deploy" tab on your Heroku Dashboard.
- Under the "Deploy method" section choose to Connect to GitHub, depending on earlier access you might be asked to authenticate using GitHub.
- Choose the projects repository in the list that apperas when you start to type in the search box. 
- Start a manual deployment of the main branch by scrolling to the bottom of the Deploy-page and click on "Deploy branch".
- Click "Open app" to view your deployed project. 
- Open the "Resources" tab and switch to Eco Dyno to keep the project up and running. 


## References/credit


### Content

Inspiration for the food and drink menues I borrowed from two of my favourite restaurants here in Gothenburg, Sweden: [Toso](https://toso.nu/) and [Cheri-Lee](https://www.cheri-lee.se/).

Datetime picker to work I turned to ChatGPT in the end since my Bootstrap one didn't work as intended.



### Media

Favicon

Images were taken from Pixels.com

