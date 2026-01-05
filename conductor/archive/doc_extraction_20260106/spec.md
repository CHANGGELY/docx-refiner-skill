# Spec: 文档自动化解析与内容初步提取

## 1. 目标
*   解析 `code之路.docx`。
*   提取所有文本，保持原有分段。
*   提取所有图片文件，并按在文档中出现的顺序编号存储。
*   生成一个 JSON 索引文件，描述文本和图片在原文档中的交替关系。

## 2. 成功标准
*   成功导出所有图片到 `extracted_assets/` 文件夹。
*   生成 `raw_content.json`，包含按顺序排列的文本块和图片路径。
*   确保没有文本或图片在提取过程中丢失。

## 3. 技术逻辑
*   使用 `python-docx` 遍历 `Document.paragraphs`。
*   利用 `paragraph._element.xpath` 探测图片关联 ID。
*   从 Word 压缩包结构的 `word/media/` 中提取原始二进制图片。
