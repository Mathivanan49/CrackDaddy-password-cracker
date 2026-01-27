import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import threading
import time
import re
import hashlib
import webbrowser

class ImprovedAutoDetectCracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Improved Auto-Detect Cracker")
        self.root.geometry("800x600")
        
        # Project info
        self.project_name = "BridgeReflex"
        self.version = "v2.0"
        self.developer = "CyberSec Team"
        
        # Algorithm patterns with better detection
        self.algorithms = {
            "md5": {
                "length": 32,
                "pattern": r"^[a-f0-9]{32}$",
                "rainbow": "rainbow_tables/md5/rainbow_md5.txt",
                "large": "rainbow_tables/md5/large.txt"
            },
            "ntlm": {
                "length": 32,
                "pattern": r"^[a-f0-9]{32}$",
                "rainbow": "rainbow_tables/ntlm/rainbow_ntlm.txt",
                "large": "rainbow_tables/ntlm/large.txt"
            },
            "sha1": {
                "length": 40,
                "pattern": r"^[a-f0-9]{40}$",
                "rainbow": "rainbow_tables/sha1/rainbow_sha1.txt",
                "large": "rainbow_tables/sha1/large.txt"
            },
            "sha224": {
                "length": 56,
                "pattern": r"^[a-f0-9]{56}$",
                "rainbow": "rainbow_tables/sha224/rainbow_sha224.txt",
                "large": "rainbow_tables/sha224/large.txt"
            },
            "sha256": {
                "length": 64,
                "pattern": r"^[a-f0-9]{64}$",
                "rainbow": "rainbow_tables/sha256/rainbow_sha256.txt",
                "large": "rainbow_tables/sha256/large.txt"
            },
            "sha3_256": {
                "length": 64,
                "pattern": r"^[a-f0-9]{64}$",
                "rainbow": "rainbow_tables/sha3_256/rainbow_sha3_256.txt",
                "large": "rainbow_tables/sha3_256/large.txt"
            }
        }
        
        self.loaded_tables = {}
        self.wordlist_loaded = False
        self.wordlist_path = None
        self.current_algo = None
        self.setup_improved_ui()
    
    def show_project_info(self):
        """Open project details in browser window"""
        project_details_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Password Cracker - Project Details</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 40px;
                    background-color: #f5f5f5;
                    line-height: 1.6;
                }}
                .container {{
                    max-width: 1100px;
                    margin: 0 auto;
                    background: white;
                    padding: 40px;
                    border-radius: 10px;
                    box-shadow: 0 0 20px rgba(0,0,0,0.1);
                }}
                h1 {{
                    color: #333;
                    text-align: center;
                    margin-bottom: 10px;
                }}
                .subtitle {{
                    text-align: center;
                    color: #666;
                    margin-bottom: 30px;
                    font-size: 18px;
                }}
                .description {{
                    background: #f8f9fa;
                    padding: 20px;
                    border-radius: 8px;
                    margin: 25px 0;
                    border-left: 4px solid #4CAF50;
                    font-size: 16px;
                }}
                table {{
                    width: 100%;
                    border-collapse: collapse;
                    margin: 25px 0;
                    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                }}
                th {{
                    background-color: #4CAF50;
                    color: white;
                    padding: 15px 20px;
                    text-align: left;
                    font-weight: bold;
                }}
                td {{
                    padding: 12px 20px;
                    border-bottom: 1px solid #ddd;
                    vertical-align: top;
                }}
                tr:hover {{
                    background-color: #f5f5f5;
                }}
                .section-title {{
                    color: #2c3e50;
                    margin-top: 35px;
                    padding-bottom: 10px;
                    border-bottom: 2px solid #4CAF50;
                    font-size: 1.4em;
                }}
                .footer {{
                    text-align: center;
                    margin-top: 40px;
                    color: #7f8c8d;
                    font-size: 14px;
                    padding-top: 20px;
                    border-top: 1px solid #eee;
                }}
                .highlight {{
                    background-color: #e8f5e9;
                    padding: 3px 8px;
                    border-radius: 4px;
                    font-weight: bold;
                    color: #2e7d32;
                }}
                .project-name {{
                    color: #2196F3;
                    font-weight: bold;
                    font-size: 1.1em;
                }}
                .member-id {{
                    color: #e74c3c;
                    font-family: monospace;
                    font-weight: bold;
                }}
                .contribution {{
                    color: #34495e;
                    font-size: 0.9em;
                    line-height: 1.4;
                }}
                .table-container {{
                    overflow-x: auto;
                    margin: 20px 0;
                }}
                .header-row {{
                    display: flex;
                    background: #4CAF50;
                    color: white;
                    font-weight: bold;
                    border-radius: 5px 5px 0 0;
                }}
                .header-cell {{
                    flex: 1;
                    padding: 15px;
                    text-align: center;
                }}
                .data-row {{
                    display: flex;
                    border-bottom: 1px solid #ddd;
                }}
                .data-row:hover {{
                    background: #f9f9f9;
                }}
                .data-cell {{
                    flex: 1;
                    padding: 12px 15px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Cyber Security Internship Project</h1>
                <div class="description">
                    This project was developed by Anonymous Hacker as part of a Cyber Security Internship. 
                    This project is designed to Secure the Organizations in Real World from Cyber Frauds performed by Hackers.
                </div>

                <h2 class="section-title">Project Details</h2>
                <table>
                    <tr>
                        <th>Project Details</th>
                        <th>Value</th>
                    </tr>
                    <tr>
                        <td>Project Name</td>
                        <td class="project-name">CrackDaddy</td>
                    </tr>
                    <tr>
                        <td>Project Description</td>
                        <td>To Crack Hashed Passwords (MD5, SHA1, SHA256,SHA3_256,NTLM,SHA224) using a given Wordlist, 
                            Rainbow Tables providing Real-Time Feedback and Supporting various file encodings.</td>
                    </tr>
                    <tr>
                        <td>Project Start Date</td>
                        <td>25-December-2025</td>
                    </tr>
                    <tr>
                        <td>Project End Date</td>
                        <td>25-January-2025</td>
                    </tr>
                    <tr>
                        <td>Project Status</td>
                        <td><span class="highlight">Completed</span></td>
                    </tr>
                </table>

                <h2 class="section-title">Team Members & Contributions</h2>
                <div class="table-container">
                    <table>
                        <thead>
                            <tr>
                                <th>Name</th>
                                <th>Employee ID</th>
                                <th>Contribution</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>MATHIVANAN M</td>
                                <td class="member-id">ST#IS#8560</td>
                                <td class="contribution">
                                    • Researched password cracking techniques and hash algorithms<br>
                                    • Defined project objectives, scope, and limitations<br>
                                    • Designed the overall workflow and system architecture
                                </td>
                            </tr>
                            <tr>
                                <td>KETHAN VIGNESH N S</td>
                                <td class="member-id">ST#IS#8552</td>
                                <td class="contribution">
                                    • Implemented multiple hashing algorithms (MD5, SHA-1, SHA-256 etc..)<br>
                                    • Developed hash generation and comparison logic<br>
                                    • Verified correctness and reliability of hash outputs
                                </td>
                            </tr>
                            <tr>
                                <td>DAFYD PAUL P</td>
                                <td class="member-id">ST#IS#8579</td>
                                <td class="contribution">
                                    • Implemented brute-force password cracking mechanism<br>
                                    • Managed character sets and attack configurations<br>
                                    • Optimized performance for faster cracking speed
                                </td>
                            </tr>
                            <tr>
                                <td>SASI DHARAN S</td>
                                <td class="member-id">ST#IS#8554</td>
                                <td class="contribution">
                                    • Implemented dictionary-based password cracking<br>
                                    • Integrated and managed wordlists (e.g., rockyou.txt)<br>
                                    • Improved efficiency of wordlist processing
                                </td>
                            </tr>
                            <tr>
                                <td>ROYSON T J</td>
                                <td class="member-id">ST#IS#8578</td>
                                <td class="contribution">
                                    • Designed command-line / GUI interface<br>
                                    • Handled user inputs and error handling<br>
                                    • Implemented Project Info button with browser redirection
                                </td>
                            </tr>
                            <tr>
                                <td>YADESHKUMAR K</td>
                                <td class="member-id">ST#IS#8582</td>
                                <td class="contribution">
                                    • Tested the tool using multiple hashes and inputs<br>
                                    • Prepared project documentation and user guide<br>
                                    • Added ethical disclaimer and usage restrictions
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <h2 class="section-title">Company Details</h2>
                <table>
                    <tr>
                        <th>Company</th>
                        <th>Contact Mail</th>
                    </tr>
                    <tr>
                        <td>Supraja Technologies</td>
                        <td>contact@suprajatechnologies.com</td>
                    </tr>
                </table>

                <div class="footer">
                    Generated on: {time.strftime("%d-%B-%Y %I:%M %p")}<br>
                    BridgeReflex v2.0 | Cyber Security Tool
                </div>
            </div>
        </body>
        </html>
        """
        
        # Create temporary HTML file
        temp_file = "project_details.html"
        with open(temp_file, "w", encoding="utf-8") as f:
            f.write(project_details_html)
        
        # Open in default browser
        webbrowser.open(f"file://{os.path.abspath(temp_file)}")
        
        # Clean up after 3 seconds
        threading.Timer(3, lambda: os.remove(temp_file) if os.path.exists(temp_file) else None).start()
    
    def setup_improved_ui(self):
        """Create improved UI with project info and dual attack methods"""
        main_frame = tk.Frame(self.root, padx=10, pady=10)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header with project info
        header_frame = tk.Frame(main_frame)
        header_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Left side - Main title
        tk.Label(header_frame, text="🔥 CrackDaddy", 
                font=("Arial", 16, "bold")).pack(side=tk.LEFT)
        
        # Right side - Project info and button
        info_frame = tk.Frame(header_frame)
        info_frame.pack(side=tk.RIGHT)
        
        # Project Info Button
        tk.Button(info_frame, text="ℹ️ Project Info", 
                 command=self.show_project_info,
                 font=("Arial", 9, "bold"),
                 bg="#3498db", fg="white",
                 relief=tk.RAISED,
                 padx=10, pady=2).pack(anchor='e', pady=(0, 2))
        
        tk.Label(info_frame, text=f"{self.project_name} {self.version}", 
                font=("Arial", 10, "bold"), fg="blue").pack(anchor='e')
        tk.Label(info_frame, text=f"by {self.developer}", 
                font=("Arial", 9), fg="gray").pack(anchor='e')
        
        # Main content frame with left and right panels
        content_frame = tk.Frame(main_frame)
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # LEFT PANEL - Rainbow Table Attack (Existing functionality)
        left_frame = tk.LabelFrame(content_frame, text="🌈 Rainbow Table Attack", 
                                  font=("Arial", 11, "bold"), padx=10, pady=10)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        # RIGHT PANEL - Wordlist Attack
        right_frame = tk.LabelFrame(content_frame, text="📚 Wordlist Attack", 
                                   font=("Arial", 11, "bold"), padx=10, pady=10)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        
        # ========== LEFT PANEL CONTENT (Rainbow Table) ==========
        # Hash input (Shared between both methods)
        tk.Label(left_frame, text="Enter Hash:", 
                font=("Arial", 11)).pack(anchor='w', pady=(0,5))
        
        self.hash_entry = tk.Entry(left_frame, width=60, font=("Consolas", 10))
        self.hash_entry.pack(pady=5, fill=tk.X)
        
        # Detection results
        self.detection_frame = tk.Frame(left_frame)
        self.detection_frame.pack(pady=10, fill=tk.X)
        
        tk.Label(self.detection_frame, text="Detection Results:", 
                font=("Arial", 11, "bold")).pack(anchor='w')
        
        self.detection_text = tk.Text(self.detection_frame, height=7, width=60,
                                     font=("Consolas", 9))
        scrollbar_det = tk.Scrollbar(self.detection_frame, command=self.detection_text.yview)
        self.detection_text.config(yscrollcommand=scrollbar_det.set)
        self.detection_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar_det.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Buttons for Rainbow Table
        button_frame = tk.Frame(left_frame)
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="🔍 Smart Detect", 
                 command=self.smart_detect, bg="#3498db", fg="white",
                 width=15).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="🌈 Load Rainbow Table", 
                 command=lambda: self.load_table("rainbow"),
                 width=18).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="📚 Load Large Table", 
                 command=lambda: self.load_table("large"),
                 width=15).pack(side=tk.LEFT, padx=5)
        
        # Manual override
        manual_frame = tk.Frame(left_frame)
        manual_frame.pack(pady=10)
        
        tk.Label(manual_frame, text="Manual Override:", 
                font=("Arial", 10)).pack(side=tk.LEFT)
        
        self.manual_algo = tk.StringVar(value="md5")
        algo_menu = ttk.Combobox(manual_frame, textvariable=self.manual_algo,
                                values=list(self.algorithms.keys()),
                                state="readonly", width=12)
        algo_menu.pack(side=tk.LEFT, padx=10)
        
        tk.Button(manual_frame, text="Use Manual", 
                 command=self.use_manual, width=10).pack(side=tk.LEFT)
        
        # Rainbow Table Crack button
        self.rainbow_crack_btn = tk.Button(left_frame, text="⚡ CRACK WITH RAINBOW TABLE", 
                                          command=self.crack_with_auto_detect,
                                          bg="green", fg="white",
                                          font=("Arial", 11, "bold"))
        self.rainbow_crack_btn.pack(pady=10, fill=tk.X)
        
        # Rainbow Table Status
        self.rainbow_status = tk.Label(left_frame, text="Rainbow Table: Ready", fg="blue")
        self.rainbow_status.pack(pady=5)
        
        # Rainbow Table Results
        tk.Label(left_frame, text="Rainbow Table Results:", 
                font=("Arial", 11, "bold")).pack(anchor='w', pady=(10,0))
        
        rainbow_results_frame = tk.Frame(left_frame)
        rainbow_results_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.rainbow_results_text = tk.Text(rainbow_results_frame, height=8, font=("Consolas", 9))
        rainbow_scrollbar = tk.Scrollbar(rainbow_results_frame, command=self.rainbow_results_text.yview)
        self.rainbow_results_text.config(yscrollcommand=rainbow_scrollbar.set)
        
        self.rainbow_results_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        rainbow_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # ========== RIGHT PANEL CONTENT (Wordlist Attack) ==========
        # Algorithm selection for wordlist
        tk.Label(right_frame, text="Select Algorithm:", 
                font=("Arial", 11)).pack(anchor='w', pady=(0,5))
        
        self.wordlist_algo = tk.StringVar(value="md5")
        wordlist_algo_menu = ttk.Combobox(right_frame, textvariable=self.wordlist_algo,
                                         values=list(self.algorithms.keys()),
                                         state="readonly", width=20)
        wordlist_algo_menu.pack(pady=5, fill=tk.X)
        
        # Wordlist controls
        wordlist_control_frame = tk.Frame(right_frame)
        wordlist_control_frame.pack(pady=10, fill=tk.X)
        
        self.wordlist_btn = tk.Button(wordlist_control_frame, text="📁 Load Wordlist", 
                                     command=self.load_wordlist,
                                     width=15)
        self.wordlist_btn.pack(side=tk.LEFT, padx=(0,5))
        
        self.wordlist_status = tk.Label(wordlist_control_frame, text="No wordlist loaded", 
                                       fg="red", font=("Arial", 9))
        self.wordlist_status.pack(side=tk.LEFT)
        
        # Default wordlist button
        tk.Button(right_frame, text="🔄 Load clean_rockyou.txt", 
                 command=self.load_default_wordlist, bg="#e67e22", fg="white",
                 width=20).pack(pady=5)
        
        # Wordlist attack button
        self.wordlist_attack_btn = tk.Button(right_frame, text="⚡ START WORDLIST ATTACK", 
                                           command=self.start_wordlist_attack,
                                           bg="#9b59b6", fg="white",
                                           font=("Arial", 11, "bold"),
                                           state="disabled")
        self.wordlist_attack_btn.pack(pady=10, fill=tk.X)
        
        # Wordlist progress
        self.wordlist_progress = ttk.Progressbar(right_frame, mode='indeterminate')
        self.wordlist_progress.pack(pady=5, fill=tk.X)
        
        # Wordlist results
        tk.Label(right_frame, text="Wordlist Attack Results:", 
                font=("Arial", 11, "bold")).pack(anchor='w', pady=(10,0))
        
        wordlist_results_frame = tk.Frame(right_frame)
        wordlist_results_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.wordlist_results_text = tk.Text(wordlist_results_frame, height=8, font=("Consolas", 9))
        wordlist_scrollbar = tk.Scrollbar(wordlist_results_frame, command=self.wordlist_results_text.yview)
        self.wordlist_results_text.config(yscrollcommand=wordlist_scrollbar.set)
        
        self.wordlist_results_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        wordlist_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Bind entry changes
        self.hash_entry.bind("<KeyRelease>", self.on_hash_change)
    
    def smart_detect(self):
        """Improved smart detection with better algorithm distinction"""
        hash_text = self.hash_entry.get().strip()
        
        if not hash_text:
            self.detection_text.delete(1.0, tk.END)
            self.detection_text.insert(1.0, "Enter a hash first!")
            return
        
        # Clean hash
        if ':' in hash_text:
            hash_text = hash_text.split(':')[0]
        
        hash_text = hash_text.lower().strip()
        hash_len = len(hash_text)
        
        # Clear detection text
        self.detection_text.delete(1.0, tk.END)
        
        detection_report = f"Hash: {hash_text}\n"
        detection_report += f"Length: {hash_len} characters\n\n"
        
        # Check if valid hex
        if not re.match(r'^[a-f0-9]+$', hash_text):
            detection_report += "❌ Not a valid hexadecimal hash\n"
            self.detection_text.insert(1.0, detection_report)
            return
        
        # Find all algorithms with matching length
        possible_algorithms = []
        for algo, info in self.algorithms.items():
            if hash_len == info["length"]:
                possible_algorithms.append(algo)
        
        if not possible_algorithms:
            detection_report += f"❌ No algorithm found for {hash_len}-char hash\n"
            self.detection_text.insert(1.0, detection_report)
            return
        
        detection_report += f"Possible algorithms: {', '.join(possible_algorithms)}\n\n"
        
        # For 32-character hashes (MD5 vs NTLM)
        if hash_len == 32:
            detection_report += "🔍 32-char hash analysis (MD5 vs NTLM):\n"
            
            # Check for known NTLM hashes
            known_ntlm_hashes = [
                "aad3b435b51404eeaad3b435b51404ee",  # empty password
                "31d6cfe0d16ae931b73c59d7e0c089c0",  # empty password LM
                "8846f7eaee8fb117ad06bdd830b7586c",  # password
                "32ed87bdb5fdc5e9cba88547376818d4",  # 123456
            ]
            
            # Check for known MD5 hashes
            known_md5_hashes = [
                "5f4dcc3b5aa765d61d8327deb882cf99",  # password
                "e10adc3949ba59abbe56e057f20f883e",  # 123456
                "d8578edf8458ce06fbc5bb76a58c5ca4",  # qwerty
            ]
            
            if hash_text in known_ntlm_hashes:
                detection_report += "  • Known NTLM hash → Likely NTLM\n"
                possible_algorithms = ["ntlm", "md5"]
            elif hash_text in known_md5_hashes:
                detection_report += "  • Known MD5 hash → Likely MD5\n"
                possible_algorithms = ["md5", "ntlm"]
            else:
                detection_report += "  • Unknown hash → Default to MD5 (more common)\n"
                possible_algorithms = ["md5", "ntlm"]
        
        # For 64-character hashes (SHA256 vs SHA3-256)
        elif hash_len == 64:
            detection_report += "🔍 64-char hash analysis (SHA256 vs SHA3-256):\n"
            
            # Check for known SHA256 hashes
            known_sha256_hashes = [
                "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # password
                "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92",  # 123456
                "65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5",  # qwerty
            ]
            
            if hash_text in known_sha256_hashes:
                detection_report += "  • Known SHA256 hash → Likely SHA256\n"
                possible_algorithms = ["sha256", "sha3_256"]
            else:
                detection_report += "  • Unknown hash → Default to SHA256 (more common)\n"
                possible_algorithms = ["sha256", "sha3_256"]
        
        # Recommend best algorithm
        if possible_algorithms:
            recommended = possible_algorithms[0]
            detection_report += f"\n🎯 Recommended algorithm: {recommended.upper()}\n"
            
            # Check if rainbow tables exist for recommended algorithm
            rainbow_exists = os.path.exists(self.algorithms[recommended]["rainbow"])
            large_exists = os.path.exists(self.algorithms[recommended]["large"])
            
            detection_report += f"Rainbow tables: {'Available' if rainbow_exists else 'Not found'}\n"
            detection_report += f"Large tables: {'Available' if large_exists else 'Not found'}\n"
            
            self.current_algo = recommended
            self.rainbow_status.config(text=f"Detected: {recommended.upper()}", fg="green")
            
            # Also update wordlist algorithm to match
            self.wordlist_algo.set(recommended)
        else:
            detection_report += "\n⚠️ Cannot determine algorithm with confidence\n"
            self.rainbow_status.config(text="Detection uncertain", fg="orange")
        
        self.detection_text.insert(1.0, detection_report)
    
    def on_hash_change(self, event=None):
        """Update detection when hash changes"""
        hash_text = self.hash_entry.get().strip()
        if hash_text and len(hash_text) > 10:
            self.smart_detect()
    
    def use_manual(self):
        """Use manually selected algorithm"""
        self.current_algo = self.manual_algo.get()
        self.rainbow_status.config(text=f"Manual: {self.current_algo.upper()}", fg="orange")
        
        # Update detection text
        self.detection_text.delete(1.0, tk.END)
        self.detection_text.insert(1.0, f"Manual override active\nAlgorithm: {self.current_algo.upper()}")
    
    def load_table(self, table_type):
        """Load a table"""
        if not hasattr(self, 'current_algo') or not self.current_algo:
            messagebox.showwarning("Warning", "Detect algorithm first or select manually!")
            return
        
        table_path = self.algorithms[self.current_algo][table_type]
        
        if not os.path.exists(table_path):
            messagebox.showerror("Error", f"Table not found:\n{table_path}")
            return
        
        self.rainbow_status.config(text=f"Loading {table_type} {self.current_algo.upper()} table...", fg="blue")
        self.rainbow_crack_btn.config(state="disabled")
        
        thread = threading.Thread(target=self._load_table_thread, 
                                 args=(table_path, table_type))
        thread.daemon = True
        thread.start()
    
    def _load_table_thread(self, table_path, table_type):
        """Thread to load table"""
        try:
            table = {}
            count = 0
            
            with open(table_path, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    line = line.strip()
                    if ':' in line:
                        parts = line.split(':', 1)
                        if len(parts) == 2:
                            hash_val, password = parts
                            table[hash_val.strip()] = password.strip()
                            count += 1
            
            key = f"{self.current_algo}_{table_type}"
            if not hasattr(self, 'loaded_tables'):
                self.loaded_tables = {}
            self.loaded_tables[key] = table
            
            self.root.after(0, self.rainbow_status.config, 
                          {"text": f"Loaded {count:,} entries from {table_type} table", "fg": "green"})
            self.root.after(0, self.rainbow_crack_btn.config, {"state": "normal"})
            
        except Exception as e:
            self.root.after(0, self.rainbow_status.config, 
                          {"text": f"Error: {str(e)}", "fg": "red"})
            self.root.after(0, self.rainbow_crack_btn.config, {"state": "disabled"})
    
    def crack_with_auto_detect(self):
        """Crack with smart detection"""
        if not hasattr(self, 'loaded_tables') or not self.loaded_tables:
            messagebox.showwarning("Warning", "Load a table first!")
            return
        
        hash_text = self.hash_entry.get().strip()
        if not hash_text:
            messagebox.showwarning("Warning", "Enter a hash to crack!")
            return
        
        # Clean hash
        if ':' in hash_text:
            hash_text = hash_text.split(':')[0]
        
        target_hash = hash_text.strip().lower()
        
        # Try all loaded tables for the current algorithm
        cracked = False
        password = None
        table_used = None
        
        start_time = time.time()
        
        for table_key in self.loaded_tables:
            if self.current_algo in table_key:
                if target_hash in self.loaded_tables[table_key]:
                    password = self.loaded_tables[table_key][target_hash]
                    table_used = table_key.split('_')[-1]  # Get 'rainbow' or 'large'
                    cracked = True
                    break
        
        elapsed = time.time() - start_time
        
        # Show results
        self.rainbow_results_text.delete(1.0, tk.END)
        
        if cracked:
            result = f"✅ RAINBOW TABLE CRACKED!\n"
            result += f"Algorithm: {self.current_algo.upper()}\n"
            result += f"Hash: {target_hash}\n"
            result += f"Password: {password}\n"
            result += f"Table: {table_used}\n"
            result += f"Time: {elapsed:.6f} seconds\n"
            self.rainbow_status.config(text="Hash cracked successfully!", fg="green")
        else:
            result = f"❌ NOT FOUND IN RAINBOW TABLES\n"
            result += f"Algorithm: {self.current_algo.upper()}\n"
            result += f"Hash: {target_hash}\n"
            result += f"Tables checked: {', '.join(self.loaded_tables.keys())}\n"
            result += f"Time: {elapsed:.6f} seconds\n"
            result += f"\n💡 Try:\n"
            result += f"1. Load the other table type (rainbow/large)\n"
            result += f"2. Try different algorithm\n"
            result += f"3. Try Wordlist Attack (right panel)\n"
            result += f"4. Verify the hash is correct\n"
            self.rainbow_status.config(text="Hash not found in tables", fg="orange")
        
        self.rainbow_results_text.insert(1.0, result)
    
    def load_wordlist(self):
        """Load a custom wordlist"""
        file_path = filedialog.askopenfilename(
            title="Select Wordlist",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if file_path:
            self.wordlist_path = file_path
            self.wordlist_loaded = True
            self.wordlist_status.config(text=f"Loaded: {os.path.basename(file_path)}", fg="green")
            self.wordlist_attack_btn.config(state="normal")
    
    def load_default_wordlist(self):
        """Load clean_rockyou.txt wordlist"""
        default_path = "clean_rockyou.txt"
        
        if not os.path.exists(default_path):
            # Try to find it in common locations
            possible_paths = [
                "clean_rockyou.txt",
                "./clean_rockyou.txt",
                "wordlists/clean_rockyou.txt",
                "../clean_rockyou.txt",
                "rockyou.txt",
                "wordlists/rockyou.txt"
            ]
            
            for path in possible_paths:
                if os.path.exists(path):
                    default_path = path
                    break
            
            if not os.path.exists(default_path):
                messagebox.showwarning("Warning", 
                    "clean_rockyou.txt not found in default locations.\nPlease load it manually.")
                return
        
        self.wordlist_path = default_path
        self.wordlist_loaded = True
        file_name = os.path.basename(default_path)
        
        # Count lines in wordlist
        try:
            with open(default_path, 'r', encoding='utf-8', errors='ignore') as f:
                line_count = sum(1 for _ in f)
            self.wordlist_status.config(text=f"Loaded: {file_name} ({line_count:,} words)", fg="green")
        except Exception as e:
            self.wordlist_status.config(text=f"Loaded: {file_name} (error counting)", fg="green")
        
        self.wordlist_attack_btn.config(state="normal")
    
    def start_wordlist_attack(self):
        """Start wordlist attack"""
        if not self.wordlist_loaded or not self.wordlist_path:
            messagebox.showwarning("Warning", "Load a wordlist first!")
            return
        
        hash_text = self.hash_entry.get().strip()
        if not hash_text:
            messagebox.showwarning("Warning", "Enter a hash to crack!")
            return
        
        # Clean hash
        if ':' in hash_text:
            hash_text = hash_text.split(':')[0]
        
        target_hash = hash_text.strip().lower()
        algorithm = self.wordlist_algo.get()
        
        # Validate hash length for selected algorithm
        expected_length = self.algorithms[algorithm]["length"]
        if len(target_hash) != expected_length:
            messagebox.showwarning("Warning", 
                f"Hash length ({len(target_hash)}) doesn't match {algorithm.upper()} "
                f"({expected_length} chars)\n"
                f"Expected {expected_length} characters, got {len(target_hash)}")
            return
        
        # Clear previous results
        self.wordlist_results_text.delete(1.0, tk.END)
        self.wordlist_results_text.insert(1.0, f"Starting wordlist attack with {algorithm.upper()}...\n"
                                              f"Target hash: {target_hash}\n"
                                              f"Wordlist: {os.path.basename(self.wordlist_path)}\n"
                                              f"{'='*50}\n")
        
        # Disable button and start progress
        self.wordlist_attack_btn.config(state="disabled")
        self.wordlist_progress.start()
        
        # Start attack in thread
        thread = threading.Thread(target=self._wordlist_attack_thread,
                                 args=(target_hash, algorithm))
        thread.daemon = True
        thread.start()
    
    def _wordlist_attack_thread(self, target_hash, algorithm):
        """Thread for wordlist attack"""
        try:
            start_time = time.time()
            cracked = False
            password = None
            attempts = 0
            last_update = start_time
            
            # Hash function mapping
            def get_hash_func(algo):
                if algo == "ntlm":
                    return lambda x: hashlib.new('md4', x.encode('utf-16le')).hexdigest()
                elif algo == "md5":
                    return lambda x: hashlib.md5(x.encode()).hexdigest()
                elif algo == "sha1":
                    return lambda x: hashlib.sha1(x.encode()).hexdigest()
                elif algo == "sha224":
                    return lambda x: hashlib.sha224(x.encode()).hexdigest()
                elif algo == "sha256":
                    return lambda x: hashlib.sha256(x.encode()).hexdigest()
                elif algo == "sha3_256":
                    return lambda x: hashlib.sha3_256(x.encode()).hexdigest()
                else:
                    return lambda x: hashlib.md5(x.encode()).hexdigest()
            
            hash_func = get_hash_func(algorithm)
            
            with open(self.wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    attempts += 1
                    word = line.strip()
                    
                    # Skip empty lines
                    if not word:
                        continue
                    
                    # Calculate hash
                    hash_result = hash_func(word)
                    
                    # Check if match
                    if hash_result == target_hash:
                        password = word
                        cracked = True
                        break
                    
                    # Update progress every 1000 attempts or 1 second
                    current_time = time.time()
                    if attempts % 1000 == 0 or current_time - last_update > 1:
                        self.root.after(0, self._update_wordlist_progress, attempts, current_time - start_time)
                        last_update = current_time
            
            elapsed = time.time() - start_time
            
            # Update UI
            self.root.after(0, self._update_wordlist_results, 
                          cracked, password, target_hash, algorithm, attempts, elapsed)
            
        except Exception as e:
            self.root.after(0, self._wordlist_error, str(e))
        finally:
            self.root.after(0, self.wordlist_progress.stop)
            self.root.after(0, self.wordlist_attack_btn.config, {"state": "normal"})
    
    def _update_wordlist_progress(self, attempts, elapsed):
        """Update wordlist attack progress"""
        if elapsed > 0:
            speed = attempts / elapsed
            status = f"Trying: {attempts:,} | Speed: {speed:.0f} hashes/sec"
            self.wordlist_status.config(text=status, fg="blue")
    
    def _update_wordlist_results(self, cracked, password, target_hash, algorithm, attempts, elapsed):
        """Update wordlist attack results"""
        self.wordlist_results_text.delete(1.0, tk.END)
        
        if cracked:
            result = f"✅ WORDLIST ATTACK SUCCESS!\n"
            result += f"{'='*50}\n"
            result += f"Algorithm: {algorithm.upper()}\n"
            result += f"Target hash: {target_hash}\n"
            result += f"Password found: {password}\n"
            result += f"Attempts: {attempts:,}\n"
            result += f"Time elapsed: {elapsed:.2f} seconds\n"
            if elapsed > 0:
                result += f"Speed: {attempts/elapsed:.0f} hashes/sec\n"
            result += f"\n💡 The password was found in the wordlist!\n"
            self.wordlist_status.config(text="✓ Password found!", fg="green")
        else:
            result = f"❌ PASSWORD NOT FOUND\n"
            result += f"{'='*50}\n"
            result += f"Algorithm: {algorithm.upper()}\n"
            result += f"Target hash: {target_hash}\n"
            result += f"Wordlist: {os.path.basename(self.wordlist_path)}\n"
            result += f"Attempts: {attempts:,}\n"
            result += f"Time elapsed: {elapsed:.2f} seconds\n"
            if elapsed > 0:
                result += f"Speed: {attempts/elapsed:.0f} hashes/sec\n"
            result += f"\n💡 Suggestions:\n"
            result += f"1. Try different algorithm\n"
            result += f"2. Use larger wordlist\n"
            result += f"3. Try Rainbow Table Attack (left panel)\n"
            result += f"4. Word may not be in wordlist\n"
            self.wordlist_status.config(text="Password not found", fg="orange")
        
        self.wordlist_results_text.insert(1.0, result)
    def _wordlist_error(self, error_msg):
        """Handle wordlist attack error"""
        self.wordlist_results_text.delete(1.0, tk.END)
        self.wordlist_results_text.insert(1.0, f"❌ ERROR:\n{error_msg}")
        self.wordlist_status.config(text="Error in attack", fg="red")
def main():
    root = tk.Tk()
    app = ImprovedAutoDetectCracker(root)
    
    # Center window
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    root.mainloop()

if __name__ == "__main__":
    main()        
