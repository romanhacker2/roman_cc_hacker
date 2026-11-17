import os
import sys
import time
import random
import string

RESET="\033[0m"; BOLD="\033[1m"; GREEN="\033[92m"; RED="\033[91m"; YELLOW="\033[93m"; BLUE="\033[94m"; CYAN="\033[96m"; WHITE="\033[97m"; MAGENTA="\033[95m"

def clear(): os.system("clear")

def show_banner():
    print(f"""{CYAN}{BOLD}
    ██████╗  ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
    ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗████╗  ██║
    ██████╔╝██║   ██║██╔████╔██║███████║██╔██╗ ██║
    ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
    ██║  ██║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
    ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
    {RED}⠀⠀⠀⠀⠀⠀⠀⣠⣶⣶⣦⡀⠀
    {RED}⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    {RED}⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    {RED}⠀⠀⠀⠀⠀⠀⣴⣶⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    {RED}⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    {RED}⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣧
    {RED}⠀⠀⠀⠀⣼⣿⣿⣿⡿⣿⣿⣆⠀⠀⠀⠀⠀⠀⣠⣴⣶⣤⡀⠀
    {RED}⠀⠀⠀⢰⣿⣿⣿⣿⠃⠈⢻⣿⣦⠀⠀⠀⠀⣸⣿⣿⣿⣿⣷⠀
    {RED}⠀⠀⠀⠘⣿⣿⣿⡏⣴⣿⣷⣝⢿⣷⢀⠀⢀⣿⣿⣿⣿⡿⠋⠀
    {RED}⠀⠀⠀⠀⢿⣿⣿⡇⢻⣿⣿⣿⣷⣶⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀
    {RED}⠀⠀⠀⠀⢸⣿⣿⣇⢸⣿⣿⡟⠙⠛⠻⣿⣿⣿⣿⡇⠀⠀⠀⠀
    {RED}⣴⣿⣿⣿⣿⣿⣿⣿⣠⣿⣿⡇⠀⠀⠀⠉⠛⣽⣿⣇⣀⣀⣀⠀
    {RED}⠙⠻⠿⠿⠿⠿⠿⠟⠿⠿⠿⠇⠀⠀⠀⠀⠀⠻⠿⠿⠛⠛⠛{RESET}
    {MAGENTA}{BOLD}      [ R O M A N   C C   G E N E R A T O R ]{RESET}
    {YELLOW}══════════════════════════════════════════════════{RESET}
    {GREEN} DEV: {WHITE}ROMAN HACKER {GREEN}| TG: {WHITE}@romanempire078{RESET}
    {YELLOW}══════════════════════════════════════════════════{RESET}
    """)

# Fake Names and Banks Data
NAMES = ["John Doe", "Ali Khan", "Sarah Smith", "Muhammad Usman", "Emily Davis", "Hamza Ali", "David Miller", "Ayesha Malik", "Michael Brown", "Bilal Ahmed"]
BANKS = ["Chase Bank", "Bank of America", "HBL Pakistan", "Meezan Bank", "Wells Fargo", "UBL", "Standard Chartered", "Citibank"]
COUNTRIES = ["United States", "United Kingdom", "Pakistan", "UAE", "Canada", "Australia"]

def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10

def generate_cc(bin_prefix, length):
    card_number = bin_prefix + "".join([str(random.randint(0, 9)) for _ in range(length - len(bin_prefix) - 1)])
    for i in range(10):
        test_num = card_number + str(i)
        if luhn_checksum(test_num) == 0:
            return test_num
    return card_number + "0"

def dark_web_animation():
    print(f"{RED}{BOLD}  [!] INITIATING DARK WEB CONNECTION...{RESET}\n")
    time.sleep(1)
    
    logs = [
        f"[TOR] Connecting to onion router...",
        f"[TOR] Bypassing firewall...",
        f"[DB] Hitting BIN Database...",
        f"[DB] Extracting valid CC formats...",
        f"[SYS] Validating checksum algorithm...",
        f"[BANK] Fetching live balances..."
    ]
    
    for log in logs:
        print(f"\033[91m  {log}\033[0m")
        time.sleep(0.3)
        
    for i in range(1, 101):
        sys.stdout.write(f"\r{CYAN}{BOLD}  [>] Checking Validity: {i}%{RESET}")
        sys.stdout.flush()
        time.sleep(0.02)
    print("\n")

def main():
    while True:
        try:
            clear()
            show_banner()
            print(f"""{BLUE}{BOLD}
    ┌──────────────────────────────────────────────────┐
    │             SELECT CARD NETWORK                  │
    ├──────────────────────────────────────────────────┤
    │  {WHITE}[1]{GREEN} VISA (Starts with 4)                      │
    │  {WHITE}[2]{GREEN} MASTERCARD (Starts with 5)                │
    │  {WHITE}[3]{GREEN} AMEX (Starts with 3)                      │
    │  {WHITE}[4]{RED} Exit System                               │
    └──────────────────────────────────────────────────┘
{RESET}""")
            
            choice = input(f"{GREEN}{BOLD}  └──► Select Option [1-4]: {RESET}").strip()
            
            if choice in ["1", "2", "3"]:
                clear()
                show_banner()
                
                try:
                    amount = int(input(f"{WHITE}{BOLD}  [?] How many CC to generate? (e.g. 1, 5, 10): {RESET}").strip())
                    if amount <= 0: raise ValueError
                except:
                    print(f"{RED}  [!] Invalid amount!{RESET}")
                    time.sleep(2)
                    continue
                    
                dark_web_animation()
                
                clear()
                show_banner()
                print(f"{GREEN}{BOLD}  [✓] GENERATED {amount} CARDS WITH LIVE BALANCES{RESET}\n")
                
                for _ in range(amount):
                    # Generate Card Number
                    if choice == "1": 
                        cc = generate_cc("4", 16)
                        cvv = str(random.randint(100, 999))
                        card_type = "VISA"
                    elif choice == "2": 
                        cc = generate_cc("5" + str(random.randint(1,5)), 16)
                        cvv = str(random.randint(100, 999))
                        card_type = "MASTERCARD"
                    else: 
                        cc = generate_cc("3" + random.choice(["4", "7"]), 15)
                        cvv = str(random.randint(1000, 9999))
                        card_type = "AMEX"
                        
                    formatted_cc = " ".join([cc[i:i+4] for i in range(0, len(cc), 4)])
                    expiry = f"{random.randint(1,12):02d}/{random.randint(25,30)}"
                    
                    # Random Realistic Data
                    name = random.choice(NAMES)
                    bank = random.choice(BANKS)
                    country = random.choice(COUNTRIES)
                    balance = f"${random.uniform(5000, 75000):,.2f}" # USD Balance
                    
                    print(f"{CYAN}{BOLD}  ╔══════════════════════════════════════════════════╗")
                    print(f"  ║                 💳 {card_type:<11} CARD                ║")
                    print(f"  ╠══════════════════════════════════════════════════╣")
                    print(f"  ║  {YELLOW}NAME    : {WHITE}{name:<35} {CYAN}║")
                    print(f"  ║  {YELLOW}CARD NO : {GREEN}{formatted_cc:<35} {CYAN}║")
                    print(f"  ║  {YELLOW}EXPIRY  : {WHITE}{expiry:<7} | CVV : {cvv:<21} {CYAN}║")
                    print(f"  ║  {YELLOW}ISSUER  : {WHITE}{bank:<35} {CYAN}║")
                    print(f"  ║  {YELLOW}COUNTRY : {WHITE}{country:<35} {CYAN}║")
                    print(f"  ║  {YELLOW}BALANCE : {GREEN}{balance:<35} {CYAN}║")
                    print(f"  ╚══════════════════════════════════════════════════╝{RESET}\n")
                    
                    time.sleep(0.5)
                    
                print(f"\n{RED}{BOLD}  [✓] CARDS INJECTED. USE AT YOUR OWN RISK.{RESET}")
                
            elif choice == "4":
                break
            else:
                time.sleep(0.5)
                
            input(f"\n{CYAN}  Press ENTER to return to main menu...{RESET}")
            
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
