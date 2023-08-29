import json
import markdown
import os
import sys
from bs4 import BeautifulSoup

def markdown_to_structured_json(file_path, output_folder):
    with open(file_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    html_content = markdown.markdown(md_content)
    soup = BeautifulSoup(html_content, 'html.parser')

    sections = []
    current_section = {"header": None, "content": ""}

    for elem in soup:
        if elem.name in ['h1', 'h2']:
            if current_section["header"]:
                sections.append(current_section)
            current_section = {"header": elem.text, "content": ""}
        else:
            if current_section["header"]:
                current_section["content"] += str(elem)

    if current_section["header"]:
        sections.append(current_section)

    json_data = {
        'file_name': os.path.basename(file_path),
        'sections': sections
    }

    output_file_path = os.path.join(output_folder, os.path.basename(file_path) + '.json')
    with open(output_file_path, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)

if len(sys.argv) < 3:
    print("Usage: python script.py [input_folder] [output_folder]")
    sys.exit(1)

input_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith('.md'):
        markdown_to_structured_json(os.path.join(input_folder, filename), output_folder)

