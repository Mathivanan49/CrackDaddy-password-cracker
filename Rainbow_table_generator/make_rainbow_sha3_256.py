import hashlib
import os

INPUT_WORDLIST = "final_passwords_unique.txt"
OUTPUT_FILE = "rainbow_tables/sha3_256/large.txt"

if not os.path.exists(INPUT_WORDLIST):
    print("[-] Wordlist not found")
    exit(1)

count = 0

with open(INPUT_WORDLIST, "r", errors="ignore") as infile, \
     open(OUTPUT_FILE, "w") as outfile:

    for line in infile:
        pwd = line.strip()
        if not pwd:
            continue

        h = hashlib.sha3_256(pwd.encode()).hexdigest()
        outfile.write(f"{h}:{pwd}\n")

        count += 1
        if count % 10000 == 0:
            print(f"[+] Processed {count} passwords")

print("✅ SHA3-256 rainbow table created")
print(f"Total entries: {count}")
