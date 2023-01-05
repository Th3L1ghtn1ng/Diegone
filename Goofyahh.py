import argparse
import requests
import sys

print("Welcome to Goofyahh!")
print("usage: Goofyahh!.py [-h] --url URL")
print("Please choose an option:")
print("[1] start a simple XSS tester")
print("[2] start a simple SQLi tester")
print("[2] ????????")
goofyahh = """


    ___    __    __         ______                   
   /   |  / /_  / /_  ____ /_  __/__  ____ _____ ___ 
  / /| | / __ \/ __ \/ __ `// / / _ \/ __ `/ __ `__ \
 / ___ |/ /_/ / /_/ / /_/ // / /  __/ /_/ / / / / / /
/_/  |_/_.___/_.___/\__,_//_/  \___/\__,_/_/ /_/ /_/ 
                    
A simple SQLi tester                    
"""
scemochilegge = """

________  .__                                            
\______ \ |__| ____   ____   ____                        
 |    |  \|  |/ __ \ / ___\ /  _ \                       
 |    `   \  \  ___// /_/  >  <_> )                      
/_______  /__|\___  >___  / \____/                       
        \/        \/_____/                               
.____              _________                             
|    |    ____    /   _____/_  _  __ ____   ____   ____  
|    |   /  _ \   \_____  \\ \/ \/ // __ \ / ___\ /  _ \ 
|    |__(  <_> )  /        \\     /\  ___// /_/  >  <_> )
|_______ \____/  /_______  / \/\_/  \___  >___  / \____/ 
        \/               \/             \/_____/         
Gogogogogo
tocca testare se il sito è vulnerabile a XSstocazzo zio cane le cipollela merda rosa
"""
choice = input("Enter your choice =>   ")
if choice == "69":
     print("Gagsona?")
if choice == "3":
     print("Daje Romaa")
     print(" Daje Romaa")
     print("  Daje Romaa")
     print("   Daje Romaa")
     print("    Daje Romaa")
     print("     Daje Romaa")
else :
     print("Invalid choice. Please try again.")
if choice == "1":
     print (scemochilegge)
# imposta l'opzione --url per l'URL del sito da scansionare
parser = argparse.ArgumentParser()
parser.add_argument('--url', required=True, help='URL del sito da scansionare')
args = parser.parse_args()

# invia una richiesta GET al sito
response = requests.get(args.url)

# cerca stringhe di input nella risposta
if '<input' in response.text:
     print('Il sito potrebbe essere vulnerabile a XSS')
else:
     print('Il sito non sembra essere vulnerabile a XSS')
if choice == "2":
  print (goofyahh)
def scan(url):
  # create a list of payloads to try
  payloads = [
    "' OR 1=1--",
    "' OR '1'='1'--",
    "') OR ('1'='1--"
  ]

  # try each payload and check if the website is vulnerable
  for payload in payloads:
    try:
      r = requests.get(url + payload)
        print("[+] Vulnerable: " + url + payload)
    except:
      print("[-] Error occurred")

# main function
if __name__ == "__main__":
  if len(sys.argv) != 3:
    print("Usage: python sql_injection_scanner.py --url <url>")
    sys.exit()

  if sys.argv[1] == "--url":
    url = sys.argv[2]
    scan(url)
  else:
    print("Usage: python sql_injection_scanner.py --url <url>")
    sys.exit()
