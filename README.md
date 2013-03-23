wtf
===========

I 'ssh' to a server almost all the time. I also happen to use
cvlc to listen to music on the server. I have a couple of mp3
files I've stored on the server. I sometimes forget which song belongs
to who, as in I forget the artist,etc --- most of mp3 files are not labelled.


smallTagzz is a small python commandline application that uses
id3 tags. It reads tags and displays the artist name, album, etc of a
given mp3 file

Usage
------
This is a command line thing. Start by compiling it


> make


After compiling, install it


> make install


If you wake up and realize you don't need it


> make uninstall


Output
-------

After it has been installed. Say you happend to see an .mp3 file in some folder.

Here's its being run with a random mp3 file in my music directory

		Artist: Bruno Mars
		Title: When I Was Your Man
		Album: Unorthodox Jukebox
		Year: 2012

Here's the entered cmd: wtf.py xxx.mp3

License Notice
---------------
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>

