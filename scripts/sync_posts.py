#!/usr/bin/env python3
"""
同步主仓库内容到 math-garden 博客
"""
import os
import shutil
from pathlib import Path
from datetime import datetime

# 路径配置
MATH_ROOT = Path(__file__).parent.parent.parent
BLOG_ROOT = MATH_ROOT / "math-garden"
POSTS_DIR = BLOG_ROOT / "_posts"

# 确保目录存在
POSTS_DIR.mkdir(exist_ok=True)

def add_frontmatter(content, title, subtitle, categories, tags, date=None):
    """添加 Jekyll front matter"""
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S +0900")
    
    fm = f"""---
layout: post
title: "{title}"
subtitle: "{subtitle}"
date: {date}
categories: [{categories}]
tags: [{tags}]
mathjax: true
---

"""
    return fm + content

def sync_problems():
    """同步问题卡片"""
    problems_dir = MATH_ROOT / "problems"
    if not problems_dir.exists():
        return
    
    count = 0
    for md_file in problems_dir.glob("problem-*.md"):
        content = md_file.read_text(encoding='utf-8')
        lines = content.split('\n')
        
        # 提取标题（第一个 # 标题）
        title = md_file.stem.replace("problem-", "").replace("-", " ").title()
        for line in lines:
            if line.startswith("# "):
                title = line[2:].strip()
                break
        
        # 添加 front matter
        new_content = add_frontmatter(
            content=content,
            title=title,
            subtitle="未解数学问题",
            categories="问题卡片",
            tags="未解问题，数学猜想"
        )
        
        # 写入博客
        output_file = POSTS_DIR / f"2026-04-13-{md_file.stem}.md"
        output_file.write_text(new_content, encoding='utf-8')
        count += 1
        print(f"✅ {md_file.name} -> {output_file.name}")
    
    print(f"\n📌 同步完成：{count} 个问题卡片")

if __name__ == "__main__":
    sync_problems()
