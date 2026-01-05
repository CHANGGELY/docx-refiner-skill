import json
import os
from context_builder import build_context

def assemble():
    system_prompt_path = "system_prompt.md"
    raw_content_path = "raw_content.json"
    output_path = "final_prompt.txt"
    
    if not os.path.exists(system_prompt_path) or not os.path.exists(raw_content_path):
        print("Error: Missing input files for assembly.")
        return
        
    # 读取系统指令
    with open(system_prompt_path, "r", encoding="utf-8") as f:
        system_instructions = f.read()
        
    # 读取并转换素材
    with open(raw_content_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        user_content = build_context(data)
        
    # 拼装
    final_content = f"{system_instructions}\n\n--- 原始素材开始 ---\n\n{user_content}\n\n--- 原始素材结束 ---"
    
    # 写入文件
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_content)
        
    print(f"[+] 终极提示词已生成: {output_path}")

if __name__ == "__main__":
    assemble()

