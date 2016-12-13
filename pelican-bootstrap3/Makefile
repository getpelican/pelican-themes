help:
	@echo 'Makefile for translation                                                  '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make extract                      Extract message strings              '
	@echo '   make update                       Extract strings and update po files  '
	@echo '   make compile                      Compile po files to mo files         ' 
	@echo '                                                                          '

extract:
	pybabel extract --mapping babel.cfg --output messages.pot ./

update: extract
	pybabel update --input-file messages.pot --output-dir translations/ --domain messages

compile:
	pybabel compile --directory translations/ --domain messages

.PHONY: help extract update compile
