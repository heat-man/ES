import os
import re
import shutil

def detect_keywords(file_path, keywords):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read().lower()
        for keyword in keywords:
            if re.search(r'\b{}\b'.format(re.escape(keyword)), content):
                return True
    return False

def process_html_files(directory, keywords, suspicious_directory):
    html_files = [file for file in os.listdir(directory)]
    for html_file in html_files:
        file_path = os.path.join(directory, html_file)
        if detect_keywords(file_path, keywords):
            print(f'The file "{html_file}" contains sensitive keywords. Copying to the suspicious directory.')
            shutil.copy(file_path, os.path.join(suspicious_directory, html_file))
        else:
            print(f'The file "{html_file}" does not contain sensitive keywords.')

if __name__ == "__main__":
    directory_path = './html'

    suspicious_directory_path = './suspicious'

    if not os.path.exists(suspicious_directory_path):
        os.makedirs(suspicious_directory_path)

    keywords_to_detect = ['hacking', 'hack', 'weapon', 'secret', 'password', 'passwd', 'admin']

    process_html_files(directory_path, keywords_to_detect, suspicious_directory_path)

