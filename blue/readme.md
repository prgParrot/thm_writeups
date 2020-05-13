# Blue

```bash

export IP=10.10.191.144

```

## [Task 1] Recon


Scan and learn what exploit this machine is vulnerable to. Please note that this machine does not respond to ping (ICMP) and may take a few minutes to boot up.

Link to Ice, the sequel to Blue: Link

You can check out the third box in this series, Blaster, here: Link

---

The virtual machine used in this room (Blue) can be downloaded for offline usage from https://darkstar7471.com/resources.html


Enjoy the room! For future rooms and write-ups, follow @darkstar7471 on Twitter.

---


1. Scan the machine. (If you are unsure how to tackle this, I recommend checking out the room RP: Nmap)

```
No answer needed
```

2. How many ports are open with a port number under 1000?

```
3
```

3. What is this machine vulnerable to? (Answer in the form of: ms??-???, ex: ms08-067)

```
ms17-010
```


## [Task 2] Gain Access

Exploit the machine and gain a foothold.
---

1. Start Metasploit

```
No answer needed
```

2. Find the exploitation code we will run against the machine. What is the full path of the code? (Ex: exploit/........)

```
exploit/windows/smb/ms17_010_eternalblue
```

3. Show options and set the one required value. What is the name of this value? (All caps for submission)

```
RHOSTS
```

4. Run the exploit!

```
No answer needed
```

5. Confirm that the exploit has run correctly. You may have to press enter for the DOS shell to appear. Background this shell (CTRL + Z). If this failed, you may have to reboot the target VM. Try running it again before a reboot of the target.

```
No answer needed
```

## [Task 3] Escalate

Escalate privileges, learn how to upgrade shells in metasploit.
---

1. If you haven't already, background the previously gained shell (CTRL + Z). Research online how to convert a shell to meterpreter shell in metasploit. What is the name of the post module we will use? (Exact path, similar to the exploit we previously selected) 

```

```

2. Select this (use MODULE_PATH). Show options, what option are we required to change? (All caps for answer)

```

```

3. Set the required option, you may need to list all of the sessions to find your target here. 

```

```

4. Run! If this doesn't work, try completing the exploit from the previous task once more.

```

```

5. Once the meterpreter shell conversion completes, select that session for use.

```

```

6. Verify that we have escalated to NT AUTHORITY\SYSTEM. Run getsystem to confirm this. Feel free to open a dos shell via the command 'shell' and run 'whoami'. This should return that we are indeed system. Background this shell afterwards and select our meterpreter session for usage again. 

```

```

7. List all of the processes running via the 'ps' command. Just because we are system doesn't mean our process is. Find a process towards the bottom of this list that is running at NT AUTHORITY\SYSTEM and write down the process id (far left column).

```

```

8. Migrate to this process using the 'migrate PROCESS_ID' command where the process id is the one you just wrote down in the previous step. This may take several attempts, migrating processes is not very stable. If this fails, you may need to re-run the conversion process or reboot the machine and start once again. If this happens, try a different process next time. 

```

```

## [Task 4] Cracking

Dump the non-default user's password and crack it!
---

1. Within our elevated meterpreter shell, run the command 'hashdump'. This will dump all of the passwords on the machine as long as we have the correct privileges to do so. What is the name of the non-default user? 

```

```

2. Copy this password hash to a file and research how to crack it. What is the cracked password?

```

```

## [Task 5] Find flags!

Find the three flags planted on this machine.

Completed Blue? Check out Ice: Link

You can check out the third box in this series, Blaster, here: Link
---

1. Flag1? (Only submit the flag contents {CONTENTS}) 

```

```

2. Flag2? *Errata: Windows really doesn't like the location of this flag and can occasionally delete it. It may be necessary in some cases to terminate/restart the machine and rerun the exploit to find this flag. This relatively rare, however, it can happen. 

```

```

3. flag3?

```

```




