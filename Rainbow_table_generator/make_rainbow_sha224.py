import hashlib
import os

INPUT_WORDLIST = "final_passwords_unique.txt"
OUTPUT_DIR = "rainbow_tables/sha224/large.txt"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "rainbow_sha224.txt")

os.makedirs(OUTPUT_DIR, exist_ok=True)

count = 0

with open(INPUT_WORDLIST, "r", errors="ignore") as infile, \
     open(OUTPUT_FILE, "w") as outfile:

    for line in infile:
        password = line.strip()
        if not password:
            continue

        sha224_hash = hashlib.sha224(password.encode()).hexdigest()
        outfile.write(f"{sha224_hash}:{password}\n")

        count += 1
        if count % 10000 == 0:
            print(f"[+] Processed {count} passwords")

print("✅ SHA-224 rainbow table created")
print("📄 File:", OUTPUT_FILE)
print("🔢 Total entries:", count)
