;; Extra Scheme Questions ;;


; Q5
(define lst
  (list (list 1) 2 '(3 . 4) 5)
)

; Q6
(define (composed f g)
  (define (res num) (f (g num)))
  res
)

; Q7
(define (remove item lst)
  (cond ((null? lst) nil)
        ((not (= item (car lst))) (cons (car lst) (remove item (cdr lst))))
        (else (remove item (cdr lst))))
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

; Q8
(define (no-repeats s)
  (if (null? s)
      nil
      (cons (car s)
            (no-repeats (filter (lambda (x) (not (= (car s) x))) (cdr s)))))
)

; Q9
(define (substitute s old new)
  (cond ((null? s) nil)
        ((pair? (car s))
          (cons (substitute (car s) old new) (substitute (cdr s) old new)))
        ((eq? old (car s))
          (cons new (substitute (cdr s) old new)))
        (else
          (cons (car s) (substitute (cdr s) old new))))
)

; Q10
(define (sub-all s olds news)
  (if (null? olds)
      s
      (sub-all (substitute s (car olds) (car news)) (cdr olds) (cdr news)))
)