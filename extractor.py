import docx
import os

def extract_all_text(file_path):
    """
    从 .docx 文件中提取所有文本段落。
    """
    doc = docx.Document(file_path)
    # 提取所有段落的文本，过滤掉纯空白行
    paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
    return paragraphs

def extract_images(file_path, output_dir):
    """
    从 .docx 文件中提取所有图片并保存到 output_dir。
    返回图片路径列表。
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    doc = docx.Document(file_path)
    image_paths = []
    
    # docx 文件本质是 ZIP，图片存在 word/media/ 下
    # 这里通过 document.part.related_parts 访问
    for i, (rel_id, part) in enumerate(doc.part.related_parts.items()):
        if "image" in part.content_type:
            # 构造文件名
            ext = part.content_type.split("/")[-1]
            image_name = f"image_{i}.{ext}"
            image_path = os.path.join(output_dir, image_name)
            
            with open(image_path, "wb") as f:
                f.write(part.blob)
            
            image_paths.append(image_path)
            
    return image_paths

if __name__ == "__main__":
    # 简单测试
    import sys
    if len(sys.argv) > 1:
        res = extract_all_text(sys.argv[1])
        for i, p in enumerate(res[:5]):
            print(f"[{i}] {p}")
