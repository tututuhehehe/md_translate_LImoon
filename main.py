import os
import re
from openai import OpenAI  # 这里以OpenAI为例，请根据实际使用的API调整

def split_content(file_path, delimiter="%6%6%6"):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 使用正则表达式分割内容，保留分隔符前后的内容
    segments = re.split(f'(\n*{delimiter}\n*)', content)
    
    # 合并小段落（防止分隔符之间内容过少）
    chunks = []
    current_chunk = []
    for seg in segments:
        current_chunk.append(seg)
        # 如果遇到分隔符或长度足够，则生成一个块
        if seg.strip() == delimiter or len('\n'.join(current_chunk)) > 3000:
            chunks.append(''.join(current_chunk))
            current_chunk = []
    
    if current_chunk:
        chunks.append(''.join(current_chunk))
    
    return chunks

def translate_chunk(text, target_lang="zh-cn"):
    # 实际API调用需要根据使用的服务商修改
    client = OpenAI(api_key="sk-rHzA6V800ij1DnlpBPeUCHg9XWeMfTRJIxWJ4SIISuHYJH1T",
                    base_url="https://api.chatanywhere.tech/v1")
    
    prompt = f"""下面是光纤通信领域内的一篇论文，请将以下Markdown内容翻译为简体中文，保持原有格式：
    {text}
    
    要求：
    1. 保留Markdown语法
    2. 保持公式块不变
    3. 专业术语准确
    4. 中文自然流畅
    5. 该论文是光纤通信领域内的论文
    """
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "你是一个专业的翻译专家"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )
    
    return response.choices[0].message.content

def process_translation(input_file, output_file):
    chunks = split_content(input_file)
    translated = []
    
    for i, chunk in enumerate(chunks):
        if chunk.strip() == "%6%6%6":
            translated.append(chunk)
            continue
        
        print(f"Processing chunk {i+1}/{len(chunks)}...")
        translated_chunk = translate_chunk(chunk)
        translated.append(translated_chunk)
        
        # 实时保存进度
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(translated))
    
    print("Translation completed!")

# 使用示例
if __name__ == "__main__":
    input_file = "your_document.md"
    output_file = "translated_document.md"
    process_translation(input_file, output_file)