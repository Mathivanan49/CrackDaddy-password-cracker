import hashlib

INPUT_WORDLIST = "final_passwords_unique.txt"   # your 100k file
OUTPUT_RAINBOW = "rainbow_tables/md5/large.txt"    # output file

count = 0

with open(INPUT_WORDLIST, "r", errors="ignore") as infile, \
     open(OUTPUT_RAINBOW, "w") as outfile:

    for line in infile:
        password = line.strip()
        if not password:
            continue

        md5_hash = hashlib.md5(password.encode()).hexdigest()
        outfile.write(f"{md5_hash}:{password}\n")

        count += 1
        if count % 10000 == 0:
            print(f"[+] Processed {count} passwords")

print(f"\n✅ Rainbow table created: {OUTPUT_RAINBOW}")
print(f"✅ Total entries: {count}")
