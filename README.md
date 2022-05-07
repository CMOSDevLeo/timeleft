# timeleft
The Program gives you the time which it takes to view the remaining video considering a speed multiplier
(procrastination-project and build because I wanted to know how to execute a python file from anywhere without having to type .py)

# How to use tool:
timeleft [TUB-multiplier] [minutes]


# How to implement python program into bash to use it from anywhere
insert as first line without anything after it: 
#!/usr/bin/env python3

Shebang explained:
https://stackoverflow.com/questions/7670303/purpose-of-usr-bin-python3-shebang

Created symbolic link from where code lies, to bin directory, for not having to type .py after timeleft using:
sudo ln -s /path/to/your/script.py /usr/bin/script

made executable with sudo chmod +x name_of_file
