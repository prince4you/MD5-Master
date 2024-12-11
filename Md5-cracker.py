import hashlib
import subprocess
import sys
import socket
from termcolor import colored
import time
import os

# Clear the terminal screen for Termux
os.system('clear')
# Function to check internet connection
def check_internet():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return True
    except OSError:
        return False

# Function to install required modules if not already installed
def install_module(module_name):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
        print(colored(f"{module_name} installed successfully.", "green"))
    except subprocess.CalledProcessError:
        print(colored(f"Error: {module_name} installation failed. Please check your internet connection.", "red"))
        sys.exit(1)

# Function to ensure pyfiglet is installed
def install_pyfiglet():
    try:
        import pyfiglet
    except ImportError:
        if check_internet():  # Check if there's an internet connection
            print(colored("pyfiglet not found. Installing...", "yellow"))
            install_module("pyfiglet")
        else:
            print(colored("No internet connection. Please connect to the internet to install pyfiglet.", "red"))
            sys.exit(1)

# Function to ensure termcolor is installed
def install_termcolor():
    try:
        import termcolor
    except ImportError:
        if check_internet():  # Check if there's an internet connection
            print(colored("termcolor not found. Installing...", "yellow"))
            install_module("termcolor")
        else:
            print(colored("No internet connection. Please connect to the internet to install termcolor.", "red"))
            sys.exit(3)

# Banner using pyfiglet
def banner():
    try:
        import pyfiglet
        ascii_banner = pyfiglet.figlet_format("HashHunter", font="slant")  # Custom banner name
        print(colored(ascii_banner, "cyan"))
        print(colored("Created by: Sunil", "green"))
        print(colored("MD5 Hash Cracking Tool - Noob Cyber Tech", "yellow"))
        print(colored("*" * 50, "magenta"))
    except ImportError:
        print(colored("Error: pyfiglet module not found. Please install it.", "red"))

# Function to crack the MD5 hash
def crack_md5_hash():
    print(colored("Welcome to the MD5 Hash Cracker!", "cyan"))
    target_hash = input(colored("Enter the MD5 hash to crack: ", "green"))
    
    wordlist_file = input(colored("Enter the path to the wordlist file: ", "green"))
    if not os.path.exists(wordlist_file):
        print(colored("❌ Wordlist file does not exist! Please check the file path.", "red"))
        return

    # Start cracking
    print(colored("\nStarting the cracking process. This may take a while...\n", "yellow"))
    print(colored("Scanning wordlist...", "blue"))
    
    # Open the wordlist file
    with open(wordlist_file, "r") as file:
        total_words = sum(1 for line in file)  # Count total words
    print(colored(f"Total words in wordlist: {total_words}", "blue"))
    
    # Start cracking and showing progress
    with open(wordlist_file, "r") as file:
        attempts = 0
        for word in file:
            word = word.strip()  # Remove any extra spaces or newlines
            generated_hash = hashlib.md5(word.encode()).hexdigest()

            # Show progress
            attempts += 1
            print(f"\r{colored(f'Trying password {attempts}/{total_words}: {word}', 'yellow')}", end="")
            
            if generated_hash == target_hash:
                print(colored(f"\n✅ Password found: {word}", "green"))
                return
            time.sleep(0.05)  # Sleep for a short time to simulate cracking process

    print(colored("❌ Password not found in the wordlist.", "red"))

if __name__ == "__main__":
    install_pyfiglet()  # Ensure pyfiglet is installed
    install_termcolor()  # Ensure termcolor is installed
    banner()  # Display the stylish banner
    crack_md5_hash()
