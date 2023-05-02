Lost in (French) Space
=============

Difficulty: easy

Tags: osint

Description
-------------
My friend went to France and sent me coordinates of interesting things he found.

Three of them look legit, but one does not make sense to me.

- `48.998 2.008`
- `45.960 0.090`
- `43.579 1.524`
- `45.007 4.335`

🚩 Flag

- the first word of the thing you find
- six lowercase letters
- wrapped in flag format, e.g. `he2023{thingy}`


Hint
-------------
The three legitimate coordinates will lead you to the fourth.


Solution
-------------
All 4 of these coordinates point to somewhere in France.
- `48.998 2.008` is next to a complex that translates to "Star Park"
- `45.960 0.090` is field in Western France
- `43.579 1.524` is on a path next to a public area that translates to "The Center of the Planets" and there is a sign nearby with information about the sun
- `45.007 4.335` is the Planet Mars observatory

3 of these points are obviously space related (as the name of the challenge implies), so the second is definitely the odd one out.

Our greatest hint comes from the 4th point, which is the Planet Mars observatory.
The key insight here is that the 2nd point is actually legitimate, but it's just for a different map...

If we track down a map of Mars, we can find the coordinates `45.960 0.090` point to a crater called "Davies".

Plugging that into the right format, we get the flag.

Flag
-------------
`he2023{davies}`
