Code Locked
=============

Difficulty: medium

Tags: reversing, web

Description
-------------
Open the code lock at [http://ch.hackyeaster.com:2311](http://ch.hackyeaster.com:2311) to get your 🚩 flag.

Note: The service is restarted every hour at x:00.


Solution
-------------
When you go to this site, you're greeted by a pin pad with the numbers `0`-`9`, `*` and `#`.

When you enter a code and press `#`, you're told whether the code is correct or not, and there is a corresponding .mp3 played.
Pressing `*` will clear your input.

Taking a look at the page source, you'll see the `main.js` file in addition to the CSS, HTML and `jquery.js` files.
In a separate folder in the sources list is a WASM file, `ec9c407e` which gets instantiated when the document loads.

There is probably a way to decompile the WASM into human-readable code and just read the passcode out of that, but that's not the apporach I took.

The code in `main.js` calls into the code directly, and uses a globally available variable as the argument.
Using this knowledge, you can simply brute force the passcode.

The text at the bottom of the page states the passcode is 8 digits, so simply write a JS function to try all 10^8 possible combinations. ([code-lock.js](./code-lock.js) in this directory is one such function and wasn't provided by the challenge.)

Less than 30 seconds later, the answer will pop out!

Flag
-------------
`he2023{w3b4553m81y_15_FUN}`