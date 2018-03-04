# MultiGame (quick-connect example)

### This is an example using pygame, to explain how to use quick-connect

### Getting started:

First, fo to the directory where you downloaded this project, and type into the console:

    pip install -r requirements.txt
    
 (This is pip3 on linux machines)
 

Once you've done that, run the server.py, then client.py, and enjoy!

### Running multiple clients on 1 machine

Due to the way quick-connect works, it might be tricky trying to run 2 clients at once, 
however there is an easy solution for this. First, start your server, and start a client.


Then, if you're on windows, type this into your console (cmd.exe) 

    ipconfig
    
And look for `IPv4 Address`, and save that. If you're on a linux machine, 
type this into the terminal:

     hostname -I
     
and save the Ip you get from that.


Then, open the settings.json file, and replace

    "ip_addr": "127.0.0.1",
    
with:

    "ip_addr: "the ip you got from the terminal",
    
Then, run the client.py program again (with the other client.py and server.py also running)
and BAM! 2 clients!


***Feel free to edit this program to whatever, this is mainly just to show off the 
[quick-connect](https://github.com/Zwork101/quick-net) module.***