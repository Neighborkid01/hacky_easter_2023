Ghost in a Shell 4
=============

Difficulty: medium

Tags: forensics

Description
-------------
```
  _, _,_  _,  _, ___   _ _, _    _,    _, _,_ __, _,  _,    , ,   ,
 / _ |_| / \ (_   |    | |\ |   /_\   (_  |_| |_  |   |     | \   /
 \ / | | \ / , )  |    | | \|   | |   , ) | | |   | , | ,   |  \ /
  ~  ~ ~  ~   ~   ~    ~ ~  ~   ~ ~    ~  ~ ~ ~~~ ~~~ ~~~   ~   ~
______________________________________________________________________
 ,--.     ,--.     ,--.     ,--.
| oo |   | oo |   | oo |   | oo |
| ~~ |   | ~~ |   | ~~ |   | ~~ |  o  o  o  o  o  o  o  o  o  o  o  o
|/\/\|   |/\/\|   |/\/\|   |/\/\|
______________________________________________________________________
```

Connect to the server, snoop around, and find the flag!

- `ssh ch.hackyeaster.com -p 2306 -l blinky`
- password is: `blinkblink`

Note: The service is restarted every hour at x:00.


Solution
-------------
Signing into the server will reveal that things are not working as expected.
Typing `ls` will show that there are 2 files and a directory, `about.txt`, `blinky` and `flag.txt`.
Trying to cat any fo these files will return
```
|\---/|
| o_o |  meow!
 \___/
```
and attempting to `cd` anywhere leaves you exactly where you were.

Aparently, all of our commands have been aliased!

Running this lil' for-loop will show us what the aliases are and unalias them: `for OUT in $(compgen -a); do type -a $OUT; unalias $OUT; done`

Now that we can move around, we can see the actual contents of our current directory:
```
about.txt
blinky/
flag.txt
home/
```

If we `cd` into `home/blinky/`, we find the file `blinkyflag.fzip`, but if we try to open it, we find it's password protected.

Looking closely at the output of the script we ran earlier, we can see the line: `fzip is aliased to '/usr/bin/zip -P "/bin/funzip"'`

There it is. The file was zipped with the password `/bin/funzip`.

When we unzip and use the password, we see we don't have permission to write the output to a file, so using the command `unzip -p blinkyflag.fzip` will print the output instead.


Flag
-------------
`he2023{al1asses-4-fUn-and-pr0fit}`