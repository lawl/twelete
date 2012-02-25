twelete
=======

Wuts dat?
---------
twelete is a small python script designed to automatically delete your old tweets.

Why did i need?
---------------
Because I post a lot of shit on twitter, which i feel doesn't need to be archived forever.
Sure, "deleting" a tweet is just a flag in twitters database, but it's not so easy to access to the public anymore.

How did i setup?
----------------
You need tweepy, on debian you can easily install it via apt.
    apt-get install python-tweepy
I'm sure you figure out how to do it on other distributions.
You might also want to add a cronjob. I hope you know how to do this.
Also please copy the sample config to ~/.config/twelete/config or something.

Please note that you need to register for the twitter API (https://dev.twitter.com/apps/new) make sure your app has read & write permissions. Fill in the keys in the config. Fire the script and off you go.

Is it buggy?
------------
Probalby.
