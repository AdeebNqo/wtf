# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <http://unlicense.org/>
from os import sep as pathsep
class song:
	full_path=""
	directory=""
	name=""
	def __init__(self,directory):
		#path is the full path with the name
		self.full_path = directory
		#directory is the directory without the song name
		sep_point = directory.rfind(pathsep)
		self.directory = directory[:sep_point];
		#name is the name of the song
		self.name = directory[sep_point+1:]
	#simple accessor methods
	def get_full_path(self):
		return self.full_path
	def get_path(self):
		return self.directory;
	def get_name(self):
		return self.name
	#methods usefull for logic of program
	def get_file(self):
		f = open(self.full_path)
		return f
from wtf_song import song
import os
class id3v1:
	#tag info (vers1)
	tag = ""
	title=""
	artist=""
	album=""
	year =""

	#informs you whether the song has valid tag or not
	valid = True
	#The actual file
	curr_song = None

	def __init__(self, song):
		self.curr_song = song.get_file()
		if (self.read_tag()!=0):
			self.valid = False

	def read_tag(self):
		#getting to the last 128 bytes of the file
		self.curr_song.seek(-128,os.SEEK_END)
		self.tag = self.curr_song.read(3)
		if (self.tag!='TAG'):
			return 1
		self.title = self.curr_song.read(30)
		self.artist = self.curr_song.read(30)
		self.album = self.curr_song.read(30)
		self.year = self.curr_song.read(4)
		return 0
	#Acessor methods for the tag values
	def get_artist(self):
		if (self.valid):
			return self.artist
		else:
			return "None"
	def get_title(self):
		if (self.valid):
			return self.title
		else:
			return "None"
	def get_album(self):
		if (self.valid):
			return self.album
		else:
			return "None"
	def get_year(self):
		if (self.valid):
			return self.year
		else:
			return "None"
