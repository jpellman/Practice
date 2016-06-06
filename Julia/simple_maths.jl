#!/usr/bin/julia

add(x, y) = x+y
subtract(x, y) = x-y
multiply(x,y) = x*y
divide(x,y) = x/y

function greaterThanTwo(x)
    if x > 2
        return true
    else
        return false
    end
end
