"""
Manually add Google analytics script to all .html files
"""

import os

# Define Google Analytics tracking ID
GA_ID = "G-JPXX63Z3XR"  # Replace with your actual ID

# Directory where Jupyter Book builds HTML files
BUILD_DIR = "_build/html"

# Google Analytics script to be inserted
GA_SCRIPT = f"""
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA_ID}');
</script>
"""

# Ensure build directory exists
if not os.path.exists(BUILD_DIR):
    print(f"❌ Error: Directory '{BUILD_DIR}' not found. Did you run 'jupyter-book build .'?")
    exit(1)

print(f"🔄 Searching for HTML files in {BUILD_DIR}...")

# Recursively process all .html files in subdirectories
for root, _, files in os.walk(BUILD_DIR):
    for filename in files:
        if filename.endswith(".html"):
            filepath = os.path.join(root, filename)

            # Read file content
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()

            # Check if GA script is already present
            if f"gtag/js?id={GA_ID}" in content:
                print(f"✅ Skipping {filepath} (Google Analytics already added)")
                continue

            # Insert script immediately after <head>
            new_content = content.replace("</head>", f"</head>{GA_SCRIPT}", 1)

            # Write the modified content back to the file
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(new_content)

            print(f"✔️ Google Analytics added to: {filepath}")

print("🎉 Google Analytics script injection complete!")

