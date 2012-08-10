#Copyright David Locke, 2012

library(rpart)

a.data <- read.csv('train_1.csv')

a.model <- rpart(Score1~DblLtrCnt+SpaceCnt+Length+DblLtrRatio+SpaceRatio, a.data, method="class")
print(a.model)
