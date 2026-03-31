import time
def download_file(filename):
    print(f"Starting download: {filename}")
    time.sleep(5)  # Simulates waiting 2 seconds for the network
    print(f"Finished download: {filename}")

start_time = time.time()
# We have 3 files to download
files = ["File_A.txt", "File_B.txt", "File_C.txt"]

# Synchronous loop: One by one
for file in files:
    download_file(file)
end_time = time.time()
print(f"Total time: {end_time - start_time:.2f} seconds")
