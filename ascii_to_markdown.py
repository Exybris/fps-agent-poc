# ascii_to_markdown.py

import os

def convert_txt_to_md(input_folder="results/screenshots", output_folder="results/screenshots_md"):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            step_num = filename.split("_")[1].split(".")[0]

            with open(os.path.join(input_folder, filename), "r") as f:
                content = f.read()

            md_content = f"# Step {step_num}\n\n" \
                         "```text\n" \
                         f"{content.strip()}\n" \
                         "```\n\n" \
                         f"_Snapshot of simulation step {step_num}_\n"

            output_path = os.path.join(output_folder, f"step_{step_num}.md")
            with open(output_path, "w") as md_file:
                md_file.write(md_content)
                print(f"✅ Converted: {filename} ➜ {output_path}")

if __name__ == "__main__":
    convert_txt_to_md()