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
;(define (reverse lst)
;  (if (null? lst)
;    nil
;    (append (reverse (cdr lst)) (list (car lst)))))

; 2c
(define (reverse lst)
  (define (reverse-helper lst acc)
    (if (null? lst)
      acc
      (reverse-helper (cdr lst) (cons (car lst) acc))))
  (reverse-helper lst '()))

; Q3
; 3a
;(define (add-to-all s lst)
;  (if (null? lst)
;    lst
;    (cons (cons s (car lst)) (add-to-all s (cdr lst)))))

;2b
(define (map f lst)
  (if (null? lst)
    lst
    (cons (f (car lst)) (map f (cdr lst)))))

;3c
(define (add-to-all s lst)
  (map (lambda (x) (cons s x)) lst))

; ***
; Q4
(define (sublists lst)
  (if (null? lst)
      '(())
    (let ((recur (sublists (cdr lst))))
      (append recur (add-to-all (car lst) recur)))))
;    (append (sublists (cdr lst))
;            (add-to-all (car lst) (sublists (cdr lst))))))

; Q5
(define (sixty-ones lst)
  (cond
    ((or (null? lst) (null? (cdr lst))) 0)
    ((and (= 6 (car lst)) (= 1 (car (cdr lst)))) (+ 1 (sixty-ones (cdr (cdr lst)))))
    (else (sixty-ones (cdr lst)))
  )
)

; Q6
(define (no-elevens n)
  (cond   ((= 0 n) '(()))
          ((= 1 n) '((6) (1)))
          (else (append (add-to-all 6 (no-elevens (- n 1)))
                  (add-to-all 1
                    (add-to-all 6 (no-elevens (- n 2)))))))
)

