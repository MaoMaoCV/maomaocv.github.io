---
layout: post
title:  AgentTuning - Enabling Generalized Agent Abilities for LLMs
date:   2023-10-19 16:03:30 +0800
image:  2023-10-19-agenttuning-enabling-generalized-agent-abilities-for-llmss.jpg
tags:   [Agent, LLM, AI, arXiv, ~0.0k Citations]
---

[arXiv](https://arxiv.org/abs/2310.12823) V1: [AGENTTUNING: ENABLING GENERALIZED AGENT ABILITIES FOR LLMS](https://arxiv.org/pdf/2310.12823.pdf)

[Github](https://github.com/THUDM/AgentTuning)

---
[NASA ADS](https) - 
[Google Scholar](https) - 
[Semantic Scholar](https://www.semanticscholar.org/paper/AgentTuning%3A-Enabling-Generalized-Agent-Abilities-Zeng-Liu/dbac9aa9a8acf46dbee969f2ca0815269f8f746d)

{% highlight markdown %}
@inproceedings{Zeng2023AgentTuningEG,
  title={AgentTuning: Enabling Generalized Agent Abilities for LLMs},
  author={Aohan Zeng and Mingdao Liu and Rui Lu and Bowen Wang and Xiao Liu and Yuxiao Dong and Jie Tang},
  year={2023},
  url={https://api.semanticscholar.org/CorpusID:264306101}
}
{% endhighlight %}

---
作者：爱可可-爱生活
链接：https://zhuanlan.zhihu.com/p/662533355
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

[CL] AgentTuning: Enabling Generalized Agent Abilities for LLMs

A Zeng, M Liu, R Lu, B Wang, X Liu, Y Dong, J Tang[Stanford University]

AgentTuning：不损害通用能力的同时改进LLM智能体能力

要点:提出AgentTuning，一种在保持通用语言模型性能的同时改进LLM的智能体能力的方法。

AgentTuning具有两个组成部分：

1) AgentInstruct，一个涵盖了6个任务的1866个高质量智能体交互轨迹的数据集 

2) 一种混合了AgentInstruct和通用数据的指令微调策略。将AgentTuning应用于Llama 2系列创建了AgentLM模型。AgentLM在保留任务和未见任务上明显优于Llama 2。分析表明，混合通用数据对于智能体任务的泛化至关重要，仅在智能体数据上微调的模型泛化性下降。错误分析显示，AgentTuning减少了Llama 2在智能体任务上的基本错误，如格式错误和重复。70B AgentLM在未见智能体任务上匹配GPT-3.5-turbo，而不会损害其在MMLU、GSM8K等通用LLM任务上的表现。动机：研究表明，现有的开放型大语言模型(LLM)在作为智能体处理复杂任务时明显落后于商业模型(如ChatGPT和GPT-4)，因此需要提升LLM的智能体能力。方法：本文提出一种名为AgentTuning的简单通用方法，通过构建AgentInstruct数据集和混合指令微调策略来增强LLM的智能体能力。优势：AgentTuning不仅能提升LLM的智能体能力，还能保持其通用能力，使其在未见的智能体任务上表现出广义的智能体能力。

一句话总结：提出AgentTuning方法，通过构建AgentInstruct数据集和混合指令微调策略，实现了提升LLM智能体能力而不损害其通用能力。 

>AgentTuning represents the very first attempt to instruction-tune LLMs using interaction trajectories across multiple agent tasks. Evaluation results indicate that AgentTuning enables the agent capabilities of LLMs with robust generalization on unseen agent tasks while remaining good on general language abilities. We have open-sourced the AgentInstruct dataset and AgentLM.

>Widely used language models (LMs) are typically built by scaling up a two-stage training pipeline: a pretraining stage that uses a very large, diverse dataset of text and a fine-tuning (sometimes, ‘alignment’) stage that uses targeted examples or other specifications of desired behaviors. While it has been hypothesized that knowledge and skills come from pre-training, and fine-tuning mostly filters this knowledge and skillset, this intuition has not been extensively tested. To aid in doing so, we introduce a novel technique for decoupling the knowledge and skills gained in these two stages, enabling a direct answer to the question, What would happen if we combined the knowledge learned by a large model during pre-training with the knowledge learned by a small model during fine-tuning (or vice versa)? Using an RL-based framework derived from recent developments in learning from human preferences, we introduce emulated fine-tuning (EFT), a principled and practical method for sampling from a distribution that approximates (or ‘emulates’) the result of pre-training and fine-tuning at different scales. Our experiments with EFT show that scaling up fine-tuning tends to improve helpfulness, while scaling up pre-training tends to improve factuality. Beyond decoupling scale, we show that EFT enables test-time adjustment of competing behavioral traits like helpfulness and harmlessness without additional training. Finally, a special case of emulated finetuning, which we call LM up-scaling, avoids resource-intensive fine-tuning of large pre-trained models by ensembling them with small fine-tuned models, essentially emulating the result of fine-tuning the large pre-trained model. Up-scaling consistently improves helpfulness and factuality of instruction-following models in the Llama, Llama-2, and Falcon families, without additional hyperparameters or training.