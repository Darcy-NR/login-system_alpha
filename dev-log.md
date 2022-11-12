  //                          //
 //////[ 12 - 11 - 2022 ]//////
//                          //

DONE:

- Prettied up the code a little, moved the code that could be moved into its own files and import them for ease of modularity, I don't think I can move anything else.

  
TO-DO:

- Fix syntactic feedback issues
- Add a comment index so that stuff is easier to navigate

NON CRITICAL TO-DO: 

- As always make sure to pretty code up before submission

====================================================================
====================================================================

  //                          //
 //////[ 10 - 11 - 2022 ]//////
//                          //

DONE:

- Systems admin account added and piped into a systems menu
  - Menu lets sys admin print out a pretty table of the current accounts.json to user-tables folder
  - This marks pretty much the final feature update! The app is basically done!

  
TO-DO:

- Fix syntactic feedback issues
  - This is all there really is left to do, is to make the UX a little less iffy, consider adding a boilerplate function for messages
  - Finally clean up the code make it look nicer and make it easier to navigate
  - Work on the documentation for the app, primarily the pseudocode and function design and run some bug tests

NON CRITICAL TO-DO: 

- As always make sure to pretty code up before submission

====================================================================
====================================================================

  //                          //
 //////[ 09 - 11 - 2022 ]//////
//                          //

DONE:

- Reset Password now works works instead of just sort of working
  - User can select if they want to randomly generate the password or make their own
  - if they make their own they have to validate it first
  - add_user() now has parameter inputs as booleans so we can use the function across the code to do different things.
  - accounts.json is now updated dynamically with last login and pwd change depending on what is done.
  
TO-DO:

- Systems admin stuff
- Pretty table accounts output function for the sysadmin -- I am thinking the way to go about it is to just say bugger it and then store it as plaintext and then on the command that outputs the accounts.json in a beautified table for the SysAdmin that we just have it omit the password as "XXXXXXXX" or whatever?
- Fix syntactic feedback issues
  - We'll probably do this via having a boilerplate view function that takes a variable string is as its input and then dynamically displays output
  - That way we can just call on that view function whenever we need to do something and that can be what routes the user around.

- We're basically done after that.

NON CRITICAL TO-DO: 

- As always make sure to pretty code up before submission

====================================================================
====================================================================

  //                          //
 //////[ 08 - 11 - 2022 ]//////
//                          //

DONE:

- Reset Password now works
  - User selects the option, it asks them to enter an account and if that account exists it lets them change the password if they can provide the email
  - Currently there is no password validation for this so that will need to be added
  - Also no option for random password so maybe it takes you through a menu to add a random password if you prefer

TO-DO:

- validators on the inputs
- have it that the login updates last login
  - Takes user account, replaces the last_login with current date? I think that should work but theres a chance that it just wipes the whole entry, we'll see
- Systems admin stuff
- Pretty table accounts output function for the sysadmin -- I am thinking the way to go about it is to just say bugger it and then store it as plaintext and then on the command that outputs the accounts.json in a beautified table for the SysAdmin that we just have it omit the password as "XXXXXXXX" or whatever?

NON CRITICAL TO-DO: 

- As always make sure to pretty code up before submission

====================================================================
====================================================================

  //                          //
 //////[ 07 - 11 - 2022 ]//////
//                          //

DONE:

- Fixed a bug with the login system
- Added a placeholder function for reset password for tomorrow.

  
TO-DO:

- validators on the inputs
- have it that the login updates last login
  - Takes user account, replaces the last_login with current date? I think that should work but theres a chance that it just wipes the whole entry, we'll see
- Systems admin stuff
- Pretty table accounts output function for the sysadmin -- I am thinking the way to go about it is to just say bugger it and then store it as plaintext and then on the command that outputs the accounts.json in a beautified table for the SysAdmin that we just have it omit the password as "XXXXXXXX" or whatever?

NON CRITICAL TO-DO: 

- None yet

====================================================================
====================================================================

  //                          //
 //////[ 03 - 11 - 2022 ]//////
//                          //

DONE:

- Add users is done
- Users are added to the accounts list now, both registers are both functional
  - Should probably investigate email validation option

  
TO-DO:

- validators on the inputs
- have it that the login updates last login
  - Takes user account, replaces the last_login with current date? I think that should work but theres a chance that it just wipes the whole entry, we'll see
- Systems admin stuff
- Pretty table accounts output function for the sysadmin -- I am thinking the way to go about it is to just say bugger it and then store it as plaintext and then on the command that outputs the accounts.json in a beautified table for the SysAdmin that we just have it omit the password as "XXXXXXXX" or whatever?

NON CRITICAL TO-DO: 

- None yet

====================================================================
====================================================================

  //                          //
 //////[ 01 - 11 - 2022 ]//////
//                          //

DONE:

- Password Validator is done
  - Password validator function checks length and checks if password is valid to within Gelos standards
  - User can enter a password and new account and if their password is not valid it will refuse
  - Users can randomly generate a password that is valid within standards and then it will output all
  
TO-DO:

- validators on the inputs
- have it that the login updates last login
- Systems admin stuff
- Pretty table accounts output function for the sysadmin -- I am thinking the way to go about it is to just say bugger it and then store it as plaintext and then on the command that outputs the accounts.json in a beautified table for the SysAdmin that we just have it omit the password as "XXXXXXXX" or whatever?

NON CRITICAL TO-DO: 

- None yet

====================================================================
====================================================================

  //                          //
 //////[ 31 - 10 - 2022 ]//////
//                          //

DONE:

- Versions are finally inified lmao
- Registration pages are partially set up
    - User can input if they want a randomly generated password or to use their own
    - inputs are ready on both
- User is shown their login time when they exit out

TO-DO:

- validators on the inputs
- have it that the login updates last login
- Systems admin stuff
- User can create a password that if it satisfies the 3 requirements or whatever can proceed
- A password generator
- Pretty table accounts output function for the sysadmin -- I am thinking the way to go about it is to just say bugger it and then store it as plaintext and then on the command that outputs the accounts.json in a beautified table for the SysAdmin that we just have it omit the password as "XXXXXXXX" or whatever?

NON CRITICAL TO-DO: 

- None yet

====================================================================
====================================================================

  //                          //
 //////[ 28 - 10 - 2022 ]//////
//                          //

DONE:

- Login System is even more finished
- The system now keeps track of failed logins via a global variable, and sends the user down a placeholder route after 3 fails
- Realistically there isn't a lot more I can do without a unified version, I've been procrastinating getting my laptop. I will see about finally unifying the codebase tomorrow night.

TO-DO:

- I do really need to unify the versions and get to work on a register user system
- User can create a password that if it satisfies the 3 requirements or whatever can proceed
- A password generator
- Pretty table accounts output function for the sysadmin -- I am thinking the way to go about it is to just say bugger it and then store it as plaintext and then on the command that outputs the accounts.json in a beautified table for the SysAdmin that we just have it omit the password as "XXXXXXXX" or whatever?

NON CRITICAL TO-DO: 

- None yet

====================================================================
====================================================================


  //                          //
 //////[ 27 - 10 - 2022 ]//////
//                          //

DONE:

- Login System is more or less functional
    - End user can provide username and password
    - If user exists and password matches then they login and are given their welcome message
    - If password doesn't match then at the moment it just gives them a static screen, I will need to figure out how the hell reset password system is gonna work, obviously it will touch a counter as it goes by? The issue is I don't have a database to store this stuff so its going to have to be instance based, the easy solution is just 3 failed logins, but that creates the issue that the user can fail any 3 logins and get sent to reset password. The thing is, who cares right, I can just send them to the splash page for reset password.

TO-DO:

- I do really need to unify the versions and get to work on a register user system
- User can create a password that if it satisfies the 3 requirements or whatever can proceed
- A password generator
- Theoretically this means I should be able to login but the issue is that the display needs to encrypt user passwords on output? I have no idea how to do this I am not sure if terry wants the stored passwords to be encrypted.
- I am thinking the way to go about it is to just say bugger it and then store it as plaintext and then on the command that outputs the accounts.json in a beautified table for the SysAdmin that we just have it omit the password as "XXXXXXXX" or whatever?
- This should be all stuff easily done tomorrow

NON CRITICAL TO-DO: 

- None yet

====================================================================
====================================================================

  //                          //
 //////[ 26 - 10 - 2022 ]//////
//                          //

DONE:

- Figured out the format for our user accounts, storing them as JSON objects in an accounts file, using python's json module we can dump the json to a python dictionary, then read it as a regular key value dictionary. Which should theoretically let us parse individual objects much like we were reading this from a database or something.

- Then we can use regular python dictionary expressions to add a new user account via variables to the existing dictionary, dump it back as a json and then write it to the file, effectively allowing us to read and write to the object as the store.

- The front end is pretty much done, I just need to unify the version control now onto github so that we can actually effectively get to work on the functionality.

TO-DO:

- I need to refactor the existing accounts json *again* it shouldn't take as long this time around it just requires assembly of the dozen or so files into standalone json objects in a single array (test-accounts.json rather than accounts.json)

- I want to get login functionality, basically...
    - User presents username and password into login()
    - Login reads storage, finds username where username == {input}
        - Are storage password and {inputpassword} ==? THAN display a simple "success message" else display a simple "fail message"
- Theoretically this means I should be able to login but the issue is that the display needs to encrypt user passwords on output? I have no idea how to do this I am not sure if terry wants the stored passwords to be encrypted.
- I am thinking the way to go about it is to just say bugger it and then store it as plaintext and then on the command that outputs the accounts.json in a beautified table for the SysAdmin that we just have it omit the password as "XXXXXXXX" or whatever?
- This should be all stuff easily done tomorrow

NON CRITICAL TO-DO: 

- None yet

