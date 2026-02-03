import hashlib
import os

INPUT_WORDLIST = "final_passwords_unique.txt"
OUTPUT_FILE = "rainbow_tables/sha256/large.txt"

count = 0

# Safety check
if not os.path.exists(INPUT_WORDLIST):
    print("[-] Wordlist not found:", INPUT_WORDLIST)
    exit(1)

with open(INPUT_WORDLIST, "r", errors="ignore") as infile, \
     open(OUTPUT_FILE, "w") as outfile:

    for line in infile:
        password = line.strip()

        if not password:
            continue

        sha256_hash = hashlib.sha256(password.encode()).hexdigest()
        outfile.write(f"{sha256_hash}:{password}\n")

        count += 1
        if count % 10000 == 0:
            print(f"[+] Processed {count} passwords")

print("\n✅ SHA-256 rainbow table created successfully")
print(f"📄 File: {OUTPUT_FILE}")
print(f"🔢 Total entries: {count}")
