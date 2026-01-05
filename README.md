# Docx Refiner - 智能文档润色工具

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-blue)](https://CHANGGELY.github.io/docx-refiner-skill/)

这是一个基于 AI 的文档润色工具，旨在将杂乱的 Word (.docx) 文档转换为结构清晰、优雅的 Markdown 格式。

## ✨ 核心特性

- **智能提取**：自动识别文档中的文本、标题和结构。
- **图片处理**：支持从 docx 中提取图片并保持位置关联。
- **公式保留**：完美处理数学公式，确保在转换过程中不丢失精度。
- **风格统一**：根据预设的风格指南进行润色，保持文档专业度。

## 🚀 快速开始

### 1. 下载 Skill 文件
你可以从 [GitHub Pages 落地页](https://CHANGGELY.github.io/docx-refiner-skill/) 下载 `docx-refiner.skill` 文件，并将其导入到你的 AI 助手（如 Claude, ChatGPT 等支持 Skill/Custom GPTs 的平台）。

### 2. 本地运行 (Python)
如果你想在本地运行工具链：

```bash
# 安装依赖
pip install -r requirements.txt

# 运行主程序
python main.py
```

## 📂 项目结构

- `docx-refiner.skill`: 核心 Skill 压缩包。
- `docx-refiner/`: Skill 的解压内容，包含提示词模板和脚本。
- `index.html`: 项目落地页。
- `main.py`: 本地运行的入口程序。
- `extractor.py`: 文档提取逻辑。
- `context_builder.py`: 上下文构建逻辑。

## 🎨 落地页预览
本项目包含一个精心设计的 [Landing Page](index.html)，采用 Apple 级审美设计，支持玻璃拟态效果。

---
&copy; 2026 Docx Refiner. Created by CHANGGELY.
