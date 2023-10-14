import os

def find_files(directory_path):
    # List all the files in the directory
    files = os.listdir(directory_path)

    # Filter files that start with "2023-05"
    relevant_files = [f for f in files if f.startswith("2023-05")]

    return relevant_files

def save_to_markdown(files, output_file):
    with open(output_file, 'w') as f:
        for file in files:
            markdown_line = f"[]({{site.baseurl}}/img/{file})\n"
            f.write(markdown_line)

if __name__ == "__main__":
    # Change this to the path of your directory containing the target files
    directory_path = "/Users/maomao/Documents/GitHub/maomaocv.github.io/img"

    # Output markdown file
    output_file = "/Users/maomao/Documents/GitHub/maomaocv.github.io/_posts/2018-08-23-flower-care-guide.markdown"

    relevant_files = find_files(directory_path)
    save_to_markdown(relevant_files, output_file)
