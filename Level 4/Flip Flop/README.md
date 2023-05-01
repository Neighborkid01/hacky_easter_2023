Flip Flop
=============

Difficulty: medium

Tags: web

Description
-------------
This awesome service can flipflop an image!

Flag is located at: /flag.txt

[http://ch.hackyeaster.com:2310](http://ch.hackyeaster.com:2310)

Note: The service is restarted every hour at x:00.


Hint
-------------
Flipflopped with Imagemagick


Solution
-------------
The Imagemagick library is vulnerable to certain tokens being inserted into the headers of .png files.
I think this is what I found that got me to the answer [https://www.metabaseq.com/imagemagick-zero-days/](https://www.metabaseq.com/imagemagick-zero-days/).

I used `pngcrush` to create a 1px png and insert the tEXt header, but I couldn't get it to run on macOS, so I ran it in a Windows VM to get the solution.


Flag
-------------
`he2023{1m4g3-tr4g1cK-aga111n}`