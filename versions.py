import requests
import json

url = "https://central-server.kelvininc.com/platformurls"

response = requests.get(url)
urls = json.loads(response.text)

for key, value in urls.items():
    metadata_url = f"https://{value}/metadata"
    try:
        response = requests.get(metadata_url)
        response.raise_for_status()
        metadata = json.loads(response.text)
        versions = metadata.get("versions", {})
        print(f"==== Versions for {key} ====")
        for version_key, version_value in versions.items():
            print(f"{version_key}: {version_value}")
    except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
        print(f"Error retrieving metadata for {key}: {e}")
