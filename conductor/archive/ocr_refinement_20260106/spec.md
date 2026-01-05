# Spec: 智能 OCR 识别、内容重组与多格式 Markdown 生成

## 1. 概述 (Overview)
本轨道旨在利用 Gemini 模型的多模态能力，对已经提取出的杂乱图文素材（来自 `raw_content.json` 和 `extracted_assets/`）进行深度处理。目标是生成一份结构严谨、逻辑清晰、保留原作者情绪且飞书完美兼容的 Markdown 文档。

**核心理念**：不开发 API 调用程序，而是构建一套可复用的 **Prompt Engineering Workflow**，让任何大模型都能直接处理这些素材。

## 2. 功能要求 (Functional Requirements)
*   **上下文构建 (Context Building)**：
    *   编写脚本将 `raw_content.json` 转换为大模型易读的文本格式（标记图文位置）。
    *   图片内容通过文件路径引用，指示模型“此处应有图，请结合上下文理解”。
*   **Prompt 设计 (Prompt Engineering)**：
    *   **角色设定**：专业技术编辑 + 具有个性的原作者替身。
    *   **逻辑重组**：分析全文，打破时序，按主题（如编程、工具、感悟）聚类。
    *   **格式规范**：
        *   行内公式 -> Unicode 文本。
        *   块级公式 -> LaTeX 代码块 + 简易渲染。
        *   保留图片引用：`![图片描述](path/to/image)`，并附带生成的 Caption。
    *   **风格保留**：严禁删减“激烈言辞”和“情绪化表达”。

## 3. 验收标准 (Acceptance Criteria)
*   [ ] 产出一个 `final_prompt.txt`，包含完整的处理指令和结构化的输入素材。
*   [ ] 经模型处理后，生成的 Markdown 文档逻辑层级分明（H1-H3）。
*   [ ] 行内公式在飞书（或纯文本编辑器）中显示正常（无乱码）。
*   [ ] 文档完整保留了原作者的个人风格和所有观点。

## 4. 不在范围内 (Out of Scope)
*   编写代码调用 OpenAI/Gemini API。
*   开发图形化界面。
