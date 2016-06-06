#!/usr/bin/julia

function sqr_ident(n)
    ident=sqr_zero(n) 
    for i in 1:n
        ident[i,i]=1
    end
    ident
end

function sqr_zero(n)
    [0 for r in 1:n, c in 1:n]
end

println(sqr_ident(8))
