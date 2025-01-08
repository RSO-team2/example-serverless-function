import requests
import json
import sys

def main(args):
    # Extract the IP address from the request
    #print(arg1)
    ip_address = args.get("ip", "8.8.8.8")  # Default to a public IP for testing

    # Call an external geolocation API (ip-api in this case)
    geo_url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(geo_url)
    
    if response.status_code == 200:
        geo_data = response.json()
        #print(geo_data)
        # Return the geolocation data
        return {
            "statusCode": 200,
            "body": json.dumps({
                "ip": geo_data.get("query", ip_address),
                "country": geo_data.get("country", "Unknown"),
                "region": geo_data.get("regionName", "Unknown"),
                "city": geo_data.get("city", "Unknown"),
                "latitude": geo_data.get("lat", "Unknown"),
                "longitude": geo_data.get("lon", "Unknown"),
                "isp": geo_data.get("isp", "Unknown"),
            })
        }
    else:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Failed to fetch geolocation data"})
        }

