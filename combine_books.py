import os
import shutil

base_dir = '/home/solregem/bot'
books = ['atlas_of_autonomy', 'cpython_codex', 'omniscience_of_python', 'pythonic_singularity']

combined_content = "# The Complete Compendium\n\n"

for book in books:
    book_path = os.path.join(base_dir, book)
    if not os.path.exists(book_path):
        continue
        
    combined_content += f"# Book: {book.replace('_', ' ').title()}\n\n"
    
    # We want to process files in a deterministic order. 
    # Sorting directories and files helps.
    for root, dirs, files in sorted(os.walk(book_path)):
        dirs.sort()
        for file in sorted(files):
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    # Add a header for the specific file
                    rel_path = os.path.relpath(file_path, book_path)
                    combined_content += f"---\n\n## Source: {rel_path}\n\n"
                    combined_content += content + "\n\n"
                except Exception as e:
                    print(f"Failed to read {file_path}: {e}")

output_path = os.path.join(base_dir, 'The_Complete_Compendium.md')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(combined_content)

print(f"Created {output_path} successfully.")

# Delete the individual book directories
for book in books:
    book_path = os.path.join(base_dir, book)
    if os.path.exists(book_path):
        shutil.rmtree(book_path)
        print(f"Deleted {book_path}")

print("All small books have been merged and deleted.")
