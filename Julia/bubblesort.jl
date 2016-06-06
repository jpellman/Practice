#!/usr/bin/env julia

function bubblesort(x)
    swapping=true
    while swapping
        swapping=false
        for i in 2:length(x)
            if x[i-1] > x[i]
               first=x[i-1]
               second=x[i]
               x[i]=first
               x[i-1]=second 
               swapping=true
            end
        end
    end
    x
end

x=[3,7200,2,42,5,100,6]
println(bubblesort(x))
