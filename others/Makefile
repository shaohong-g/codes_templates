# Windows		:	mingw32-make
# linux/macOS	:	make
# https://opensource.com/article/18/8/what-how-makefile


.PHONY: all say_hello generate clean # define all the targets that are not files so that make will not get confused
# all: say_hello generate # run more than one target
# .DEFAULT_GOAL := clean # run specific target

var1 := Hello World
var2 := 1
phpadmin = 0

say_hello:
	@echo "${var1} ${var2}"
ifeq ($(phpadmin), 0)
	@echo "phpadmin = False -> $(phpadmin)"
else
	@echo "phpadmin = True -> $(phpadmin)"
endif
	@if [ "test" = "test" ]; then\
		echo "Hello world";\
	fi
	
generate:
	@echo "Creating empty text files..."
	touch file-{1..10}.txt

clean:
	@echo "Cleaning up..."
	rm *.txt