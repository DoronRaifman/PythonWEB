import os
from pathlib import Path


def lines_count(start_folder: str, folder: str, exclude_list: list, summery_list: list):
    total_count = 0
    all_files = [entry for entry in os.listdir(folder) if entry.lower() not in exclude_list]
    dir_list = [entry for entry in all_files if os.path.isdir(os.path.join(folder, entry))]
    file_list = [entry for entry in all_files if os.path.isfile(os.path.join(folder, entry))]
    for dir_ent in dir_list:
        dir_entry = os.path.join(folder, dir_ent)
        total_count += lines_count(start_folder, dir_entry, exclude_list, summery_list)
    for file in file_list:
        try:
            file_name = os.path.join(folder, file)
            with open(file_name, "r") as f:
                count_temp = len(f.readlines())
                # print(f"      {file} - {count_temp:6d}")
            total_count += count_temp
        except Exception as ex:
            pass
            # print(f"Exception {ex}")
    if len(summery_list) == 0 or os.path.split(folder)[1] in summery_list:
        print(f"-> folder {folder[len(start_folder) + 1:]} - {total_count:,}")
    return total_count


if __name__ == '__main__':
    # base_path = Path(__file__).parent.parent.parent.parent
    # start_path = os.path.abspath(base_path)
    # print(f"Line count for project {start_path}")
    files_root = Path(__file__)
    root_path = os.path.abspath(files_root)

    fragments = root_path.split('\\')
    start_path = r"C:\Dev"
    print(f"Code lines report for {start_path}")
    summery_list = ["ak-utils", "Software", "python", "go", "backend-server", "web-ui"]
    exclude_folder_list = [
        "venv", ".idea", ".git", ".vs", ".vscode", "bin", "debug", "x64",".nuget", "obj"
    ]
    count = lines_count(start_path, start_path, exclude_folder_list, summery_list)
    # count = lines_count(start_path, start_path, [".py"], exclude_folder_list, [])
    print("-----------------------------------")
    print(f"Total count {count:,}")
