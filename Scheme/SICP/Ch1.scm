; Exercise 1.1
; 10
; 12
; 8
; 3
; 10
; 
;
; 19
; False
; 4 <-- wrong, I somehow thought this was an or operation
; 16
; 6
; 16
; 
; Exercise 1.2
( /
	( + 5 4 ( - 2
			( - 3
				( + 6
					( / 1 3)
				)
			)
		)
	)
	( * 3 
		( - 6 2 )
		( - 2 7 )
	)
)

; Exercise 1.3
( define (square a) ( * a a ) )
( define (sum-of-squares a b) ( + (square a) (square b)))
( define (returnlargest a b ) ( if ( > a b ) a b ) )
( define (twolargestss a b c) ( sum-of-squares (returnlargest a b) (returnlargest a c)))
