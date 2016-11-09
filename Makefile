# Variables
zipfile = "bin/mental-gymnastics.zip"
outfile = "bin/mental-gymnastics"

# Run the main function
run:
	@python main.py

# Run tests
test:
	@python -m unittest discover -b tests -p '*_test.py'

# Clean out the compiled files
clean:
	@rm -rf bin/
	@find . -name '*.pyc' -delete
	@find . -name '__pycache__' -delete

# Building a python package
package: clean
	@mkdir -p bin/
	@zip -r $(zipfile) *.py
	@zip -r $(zipfile) games/*.py

	@echo "#!/usr/bin/env python3\n" > $(outfile)
	@cat $(zipfile) >> $(outfile)
	@chmod +x $(outfile)

	@rm $(zipfile)
