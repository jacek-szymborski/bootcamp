import json
import urllib.request

def get_location_id(location_name):
    url =f"https://www.metaweather.com/api/location/search/?query={location_name}"
    with urllib.request.urlopen(url) as f:
        results = json.loads(f.read)

if __name__ == "__main__":
    location_id = get_location_id(sys.argv[1])
    print(location_id)