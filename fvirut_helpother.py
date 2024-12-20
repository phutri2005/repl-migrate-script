import random
import threading
import requests
import json


# Function to generate a random IP address
def generate_random_ip():
    """Generate a random IP address."""
    return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"


# Function to send a POST request
def send_post_request(url):
    """Send POST requests with random IP addresses in an infinite loop."""
    while True:  # Infinite loop
        # Generate a random IP
        random_ip = generate_random_ip()

        # Create the JSON payload
        payload = {"ip": random_ip}

        try:
            # Send the POST request using the requests library
            response = requests.post(url, json=payload,
                                     timeout=5)  # Add timeout for stability
            if response.status_code == 200:
                print(f"Request sent successfully with IP: {random_ip}")
            else:
                print(
                    f"Request failed with status code {response.status_code} and IP: {random_ip}"
                )
        except requests.RequestException as e:
            print(f"Error sending request with IP {random_ip}: {e}")


# Main function to start multithreaded requests
def main():
    # Target URL
    url = "https://saaadnesss.shop/run"

    # Number of threads
    num_threads = 10

    # Create and start threads
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=send_post_request, args=(url, ))
        thread.daemon = True  # Set threads as daemon so they terminate with the program
        threads.append(thread)
        thread.start()

    # Keep the main thread running
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
