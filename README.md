SimpleHTMLUpdateChecker
=======================

This simple Python script can be used to check for updates by parsing HTML 
sources using regular expressions.

Usage
-----

1. Modify the file *updateList.txt*. Some examples are included.  This file is 
   a semicolon delimited ASCII-file with four columns:

* Column 1: Name of the Webseite/Software (used for displaying updates only)
* Column 2: URL
* Column 3: Regular expression, e.g. `<h2>Current Version – (.*?)</h2>` 
            where `(.*?)` is the extracted value of the version information
* Column 4: Currently installed version

2. Install all prerequisites and run the main file *SimpleHTMLUpdateChecker.py* 
   in Python.

Prerequisites
-------------

Python packages:

* os
* shutil
* requests
* ssl
* urllib
* chardet
* re
* tkinter