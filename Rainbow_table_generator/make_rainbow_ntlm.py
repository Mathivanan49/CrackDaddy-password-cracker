import hashlib
import os

INPUT_WORDLIST = "clean_passwords.txt"
OUTPUT_FILE = "rainbow_tables/ntlm/rainbow_ntlm.txt"

count = 0

if not os.path.exists(INPUT_WORDLIST):
    print("[-] Wordlist not found")
    exit(1)

with open(INPUT_WORDLIST, "r", errors="ignore") as infile, \
     open(OUTPUT_FILE, "w") as outfile:

    for line in infile:
        password = line.strip()
        if not password:
            continue

        # NTLM = MD4(UTF-16LE(password))
        ntlm_hash = hashlib.new(
            "md4", password.encode("utf-16le")
        ).hexdigest()

        outfile.write(f"{ntlm_hash}:{password}\n")

        count += 1
        if count % 10000 == 0:
            print(f"[+] Processed {count}")

print("\n✅ NTLM rainbow table created")
print(f"📄 File: {OUTPUT_FILE}")
print(f"🔢 Total entries: {count}")
