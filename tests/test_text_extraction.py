import os
import sys

# 将当前目录加入搜索路径
sys.path.append(os.getcwd())

def test_extract_text():
    # 尝试导入我们即将编写的模块
    try:
        from extractor import extract_all_text
    except ImportError:
        print("Error: extractor.py not found or extract_all_text not defined.")
        sys.exit(1)
    
    file_path = "code之路.docx"
    text_content = extract_all_text(file_path)
    
    print(f"Extracted {len(text_content)} paragraphs.")
    if not isinstance(text_content, list):
        print("Error: Extracted content should be a list.")
        sys.exit(1)
    
    if len(text_content) == 0:
        print("Error: No text extracted.")
        sys.exit(1)
    
    # 简单检查第一行是否有内容
    if not text_content[0].strip():
        print("Warning: First paragraph is empty.")

if __name__ == "__main__":
    test_extract_text()
