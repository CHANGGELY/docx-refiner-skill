import json
import os
from extractor import extract_full_document

def main():
    # 从环境变量获取配置，默认值为硬编码值
    input_file = os.getenv("INPUT_FILE", "code之路.docx")
    output_dir = os.getenv("OUTPUT_DIR", "extracted_assets")
    index_file = os.getenv("INDEX_FILE", "raw_content.json")
    
    print(f"[*] 正在处理文档: {input_file}...")
    
    # 提取内容
    indexed_content = extract_full_document(input_file, output_dir)
    
    # 将索引写入 JSON
    with open(index_file, "w", encoding="utf-8") as f:
        json.dump(indexed_content, f, ensure_ascii=False, indent=2)
        
    print(f"[+] 处理完成！")
    print(f"[+] 提取了 {len(indexed_content)} 个元素。")
    print(f"[+] 索引文件已保存至: {index_file}")
    print(f"[+] 图片资源已保存至: {output_dir}/")

if __name__ == "__main__":
    main()
