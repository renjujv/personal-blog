---
title: "Changing the Jenkins port on MacOS"
date: "2022-04-22T23:46:37.121Z"
description: "This article describes an issue I faced while changing the port for home-brew installed Jenkins LTS on MacOS specifically on Apple M1 chip and how to fix it"
---

A quick Google search pointed me to the below answer on StackOverflow - https://stackoverflow.com/a/51945048/5132408

However, that didn't work for me. What mentioned there pertained to old Homebrew installation setup. As in my case, for Apple M1 chip based machines, the Homebrew installation folder have changed from `usr/local` to `/opt/homebrew`

If you have a regular Jenkins installation without Homebrew, check the last section - **Other installation methods**.
## Jenkins installed via Homebrew
![Changing Jenkins port for brew installation](./change_jenkins_port_brew-iterm.webp)

### 1. Change the port in Jenkins configuration
If you installed Jenkins using Homebrew(recommended) like I did, the `homebrew.mxcl.jenkins-lts.plist` file in jenkins installation directory contains all the cli arguments used while starting jenkins. Open the file to edit it:

`nano /opt/homebrew/Cellar/jenkins-lts/<your_jenkins_version>/homebrew.mxcl.jenkins-lts.plist`

Change the port number from 8080(default) to any free port, say 8081 and save the file.



> Note: I have created an alias for sublime text and use sublime almost always when I need to use a text editor.Therefore, you will see `sublime` instead of `nano` in the screenshot

### 2. Unload the existing Jenkins LaunchAgent
`launchctl unload -w ~/Library/LaunchAgents/homebrew.mxcl.jenkins-lts.plist`

We are doing this to update the MacOS LaunchAgent for Jenkins with new configuration.

If we skip this current step, Jenkins will still use existing configuration from the existing LaunchAgent and won't take the update we did in Step 1.

The update will happen while starting Jenkins using the command in next Step 3. 

### 3. Start Jenkins
While unloading Jenkins in the above step(step 2), the service would have stopped automatically. Now, we can start the service using below command and this will update port configuration to the LaunchAgent file as well.

`brew services start jenkins-lts`

That's it. Now try going to the `localhost:8081` port and you can see Jenkins loading up and then the login screen as shown below:

![Jenkins login page](./jenkins_login_page.webp)

---
## Other installation methods
If you installed Jenkins using other methods like the pkg installer, the below commands should work. Haven't tried it myself. You might need to check the documentation of installer you used.
```
sudo defaults write /Library/Preferences/org.jenkins-ci.plist httpPort 9999
sudo launchctl unload /Library/LaunchDaemons/org.jenkins-ci.plist
sudo launchctl load /Library/LaunchDaemons/org.jenkins-ci.plist
```