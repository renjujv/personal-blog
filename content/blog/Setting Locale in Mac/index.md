---
title: Setting Locale in Mac
date: "2021-04-30T22:40:32.169Z"
description: This is a custom description for SEO and Open Graph purposes, rather than the default generated excerpt. Simply add a description field to the frontmatter.
---

# Setting Locale in Mac

If you have faced issues in your Applications, especially, terminal based programs, with regards to invalid Locale setting, please read on to know how to fix it.

## Steps
1. First of all, check your current locale setting
`locale`

1. Then, check the available locales in the machine
`locale -a`

1. The last step is to add the below two lines into your init scripts.

```bash
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
```

For bash/sh shell, the init script is located at ~/.bash_profile or ~/.bashrc
For Zsh shell, it is located at ~/.zshrc