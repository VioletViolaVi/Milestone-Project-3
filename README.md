# My Third Project: Cinemagic
This project is based on creating an app/a website that is focussed on showing users different movies made available to watch at Cinemagic cinemas. The goal of this project is to encourage as many users as possible to sign up with Cinemagic to book movie tickets for watching the films advertised and then return to leave their opinions about the films they watched. In addition, this project makes use of the CRUD operations. Users are able to create accounts with Cinemagic, read details about movies and other user’s reviews, update their bookings to make changes to certain features such as the number of tickets they wish to book, the location they want to watch the movie etc and delete their bookings if they change their mind on their movie choice.

# UX
This website/app is for anyone who is interested in watching movies and relies on the personal opinion of others when deciding what movies to watch.
The user will want to achieve the ability to scroll through the movie options and have its details, posters and reviews immediately made available on the same landing page to help them make a decision, quickly on which movies to book tickets for.
Using this project is the best way to achieve this as it has taken precaution to ensure all information about the movies were made available on the homepage and accessible to everyone regardless of whether or not they have set up an account with Cinemagic.
## User Stories
- As a user of Cinemagic, I want to sign up to create an account, so that I can book tickets to watch one of the movies advertised by this company.
- As a user of Cinemagic, I want to create bookings of my movies of choice, so that I can document the: number of tickets, date of showing and location of the cinema I’ve requested.
- As a user of Cinemagic, I want to read the movie details and reviews of the offered movies, so I can make a more informed decision on which movie to select.
- As a user of Cinemagic, I want to read my booking information on my account, so I can be reminded of the: movie name, ticket quantity, showing date and location of the cinema I selected.
- As a user of Cinemagic, I want to be free to update my booking details on my account, so I can make changes to the: movie choice, ticket quantity, showing date and/or location of the cinema I selected if needed.
- As a user of Cinemagic, I want to be free to delete my bookings from my account, so I can declutter my account from unnecessary booking information resulting from having already seen the movie or changing my mind completely and deciding not to watch anymore.
## Designer Goals
- As the designer of Cinemagic, I want to create a sign up page that the user can be automatically directed to if they are not already logged in when trying to make a booking. I also want to ensure only a few relevant pieces of information are requested from the user when signing up, so the sign up process can be a quick and easy one to endure.
- As the designer of Cinemagic, I want to make the booking process appear on a modal whilst still on the homepage and then automatically direct the user to another page displaying all the information they just booked, so the user will have immediate access to their booking information for their reference.
- As the designer of Cinemagic, I want to organise the homepage to display the movie posters alongside their respective movie details and reviews centre-align with the user’s viewpoint, so obtaining information about the movies being offered will be made easier for them.
- As the designer of Cinemagic, I want to structure the user’s bookings page clearly with all the booked information placed in their correct sections and at the centre of the screen, so the user will easily be able to refer to their booked choices.
- As the designer of Cinemagic, I want to provide a fully functioning “change” button tailor made for each different set of bookings, so the user can simply press that button to edit the prefilled form of their current booking if they wish to make changes.
- As the designer of Cinemagic, I want to provide a fully functioning “delete” button tailor made for each different set of bookings, so the user can simply press that button to delete the respective movie booking they desire.
## Wireframes
![sidebar-mobile](wireframes/images/1.sidebar-mobile.PNG)
![sidebar-tablet](wireframes/images/2.sidebar-tablet.PNG)
![home-mobile](wireframes/images/3.home-mobile.PNG)
![home-tablet](wireframes/images/4.home-tablet.PNG)
![home-desktop](wireframes/images/5.home-desktop.PNG)
![review-modal-mobile](wireframes/images/6.review-modal-mobile.PNG)
![review-modal-tablet](wireframes/images/7.review-modal-tablet.PNG)
![review-modal-desktop](wireframes/images/8.review-modal-desktop.PNG)
![signup-mobile](wireframes/images/9.signup-mobile.PNG)
![signup-tablet](wireframes/images/10.signup-tablet.PNG)
![signup-desktop](wireframes/images/11.signup-desktop.PNG)
![login-mobile](wireframes/images/12.login-mobile.PNG)
![login-tablet](wireframes/images/13.login-tablet.PNG)
![login-desktop](wireframes/images/14.login-desktop.PNG)
![booking-modal-mobile](wireframes/images/15.booking-modal-mobile.PNG)
![booking-modal-tablet](wireframes/images/16.booking-modal-tablet.PNG)
![booking-modal-desktop](wireframes/images/17.booking-modal-desktop.PNG)
![bookings-page-mobile](wireframes/images/18.bookings-page-mobile.PNG)
![bookings-page-tablet](wireframes/images/19.bookings-page-tablet.PNG)
![bookings-page-desktop](wireframes/images/20.bookings-page-desktop.PNG)
![confirmation-modal-mobile](wireframes/images/21.confirmation-modal-mobile.PNG)
![confirmation-modal-tablet](wireframes/images/22.confirmation-modal-tablet.PNG)
![confirmation-modal-desktop](wireframes/images/23.confirmation-modal-desktop.PNG)
## Wireframe and Final Project Differences
### Home Page
* The “Reviews” button on the carousel was omitted. Instead each movie poster was made clickable where once clicked, the user would be taken to the corresponding movie review section underneath. As a result, the movie posters were fully visible to the users; not blocked in part by any buttons.
* The “BOOK NOW” button to be placed underneath the carousel was omitted. The button was left to only exist at the end of each review section making it faster and more convenient for the user to book a specific movie.  
* The stars for the star rating system were omitted from being used for the final version of the project. The decision was made to focus on the ability of the user to add descriptive comments about the different movies. It was seen as a more informative method for the user to gain a better understanding on how they might perceive the movie if they were to watch it, by scanning through the opinions left by other users.
* For the first selection box of the booking pop-up modal, the name of the respective movie was made the default choice. The “Ticket Quantity” selection box was changed into an input box so any number chosen by the user could be inputted (except 0). The title of the last selection box was altered to “Select Location”. Also, the “BOOK NOW” button was changed to read “SUBMIT” to emphasise that this was what will cause the user’s inputted data to be sent to Cinemagic. These changes were made to make it easier for the users to complete the form with ease.
* The “LEAVE A REVIEW” button was omitted from the homepage to only be present on the user’s bookings page. This was to make leaving a review simpler for the user as they would be able to reference the correct movie they had watched from the same page they were leaving a comment.
### My Bookings Page
* To create a more consistent layout, all the movie’s images were placed on the left-hand side with their details on the right and their reviews at the bottom. Their positions were no longer to be alternated. This was to help user’s learn how to navigate through the website quickly, avoiding frustration.  
* Regarding the user’s booking page, the images were replaced with their movie details i.e.: number of tickets, location of cinema, date for attendance and the owner of the booking. This aimed to provide a more descriptive account of the bookings when referencing, reading or making changes to them. Using an image was not sufficient. In addition, all the buttons were placed underneath the movie details to create a more organised structure.
* The “Rate it” title was replaced with the “Leave a Review” title in the leave a review pop-up modal because the stars were omitted; as previously mentioned .
* The delete pop-up modal’s content was changed to include the name of the selected booked movie to be deleted instead of just the “Are you sure?” confirmation question. It makes it clearer to the user which movie has been selected for deletion. Also, the “No” button was moved to the left-hand side in order to be seen before the “ Yes” button. This was done to further help avoid the user from deleting a booking by mistake; giving them more time to confirm.
### Administration Page
* An admin page was added. This was only accessible to the administration user. The decision was made to add this page to provide an easier way to interact with the MongoDB database when handling data. 
### Footer
* The “BOOK NOW” button was removed from the user’s bookings page as it could not have the respective movie names as a default selected choice due to there being no other content on the page whenever no bookings were present. This button was to only exist on the homepage as a result.  
* In an attempt to add more design to the footer, the social icons were styled in a grid on top of each other instead of just being inline for all screen sizes.

# Features
## Existing Features

# Deployment
This project was deployed to Heroku using the following steps:
1. Set __*debug=False*__ in the app.py file.
2. Created a requirements.txt file from the terminal, using __*pip3 freeze --local > requirements.txt*__, to allow Heroku to detect this project as a python app. 
3. Created a Procfile using __*echo web: python app.py > Procfile*__ from the Gitpod terminal so Heroku would be informed on which file runs the app and how to run this project. 
4. Created a web process using __*heroku ps:scale web=1*__ in the Gitpod terminal of the project.
5. Set the __*IP*__ address and __*PORT*__ environmental variables to __*0.0.0.0*__ and __*5000*__ respectively, to create the config variables on Heroku.
6. Added the __*SECRET KEY*__, __*MONGO URI*__ string and the __*MONGO_DBNAME*__ to Heroku as part of the config variables.
7. Created a new Heroku app, uniquely named it after this project i.e. __*milestone-project-3-vivian*__ and set its region to Europe.
8. Installed the Heroku command line interface/toolbelt and typed __*heroku*__ in the Gitpod terminal to ensure Heroku had been installed in Gitpod.
9. Typed __*heroku login*__ in the Gitpod terminal and copied the URL browser link provided into a new browser to login into Heroku.
10. Linked local GitHub repository to Heroku which allowed for git commits, from the Gitpod terminal, to be pushed from Gitpod to Heroku.
11. Added the Heroku git URL as a remote in the Gitpod terminal using __*git remote add heroku https://git .heroku.com/milestone-project-3-vivian.git*__
12. Used __*git add .*__ to add everything from the project then __*git commit -m “Deploy project” and git push -u heroku master*__ to commit and push the project to Heroku respectively.
13. Clicked the __*Enable Automatic Deploys*__ button located in the __*Deploy*__ section of Heroku to allow for automatic deploys.
14. Clicked the __*Deploy Branch*__ button located in the __*Deploy*__ section of Heroku to finally deploy this project.
15. Clicked the __*View*__ button to launch this project's app.

# Credits
## Content
- Some of the responsive breakpoints used were taken from Bootstrap.
- The fonts used in this project were taken from Font Awesome.
- Code from Materialize was used to create the following:
  - The movie carousel
  - All the modals 
  - All tables present on the administration page
  - All the buttons
  - Both the top and side navigation bars
## Media
- The images used for this app/website were taken from Unsplash.
## Acknowledgements
- I received inspiration for this project from the following websites:
  - MOVIETICKETS.COM: https://www.movietickets.com/
  - IMDb: https://www.imdb.com/
  - ODEON: https://www.odeon.co.uk/ 
  - SHOWCASE: https://www.showcasecinemas.co.uk/
  - VUE: https://www.myvue.com/
  - Stackoverflow: https://stackoverflow.com/questions/38196104/how-to-change-background-color-of-datepicker-form-in-materialize-design
  - W3schools.com : https://www.w3schools.com/howto/howto_css_image_text.asp
  - RandomKeygen: https://randomkeygen.com/
  - Masterpiece Generator: https://www.name-generator.org.uk/quick/ 
  - Fantasy Name Generators: https://www.fantasynamegenerators.com/film-studio-names.php 





tec. used:
https://www.mongodb.com/cloud

https://randomkeygen.com/ - random password generator
https://www.w3schools.com/howto/howto_css_image_text.asp - text on images
https://www.name-generator.org.uk/quick/ - name generator
https://www.fantasynamegenerators.com/film-studio-names.php - studio generator
https://stackoverflow.com/questions/38196104/how-to-change-background-color-of-datepicker-form-in-materialize-design - datepicker css custom
https://unsplash.com/photos/rX12B5uX7QM - drowning, Photo by Ian Espinosa
https://unsplash.com/photos/AbNO2iejoXA - dog, Photo by Ryan Walton
https://unsplash.com/photos/oMpAz-DN-9I - moon, Photo by Greg Rakozy
https://unsplash.com/photos/NMk1Vggt2hg - survival, Photo by Daniel Jensen
https://unsplash.com/photos/xgsbOPIx75I - rose, Photo by Mathilda Khoo
https://unsplash.com/photos/9cRDDvhpBRw - handholding, Photo by Valentin Antonucci
https://unsplash.com/photos/hYr1wGeDSU0 - woman, Photo by Dollar Gill
https://unsplash.com/photos/Jigc7F9q7Ik - skull, Photo by Max Kleinen
https://unsplash.com/photos/mSoetyVbW_Y - seaport, Photo by Alessio Lin
https://unsplash.com/photos/aoEwuEH7YAs - man, Photo by Lucas Gouvêa
