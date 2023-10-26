---
layout: post
title:  MemGPT - Towards LLMs as Operating Systems
date:   2023-10-12 16:03:30 +0800
image:  2023-10-12-memgpt-towards-llms-as-operating-systems_squared.jpg
tags:   [Agent, AI, arXiv, ~0.0k Citations]
---

[arXiv](https://arxiv.org/abs/2310.08560) V1: [MEMGPT: TOWARDS LLMS AS OPERATING SYSTEMS](https://arxiv.org/pdf/2310.08560.pdf)

---
[NASA ADS](https) - 
[Google Scholar](https) - 
[Semantic Scholar](https://www.semanticscholar.org/paper/MemGPT%3A-Towards-LLMs-as-Operating-Systems-Packer-Fang/908dad62c0e43d80e3e3cb3c0402f7c71c70499c)

{% highlight markdown %}
@inproceedings{Packer2023MemGPTTL,
  title={MemGPT: Towards LLMs as Operating Systems},
  author={Charles Packer and Vivian Fang and Shishir G. Patil and Kevin Lin and Sarah Wooders and Joseph E. Gonzalez},
  year={2023},
  url={https://api.semanticscholar.org/CorpusID:263909014}
}
{% endhighlight %}

---
作者：爱可可-爱生活
链接：https://zhuanlan.zhihu.com/p/661370570
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

MemGPT: Towards LLMs as Operating SystemsC Packer, V Fang, S G. Patil, K Lin, S Wooders, J E. Gonzalez[UC Berkeley]MemGPT：受操作系统启发的大上下文LLM要点:提出MemGPT，一个启发于操作系统的系统，通过虚拟上下文管理为LLM提供大上下文的幻觉。MemGPT将LLM有限的上下文窗口视为一个受约束的内存资源，并使用了一个分层结构，包含主上下文(类似主内存)和外部上下文(类似磁盘存储)。它通过自导向的内存函数启用LLM修改主上下文，类似于操作系统在内存层间分页数据，控制流是事件驱动的。MemGPT在文档分析和会话智能体两个领域得到评估，这两个领域都受限于LLM的有限上下文窗口。在文档分析方面，MemGPT通过分页将文档页入主上下文来处理超过LLM上下文长度的文本，优于截断基线。在会话智能体方面，MemGPT利用内存增加一致性(通过回忆)和吸引力(通过工作内存)，优于有限上下文的基线。本文展示了虚拟上下文管理可以克服固定LLM上下文限制，并且操作系统技术如分层内存和中断对LLM同样有利。动机：现有的大型语言模型在处理长对话和文档分析等任务时受到有限上下文窗口的限制，因此需要一种能扩展上下文窗口的方法。方法：提出虚拟上下文管理技术，受传统操作系统中层级内存系统的启发，通过在快速和慢速内存之间移动数据来实现大内存资源的外观。同时，引入了MemGPT(Memory-GPT)系统，通过智能管理不同内存层次，有效地在有限上下文窗口内提供扩展上下文，并利用中断来管理自身与用户之间的控制流。优势：可以分析超出基础语言模型上下文窗口的大型文档，并能创建具有记忆、反思和动态演化能力的对话智能体。

一句话总结：提出MemGPT，一种内存管理技术，通过虚拟上下文管理扩展了大型语言模型的上下文窗口，实现了处理长对话和文档分析任务的能力。 

Large language models (LLMs) have revolutionized AI, but are constrained by limited context windows, hindering their utility in tasks like extended conversations and document analysis. To enable using context beyond limited context windows, we propose virtual context management, a technique drawing inspiration from hierarchical memory systems in traditional operating systems that provide the appearance of large memory resources through data movement between fast and slow memory. Using this technique, we introduce MemGPT (Memory-GPT), a system that intelligently manages different memory tiers in order to effectively provide extended context within the LLM’s limited context window, and utilizes interrupts to manage control flow between itself and the user. We evaluate our OS-inspired design in two domains where the limited context windows of modern LLMs severely handicaps their performance: document analysis, where MemGPT is able to analyze large documents that far exceed the underlying LLM’s context window, and multi-session chat, where MemGPT can create conversational agents that remember, reflect, and evolve dynamically through long-term interactions with their users. We release MemGPT code and data for our experiments at https://memgpt.ai.