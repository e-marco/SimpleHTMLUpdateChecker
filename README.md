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

MIT License
-----------

Copyright (c) 2019 Marco Ernst

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.