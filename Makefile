default:
	@python comp.py
run:
	@python wtf.py
clean:
	@rm -f *pyc
install:
	@chmod a+x wtf.py
	@sudo mv wtf.py /usr/bin
	@sudo mv wtf_song.pyc /usr/bin
uninstall:
	@echo Uninstalling wtf.py
	@sudo rm /usr/bin/wtf.py
	@sudo rm /usr/bin/wtf_song.pyc
