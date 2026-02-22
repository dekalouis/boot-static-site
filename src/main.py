import os
import shutil
import sys

from copystatic import copy_files_recursive
from gencontent import generate_page, generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"
dir_path_docs = "./docs"

def main():
    print("Deleting docs directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)
    
    # Get basepath from command line arguments, default to "/"
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
        if not basepath.startswith("/"):
            basepath = "/" + basepath
        if not basepath.endswith("/"):
            basepath += "/"

    print("Copying static files to docs directory...")
    copy_files_recursive(dir_path_static, dir_path_docs)

    print("Generating page...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_docs, basepath)


main()
