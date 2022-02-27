---
title: Setting Locale in Mac
date: "2021-04-30T22:40:32.169Z"
description: "Explains how to set up a locale in Mac OS."
---

If you have faced issues in your Applications, especially, terminal based programs, with regards to invalid Locale setting, please read on to know how to fix it.

## Steps
1. First of all, check your current locale setting using the command: `locale`

2. Then, check the locales available in your machine using the 'all' option: `locale -a`

3. Choose an appropriate locale for you from the available list.

4. The last step is to add the below two lines into your init scripts(.bash_profile, .bashrc, .zshrc e.t.c)
```bash
export LC_ALL=<your_preferred_locale>
export LANG=<your_preferred_locale>
```

>**Note:** 
>
> The init script is usually located in your home directory.
> 
> For bash/sh shell, the init script is located at `~/.bash_profile` or `~/.bashrc`
>
>For Zsh shell, it is located at `~/.zshrc`

In my case, I mentioned `en_US` as my locale since that is one of the most supported locales.

```bash
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
```
---
PS: If you still face issues with any of the applications, try using one of the more generic locales like `en_US`. Your specific locale might not be compatible with all the applications.