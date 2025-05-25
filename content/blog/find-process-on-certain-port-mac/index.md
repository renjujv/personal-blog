## Finding the process or application running on a given port

For anyone dealing regularly with running web apps or containers locally, they would have faced the issue of some unknown application or process occupying a certain port. 
This is actually a note to self for the next time I'm trying to find a solution for this. 

Mac and Linux provides some built in utilities that helps in such situations. One of them in LSOF.

To find the process or application that's using a certain port, use the below command
```
lsof -i -n -P | grep TCP | grep 3001
```
In the above command, we are checking for the process/app that's running on port `3001`

Above command gives us a list of processes with details - Process name, process ID, user and some additional info.
<img width="949" alt="image" src="https://github.com/user-attachments/assets/531a4d0b-bd3d-4f18-91da-6f957d2b6785" />
The information relevant to us here is the Process name and the process ID.

In most cases, you want to kill the process and free up the port. We can simply use the kill command with the process ID to do this.
```
kill 6029 
```

where 6029 is the process ID we found with previous command.
Kill is available in mac and linux. There might be other commands that does the same job in other flavours of linux.


Here's more details on the usage of `lsof` command
<img width="692" alt="image" src="https://github.com/user-attachments/assets/c2d34a11-f008-4959-a39e-8d4619aba9f9" />
