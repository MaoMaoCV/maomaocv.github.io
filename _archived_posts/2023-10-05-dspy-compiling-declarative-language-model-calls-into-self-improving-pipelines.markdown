---
layout: post
title:  DSPy - Compiling Declarative Language Model Calls Into Self-improving Pipelines
date:   2023-10-05 16:03:30 +0800
image:  2023-10-05-dspy-compiling-declarative-language-model-calls-into-self-improving-pipelines_squared.jpg
tags:   [Agent, AI, arXiv, ~0.0k Citations]
---

[arXiv](https://arxiv.org/abs/2310.03714) V1: [DSPY: COMPILING DECLARATIVE LANGUAGE MODEL CALLS INTO SELF-IMPROVING PIPELINES](https://arxiv.org/pdf/2310.03714.pdf)

---
[NASA ADS](https) - 
[Google Scholar](https) - 
[Semantic Scholar](https://www.semanticscholar.org/paper/DSPy%3A-Compiling-Declarative-Language-Model-Calls-Khattab-Singhvi/2069aaaa281eb13bcd9330fc4d43f24f6b436a53)

{% highlight markdown %}
@article{Khattab2023DSPyCD,
  title={DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines},
  author={O. Khattab and Arnav Singhvi and Paridhi Maheshwari and Zhiyuan Zhang and Keshav Santhanam and Sri Vardhamanan and Saiful Haq and Ashutosh Sharma and Thomas T. Joshi and Hanna Moazam and Heather Miller and Matei Zaharia and Christopher Potts},
  journal={ArXiv},
  year={2023},
  volume={abs/2310.03714},
  url={https://api.semanticscholar.org/CorpusID:263671701}
}
{% endhighlight %}

---
作者：爱可可-爱生活
链接：https://zhuanlan.zhihu.com/p/660005420
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

[CL] DSPy: Compiling Declarative Language Model Calls into Self-Improving PipelinesO Khattab, A Singhvi, P Maheshwari, Z Zhang, K Santhanam, S Vardhamanan…[Stanford University & UC Berkeley & Amazon Alexa AI]DSPy：将声明式语言模型调用编译成自我改进管道要点:提出DSPy，一个使用预训练语言模型(LM)和其他工具管道设计AI系统的新的编程模型DSPy贡献了三个主要抽象：签名，模块和长程提示器签名使用自然语言类型声明抽象模块的输入/输出行为模块取代了手工提示技术，可以组合成管道长程提示器是通过提示或微调来优化模块的优化器关于数学词问题和多跳问答的案例研究表明，DSPy程序优于手工编写的提示使用DSPy，像Llama2-13b-chat这样的小型语言模型可以与使用专家提示的大型专有语言模型竞争DSPy提供了一种系统的方法来探索复杂的语言模型管道，而不需要大量的提示工程动机：现有的语言模型管道通常使用经过试错发现的“提示模板”，这种方法不够系统化，容易出现问题。本文引入一种更系统化的方法来设计和优化语言模型管道。方法：引入一种名为DSPy的编程模型，将语言模型管道抽象为文本转换图，通过声明性模块调用语言模型。DSPy模块可以通过学习来应用提示、微调、增强和推理技术的组合。论文还设计了一个编译器，可以优化任何DSPy管道以最大化给定的指标。优势：DSPy程序能快速生成优化的语言模型管道，并在几分钟之内超越标准的少样本提示和专家创建的演示的管道。此外，DSPy程序编译到较小的语言模型上也可以与依赖专家编写的提示链的方法竞争。

一句话总结：引入了DSPy编程模型，将语言模型管道抽象为文本转换图，设计了一个编译器，可以优化任意DSPy程序，使其在几分钟内生成优化的语言模型管道。 

The ML community is rapidly exploring techniques for prompting language models (LMs) and for stacking them into pipelines that solve complex tasks. Unfortunately, existing LM pipelines are typically implemented using hard-coded “prompt templates”, i.e. lengthy strings discovered via trial and error. Toward a more systematic approach for developing and optimizing LM pipelines, we introduce DSPy, a programming model that abstracts LM pipelines as text transformation graphs, i.e. imperative computation graphs where LMs are invoked through declarative modules. DSPy modules are parameterized, meaning they can learn (by creating and collecting demonstrations) how to apply compositions of prompting, finetuning, augmentation, and reasoning techniques. We design a compiler that will optimize any DSPy pipeline to maximize a given metric. We conduct two case studies, showing that succinct DSPy programs can express and optimize sophisticated LM pipelines that reason about math word problems, tackle multihop retrieval, answer complex questions, and control agent loops. Within minutes of compiling, a few lines of DSPy allow GPT-3.5 and llama2-13b-chat to selfbootstrap pipelines that outperform standard few-shot prompting (generally by over 25% and 65%, respectively) and pipelines with expert-created demonstrations (by up to 5–46% and 16–40%, respectively). On top of that, DSPy programs compiled to open and relatively small LMs like 770M-parameter T5 and llama2-13b-chat are competitive with approaches that rely on expert-written prompt chains for proprietary GPT-3.5. DSPy is available at https://github.com/stanfordnlp/dspy.