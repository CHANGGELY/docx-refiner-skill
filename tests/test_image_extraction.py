import os
import sys
import shutil

# 将当前目录加入搜索路径
sys.path.append(os.getcwd())

def test_extract_images():
    try:
        from extractor import extract_images
    except ImportError:
        print("Error: extract_images not defined in extractor.py")
        sys.exit(1)
    
    file_path = "code之路.docx"
    output_dir = "test_assets"
    
    # 清理旧环境
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    
    image_paths = extract_images(file_path, output_dir)
    
    print(f"Extracted {len(image_paths)} images.")
    
    if not os.path.exists(output_dir):
        print(f"Error: Output directory {output_dir} was not created.")
        sys.exit(1)
        
    if len(image_paths) == 0:
        print("Warning: No images extracted (Document might not have images).")
    else:
        for path in image_paths:
            if not os.path.exists(path):
                print(f"Error: Image file {path} missing.")
                sys.exit(1)

if __name__ == "__main__":
    test_extract_images()
