---
layout: home
title: 首页
---

<div class="hero">
  <h1 class="hero-title">Graham 的数学花园</h1>
  <p class="hero-subtitle">系统整理数学问题、经典猜想与证明思路。</p>
  <p class="hero-description">这里记录数论、分析与未解问题，把复杂的数学主题整理成更清晰、可持续阅读的内容。</p>
</div>

<div class="topics-section">
  <div class="topic-card">
    <h3><a href="/math-garden/archive/?category=number-theory">数论</a></h3>
    <p>素数分布、黎曼猜想、哥德巴赫猜想、孪生素数猜想……探索整数的深层结构。</p>
  </div>
  
  <div class="topic-card">
    <h3><a href="/math-garden/archive/?category=analysis">分析</a></h3>
    <p>实分析、复分析、泛函分析，理解连续与极限的语言。</p>
  </div>
  
  <div class="topic-card">
    <h3><a href="/math-garden/archive/?category=unsolved">未解问题</a></h3>
    <p>千禧年难题、著名猜想、开放问题，站在数学的前沿。</p>
  </div>
</div>

<div class="posts-section">
  <h2 class="section-title">最新文章</h2>
  <ul class="post-list">
    {% for post in site.posts limit: 10 %}
      <li class="post-item">
        <div class="post-meta">{{ post.date | date: "%Y-%m-%d" }}</div>
        <h3 class="post-title">
          <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
        </h3>
        {% if post.subtitle %}
          <p class="post-subtitle">{{ post.subtitle }}</p>
        {% endif %}
      </li>
    {% endfor %}
  </ul>
</div>
