;;; ROT13 (LISP)
;; Paulo Elienay II

;; ROT13 ("rotate by 13 places", sometimes hyphenated ROT-13) is a simple letter substitution cipher
;; that replaces a letter with the 13th letter after it, in the alphabet. ROT13 is a special case of
;; the Caesar cipher which was developed in ancient Rome. (https://en.wikipedia.org/wiki/ROT13)

(setq *print-case* :upcase)

(defun get_message ()
  (format t "What's your message? ~%")
  (defvar message (read-line))
  (defvar message_list (coerce message 'list))
  ;; TODO ADD IFELSE FOR: (> 77) (< 78)
  (loop for letter in message_list
        do (cond
             ((< (char-code letter) 110) (format t "~a" (code-char (+ (char-code letter) 13))))
             ((> (char-code letter) 100) (format t "~a" (code-char (- (char-code letter) 13))))
  ))
(get_message)
