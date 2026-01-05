import os
import sys

def test_prompt_content():
    prompt_path = "system_prompt.md"
    if not os.path.exists(prompt_path):
        print("Error: system_prompt.md missing.")
        sys.exit(1)
        
    with open(prompt_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    required_keywords = ["人格魅力", "主题优先", "LaTeX", "Unicode", "飞书"]
    for kw in required_keywords:
        if kw not in content:
            print(f"Error: Missing key requirement in prompt: {kw}")
            sys.exit(1)
    
    print("Prompt content validated successfully.")

if __name__ == "__main__":
    test_prompt_content()
