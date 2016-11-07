# Run the main function
run:
	@python main.py

# Run tests
test:
	@python -m unittest discover -s . -p '*_test.py'

# Clean out the compiled files
clean:
	@find . -name '*.pyc' -delete
