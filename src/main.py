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

# Right now our site always assumes that / is the root path of the site (e.g. http://localhost:8888/. Make it configurable by:
# In main.py use the sys.argv to grab the first CLI argument to the program. Save it as the basepath. If one isn't provided, default to /.
# Pass the basepath to the generate_pages_recursive and generate_page functions.
# In generate_page, after you replace the {{ Title }} and {{ Content }}, replace any instances of:
# href="/ with href="{basepath}
# src="/ with src="{basepath}
# Create a new build.sh script that builds the site for production:
# The script is simple: python3 src/main.py "/REPO_NAME/" (replace REPO_NAME with your actual GitHub repo name)
# Your main.py is also used for local testing, so it will still need the default / baseurl
# Run the new build script and ensure that the site is built correctly
# Update your main.py to build the site into the docs directory instead of public. GitHub pages serves sites from the docs directory of your main branch by default.
# Delete the public directory, and remove it from your .gitignore file.
# Rebuild the site into the docs directory.
# Open your repository's settings on GitHub and select Pages in the Code and automation section to config the publishing source.
# Set the source to the main branch and the docs directory.
# Save the settings.
# (Now the /docs directory on your main branch will auto deploy to your GitHub Pages URL once something is in it.)
# Commit and push your changes to GitHub
# Open the live URL (https://USERNAME.github.io/REPO_NAME/) in your browser and ensure that the site is live and working correctly. You can check the status and find the exact URL in the GitHub Pages section of your repository settings.

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
