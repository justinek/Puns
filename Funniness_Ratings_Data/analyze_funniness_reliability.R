d1 = read.csv("FullSet_partial/Funniness/normalized.long.split1.csv")
d2 = read.csv("FullSet_partial/Funniness/normalized.long.split2.csv")

d1.summary = summarySE(d1, measurevar="rating", groupvars=c("tar_num", "isPun", "abSpl"))

d2.summary = summarySE(d2, measurevar="rating", groupvars=c("tar_num", "isPun", "abSpl"))

d1.summary.pun = d1.summary[d1.summary$isPun == 0,]
d1.summary.nonpun = d1.summary[d1.summary$isPun == 1,]

d2.summary.pun = d2.summary[d2.summary$isPun == 0,]
d2.summary.nonpun = d2.summary[d2.summary$isPun == 1,]

cor.test(d1.summary$rating, d2.summary$rating)
cor.test(d1.summary.pun$rating, d2.summary.pun$rating)
cor.test(d1.summary.nonpun$rating, d2.summary.nonpun$rating)

summary(lm(d1.summary$rating ~ d2.summary$rating))
summary(lm(d1.summary.pun$rating ~ d2.summary.pun$rating))
summary(lm(d1.summary.nonpun$rating ~ d2.summary.nonpun$rating))


0
compare_rating <-data.frame(row.names = seq(1,160,1))
compare_rating$tar_num = d1.summary$tar_num
compare_rating$isPun = factor(d1.summary$isPun)
compare_rating$d1 = d1.summary$rating
compare_rating$d2 = d2.summary$rating

ggplot(compare_rating, aes(x=d1, y=d2, color=isPun)) +
  geom_point() + geom_smooth(method=lm) +
  xlab("split1") +
  ylab("split2") +
  theme_bw()