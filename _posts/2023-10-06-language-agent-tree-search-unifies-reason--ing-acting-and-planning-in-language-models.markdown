---
layout: post
title:  Language Agent Tree Search Unifies Reason- Ing Acting and Planning in Language Models
date:   2023-10-06 16:03:30 +0800
image:  2023-10-06-language-agent-tree-search-unifies-reason--ing-acting-and-planning-in-language-models_squared.jpg
tags:   [Agent, AI, arXiv, ~0.0k Citations]
---

[arXiv](https://arxiv.org/abs/2310.04406) V1: [LANGUAGE AGENT TREE SEARCH UNIFIES REASON- ING ACTING AND PLANNING IN LANGUAGE MODELS](https://arxiv.org/pdf/2310.04406.pdf)

---
[NASA ADS](https) - 
[Google Scholar](https) - 
[Semantic Scholar](https://www.semanticscholar.org/paper/Learning-Interactive-Real-World-Simulators-Yang-Du/c3d14e7a319ab764297a60112ce74af201762a73)

{% highlight markdown %}
@article{Zhou2023LanguageAT,
  title={Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models},
  author={Andy Zhou and Kai Yan and Michal Shlapentokh-Rothman and Haohan Wang and Yu-Xiong Wang},
  journal={ArXiv},
  year={2023},
  volume={abs/2310.04406},
  url={https://api.semanticscholar.org/CorpusID:263829963}
}
{% endhighlight %}

---
作者：爱可可-爱生活
链接：https://zhuanlan.zhihu.com/p/660406588
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

[CL] Language Agent Tree Search Unifies Reasoning Acting and Planning in Language ModelsA Zhou, K Yan, M Shlapentokh-Rothman, H Wang, Y Wang[University of Illinois at Urbana-Champaign]用语言Agent树搜索统一语言模型的推理行为和规划要点:提出语言Agent树搜索(LATS)框架，结合规划、行动和推理来增强大型语言模型(LLM)的问题解决能力。LATS将基于模型的强化学习中的蒙特卡罗树搜索改编为语言Agent，将预训练的LLM重塑为Agent、价值函数和优化器。LATS通过搜索算法有意识地从采样操作中构建最佳轨迹，超越了贪婪解码单个轨迹的反射式提示方法。LATS通过环境观察和自我反思来结合外部反馈，以增强模型的敏感性，并使智能体能从经验中学习。在编程、问答和网络导航等各领域的实验展示了LATS在自主推理和决策中的通用性。在HumanEval上，LATS与GPT-4结合，编程达到94.4%的准确率。在WebShop上，它与GPT-3.5结合，平均得分达到75.9，超过了基线。动机：传统的大型语言模型在决策任务中表现出色，但它们的行为过于简单，无法作为自主Agent进行广泛部署。本文旨在引入LATS(Language Agent Tree Search)框架，将语言模型的规划、行为和推理能力相结合，提升决策能力。方法：提出LATS框架，利用蒙特卡罗树搜索将语言模型作为Agent、值函数和优化器，通过对可能的推理和行为步骤进行搜索来统一规划、行为和推理策略。关键在于引入外部反馈的环境，提供更加深思熟虑和适应性的问题解决机制。优势：LATS框架在编程、HotPotQA和WebShop等多个领域的实验评估中展示了其在推理和行为方面的适用性。特别是在HumanEval中，使用GPT-4进行编程时，LATS实现了94.4%的准确率，在WebShop中使用GPT-3.5进行网页浏览时，平均得分为75.9，展示了该方法的有效性和广泛性。

一句话总结：提出LATS框架，将语言模型的规划、行为和推理能力相结合，通过蒙特卡罗树搜索和外部反馈的环境，提升了决策能力，具有广泛的适用性和提升性能的优势。

 While large language models (LLMs) have demonstrated impressive performance on a range of decision-making tasks, they rely on simple acting processes and fall short of broad deployment as autonomous agents. We introduce LATS (Language Agent Tree Search), a general framework that synergizes the capabilities of LLMs in planning, acting, and reasoning. Drawing inspiration from Monte Carlo tree search in model-based reinforcement learning, LATS employs LLMs as agents, value functions, and optimizers, repurposing their latent strengths for enhanced decision-making. What is crucial in this method is the use of an environment for external feedback, which offers a more deliberate and adaptive problem-solving mechanism that moves beyond the limitations of existing techniques. Our experimental evaluation across diverse domains, such as programming, HotPotQA, and WebShop, illustrates the applicability of LATS for both reasoning and acting. In particular, LATS achieves 94.4% for programming on HumanEval with GPT-4 and an average score of 75.9 for web browsing on WebShop with GPT-3.5, demonstrating the effectiveness and generality of our method.