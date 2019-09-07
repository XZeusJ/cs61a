; Q1
(define (sum-every-other lst)
  (cond ((null? lst) 0)
    (else (+ (car lst)
            (sum-every-other (cdr lst))))))

; Q2-2a
(define (append a b)
  (if (null? a)
    b
    (cons (car a) (append (cdr a) b))))


; 2b
(define (reverse lst)
  (if (null? lst)
      nil
    (append (reverse (cdr lst)) (list (car lst)))))

; 2c
(define (reverse lst)
)