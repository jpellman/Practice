#!/usr/bin/env julia

function CracklePop()
    for i in 1:100
        if i%3==0 && i%5==0
            println("CracklePop")
        elseif i%3==0
            println("Crackle")
        elseif i%5==0
            println("Pop")
        else
            println(i)
        end
    end
end

CracklePop()
