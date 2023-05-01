Going Round
=============

Difficulty: medium

Tags: crypto

Description
-------------
I got a flag, but it's encrypted somehow:
`ip0232j{1t_x_v0z4b3bm__v4xvq}a`

It was created using the following service:

[http://ch.hackyeaster.com:2305](http://ch.hackyeaster.com:2305)

Note: The service is restarted every hour at x:00.


Solution
-------------
Going to this site, you’ll see a button that says "click me!". Clicking the button will make a `GET` request to `http://ch.hackyeaster.com:2305/encrypt?s=sample`, and the resulting page shows the text "eatuit".

Going to the same URL with `s=ip0232j{1t_x_v0z4b3bm__v4xvq}a` returns `tq2023{rx1b_z_d0f4f3_uz_b4ude}`.
Now that looks pretty close to the flag...

You can continue to take the output and pass that as the `s` parameter, and eventually, the flag pops out.
This is fairly easy to do with Postman and a collection runner. (See `Hacky Easter 2023.postman_collection.json`)


Flag
-------------
`he2023{fl1p_n_r0t4t3_in_p4irs}`