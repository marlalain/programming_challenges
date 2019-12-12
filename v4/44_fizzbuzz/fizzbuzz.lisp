;;; FizzBuzz in Common Lisp
;;; Made By Paulo Elienay II

(defun fizzbuzz (range)
  (loop for i from 0 to range do (cond
                                   ((= (mod i 15) 0) (print (concatenate 'string (write-to-string i) ": FizzBuzz")))
                                   ((= (mod i 3) 0) (print (concatenate 'string (write-to-string i) ": Fizz")))
                                   ((= (mod i 5) 0) (print (concatenate 'string (write-to-string i) ": Buzz"))))))

(fizzbuzz 100)
