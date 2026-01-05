import docx

def extract_all_text(file_path):
    """
    从 .docx 文件中提取所有文本段落。
    """
    doc = docx.Document(file_path)
    # 提取所有段落的文本，过滤掉纯空白行
    paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
    return paragraphs

if __name__ == "__main__":
    # 简单测试
    import sys
    if len(sys.argv) > 1:
        res = extract_all_text(sys.argv[1])
        for i, p in enumerate(res[:5]):
            print(f"[{i}] {p}")
