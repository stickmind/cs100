# 第一讲 介绍

```{toctree}
:hidden:

lab00/index
```

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=427281261&bvid=BV1s3411G7yM&cid=740918799&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="100%" height="480" sandbox="allow-top-navigation allow-same-origin allow-forms allow-scripts"></iframe>

## 计算机科学

本课程讲授**计算机科学**（computer science），但要注意的是，这门课程既不讲科学，也不讲计算机。这样的声明并非是为了标新立异。

首先这些内容并不算是真正的科学（science），而更偏重于工程。另外，当你问一位计算机科学家在研究什么时，他们通常也不会说自己在研究计算机（computer），就类似生物学家不会说自己是研究显微镜一样。

他们一般会告诉你，自己在研究的是计算机科学中的某个方向，例如系统、人工智能、图形学、网络、安全、编译原理、科学计算等等。每个方向又会细分为很多不同的子方向。建议大家通过搜索引擎搜索这些关键词，了解这些不同的方向具体研究的是哪些内容。

计算机科学主要研究以下三个方面：

- 什么样的问题可以通过计算来解决？
- 如何解决这样的问题？
- 哪些技术可以实现更高效的解法？

## 描述性/程序性知识

为了更好地佐证上述声明，我们再举一个几何和测量工具的例子。早期的几何学是有关长度、角度、面积和体积的经验性定律的收集，这些都是因为实际需要（比如勘探、建筑、天文和一些手工业）而发展的。古人将这些观察经验总结为“描述性的”、“是什么”的知识，进而发展出了几何学。

几何就包含了测量和测量工具——但是，几何学研究的对象并不仅仅是测量工具，而是一种**描述性知识**（declarative knowledge），关注“什么是真”这样的命题；与此相反，计算机科学的内容更偏向于**程序性知识**（imperative knowledge），关注“如何做”这样的任务，更侧重于实践。

关于程序性知识的概念，我们可以回忆数学课上“求两个整数最大公约数”的计算过程，具体步骤如下：

1. 将两个整数用较大数除以较小数，得到商和余数。
2. 如果余数为零，则较小数即为最大公约数。
3. 如果余数不为零，则将较小数作为新的被除数，余数作为新的除数，再次执行步骤 1。
4. 重复步骤 1 和步骤 3，直到余数为零。

为什么说这样的程序性、过程性、命令式的知识更有趣呢？因为当面对海量信息需要处理的时候，我们仍然可以采用这样的步骤计算出想要的结果。

当今社会文明的建设已经完全离不开代码，就个人来讲，编程可以很快地实现你的很多想法。正如 Hany Farid 所说：“One of the powers of code is that it is arguably one of the most powerful techniques for taking an idea in your head and translating it into something that you can actually do.”

## 编程语言

那么当我们想让计算机完成这样的“程序性任务”时，我们就需要使用编程语言将问题进行实例化。本课程将使用 Python 编程语言。

虽然不需要精通 Python 的方方面面，但需要你完全理解其基础内容。其次，如何将多项技术整合到一个较大的项目中也是本课程需要你掌握的。最后，本课程还会研究计算机是如何与编程语言进行交互的，在课程最后，你将有机会实现一个编程语言解释器项目。

课程的目标不是将大部分精力花费在编程语言的学习上，而是学习编程相关的概念。学会一门特定的编程语言，仅仅是本课程的附带产物。一旦你掌握了编程的概念，学习一门新的编程语言将会变得非常容易。

除了 Python，课程还会介绍另外两门编程语言：Scheme 和 SQL。从事软件开发需要你有能力快速掌握多门不同的编程语言，这是由于实际的软件大多是由多个编程语言共同开发完成的。

总的来说，本课程需要你投入大量的时间和精力。即便遇到较为困难的知识点，你也不必沮丧。通过不断地练习，你一定可以掌握这些内容。

## 管理复杂性

编程的概念是本课程着重需要介绍的，但更重要的是讲解如何管理**复杂性**（complexity），这是所有计算机科学家都会面临的共同问题。

Hany Farid 强调：“You are going to be writing code, which is a part but not all of what this course is about. This course is about how to think computationally, how to think about approaching a problem in a systematic, quantitative, and logical way, and solving the problem.”

本课程教授的重点是**编程**（programming），而不是某个特定的**编程语言**（programming language）。在计算机科学中，编程一词更多指的是思想，而不是动作。当课程中讨论编程概念时，并不等同于简单的编码。编程是通过一系列技术手段来控制程序的复杂性，例如函数式编程、数据抽象、面向对象编程等。

管理复杂性通常有以下三种方式：

- 过程（procedure）和数据（data）抽象思维
- 常规接口（conventional interface）和编程范式（programming paradigm）
- 元编程抽象（meta-linguistic abstraction）

## 关于学习

学习本就是一个煎熬的过程。网络上流传的各种答案就如同“毒品”一般，参考那些解读只会给你带来短暂的成就感。你感觉自己学会了，但其实你不仅没有学会，还浪费了课程配套的这些作业和项目。

什么是学习？Hany Farid 特别强调：“There is this notion that learning happens when you solve a problem. That is completely wrong. **Learning happens when you don't solve the problem**. The process of failure, the process of struggling, and the process of taking hours to solve something are where the learning is happening.”

这就好比历史上有很多人尝试过发明永动机，虽然无一例外全都失败了，但正是这些失败启发了人们习得了能量守恒定律。

编程有的时候是一件比较枯燥的事情，可能输错一个标点，就会浪费你半天的时间。对于一些较为困难的问题，特别是递归思维的培养，不要尝试一鼓作气“死磕”。可以把这些问题放在脑海里，吃饭的时候想，睡觉的时候想……很可能当你第二天起床的时候，突然就有了思路。这才是学习真正令人激动的时刻！

总之记住，不要气馁，这就是编程本身的样子！“Don't be frustrated by things not working. That's the way it's supposed to be. That's what the process of learning is.”



