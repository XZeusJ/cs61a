; 4.1
(define (factorial x)
  (if (< x 2)
    1
    (* x (factorial (- x 1))))
)

; 4.2
(define (fib n)
  (if (or (= n 0) (= n 1))
    n
    (+ (fib (- n 1)) (fib (- n 2)))
  )
)

; 5.1
(define (concat a b)
  (cond
    ((null? a) b)
    (else (cons (car a) (concat (cdr a) b)))
  )
)

; 5.2
(define (replicate x n)
  (if (= n 0)
    nil
    (cons x (replicate x (- n 1)))
  )
)

; 5.3
(define (uncompress s)
  (if (null? s)
    nil
    (concat (replicate (car (car s))
              (car (cdr (car s))))
      (uncompress (cdr s)))
  )
)

; 5.4
(define (map fn lst)
  (if (null? lst)
    nil
    (cons (fn (car lst)) (map fn (cdr lst)))
  )
)

; 5.5
(define (deep-map fn lst)
  (cond
    ((null? lst)
      nil)
    ((pair? (car lst))
      (cons (deep-map fn (car lst)) (deep-map fn (cdr lst))))
    (else
      (cons (fn (car lst)) (deep-map fn (cdr lst))))
  )
)

; 6.1
(define (make-tree label branches)
  (cons label branches)
)

(define (label tree)
  (car tree)
)

(define (branches tree)
  (cdr tree)
)

; 6.2
(define (tree-sum tree)
  (+ (label tree)
     (sum (map tree-sum (branches tree))))
)
(define (sum lst)
  (if (null? lst)
    0
    (+ (car lst) (sum (cdr lst)))
  )
)

; 6.3 **
(define (path-product-tree t)
  (define (path-product t product)
    (let ((prod (* product (label t))))
      (make-tree prod
        (map (lambda (t) (path-product t prod))
          (branches tree)))
    )
  )
  (path-product t 1)
)


