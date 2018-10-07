2. 跟猜数字游戏很像，但是更general一点：让你猜几种颜色的组合，有一个长为n的array，每个位置是一个颜色，比如red，blue等等，然后游戏规则是给定一个已知颜色组合的array，让你猜这些颜色是啥。然后有个API可以调用，叫getGuessResult(Collor[] guess), 返回格式如下:
{
  "Correct": 1,.1point3acres网
  "Partial Correct": 2
  "Incorrect": 3
}
意思是既猜对颜色并且猜对位置的有1个，猜对颜色但是位置不对的有两个，完全不在已知颜色组合中的有3个。而且有种特殊情况：比如input = ["Red", "Blue", "Yellow", "Red"], guess=["Red", "Red", "Red", "White"], result应该是. From 1point 3acres bbs
{
  "Correct": 1,
  "Partial Correct": 1
  "Incorrect": 2.本文原创自1point3acres论坛
}. 牛人云集,一亩三分地

面试官解释说第一个red是correct， 第二个red是partial，第三个red不应该是partial，因为第二个Red已经对应了input中的第四个red。
OK，我以为要写猜的策略，结果面试官说不用，你写一个如何根据input colors和guess colors生成result。 写完之后，他又说我给你一个guess color array，你写个算法生成下一次应该猜的color组合的集合，理论上有k^n种组合（k个颜色，数组长为n），但是因为已经知道了上次猜的结果，下次猜的颜色组合数肯定比这个少。我没想到这么问，苦想半天有思路的时候没时间写了。。

http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=445190&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3046%5D%5Bvalue%5D%3D1%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311