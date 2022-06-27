This is a repo for a GIMP plugin that I wrote while developing a board game.

It could possibly serve as an example of how to use some of the GIMP script calls. There were precious few examples online of people doing GIMP plugins, so maybe this'll save someone time. Though, as with most software, I assume this is unintelligable to anyone else and will soon be to me as well once I've committed it and forgotten how it works.

The way to use this is to:
1) Save monster-fill.py into the plugins directory (in Windows it's C:\Program Files\GIMP 2\lib\gimp\2.0\plug-ins)
2) Open the adjacent cards_template.xcf in GIMP
3) Filters -> Test -> monsterfill

It should fill in the numbers in the correct spots on the cards. The text for each card should be grouped by layers which I found fairly convenient when looking through them.
