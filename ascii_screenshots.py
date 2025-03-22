# ascii_snapshots.py

def extract_steps(filename="results/logs.txt", selected_steps=None, output_folder = "results/screenshots"):
    import os

    if selected_steps is None:
        selected_steps = [0, 10, 25, 35, 49]

    os.makedirs(output_folder, exist_ok=True)

    with open(filename, "r") as f:
        content = f.read().split("\n\n")

    for block in content:
        if block.strip().startswith("Step"):
            lines = block.strip().split("\n")
            step_line = lines[0]
            try:
                step_num = int(step_line.replace("Step", "").strip())
            except:
                continue

            if step_num in selected_steps:
                filename_out = os.path.join(output_folder, f"step_{step_num}.txt")
                with open(filename_out, "w") as out_file:
                    out_file.write("\n".join(lines))
                print(f"✅ Saved: step {step_num} ➜ {filename_out}")


if __name__ == "__main__":
    extract_steps()