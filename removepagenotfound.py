from pathlib import Path


def is_page_not_found_file_item(item):
    if item.is_file():
        try:
            with open(item, "r") as file:
                data = file.read()
                if "<title>Not Found</title>" in data:
                    return True
        except UnicodeDecodeError:
            print(f"Error reading {item}")
        return False


for item in Path("docs").glob("**/*.html"):
    if is_page_not_found_file_item(item):
        print(f"Removing {item}")
        item.unlink()
