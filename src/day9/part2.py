def parse_disk_map(data):
    hard_drive = []
    block_id = 0  # Start file IDs from 0

    for i, char in enumerate(data):
        try:
            count = int(char)
        except ValueError:
            print(f"Invalid character '{char}' at position {i}. Skipping.")
            continue  # Skip invalid characters

        if i % 2 == 0:
            # Even index: append file blocks with current block_id
            for _ in range(count):
                hard_drive.append(block_id)
            block_id += 1  # Increment file ID for next file
        else:
            # Odd index: append free space blocks
            for _ in range(count):
                hard_drive.append('.')
    
    return hard_drive

def identify_files(hard_drive):
    files = {}  # Dictionary to store file_id: (start_index, end_index)
    current_file_id = None
    start_index = 0

    for i, block in enumerate(hard_drive):
        if block != '.':
            if current_file_id is None:
                # Start of a new file
                current_file_id = block
                start_index = i
            elif block != current_file_id:
                # Start of a different file; save the previous one
                files[current_file_id] = (start_index, i - 1)
                current_file_id = block
                start_index = i
        else:
            if current_file_id is not None:
                # End of the current file
                files[current_file_id] = (start_index, i - 1)
                current_file_id = None

    # Handle the last file if it ends at the end of the hard_drive
    if current_file_id is not None:
        files[current_file_id] = (start_index, len(hard_drive) - 1)
    
    return files

def find_free_spans(hard_drive):
    free_spans = []  # List of (start_index, length)
    in_free_span = False
    start_index = 0

    for i, block in enumerate(hard_drive):
        if block == '.':
            if not in_free_span:
                # Start of a free span
                in_free_span = True
                start_index = i
        else:
            if in_free_span:
                # End of a free span
                span_length = i - start_index
                free_spans.append((start_index, span_length))
                in_free_span = False

    # Handle free span at the end
    if in_free_span:
        span_length = len(hard_drive) - start_index
        free_spans.append((start_index, span_length))
    
    return free_spans

def move_files(hard_drive, files):
    """
    Moves entire files to the leftmost available free space that can fit the file.
    Files are moved in decreasing order of file ID.
    """
    # Sort files in decreasing order of file_id
    sorted_files = sorted(files.keys(), reverse=True)

    for file_id in sorted_files:
        start, end = files[file_id]
        file_size = end - start + 1

        # Find the leftmost free span that can fit the file
        target_start = None
        for i in range(len(hard_drive) - file_size + 1):
            # Check if the span from i to i + file_size is all free ('.')
            if all(block == '.' for block in hard_drive[i:i + file_size]):
                target_start = i
                break  # Found the leftmost suitable span

        if target_start is not None and target_start < start:
            print(f"Moving File {file_id} from [{start}, {end}] to [{target_start}, {target_start + file_size -1}]")

            # Move the file: overwrite the target span with the file's blocks
            hard_drive[target_start:target_start + file_size] = [file_id] * file_size

            # Replace the old position with '.'s
            hard_drive[start:end + 1] = ['.'] * file_size

            # Update the file's new position in the files dictionary
            files[file_id] = (target_start, target_start + file_size - 1)

            # print(f"Hard Drive After Moving File {file_id}: {''.join(str(block) if block != '.' else '.' for block in hard_drive)}")

    return hard_drive

def calculate_checksum(hard_drive):
    checksum = 0
    for position, block in enumerate(hard_drive):
        if block != '.':
            checksum += position * block
    return checksum

def main():
    # Read the input data from 'input.txt'
    try:
        with open('input.txt', 'r') as f:
            data = f.read().strip()
    except FileNotFoundError:
        print("Error: 'input.txt' not found.")
        return

    # Parse the disk map
    hard_drive = parse_disk_map(data)

    # Debug: Print initial hard_drive
    print("Initial hard_drive:", ''.join(str(block) if block != '.' else '.' for block in hard_drive))

    # Identify files and their positions
    files = identify_files(hard_drive)

    # Debug: Print identified files
    print("Identified Files (file_id: start_index - end_index):")
    for fid in sorted(files.keys()):
        print(f"File {fid}: {files[fid][0]} - {files[fid][1]}")

    hard_drive = move_files(hard_drive, files)

    print("Hard Drive After Moving Files:", ''.join(str(block) if block != '.' else '.' for block in hard_drive))

    checksum = calculate_checksum(hard_drive)

    print("Filesystem Checksum:", checksum)

if __name__ == "__main__":
    main()
