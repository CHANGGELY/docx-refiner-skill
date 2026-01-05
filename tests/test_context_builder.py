import os
import sys
import json

# 从环境变量获取配置，默认值为硬编码值
index_file = os.getenv("TEST_INDEX_FILE", "raw_content.json")

# 将当前目录加入搜索路径
sys.path.append(os.getcwd())

def test_context_building():
    try:
        from context_builder import build_context
    except ImportError:
        print("Error: build_context not defined in context_builder.py")
        sys.exit(1)
    
    # 模拟输入数据
    mock_data = [
        {"type": "text", "content": "Hello World"},
        {"type": "image", "content": "extracted_assets/image_0.png"}
    ]
    
    result = build_context(mock_data)
    
    print(f"Resulting context:\n{result}")
    
    # 验证输出格式
    if "Hello World" not in result:
        print("Error: Text content missing in result.")
        sys.exit(1)
    
    if "[IMAGE: extracted_assets/image_0.png]" not in result:
        print("Error: Image placeholder missing in result.")
        sys.exit(1)

if __name__ == "__main__":
    test_context_building()

