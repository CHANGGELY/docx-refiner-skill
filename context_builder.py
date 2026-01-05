def build_context(data_list):
    """
    将提取的 JSON 数据转换为大模型易读的 Markdown 文本。
    """
    output = []
    for item in data_list:
        if item['type'] == 'text':
            output.append(item['content'])
        elif item['type'] == 'image':
            output.append(f"\n[IMAGE: {item['content']}]\n")
            
    return "\n".join(output)

if __name__ == "__main__":
    import json
    import os
    
    # 从环境变量获取配置，默认值为硬编码值
    input_file = os.getenv("INDEX_FILE", "raw_content.json")
    if os.path.exists(input_file):
        with open(input_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            print(build_context(data))
