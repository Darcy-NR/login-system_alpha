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

