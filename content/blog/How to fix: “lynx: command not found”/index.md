---
title: "How to fix: 'lynx: command not found'"
date: "2021-06-01T23:46:37.121Z"
---

Apachectl is the recommended method to administer Apache server i.e httpd

## The problem
However, I recently ran into the following error while trying apachectl command to check the server status.

```bash
[renju][~][$] apachectl status
bin/apachectl: line 95: lynx: command not found
```

### Now, what is lynx?
A quick google search explained that lynx is a utility text-based browser in unix that is used by httpd

I assume the reason is that the dependency is not handled by httpd by themselves. They might have assumed that every distribution comes with it. Even proprietary OS like Mac OS!

## The quick Solution
Anyway, the quick solution is to install lynx in your machine.

I used [brew](https://brew.sh/) to install it using the below command:

`brew install lynx`

And that’s it. apachectl works as expected now.

## The harder way
If you would prefer mundane tasks or if you don’t use HomeBrew(I feel bad for you), you can also download it from here: [Lynx – Official](http://lynx.isc.org/release/)