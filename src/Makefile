all: generate alternate verify clean

generate:
	pyinstaller --onefile -n generator.exe crc_generator.py

alternate:
	pyinstaller --onefile -n alter.exe crc_alternator.py

verify:
	pyinstaller --onefile -n verifier.exe crc_verifier.py

clean:
	del /Q alter.exe.spec generator.exe.spec verifier.exe.spec
	rmdir /Q /S __pycache__ build
