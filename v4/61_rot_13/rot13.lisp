; LISP

(print "Hello World!")
(format t "Hello, again ~%")

(print "What's your name?")
(defvar *name* (read))
(format t "Hi, ~a ~%" *name*)
