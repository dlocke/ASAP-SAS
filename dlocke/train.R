#Copyright David Locke, 2012

library(rpart)

for(x in c(1:10))
{
  print(x)
  train_file <- paste('train_', x, '.csv', sep="")
  a.data <- read.csv(train_file)

  a.model <- rpart(Score1~DblLtrCnt+SpaceCnt+Length+DblLtrRatio+SpaceRatio, a.data, method="class")
  print(a.model)

  pred_file <- paste('pred_', x, '.csv', sep="")
  b.data <- read.csv(pred_file)

  scores <- predict(a.model, b.data, type="class")
  out.data <- data.frame(id=b.data[,"Id"], score=as.integer(as.character(scores)))

  write.table(out.data, "submission.csv", append=TRUE, sep=",", row.names=FALSE, col.names=FALSE)
}
