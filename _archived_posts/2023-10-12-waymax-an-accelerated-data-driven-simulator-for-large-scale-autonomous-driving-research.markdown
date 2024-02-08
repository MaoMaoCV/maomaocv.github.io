---
layout: post
title:  Waymax - an Accelerated, Data-driven Simulator for Large-scale Autonomous Driving Research
date:   2023-10-12 16:03:30 +0800
image:  2023-10-12-waymax-an-accelerated-data-driven-simulator-for-large-scale-autonomous-driving-research_squared.jpg
tags:   [Transformer, AI, arXiv, ~0.0k Citations]
---

[arXiv](https://arxiv.org/abs/2310.08710) V1: [Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research](https://arxiv.org/pdf/2310.08710.pdf)

---
[NASA ADS](https) - 
[Google Scholar](https) - 
[Semantic Scholar](https://www.semanticscholar.org/paper/Waymax%3A-An-Accelerated%2C-Data-Driven-Simulator-for-Gulino-Fu/5d09c6a8bae91da2640f1926df2a94e940556d27)

{% highlight markdown %}
@inproceedings{Gulino2023WaymaxAA,
  title={Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research},
  author={Cole Gulino and Justin Fu and Wenjie Luo and George Tucker and Eli Bronstein and Yiren Lu and Jean Harb and Xinlei Pan and Yan Wang and Xiangyu Chen and John D. Co-Reyes and Rishabh Agarwal and Rebecca Roelofs and Yao Lu and Nico Montali and Paul Mougin and Zoey Yang and Brandyn White and Aleksandra Faust and Rowan Thomas McAllister and Drago Anguelov and Benjamin Sapp},
  year={2023},
  url={https://api.semanticscholar.org/CorpusID:264128139}
}
{% endhighlight %}

---
作者：爱可可-爱生活
链接：https://zhuanlan.zhihu.com/p/661695225
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

[RO] Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving ResearchC Gulino, J Fu, W Luo, G Tucker, E Bronstein, Y Lu, J Harb…[Waymo Research & Google DeepMind]Waymax：用于大规模无人驾驶研究的数据驱动型加速模拟器要点:提出Waymax，一个用于大规模无人驾驶研究的加速数据驱动模拟器。Waymax使用公开发布的真实世界驾驶数据(如Waymo开放运动数据集)来初始化或回放各种多智能体模拟场景。Waymax完全运行在硬件加速器(如TPU/GPU)上，支持图中的模拟进行训练，适合现代大规模分布式机器学习工作流程。为支持在线训练和评估，Waymax包括几种学习和硬编码的行为模型，允许在模拟中进行逼真的交互。基准化了一套流行的模仿和强化学习算法，进行了不同设计决策的消融研究，强调路线作为规划智能体的指导以及强化学习过拟合模拟智能体的能力。动机：开发一种用于自动驾驶研究的加速、数据驱动的模拟器，以实现大规模的模拟和测试。方法：使用公开发布的真实驾驶数据初始化或回放多智能体仿真场景，在硬件加速器上完全运行，支持训练中的图内仿真。优势：通过使用真实数据初始化多样化的场景和模拟行为模型，提供了更真实的交互模拟，同时支持高速和高吞吐量的硬件加速。

一句话总结：Waymax是一种加速的、数据驱动的模拟器，通过用真实驾驶数据初始化多智能体仿真场景，提供了更真实的交互模拟，支持高速和高吞吐量的硬件加速。 

Simulation is an essential tool to develop and benchmark autonomous vehicle planning software in a safe and cost-effective manner. However, realistic simulation requires accurate modeling of nuanced and complex multi-agent interactive behaviors. To address these challenges, we introduce Waymax, a new data-driven simulator for autonomous driving in multi-agent scenes, designed for large-scale simulation and testing. Waymax uses publicly-released, real-world driving data (e.g., the Waymo Open Motion Dataset [15]) to initialize or play back a diverse set of multi-agent simulated scenarios. It runs entirely on hardware accelerators such as TPUs/GPUs and supports in-graph simulation for training, making it suitable for modern large-scale, distributed machine learning workflows. To support online training and evaluation, Waymax includes several learned and hard-coded behavior models that allow for realistic interaction within simulation. To supplement Waymax, we benchmark a suite of popular imitation and reinforcement learning algorithms with ablation studies on different design decisions, where we highlight the effectiveness of routes as guidance for planning agents and the ability of RL to overfit against simulated agents.