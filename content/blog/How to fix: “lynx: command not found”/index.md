---
title: "How to fix: 'lynx: command not found'"
date: "2021-06-01T23:46:37.121Z"
description: "This article describes an issue I faced while using apachectl for managing Apache server and the steps I did to fix it."
---

Apachectl is one of the most popular methods to administer Apache server i.e httpd. I mostly use it for hosting some web apps during testing locally since it's built in and requires minimal setup.

## The problem
However, I recently ran into the following error while trying apachectl command to check the server status.

```bash
[renju][~][$] apachectl status
bin/apachectl: line 95: lynx: command not found
```

### Now, what is lynx?
A quick google search explained that lynx is a utility text-based browser in unix that is used by httpd

## The quick Solution
Anyway, the quick solution is to install lynx in your machine.

I used [brew](https://brew.sh/) to install it using the below command:

`brew install lynx`

And that’s it. apachectl works as expected now.

## The harder way
If you don’t use HomeBrew(I feel bad for you) or if you would prefer mundane tasks, you can also download it from here and install it yourself:

[Lynx – Official Website](http://lynx.isc.org/release/)

## Probable root cause
I assume this could have been caused due to me messing around with the brew versions or packages last week. That's the only recent action I remember of that could have caused this. Lynx might have been a dependency for one of the packages and might have been removed due to brew package uninstallation and cleanup!