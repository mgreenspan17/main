# create_structure.py -  module
# Version: 1.0.0 - 2025-08-19 - Repository standardization
# Use case: Part of  project automation


import os

# Define the directory structure
structure = {
    "SSOT": {
        "notion_tools": ["fetch_databases.py", "sync_pages.py"],
        "system_tools": ["trender.py", "utils.py"],
        "proxy_service": ["proxy_service.py"],
        "tests": ["test_notion_tools.py", "test_system_tools.py"],
    }
}

# Base path for the structure
base_path = os.getcwd()  # You can change this to a specific directory

# Create folders and files
for root, subdirs in structure.items():
    root_path = os.path.join(base_path, root)
    os.makedirs(root_path, exist_ok=True)
    for subdir, files in subdirs.items():
        subdir_path = os.path.join(root_path, subdir)
        os.makedirs(subdir_path, exist_ok=True)
        for file_name in files:
            file_path = os.path.join(subdir_path, file_name)
            with open(file_path, "w") as f:
                # Add a comment to each file
                f.write(f"# Placeholder for {file_name}\n")

# Create top-level files
top_level_files = ["requirements.txt", "README.md"]
for file_name in top_level_files:
    file_path = os.path.join(base_path, "SSOT", file_name)
    with open(file_path, "w") as f:
        if file_name == "README.md":
            f.write("# SSOT (Single Source of Truth)\n\n## Overview\n")
        elif file_name == "requirements.txt":
            f.write("# Add your project dependencies here\n")
    

if __name__ == "__main__":
    # Main execution block
    print(f"Running {__file__}")
