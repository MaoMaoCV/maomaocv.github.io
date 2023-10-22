---
layout: post
title:  Learning Interactive Real-World Simulators
date:   2023-10-09 16:03:30 +0800
image:  2023-10-09-learning-interactive-real-world-simulators_squared.jpg
tags:   [Agent, AI, arXiv, ~0.0k Citations]
---

[arXiv](https://arxiv.org/abs/2310.06114) V1: [Learning Interactive Real-World Simulators](https://arxiv.org/pdf/2310.06114.pdf)

---
[NASA ADS](https) - 
[Google Scholar](https) - 
[Semantic Scholar](https://www.semanticscholar.org/paper/Learning-Interactive-Real-World-Simulators-Yang-Du/c3d14e7a319ab764297a60112ce74af201762a73)

{% highlight markdown %}
@inproceedings{Chen2023FireActTL,
  title={FireAct: Toward Language Agent Fine-tuning},
  author={Baian Chen and Chang Shu and Ehsan Shareghi and Nigel Collier and Karthik Narasimhan and Shunyu Yao},
  year={2023},
  url={https://api.semanticscholar.org/CorpusID:263829338}
}
{% endhighlight %}

---
作者：爱可可-爱生活
链接：https://zhuanlan.zhihu.com/p/660824265
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

[LG] Learning Interactive Real-World SimulatorsM Yang, Y Du, K Ghasemipour, J Tompson, D Schuurmans, P Abbeel[UC Berkeley & MIT & Google DeepMind]交互式真实世界模拟器学习要点:通过结合不同的数据集和生成模型，探索建立一个交互式的真实世界通用模拟器(UniSim)。数据集覆盖不同轴心如对象、场景、动作、运动、语言，将观察和动作提取到一个共同格式中。在这个多模态数据上训练视频扩散模型，以模拟给定前一观察和动作下的下一观察。UniSim的推理类似POMDP的推出，支持长时间模拟进行决策。UniSim可以模拟真实的经验来训练具身AI模型，如视觉语言规划器和控制策略。这些纯粹在UniSim中训练的模型可以零样本泛化到真实世界，展示了模拟器的有用性。UniSim还可以模拟罕见事件如汽车撞车，以改进视频理解模型。总体来说，编排多模态数据学习像UniSim这样的条件生成模型，是建立强大模拟器的一个有希望的方向。动机：构建一个真实世界的交互式模拟器，通过生成建模来模拟人类、机器人和其他交互式智能体的行为，以实现可控的内容创作和培训。方法：通过精心协调丰富的数据集，每个数据集提供整体体验的不同方面，通过生成建模学习到真实世界交互的通用模拟器(UniSim)。优势：UniSim可以模拟高级指令和低级控制的视觉结果，使高级视觉语言规划器和低级强化学习策略能在学习纯粹的模拟器后进行领样本的真实世界迁移。

一句话总结：通过精心协调丰富的数据集，构建一个通用模拟器(UniSim)，能模拟真实世界的交互体验，实现高级视觉语言规划和强化学习策略的领样本真实世界迁移。 

Generative models trained on internet data have revolutionized how text, image, and video content can be created. Perhaps the next milestone for generative models is to simulate realistic experience in response to actions taken by humans, robots, and other interactive agents. Applications of a real-world simulator range from controllable content creation in games and movies, to training embodied agents purely in simulation that can be directly deployed in the real world. We explore the possibility of learning a universal simulator (UniSim) of real-world interaction through generative modeling. We first make the important observation that natural datasets available for learning a real-world simulator are often rich along different axes (e.g., abundant objects in image data, densely sampled actions in robotics data, and diverse movements in navigation data). With careful orchestration of diverse datasets, each providing a different aspect of the overall experience, UniSim can emulate how humans and agents interact with the world by simulating the visual outcome of both high-level instructions such as “open the drawer” and low-level controls such as “move by x, y” from otherwise static scenes and objects. There are numerous use cases for such a real-world simulator. As an example, we use UniSim to train both high-level vision-language planners and low-level reinforcement learning policies, each of which exhibit zero-shot real-world transfer after training purely in a learned real-world simulator. We also show that other types of intelligence such as video captioning models can benefit from training with simulated experience in UniSim, opening up even wider applications. Video demos can be found at universal-simulator.github.io.