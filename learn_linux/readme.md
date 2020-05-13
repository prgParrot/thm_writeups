# Learn Linux

```bash
export IP=10.10.195.61
```

# Task 1. Intro

> This room is designed to teach you about Linux concepts, and tools. Because of this, this room expects no prior knowledge. The only expectation this room has is an eagerness to learn, and a willingness to google if you're stuck :). This room has a natural flow to it; however, if you are experienced in Linux, and just want a refresher on a specific topic, you can jump around as need be.

1. Read the above

```
No answer needed
```

# Task 2. Methodology

> After careful consideration, I've deemed the best way to go about this is to introduce various concepts in sections, with each section being more complex and requiring knowledge from the previous section. To better enable the transition between section, I've split each section into different users in the VM; when you finish a section you'll have to complete a challenge and then you'll be able to move onto the next section. 

1. Read the above

```
No answer needed
```

# Task 3 [Section 1: SSH] - Intro

> SSH is the act of remotely accessing a machine. SSH allows you to run commands interactively on the remote machine. This is done through the use of a program on the target machine, which allows the ssh client to interface with the target host.

> While the most common usage of a regular operating system is graphical(allowing you to see pictures, web browsers, file managers etc.) SSH works through a command line, meaning anything done on the target machine will be done through a command prompt similar to this.

![SSH Terminal](https://i.imgur.com/4QD2LNB.png)

> It may look intimidating at first, but you'll soon find out you can do much of the same functionality that you're able to do using graphical user interfaces!

> It is an invaluable tool, and how you will be accessing this machine to learn and to do the challenges. Depending on the operating system there are different ways of SSHing into a machine. This section will purely focus on the windows way(PuTTY), and after we learn more about linux commands, and how they work, we'll return back to this section and learn about the linux method.

1. Read the above

```
No answer needed
```

# Task 4 [Section 1: SSH] - Putty and ssh

> The download for putty can be found here, once you download it go through the install process. Once you've installed it, open it and you should see this screen

![First](https://i.imgur.com/LN2dIZG.png)

> The field that we are most interested in is "Host Name (or IP Address)". This is where the `$IP` that you got when you deployed the machine comes into play. That's because the format of SSH connections is &lt;user&gt;@&lt;host&gt;, and in this case host is equal to `10.10.222.165`. The user for this trial will be shiba1, so the completed "Host Name" field should like this.

![Second](https://i.imgur.com/ADpZspQ.jpg)

> (Note: the 10.10.10.10 is just an example, and you should replace that with $IP)

> From there click open, and you'll be greeted with 

![Third](https://i.imgur.com/nlzlrun.jpg)

> Click yes(this prompt is purely for verification purposes) and you'll be prompted for a password:

![Fourth](https://i.imgur.com/9mMhNv4.jpg)

> Enter "shiba1" and click enter, and you'll have logged in!

![Fifth](https://i.imgur.com/v0N82PO.jpg)

> Note: sometimes putty just may not work, in that case follow the ssh binary guide listed below!

> As an alternative to putty, you may have an ssh binary on your computer. That binary is accessed by going to your terminal(cmd/MacOS Terminal), and typing ssh.

![Sixth](https://i.imgur.com/SNNCMwf.jpg)

> The syntax on how to use this command is ssh &lt;user&gt;@&lt;host&gt;. So to ssh into the machine you'll need to type in ssh shiba1@10.10.222.165. It will prompt you for the user password, which in this case is also shiba1.

![Seventh](https://i.imgur.com/VO2Q6qc.png)

> That's it, you can now run commands interactively!!! :)))

1. SSH into the server

```
No answer needed
```

# Task 5 [Section 2: Running Commands] - Basic Command Execution

> Now that you've logged into the server, you're gonna wanna do things, and everything that can be done over SSH is done by running commands. To start out, we'll take a look at some of the basic commands, and the first command will be `echo`. Type `echo hello`, and press enter and you'll see your input echoed back at you.

![First](https://i.imgur.com/QGPXIFc.jpg)

> Much like the word it's named after, `echo` returns whatever is inputted into it. Congratulations, you've just ran your first Linux command!

1. Read the above

```
No answer needed
```

# Task 6 [Section 2: Running Commands] - Manual Pages and Flags

> Most of the commands you'll learn about have a lot of options that are not immediately known at first glance, these options are known as flags, and have the format &lt;command&gt; &lt;flag&gt; &lt;input&gt;. These flags can be learned about using the man command. The man command has the format man &lt;command&gt;. Therefore, to learn about flags for the echo command, we would type man echo. Typing that shows us a nicely formatted document:

![First](https://i.imgur.com/FixWl4Y.jpg)

> We get alot of information, but the flags are stored in the description section. For example the flag to remove the newline is -n. So to output `"Shiba"` without the newline you would type `echo -n Shiba`.

> Note: Some commands support the -h flag, meaning you can type `&lt;command&gt; -h` and get a list of flags and other useful information without using `man`.

1. How would you output hello without a newline

```
echo -n hello
```

# Task 7 [Section 3: Basic File Operations] - ls

> ls is a command that lists information about every file/directory in the directory. Just running the ls command outputs the name of every file in the directory

![First](https://i.imgur.com/AMpO7qK.jpg)

> As with other commands ls has many flags that can manipulate the output.  For example `ls -a` shows all files/directories including ones that start with `.`

![Second](https://i.imgur.com/Wp9M8pF.jpg)

1. What flag outputs all entries

```
-a
```

2. What flag outputs things in a "long list" format

```
-l
```

# Task 8 [Section 3: Basic File Operations] - cat

> cat short for concatenate, does exactly that, it outputs the contents of files to the console. For example, given a file called a.txt which contains the data "hello", `cat a.txt` would output hello.

![First](https://i.imgur.com/fFfe9tz.jpg)

> Note: cat supports the --help flag meaning that you can see useful flags without going to the man page!

![Second](https://i.imgur.com/vzjsPck.jpg)

1. What flag numbers all output lines

```
-n
```

# Task 9 [Section 3: Basic File Operations] - touch

> touch is a pretty simple command, it creates files. Given the command `touch b.txt`, b.txt would be created.

![First](https://i.imgur.com/4Yw3YKY.png)

1. Read the above

```
No answer needed
```


# Task 9 [Section 3: Basic File Operations] - Running A binary

> Occasionally there will be times when you want to run downloaded or user created programs. This is done by providing the full path to the binary, for example say you download a binary that outputs noot, providing the full path to that binary will execute it.

![First](https://i.imgur.com/PKDp1eF.jpg)

> Note: A binary is just executable code, think a windows exe file

> This seems like a good time to mention Relative Paths! Every time you intend on running the binary, you don't need to provide a full path, you can use Relative Paths.

> Relative Paths:

> The chart below will assume the current path is /tmp/aa

|Relative Path|      Meaning      |Absolute Path|Relative Path|Running a binary with a Relative Path|Running A binary with an Absolute Path|
|:-----------:|:-----------------:|:-----------:|:-----------:|:-----------------------------------:|:------------------------------------:|
|      .      |Current Directory  | /tmp/aa     |       .     |               ./hello               |             /tmp/aaa/hello           |
|      ..     | Directory before the current directory  | /tmp  | ..  | ../hello  | /tmp/hello |
| ~  | The user's home directory  | /home/&lt;current user&gt;  | ~  | ~/hello  | /home/&lt;user&gt;/hello |

> These shortcuts are incredibly efficient, and save time. These shortcuts for every command, so if I were to run ls . it would be the same as running ls &lt;current directory&gt;

![Second](https://i.imgur.com/hfre7mJ.jpg)

1. How would you run a binary called hello using the directory shortcut . ?

```
No answer needed
```

2. How would you run a binary called hello in your home directory using the shortcut ~ ?

```
~/hello
```

3. How would you run a binary called hello in the previous directory using the shortcut .. ?

```
../hello
```

# Task 11 Binary - Shiba1

> Now that you've learned basic file operations, you can solve the first challenge! This challenge is pretty simple, create a file called noot.txt.

> Once you're done run the binary and you'll be given the password for the user shiba2!

> Note: the name of the binary is shiba1, as shown in the title

1. What's the password for shiba2

```
pinguftw
```

# Task 12 su

> Now that we have our next user password, it seems like a good time to cover su. su is a command that allows you to change the user, without logging out and logging back in again. For example if you wanted to switch to shiba2 while you're the user shiba1, you would type `su shiba2` . You would then be prompted for a password and if you entered shiba2's password you would then become shiba2

![First](https://i.imgur.com/iZhPtJf.jpg)

> Note: Typing `su` on its own is equivalent to typing `su root`.

1. How do you specify which shell is used when you login?

```

```




