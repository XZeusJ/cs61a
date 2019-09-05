## Scheme basic syntax
### Expressions
### primitives
Just like in Python, atomic, or primitive, expressions in Scheme take a single step to evaluate. These include numbers, booleans, symbols.
```
scm> 1234    ; integer
1234
scm> 123.4   ; real number
123.4
```
### Symbols
Out of these, the symbol type is the only one we didn't encounter in Python. A symbol acts a lot like a Python name, but not exactly. Specifically, a symbol in Scheme is also a type of value. On the other hand, in Python, names only serve as expressions; a Python expression can never evaluate to a name.
```
scm> quotient      ; A name bound to a built-in procedure
#[quotient]
scm> 'quotient     ; An expression that evaluates to a symbol
quotient
scm> 'hello-world!
hello-world!
```
### Booleans
In Scheme, all values except the special boolean value #f are interpreted as true values (unlike Python, where there are some false-y values like 0). Our particular version of the Scheme interpreter allows you to write True and False in place of #t and #f. This is not standard.
```
scm> #t
#t
scm> #f
#f
```
### Call epressions
Like Python, the operator in a Scheme call expression comes before all the operands. Unlike Python, the operator is included within the parentheses and the operands are separated by spaces rather than with commas. However, evaluation of a Scheme call expression follows the exact same rules as in Python:  
1. Evaluate the operator. It should evaluate to a procedure.  
2. Evaluate the operands, left to right.  
3. Apply the procedure to the evaluated operands.  
Here are some examples using built-in procedures:  
```
scm> (+ 1 2)
3
scm> (- 10 (/ 6 2))
7
scm> (modulo 35 4)
3
scm> (even? (quotient 45 2))
#t
```
### Special forms
Some examples of special forms that we'll study today are the if, cond, define, and lambda forms. Read their corresponding sections below to find out what their rules of evaluation are!
### Control Structures
#### if Expressions
The if special form allows us to evaluate one of two expressions based on a predicate. It takes in two required arguments and an optional third argument:  
```
(if <predicate> <if-true> [if-false])
```
The first operand is what's known as a predicate expression in Scheme, an expression whose value is interpreted as either #t or #f.  
The rules for evaluating an if special form expression are as follows:  
1. Evaluate <predicate>.  
2. If <predicate> evaluates to a truth-y value, evaluate and return the value if the expression <if-true>. Otherwise, evaluate and return the value of [if-false] if it is provided.  
```
scm> (if (> x 3)
         1
         2)
```
Although the code may look the same, what happens when each block of code is evaluated is actually very different. Specifically, the Scheme expression, given that it is an expression, evaluates to some value. However, the Python if statement simply directs the flow of the program.

Another difference between the two is that it's possible to add more lines of code into the suites of the Python if statement, while a Scheme if expression expects just a single expression for each of the true result and the false result.  

One final difference is that in Scheme, you cannot write elif cases. If you want to have multiple cases using the if expression, you would need multiple branched if expressions

#### cond Expressions
Using nested if expressions doesn't seem like a very practical way to take care of multiple cases. Instead, we can use the cond special form, a general conditional expression similar to a multi-clause if/elif/else conditional expression in Python. cond takes in an arbitrary number of arguments known as clauses. A clause is written as a list containing two expressions: (<p> <e>).
```
(cond
    (<p1> <e1>)
    (<p2> <e2>)
    ...
    (<pn> <en>)
    [(else <else-expression>)])
```

### Lists
#### Pairs
A pair is a built-in data type in Scheme that holds two values. To create a pair, use the cons procedure, which takes in two arguments:
```
scm> (cons 3 5)
(3 . 5)
```
Elements in a pair are displayed as separated by a dot. We can use the car and cdr procedures to retrieve the first and second elements in the pair, respectively.
```
scm> (car (cons 3 5))
3
scm> (cdr (cons 3 5))
5
```
It's possible to nest cons calls such that an element within a pair is another pair!
```
scm> (cons (cons 1 2) 3)
((1 . 2) . 3)
scm> (cons 1 (cons 2 3))
(1 2 . 3)
```
You may be wondering why the first dot disappeared in the value of the second expression (i.e., why isn't it displayed as (1 . (2 . 3))?). This is because when Scheme sees a dot followed by an open parenthesis, it will remove the dot, the open parenthesis, and the corresponding close parenthesis:
```
(a . ( ... )) -> (a ...)
```
#### Well-formed lists
```
scm> (define a (cons 1 (cons 2 (cons 3 nil))))  ; Assign the list to the name a
scm> a
(1 2 3)
scm> (car a)
1
scm> (cdr a)
(2 3)
scm> (car (cdr (cdr a)))
3
```
#### list Procedure
There are a few other ways to create lists. The list procedure takes in an arbitrary number of arguments and constructs a well-formed list with the values of these arguments:
```
scm> (list 1 2 3)
(1 2 3)
scm> (list 1 (list 2 3) 4)
(1 (2 3) 4)
scm> (list (cons 1 2) 3 4)
((1 . 2) 3 4)
```
#### Quote Form
We can also use the quote form to create a list, which will construct the exact list that is given. Unlike with the list procedure, the argument to ' is not evaluated.
```
scm> '(1 2 3)
(1 2 3)
scm> '(1 2 . 3)
(1 2 . 3)
scm> '(cons 1 2)           ; Argument to quote is not evaluated
(cons 1 2)
scm> '(1 (2 3 4))
(1 (2 3 4))
scm> '(1 . (2 3 4))        ; Removes dot/parentheses when possible
(1 2 3 4)
```
#### Built-In Procedures for Lists
There are a few other built-in procedures in Scheme that are used for lists. Try them out in the interpreter!
```
scm> (null? nil)                ; Checks if a list is empty
#t
scm> (append '(1 2 3) '(4 5 6)) ; Concatenates two lists
(1 2 3 4 5 6)
scm> (length '(1 2 3 4 5))      ; Returns the number of elements in a list
5
```
### Defining procedures
The special form define is used to define variables and functions in Scheme. There are two versions of the define special form. To define variables, we use the define form with the following syntax:
```
(define <name> <expression>)
```
The rules to evaluate this expression are  
1. Evaluate the <expression>.  
2. Bind its value to the <name> in the current frame.  
3. Return <name>.  
The second version of define is used to define procedures:  
```
(define (<name> <param1> <param2> ...) <body> )
```
To evaluate this expression:  
1. Create a lambda procedure with the given parameters and <body>.  
2. Bind the procedure to the <name> in the current frame.  
3. Return <name>.  
The following two expressions are equivalent:
```
scm> (define foo (lambda (x y) (+ x y)))
foo
scm> (define (foo x y) (+ x y))
foo
```
define is a special form because its operands are not evaluated at all! For example, <body> is not evaluated when a procedure is defined, but rather when it is called. <name> and the parameter names are all names that should not be evaluated when executing this define expression.

#### Lambdas
All Scheme procedures are lambda procedures. To create a lambda procedure, we can use the lambda special form:
```
(lambda (<param1> <param2> ...) <body>)
```
This expression will create and return a function with the given parameters and body, but it will not alter the current environment. This is very similar to a lambda expression in Python!
```
scm> (lambda (x y) (+ x y))        ; Returns a lambda function, but doesn't assign it to a name
(lambda (x y) (+ x y))
scm> ((lambda (x y) (+ x y)) 3 4)  ; Create and call a lambda function in one line
7
```
A procedure may take in any number of parameters. The <body> may contain multiple expressions. There is not an equivalent version of a Python return statement in Scheme. The function will simply return **the value of the last expression** in the body.
