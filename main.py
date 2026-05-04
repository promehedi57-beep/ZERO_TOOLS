import base64, zlib, marshal, os, sys, time
from datetime import datetime

# Color Codes
R = '\033[1;31m' # Red
G = '\033[1;32m' # Green
Y = '\033[1;33m' # Yellow
C = '\033[1;36m' # Cyan
W = '\033[1;37m' # White
B = '\033[1;34m' # Blue

def clear():
    os.system('clear')

def type_text(text, speed=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def startup_loading():
    clear()
    print(f"\n{C} [*] Initializing ZERO System...")
    time.sleep(0.5)
    
    # Smooth Progress Bar
    bar_length = 40
    for i in range(bar_length + 1):
        percent = int((i / bar_length) * 100)
        bar = '█' * i + '-' * (bar_length - i)
        sys.stdout.write(f'\r{Y} [>] Booting: [{G}{bar}{Y}] {percent}%')
        sys.stdout.flush()
        time.sleep(0.04) # Speed of loading
        
    print(f"\n{G} [√] System Booted Successfully!\n")
    time.sleep(0.5)

def process_spinner(text):
    spinner = ['|', '/', '-', '\\']
    for i in range(15):
        sys.stdout.write(f'\r{C} [*] {text} {Y}{spinner[i % len(spinner)]}')
        sys.stdout.flush()
        time.sleep(0.1)
    print(f'\r{G} [√] {text} Done!        ')

def banner():
    clear()
    print(f"""
{C}  ███████╗███████╗██████╗  ██████╗ 
{C}  ╚══███╔╝██╔════╝██╔══██╗██╔═══██╗
{C}    ███╔╝ █████╗  ██████╔╝██║   ██║
{C}   ███╔╝  ██╔══╝  ██╔══██╗██║   ██║
{C}  ███████╗███████╗██║  ██║╚██████╔╝
{C}  ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ 
{Y}     Professional Code Obfuscator {W}|{G} v3.0
{W}  -----------------------------------------------
{B}  Developer  : {W}ZERO
{B}  Owner      : {W}Mehedi
{B}  Storage    : {W}Internal Storage (MT Manager)
{W}  -----------------------------------------------
    """)

def obfuscate():
    startup_loading()
    banner()
    
    # Input File
    file_path = input(f"{Y} [+] Enter your python file name (e.g., bot.py): {W}")
    
    if not os.path.isfile(file_path):
        print(f"\n{R} [!] Error: File '{file_path}' not found in current directory!")
        sys.exit()

    # Define Output Directory (Accessible by MT Manager)
    # Checks if Termux sdcard is available, otherwise uses current dir
    if os.path.exists('/sdcard'):
        output_folder = "/sdcard/ZERO_PROJECTS"
    else:
        output_folder = "ZERO_PROJECTS"
        
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    output_filename = f"enc_{file_path}"
    full_output_path = os.path.join(output_folder, output_filename)

    print()
    process_spinner("Compiling & Encrypting Code...")

    try:
        # Read Original Code
        with open(file_path, 'r') as f:
            source = f.read()

        # Obfuscation Logic (Marshal -> Zlib -> Base64)
        compiled_code = compile(source, '', 'exec')
        marshaled = marshal.dumps(compiled_code)
        compressed = zlib.compress(marshaled)
        encoded = base64.b64encode(compressed)

        # Write to Output File with Professional Header
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(full_output_path, 'w') as f:
            f.write(f"# ------------------------------------------\n")
            f.write(f"# Encrypted By : ZERO OBFUSCATOR v3.0\n")
            f.write(f"# Developer    : ZERO\n")
            f.write(f"# Owner        : Mehedi\n")
            f.write(f"# Enc Date     : {now}\n")
            f.write(f"# Warning      : Do not try to decode.\n")
            f.write(f"# ------------------------------------------\n")
            f.write(f"import base64, zlib, marshal\n")
            f.write(f"exec(marshal.loads(zlib.decompress(base64.b64decode({encoded}))))")

        print(f"\n{G} [√] Code Obfuscated Successfully!")
        print(f"{W} -----------------------------------------------")
        print(f"{Y} Output File : {G}{output_filename}")
        print(f"{Y} Location    : {C}{full_output_path}")
        print(f"{W} -----------------------------------------------")
        type_text(f"{C} [>] Open MT Manager. You will find a folder named 'ZERO_PROJECTS'.")
        type_text(f"{C} [>] Your file is ready to be copied to your VPS!")

    except Exception as e:
        print(f"\n{R} [!] An unexpected error occurred: {e}")

if __name__ == "__main__":
    try:
        obfuscate()
    except KeyboardInterrupt:
        print(f"\n{R} [!] Process cancelled by user.")
        sys.exit()
