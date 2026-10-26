import hashlib
import os
import argparse
import sys
import re

arte_ascii = f"""\n        
        Brute force 
     ⢀⣠⣤⣶⣶⣿⣿⣿⣶⣶⣤⡀
⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀
⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀
⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀
⠀⠀⢸⣿⣿⣿⣿⣿⡏⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
⠀⠀⠘⣿⣿⣟⡿⢿⣷⢸⠞⠛⢽⣾⣛⡟⣿⣿⣿⠁⠀⠀
⠀⠀⠀⠻⣿⡟⢶⡿⡿⠀⠀⠀⠀⠹⠯⠏⢸⣿⣿⠀⠀
⠀⠀⠀⠀⠛⣾⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡏⠀⠀
⠀⠀⠀⠀⠀⣿⣿⣄⠀⠀⠈⠍⠀⠀⢀⣼⣿⣿⡇⠀⠀
⠀⠀⠀⠀⠀⠈⠀⠘⢉⠖⠠⠤⠤⠀⠈⡌⣿⡏⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡠⠔⠊⠀⠀⠀⠀⠀⠀⠈⣿⡀⠀⠀⠀
⠀⡠⠂⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠈⠁⠂⢄
⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀ ⠈ 
            By Sanosec"""


class clr:
    BLACK   = '\033[30m'
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    BLUE    = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN    = '\033[36m'
    WHITE   = '\033[37m'
    RESET   = '\033[0;0;0m'
    BOLD    = '\033[1m'


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=f"{clr.RED}Brute force :P{clr.RESET}"
    )
    parser.add_argument('-w','--wordlist', dest='wordlist',
                        help='Target the location of wordlist')
    parser.add_argument('-s','--hash', dest='hash',
                        help='Hash you want discover')
    parser.add_argument('-d','--detect', dest='detec', action='store_true',
                        help='Discovery the hash type')
    parser.add_argument('-t','--type', dest='tipo',
                        help='Type of hash you want bruteforce (optional)')
    return parser.parse_args()


class bruteforce:
    def __init__(
            self,
            wordlist: str,
            hashs: str,
            detec: bool,
            tipo: str,
    ):
        self.wordlist = wordlist
        self.hashs = hashs
        self.detec = detec
        self.tipo = tipo

    def detect(self):
        if not self.hashs:
            print(f"{clr.RED}[-] You need write the hash with -s/--hash to detect.{clr.RESET}")
            return
            
        hash_limpa = self.hashs.strip()
        if not re.fullmatch(r'^[a-fA-F0-9]+$', hash_limpa):
            print(f"{clr.RED}[-] Invalid format{clr.RESET}")
            return
            
        tamanho = len(hash_limpa)
        algoritm = {
            32: "MD5",
            40: "SHA-1",
            56: "SHA-224",
            64: "SHA-256",
            96: "SHA-384",
            128: "SHA-512",
        }

        tipo_encontrado = algoritm.get(tamanho, f"Unknown format ({tamanho})")
        print(f"{clr.GREEN}[+] Tipo de hash detectado: {tipo_encontrado}{clr.RESET}")

    def bruteforce(self):
        if not self.hashs:
            print(f"{clr.RED}[-] Você precisa fornecer uma hash usando -s/--hash.{clr.RESET}")
            return

        if not self.wordlist:
            print(f"{clr.RED}[-] Você precisa fornecer uma wordlist usando -w/--wordlist para fazer o brute force.{clr.RESET}")
            return

        hashs_clean = self.hashs.strip()
        if not re.fullmatch(r'^[a-fA-F0-9]+$', hashs_clean):
            print(f"{clr.RED}[-] Invalid format{clr.RESET}")
            return

        tamanho = len(hashs_clean)
         
        algoritm = {
            32: ("MD5", hashlib.md5),
            40: ("SHA-1", hashlib.sha1),
            56: ("SHA-224", hashlib.sha224),
            64: ("SHA-256", hashlib.sha256),
            96: ("SHA-384", hashlib.sha384),
            128: ("SHA-512", hashlib.sha512),
        }

        hash_info = algoritm.get(tamanho)
        if not hash_info:
            print(f"{clr.RED}[-] Invalid hash size ({tamanho} characters){clr.RESET}")
            return

        nome_algoritmo, function_hash = hash_info
        print(f"{clr.CYAN}[+] Algoritmo identificado automaticamente: {nome_algoritmo}{clr.RESET}")
        print(f"{clr.GREEN}[+] Starting brute force using {self.wordlist}...{clr.RESET}")

        try:
            with open(self.wordlist, "r", encoding='utf-8', errors='ignore') as arquivo:
                encontrado = False

                for linha in arquivo:
                    palavra = linha.strip()
                    palavra_bytes = palavra.encode('utf-8')
                    
                    
                    if function_hash(palavra_bytes).hexdigest() == hashs_clean:
                        print(f"\n{clr.GREEN}[✔] Found password ({nome_algoritmo}): {palavra}{clr.RESET}")
                        encontrado = True
                        break

                if not encontrado:
                    print(f"{clr.YELLOW}[-] Password not found in the wordlist.{clr.RESET}")

        except FileNotFoundError:
            print(f"{clr.RED}[-] Can't reach the wordlist file: {self.wordlist}{clr.RESET}")


if __name__ == "__main__":
    print(arte_ascii)
    args = parse_args()
    
    cracker = bruteforce(wordlist=args.wordlist, hashs=args.hash, detec=args.detec, tipo=args.tipo)
    
    if args.detec:
        cracker.detect()
        sys.exit(0)

    cracker.bruteforce()
