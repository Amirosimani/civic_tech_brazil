data <- read.csv(file.choose(), header = TRUE, sep = '|')
#library("ff")
#x<- read.csv.ffdf(file="/Users/Amiros/GitHub/civic_tech/1746data.csv", header=TRUE, VERBOSE=TRUE, sep = '|',first.rows=10000, next.rows=50000, colClasses=NA)
rapply(data,function(x)length(unique(x)))
unique(data$bairro)
