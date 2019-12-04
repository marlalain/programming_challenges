# ROT 13 (Rotate 13 Places)

ROT13 (“rotate by 13 places”, sometimes hyphenated ROT-13) is a simple letter substitution cipher that replaces a letter with the 13th letter after it, in the alphabet. ROT13 is a special case of the Caesar cipher which was developed in ancient Rome.

---

![ROT 13 Example](https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/ROT13_table_with_example.svg/1280px-ROT13_table_with_example.svg.png)


## The Logic

How ROT 13 works is pretty simple, you get an alphabetical char and then 'adds'
13 digits to that number (A = N, P = C). So you have two parts for the code, the pre-N and post-N.

* **pre-N** (<110, <77)
  
  Every char in that zone you want to add 13 digits to it, so A => N.
  
* **post-N** (>110, >77)
  
  Every char in that zone you want to subtarct 13 digits to it, so N => A.

```common-lisp
(loop for letter in message_list
        do (if (< (char-code letter) 110)
               (format t "~a" (code-char (+ (char-code letter) 13)))
               (format t "~a" (code-char (- (char-code letter) 13)))))
```

## How to run
TODO
