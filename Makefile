help:
	@echo "Makefile targets:"
	@echo "    clean         - remove generated files"
	@echo "    tags          - regenerate the TAGS file"
	@echo "    test          - run the tests"
	@echo "    covg          - run tests and get a coverage report"
	@echo " "

clean:
	find . -name "*~" | xargs rm -f
	rm -rf {,tests,textbase}/__pycache__

tags:
	ack -l --py "==TAGGABLE==" | xargs etags

test:
	py.test

covg:
	py.test --cov --cov-report term-missing
