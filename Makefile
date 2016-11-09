# Run the main function
run:
	@python main.py

# Run tests
test:
	@python -m unittest discover -b tests -p '*_test.py'

# Clean out the compiled files
clean:
	rm -rf bin/
	@find . -name '*.pyc' -delete
	@find . -name '__pycache__' -delete

# Building a python package
package:
	mkdir -p bin/
	zip -r bin/mental-gymnastics.zip **/*.py
