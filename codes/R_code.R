# Clean Data

stockdata <- read.csv('data20_new.csv',stringsAsFactors = F)
tmp <- as.Date(stockdata$Date,'%m/%d/%Y')
Year <- as.numeric(format(tmp,'%Y'))
Month <- as.numeric(format(tmp,'%m'))
testdata <- data.frame(stockdata$Name,stockdata[,4:14],stockdata$Date_Number,stockdata[,19:23],stockdata$label)
train <- na.omit(testdata)

# Transfer .csv data file to libsvm format

library(e1071)
library(SparseM)
train$stockdata.label <- as.numeric(train$stockdata.label)
x <- as.matrix(train[,1:18])
y <- as.matrix(train[,19])

xs <- as.matrix.csr(x)
write.matrix.csr(xs,y=y,file='out2.txt')
