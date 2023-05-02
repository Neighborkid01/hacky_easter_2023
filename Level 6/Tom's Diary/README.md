Tom's Diary
=============

Difficulty: medium

Tags: crypto

Description
-------------
Tom found a flag and wrote something about it in his diary.

Can you get the flag?


Hint
-------------
Neither brute force nor word lists are necessary.


Solution
-------------
Tom's diary seems to have a garbled mess of text, but the keen eyed among you might realize this blob to be a base64 encoded string.
If we decode it, we end up with a .zip file.

Unzipping the file will prompt us with a password, but what could it be?

There are two rows of forward slashes `// // //` at the beginning of the file, and two rows of backslashes `\\ \\ \\` at the end, but the slashes in the middle seem different.

A quick search can reveal something called Tom Tom Code that uses forward and backslashes to encode text.

If we use the Tom Tom Code to decode the slashes in the middle, we get the password `slashesforprofit`.

Entering the password will give us `flag.txt`, which is just what we're looking for.

Flag
-------------
`he2023{sl4sh3s_m4k3_m3_h4ppy}`