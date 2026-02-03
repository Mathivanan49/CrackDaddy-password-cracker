import hashlib

INPUT_WORDLIST = "final_passwords_unique.txt"
OUTPUT_RAINBOW = "rainbow_tables/sha1/large.txt"

with open(INPUT_WORDLIST, "r", errors="ignore") as infile, \
     open(OUTPUT_RAINBOW, "w") as outfile:

    for line in infile:
        pwd = line.strip()
        if not pwd:
            continue
        sha1 = hashlib.sha1(pwd.encode()).hexdigest()
        outfile.write(f"{sha1}:{pwd}\n")

print("SHA1 rainbow table created")
