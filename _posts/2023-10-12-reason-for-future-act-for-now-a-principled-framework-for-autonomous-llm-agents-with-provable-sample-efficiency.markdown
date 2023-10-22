---
layout: post
title:  Reason for Future, Act for Now - a Principled Framework for Autonomous Llm Agents with Provable Sample Efficiency
date:   2023-10-12 16:03:30 +0800
image:  2023-10-12-reason-for-future-act-for-now-a-principled-framework-for-autonomous-llm-agents-with-provable-sample-efficiency_squared.jpg
tags:   [Agent, LLM, AI, arXiv, ~0.0k Citations]
---

[arXiv](https://arxiv.org/abs/2309.17382) V1: [Reason for Future, Act for Now: A Principled Framework for Autonomous LLM Agents with Provable Sample Efficiency](https://arxiv.org/pdf/2309.17382.pdf)

---
[NASA ADS](https) - 
[Google Scholar](https) - 
[Semantic Scholar](https://www.semanticscholar.org/paper/Reason-for-Future%2C-Act-for-Now%3A-A-Principled-for-Liu-Hu/d3ca116177369bf6fbe27de64506a2f401aca996)

{% highlight markdown %}
@article{Liu2023ReasonFF,
  title={Reason for Future, Act for Now: A Principled Framework for Autonomous LLM Agents with Provable Sample Efficiency},
  author={Zhihan Liu and Hao Hu and Shenao Zhang and Hongyi Guo and Shuqi Ke and Boyi Liu and Zhaoran Wang},
  journal={ArXiv},
  year={2023},
  volume={abs/2309.17382},
  url={https://api.semanticscholar.org/CorpusID:263310943}
}
{% endhighlight %}

---
作者：爱可可-爱生活
链接：https://zhuanlan.zhihu.com/p/661905941
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

[LG] Reason for Future, Act for Now: A Principled Framework for Autonomous LLM Agents with Provable Sample EfficiencyZ Liu, H Hu, S Zhang, H Guo, S Ke, B Liu, Z Wang[Northwestern University & Tsinghua University]Reason for Future, Act for Now: 可证样本高效的自主LLM智能体原则性框架要点:提出一种称为“Reason for Future, Act for Now(RAFA)”的新框架，以桥接自治大语言模型(LLM)智能体的推理和行动之间的差距。在贝叶斯自适应马尔可夫决策过程(MDP)框架下形式化了LLM的推理和行动，其中潜变量是未知的环境，通过学习和规划子例程构建推理例程，以模拟actor-模型或actor-critic更新。学习子例程从记忆缓冲区形成对未知环境的后验，规划子例程在长期范围内生成最优策略/轨迹以最大化价值函数。智能体推理出长期的最优规划(“Reason for Future”)，但只执行第一步行动(“Act for Now”)，在状态转换时重新调用推理以重新规划。通过组合长期推理和短期行动迭代优化行动，实现√T遗憾，突出了先验知识和不确定性减少的互动。在经验上优于现有的框架，第一个具有可证明的样本效率保证的自治LLM智能体，LLM充当内部推理机制而不是actor/critic。动机：将大型语言模型(LLM)的推理能力转化为行动在现实世界中仍然具有挑战性。尤其是如何通过推理的内部机制在与外部环境的最少交互次数内可靠地完成给定任务仍不清楚。方法：提出一个有可证明遗憾保证的基于贝叶斯自适应马尔可夫决策过程(MDP)的原则性框架，用于协调推理和行动。具体而言，设计了一个用于推理的提示模板，从内存缓冲区中学习并规划未来的轨迹，然后采取规划轨迹的初始行动，并将收集的反馈存储在内存缓冲区中，然后重新调用推理过程从新状态重新规划未来的轨迹。优势：将LLM中的推理转化为贝叶斯自适应MDP中的学习和规划，通过在上下文中进行学习和规划子例程的方式来模拟MDP的actor-critic更新。理论分析证明了长期推理和短期行动的新组合实现了√T遗憾。通过将“经典”的MDP技术纳入其中，RAFA引入了首个具有可证明后悔保证的自主LLM智能体。

一句话总结：提出“Reason for Future, Act for Now(RAFA)”原则性框架，将LLM中的推理转化为贝叶斯自适应MDP中的学习和规划，实现了具有可证明遗憾保证的自主LLM智能体。 

>Large language models (LLMs) demonstrate impressive reasoning abilities, but translating reasoning into actions in the real world remains challenging. In particular, it remains unclear how to complete a given task provably within a minimum number of interactions with the external environment, e.g., through an internal mechanism of reasoning. To this end, we propose a principled framework with provable regret guarantees to orchestrate reasoning and acting, which we call "reason for future, act for now" (\texttt{RAFA}). Specifically, we design a prompt template for reasoning that learns from the memory buffer and plans a future trajectory over a long horizon ("reason for future"). At each step, the LLM agent takes the initial action of the planned trajectory ("act for now"), stores the collected feedback in the memory buffer, and reinvokes the reasoning routine to replan the future trajectory from the new state. The key idea is to cast reasoning in LLMs as learning and planning in Bayesian adaptive Markov decision processes (MDPs). Correspondingly, we prompt LLMs to form an updated posterior of the unknown environment from the memory buffer (learning) and generate an optimal trajectory for multiple future steps that maximizes a value function (planning). The learning and planning subroutines are performed in an "in-context" manner to emulate the actor-critic update for MDPs. Our theoretical analysis proves that the novel combination of long-term reasoning and short-term acting achieves a T‾‾√ regret. In particular, the regret bound highlights an intriguing interplay between the prior knowledge obtained through pretraining and the uncertainty reduction achieved by reasoning and acting. Our empirical validation shows that it outperforms various existing frameworks and achieves nearly perfect scores on a few benchmarks.