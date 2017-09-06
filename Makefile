all:
	scons
	python3 arcin-utils/hidloader_append.py arcin.elf arcin-utils/hidloader_v2.exe arcin_flash_custom.exe