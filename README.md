# PennApps Backend Technical Challenge
Here is what I ended up doing:
For part 1, I implemented the authentication fully and I also decided to do the <b>BONUS</b> for this step which means I decided to protect the ('/') and ('/application') routes as I felt that we only want people associated with an account to be able to access the home page and be able to submit an application.

For part 2, I implemented the application and heavily modified models.py to support the fields of interest to us (everything is in models.py). Furthermore, I also implemented the <b>BONUS</b> for this so teammates can only add other registered user emails as teammates.

Part 3 <b>BONUS</b>
I allowed users to edit their applications, and this means that it pre-populates the appropriate information in the form.
I used Django forms to help with the application and the authentication steps. It makes the code more readable
I use the template tags to implement various conditionals throughout the templates. Essentially, these are vital for the editing portions for number 1.

