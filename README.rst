#SUBSTRING Version 0.2

##Multi-Operational and Flexible Substring Package

##This is indeed a need for the developer community to experience such simple, easy-to-use and extremely user friendly Python package which does your usual job of cutting out a piece of substring from the parent string without writing certain lines of code. Nobody wants to spend their valuable time in writing such simple code when they can work on the bigger and other important contributions to the developers' community. This package has the following two methods associated with it:

###1) substringByChar()
It has four parameters namely, initialString, startChar, endChar, and stepSize(default=1). It would spit out the substring on the basis of the characters entered. For example, consider a string "abcdefghijklmnopqrstuvwxyz" and I can pull out the substring "defghijkl" by just specifying the start and end characters as "d" and "l" respectively. It has also the feature of step size where you can change and get your substrings accordingly.

###2) substringByInd()
It has four parameters namely, initialString, startInd, endInd, and stepSize(default=1). It would spit out the substring on the basis of the indices entered. For example, consider a string "abcdefghijklmnopqrstuvwxyz" and I can pull out the substring "defghijkl" by just specifying the start and end indices as 3 and 11 respectively because "d" and "l" represent the indices 3 and 11 respectively. It has also the feature of step size where you can change and get your substrings accordingly.

####This package is "Multi-Operational" because it not only gets you the substring of your choice with such ease but also allows you to play around with the step sizes that you want. For example, consider the same string "abcdefghijklmnopqrstuvwxyz", and you can pull out "aceg" by entering the startChar, endChar, stepSize as "a", "g" and 2 respectively.

####With such ease of use, this package efficiently handles all the exceptions caused and lets the user know about them which makes the user experience very rich.
