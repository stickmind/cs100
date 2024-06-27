#lang sicp

;self-evaluating primitives
29
"this is a string"
#t
#f

;combination
(+ 2 3)
(+ (* 2 3) 4)

;abstract an expression
(define score 23)
(define total (+ 12 13))
(* 100 (/ score total))