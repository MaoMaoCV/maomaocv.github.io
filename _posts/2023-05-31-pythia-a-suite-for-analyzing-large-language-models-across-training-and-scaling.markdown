---
layout: post
title:  Pythia - A Suite for Analyzing Large Language Models Across Training and Scaling
date:   2023-05-31 16:03:30 +0800
image:  2023-05-31s.jpg
tags:   [Transformer, LLM, AI, arXiv]
---

[arXiv](https://arxiv.org/abs/2304.01373) V1: [Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling](https://arxiv.org/pdf/2304.01373.pdf)

[Github](https: //github.com/EleutherAI/pythia)

---
[NASA ADS](https) - 
[Google Scholar](https) - 
[Semantic Scholar](https)

{% highlight markdown %}

{% endhighlight %}

---
Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling

Authors: Stella Biderman, Hailey Schoelkopf, Quentin Anthony, Herbie Bradley, Kyle O'Brien,
Eric Hallahan, Mohammad Aah Khan, Shivanshu Purohit, USVSN Sai Prashanth, Edward Raff,

Aviya Skowron, Lintang Sutawika, Oskar van der Wal

Abstract:

Objective: The paper seeks to understand how large language models (LLMs) develop and
evolve over the course of training and how these patterns change as models scale.

Contribution: The authors introduce "Pythia", a suite of 16 LLMs trained on public data in
the exact same order, with sizes ranging from 70M to 12B parameters.

Resources: They provide public access to 154 checkpoints for each of the 16 models, along
with tools to download and reconstruct their exact training dataloaders for further study.

Use Cases: The authors envision Pythia to facilitate research in various areas. They present
several case studies, including novel findings in memorization, the effects of term
frequency on few-shot performance, and efforts to reduce gender bias.

Findings: The controlled setup of Pythia can be used to glean novel insights into LLMs and
their training dynamics.

Availability: The trained models, analysis code, training code, and training data are available
on GitHub.

Introduction:

* Large transformer models have become the dominant approach for generative tasks in
natural language processing over the past few years.
* Beyond NLP, transformers have also been used in diverse areas such as text-to-image
SVallesicn