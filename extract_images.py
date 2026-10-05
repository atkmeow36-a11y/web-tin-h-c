import zipfile, os, sys

# Try both uploaded docx files
docx_files = [
    r'C:\Users\ADMIN\.gemini\antigravity\brain\179fd058-e644-408e-ac27-a84e80894883\.user_uploaded\media_1791185969410.docx',
    r'C:\Users\ADMIN\.gemini\antigravity\brain\179fd058-e644-408e-ac27-a84e80894883\.user_uploaded\media_1791086007289.docx',
]
out_dir = os.path.join(r'd:\bài thuyết trình tin học', 'images')
os.makedirs(out_dir, exist_ok=True)

for docx_path in docx_files:
    print(f'Checking: {os.path.basename(docx_path)}')
    try:
        with zipfile.ZipFile(docx_path, 'r') as z:
            media_files = [n for n in z.namelist() if n.startswith('word/media/')]
            print(f'  Found {len(media_files)} media files')
            for name in media_files:
                base = os.path.basename(name)
                target = os.path.join(out_dir, base)
                data = z.read(name)
                with open(target, 'wb') as f:
                    f.write(data)
                print(f'  Extracted: {base} ({len(data)} bytes)')
    except Exception as e:
        print(f'  Error: {e}')

print('Done.')
