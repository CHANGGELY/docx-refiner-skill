import os
import sys

# 将当前目录加入搜索路径
sys.path.append(os.getcwd())

def test_document_indexing():
    try:
        from extractor import extract_full_document
    except ImportError:
        print("Error: extract_full_document not defined in extractor.py")
        sys.exit(1)
    
    file_path = "code之路.docx"
    output_dir = "test_indexed_assets"
    
    indexed_content = extract_full_document(file_path, output_dir)
    
    print(f"Total elements indexed: {len(indexed_content)}")
    
    has_text = any(item['type'] == 'text' for item in indexed_content)
    has_image = any(item['type'] == 'image' for item in indexed_content)
    
    if not has_text:
        print("Error: No text indexed.")
        sys.exit(1)
        
    # 如果文档确实有图片，检查图片路径是否有效
    for item in indexed_content:
        if item['type'] == 'image':
            if not os.path.exists(item['content']):
                print(f"Error: Referenced image {item['content']} does not exist.")
                sys.exit(1)

if __name__ == "__main__":
    test_document_indexing()
