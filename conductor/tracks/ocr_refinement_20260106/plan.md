# Plan: 智能 OCR 识别、内容重组与多格式 Markdown 生成

## Phase 1: 提示词工程与上下文构建
- [x] Task: 编写 `context_builder.py`，将 JSON 转换为 Markdown 格式的 Prompt 素材。 [8749c14]
- [x] Task: 设计核心 System Prompt，包含重组、润色、公式和图片处理规则。 [cb53e20]
- [x] Task: 生成完整的 `final_prompt.txt`（Prompt + 素材）。 [87ea276]
- [ ] Task: Conductor - User Manual Verification '提示词工程与上下文构建' (Protocol in workflow.md)

## Phase 2: 执行润色与重组 (AI 处理)
- [x] Task: 将 `final_prompt.txt`的内容作为输入，由 AI 执行处理任务。 [258f8ff]
- [ ] Task: 将 AI 的输出保存为 `refined_draft.md`。
- [ ] Task: Conductor - User Manual Verification '执行润色与重组' (Protocol in workflow.md)

## Phase 3: 最终格式化与输出
- [x] Task: 编写 `post_processor.py`，修正 `refined_draft.md` 中的图片路径（确保相对路径正确）。 [99bb3c8]
- [x] Task: 生成最终交付物 `final_polished_output.md`。 [99bb3c8]
- [ ] Task: Conductor - User Manual Verification '最终格式化与输出' (Protocol in workflow.md)
