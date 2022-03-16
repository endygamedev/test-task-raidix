NAME = helloraidix
CC = gcc
CC_FLAGS = -std=c99 -Werror -Wall -Wextra -Wpedantic


all:
	${CC} ${NAME}.c ${CC_FLAGS} -o ${NAME}


install:
	mkdir -p ${DESTDIR}
	install ${NAME} ${DESTDIR}
