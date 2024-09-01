from docx import Document
import os

def save_section_as_txt(section_title, content, output_dir):
    """
    保存每个文档部分为单独的txt文件。
    """
    sanitized_title = section_title.replace('/', '_')
    filename = os.path.join(output_dir, f"{sanitized_title}.txt")
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

def split_docx_to_txt(input_file):
    """
    将Word文档中的内容按标题分割，并分别保存为txt文件。
    """
    doc = Document(input_file)
    output_dir = os.path.splitext(input_file)[0] + "_txt"
    os.makedirs(output_dir, exist_ok=True)

    current_section_title = None
    current_content = ""

    for paragraph in doc.paragraphs:
        if paragraph.style.name.startswith('Heading'):  # 根据样式名判断标题
            if current_section_title:
                save_section_as_txt(current_section_title, current_content, output_dir)
            current_section_title = paragraph.text
            current_content = ""
        else:
            current_content += paragraph.text + "\n"

    # 保存最后一个部分
    if current_section_title:
        save_section_as_txt(current_section_title, current_content, output_dir)

    print(f"文档内容已保存至目录：{output_dir}")

# 使用示例：将 'your_document.docx' 替换为你实际的Word文档路径
split_docx_to_txt('output.docx')
