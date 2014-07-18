# Python based Data Collection Client for the API Usability Analyzer Server

This repository hosts a sample implementation of a client than tracks changes made to file in a specific directory and uploads the changes to an [API Usability Analyzer Server](https://github.com/bkahlert/api-usability-analyzer-server-java-ee).

The client also generates a unique ID for the observed subject and forwards it to the server so actions on observed web pages can be linked to the locally tracked file changes.

## Getting Started
1. Fork this repository
2. Configure the client
2.1. (optional) Put a copy of robocopy.exe to the client's root directory **if** you need to collect data on a Windows machine older than Windows Vista.
2.2. Change the string "your.server" in apiua.py and bkahlert.py to your data collection server
3. Deploy the client
3.1. Install python on all computers you want to observe
3.2. Put a copy of the client on all computer you want to observe in the observed directory in a folder named "apiua" (you may place it wherever you want - in this case you need to change its location in bkahlert.py)
4. Call the client every time you want it to check for changes and upload them to your data collection server.

## Calling the client

The following line shows how to call the client:
```Shell
python /absolute/path/src/apiua/apiua.py {event} {build_dir} {working_dir} 
```

The client knows four events:
1. **init** should be called if some build system initializes the source file. This makes the client collect the possibly changed data and also makes sure the subject has an ID and links it to the browser's fingerprint.  
Example  
```Shell
python /absolute/path/src/apiua/apiua.py init /project/path/build /project/path/src
```
1. **build** should be called if the user attempts to build a target. This makes the client collect the possibly changed data.
Example  
```Shell
python /absolute/path/src/apiua/apiua.py build /project/path/build /project/path/src
```

The collected data are sent to the server configured as explained in the getting started section. The client is failure tolerant. It keeps all collected data in /absolute/path/src**/apiua/userdata** and attempts to send all data that can not be found on the data collection server yet.

## Testing

1. Install client
2. Call client with init  
Your default browser should open the registration page  
In your source directory you should find the file .APIUA containing your ID
3. Check if the data collections server's collected data contain data (diff and doclog) for the ID found in .APIUA

License
-------
[The GNU General Public License v3.0 (GPLv3)](LICENSE)  
Copyright (c) 2011-2014 [Björn Kahlert, Freie Universität Berlin](http://www.mi.fu-berlin.de/w/Main/BjoernKahlert)