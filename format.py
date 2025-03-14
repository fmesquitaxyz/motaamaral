import glob
import re
import argparse
from datetime import datetime


def generate_front_matter(title, date):
    return f"---\nlayout: default\ntitle: {title}\ndate: {date}\n---\n"


def double_newlines(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as infile:
        match = re.match(r"_raw/(\d{4}-\d{2}-\d{2})", input_file)
        if match:
            date = match.group(1)
        else:
            raise Exception("no date in filename!")
        title, text = infile.read().split("\n", 1)
        text = text.strip()
        title = title.strip()

    front_matter = generate_front_matter(title, date)
    modified_content = (
        front_matter + f"# {title}\n\n" + re.sub(r"(?<!\n)\n", "\n\n", text)
    )

    # Generate the output file name with date and title
    output_file = f"{date}-{re.sub(r'[^a-zA-Z0-9]', '-', title.lower())}.md"

    with open(f"_posts/{output_file}", "w", encoding="utf-8") as outfile:
        outfile.write(modified_content)

    print(f"Newlines doubled. Output saved to {output_file}")


def process_files(file_pattern):
    files = glob.glob(f"_raw/{file_pattern}")

    if not files:
        print(f"No files found matching the pattern: {file_pattern}")
        return

    for input_file in files:
        print(input_file)
        double_newlines(input_file, None)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Double newlines in specified files.")
    parser.add_argument("file_pattern", help="File pattern using regex")

    args = parser.parse_args()

    process_files(args.file_pattern)
