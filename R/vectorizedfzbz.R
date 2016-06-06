# vectorizedfzbz.R
# The traditional Fizz Buzz interview question, but vectorized and in R.
# John Pellman, 2014

fizzbuzz <- function(x){
  if ((x%%3==0) && (x%%5==0)){
    fzbz <- "fizzbuzz"
  } else if (x%%3==0){
    fzbz <- "fizz"
  } else if (x%%5==0){
    fzbz <- "buzz"
  } else {
    fzbz <- x
  }
  fzbz
}

fizzbuzzresults <- sapply(1:100, fizzbuzz)
cat(fizzbuzzresults, sep="\n")
