This program is designed to convert JSON data into XML format. 

The program can be run with the makefile by using the command `make`.
Users may also run the command `make test` to run the test.py script, which tests the functionality of the dict2xml.py logic using examples found in the Examples folder.
Users should use the command `make clean` after each run to clean up unnecessary files. 

The program consists of the following files:
    -`main.py`
    -`dict2xml.py`

main.py controls the user interaction. It gets the JSON file from the user and loads it as a python dictionary. main.py also makes a call to the dict2xml.py file, performing the logic of converting the python dictionary into XML format. After getting the XML data from the dict2xml.py file, the main.py formats the XML text. Finally, it outputs the formatted XML to a file of the user's choosing.

dict2xml.py contains the main logic of the program. It was designed with the understanding that the various scenarios must be handled differently. For objects, it's enough to create a child from the dictionary. For arrays or lists, children must be created from the array. That is, objects and arrays must loop through different objects. The other scenarios that would result in a different outcome were for handling null values and for the outputting of values. 

The program uses the following native python libraries:
    -`os`
    -`json`
    -`xml.etree.ElementTree `
    -`xml.dom.minidom`

The os library is used to verify file paths and names. 
The json library is used to decode json data into a python dictionary.
The ElementTree library is used to create xml data from a python dictionary. 
The minidom library is used to "pretty-print" the xml data. 

In the project file, you will also find a folder named `Examples`. The Examples folder contains .JSON files which were used to manually and automatically test the program. This folder was left to give users files which they may use to test the programs functionality, if needed.

A test program was created to assist with automatic testing. The test file is called `test.py` and can be run using `make test`, as previously mentioned. It uses assert statements to test for expected XML results using the JSON files found in the Examples folder. 

References:
https://docs.python.org/3/library/os.html
https://docs.python.org/3/library/json.html
https://docs.python.org/3/library/xml.etree.elementtree.html
https://docs.python.org/3/library/xml.dom.minidom.html