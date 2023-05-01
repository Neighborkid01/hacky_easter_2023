Igor's Gory Passwordsafe
=============

Difficulty: easy

Tags: web

Description
-------------
You found the following letter:

Hi Peter

_Thanks again for your help in cryptography to make the passwordsafe secure. Now_

- _The passwords of the user are stored in a irreversible way (bcrypt)_
- _All passwords in the safe are encrypted by a strong symmetric key_

_Kind regards, Roy_

Open the passwordsafe at at [http://ch.hackyeaster.com:2312](http://ch.hackyeaster.com:2312) to get your 🚩 flag.

Note: The service is restarted every hour at x:00.


Hint
-------------
No brute forcing needed, really!


Solution
-------------
This challenge presents you with a few options in the nav bar and a login page.
You can register a new user and you'll be redirected to a list of your passwords(which is currently none).

Click `Add password` from the menu and fill out the form (the contents don't matter), and you'll see it be added to the list.
There are a few things you can do from here, but one of those is click the link to copy your password.

If you're watching the networking tab in your browser's developer tools, you might notice a request to `http://ch.hackyeaster.com:2312/get/12` (or whatever the ID of your password is).

This GET request returns the password in plaintext, so it's definitely not the most secure password manager...

If you move this into a tool like Postman, you can change the ID to see which passwords you can access.
After adding the cookie from your browser, you can see that you can access any password in the database.

With a bit of playing around, you'll find that `http://ch.hackyeaster.com:2312/get/7` returns the flag.

Flag
-------------
`he2023{1d0R_c4n_d3str0y_ur_Crypt0_3ff0rt}`