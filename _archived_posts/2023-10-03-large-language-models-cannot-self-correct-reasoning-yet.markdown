---
layout: post
title:  Large Language Models Cannot Self-Correct Reasoning yet
date:   2023-10-03 16:03:30 +0800
image:  2023-10-03-large-language-models-cannot-self-correct-reasoning-yet_squared.jpg
tags:   [Self-Correct, Self-Consistency, Chain of Thought, Agent, Multi-agent, GSM8K, CommonSenseQA, HotpotQA, CommonGen-Hard, AI Consistency, AI Reasoning, AI, arXiv, ~0.0k Citations]
---

[arXiv](https://arxiv.org/abs/2310.01798) V1: [LARGE LANGUAGE MODELS CANNOT SELF-CORRECT REASONING YET](https://arxiv.org/pdf/2310.01798.pdf)

---
[NASA ADS](https) - 
[Google Scholar](https) - 
[Semantic Scholar](https://www.semanticscholar.org/paper/Large-Language-Models-Cannot-Self-Correct-Reasoning-Huang-Chen/6d4bacb69923e1e94fb4de468b939ce6db32fb51)

{% highlight markdown %}
@article{Huang2023LargeLM,
  title={Large Language Models Cannot Self-Correct Reasoning Yet},
  author={Jie Huang and Xinyun Chen and Swaroop Mishra and Huaixiu Steven Zheng and Adams Wei Yu and Xinying Song and Denny Zhou},
  journal={ArXiv},
  year={2023},
  volume={abs/2310.01798},
  url={https://api.semanticscholar.org/CorpusID:263609132}
}
{% endhighlight %}

---
作者：爱可可-爱生活
链接：https://zhuanlan.zhihu.com/p/659576840
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

[CL] Large Language Models Cannot Self-Correct Reasoning 

YetJ Huang, X Chen, S Mishra, H S Zheng, A W Yu, X Song, D Zhou[Google DeepMind]

大型语言模型尚无法自我修正推理要点:

本文聚焦在内在自我校正，语言模型仅依靠其自身能力尝试校正初始回复，不利用外部反馈。
与部分乐观预期不同，结果显示语言模型在推理任务中难以自我校正，校正后表现常有退步。
文中分析了缺乏提升的原因，如初始回复已优化，校正中的补充提示可能使模型偏离最佳回复。
当自我校正有帮助时，是因为反馈提供了初始提示未包含的有用指导，提示设计非常重要。
对推理任务，自我校正与标准提示相比几乎没有切实好处，多Agent辩论也存在类似问题。
作者敦促社区务实看待自我校正，强调其在推理中的局限，并鼓励探索能真正改进推理的方法。

动机：对大型语言模型(LLM)的自我修正能力进行批判性审查，特别关注其在推理方面的表现，
并提出未来研究和实践应用的建议。

方法：通过研究内在自我修正的概念，即LLM仅凭其内在能力尝试纠正其初始回答，而不依赖外部反馈，
来探究LLM的自我修正能力。研究结果显示，在推理方面，LLM在没有外部反馈的情况下很难自我修正其回答，
并且有时甚至会导致性能下降。
此外，论文还探讨了多Agent辩论作为一种改进推理能力的方法，并指出其效果并不比自一致性方法更好。

优势：对LLM的自我修正能力进行了深入研究，并揭示了其在推理方面的局限性。
论文还提出对LLM自我修正能力的细微差别进行思考，并鼓励未来研究探索能真正改正推理的方法，例如引入外部反馈。

一句话总结：批判性地研究了大型语言模型的自我修正能力，发现在推理方面，
模型很难在没有外部反馈的情况下进行自我修正，并提出对未来研究的启示和应用建议。 

>Large Language Models (LLMs) have emerged as a groundbreaking technology with their unparalleled text generation capabilities across various applications. Nevertheless, concerns persist regarding the accuracy and appropriateness of their generated content. A contemporary methodology, self-correction, has been proposed as a remedy to these issues. Building upon this premise, this paper critically examines the role and efficacy of self-correction within LLMs, shedding light on its true potential and limitations. Central to our investigation is the notion of intrinsic self-correction, whereby an LLM attempts to correct its initial responses based solely on its inherent capabilities, without the crutch of external feedback. In the context of reasoning, our research indicates that LLMs struggle to selfcorrect their responses without external feedback, and at times, their performance might even degrade post self-correction. Drawing from these insights, we offer suggestions for future research and practical applications in this field.

“Post-hoc prompting,” where the prompting is applied after the responses have been generated. “Pre-hoc prompting” is appplied before the responses.

The paper suggests that Self-correction works because the answer is already within the LLM's search space.