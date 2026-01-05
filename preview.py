import json

def generate_preview():
    with open("raw_content.json", "r", encoding="utf-8") as f:
        content = json.load(f)
        
    html = ["<html><body><h1>文档提取预览</h1>"]
    for item in content:
        if item['type'] == 'text':
            html.append(f"<p style='border-bottom: 1px solid #eee; padding: 5px;'>{item['content']}</p>")
        elif item['type'] == 'image':
            html.append(f"<div style='background: #f9f9f9; padding: 10px; margin: 10px 0;'>")
            html.append(f"<p><b>[图片资源]</b></p>")
            html.append(f"<img src='{item['content']}' style='max-width: 500px; display: block;'>")
            html.append(f"</div>")
    html.append("</body></html>")
    
    with open("preview.html", "w", encoding="utf-8") as f:
        f.write("\n".join(html))
    print("[+] 预览文件已生成: preview.html")

if __name__ == "__main__":
    generate_preview()

