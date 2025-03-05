from os import path, walk

def find_matches(search_dir, search_patterns):
    found_paths = []
    for current_dir, sub_dirs, files in walk(search_dir):
        for pattern in search_patterns:
            if pattern in files or pattern in sub_dirs:
                found_paths.append(path.join(current_dir, pattern))
    return found_paths