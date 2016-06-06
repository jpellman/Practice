#!/usr/bin/env julia

function mergesort(x)
    # Base case
    if length(x)==1
        return x
    else
        y=mergesort(x[1:div(length(x),2)])
        z=mergesort(x[div(length(x),2)+1:end])
        x=zeros(Int64,1,length(y)+length(z))
        y_idx=1
        z_idx=1
        for idx in 1:length(x)
           if y_idx > length(y)
               x[idx]=z[z_idx]
               z_idx+=1
           elseif z_idx > length(z)
               x[idx]=y[y_idx]
               y_idx+=1
           elseif y[y_idx] < z[z_idx]
               x[idx]=y[y_idx]
               y_idx+=1
           elseif z[z_idx] < y[y_idx]
               x[idx]=z[z_idx]
               z_idx+=1
           end
        end
        return x
    end
end

x=[3,7200,2,42,5,100,6]
println(mergesort(x))
