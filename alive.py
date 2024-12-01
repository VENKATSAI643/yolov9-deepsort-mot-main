import time
import requests
import logging

# Configure logging
logging.basicConfig(filename='keep_alive.log', level=logging.INFO, 
                    format='%(asctime)s %(levelname)s:%(message)s')

def keep_alive(url):
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                logging.info("Server is alive")
            else:
                logging.warning(f"Server responded with status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to reach server: {e}")
        time.sleep(30)  # Send a request every 30 seconds

if __name__ == "__main__":
    # Replace 'http://localhost:5000' with your local server's URL
    keep_alive("https://p3r1pgh8-5000.inc1.devtunnels.ms")
    keep_alive("https://p3r1pgh8-5000.inc1.devtunnels.ms/upload")

