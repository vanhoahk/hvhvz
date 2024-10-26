import requests
from byte import *
from accountmangment import *

successful_count = 0  # Initialize a counter for successful responses

def like(token, id):
    global successful_count  # Ensure the function can modify the global counter
    url = 'https://202.81.99.18/LikeProfile'
    headers = {
        'X-Unity-Version': '2018.4.11f1',
        'ReleaseVersion': 'OB46',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-GA': 'v1 1',
        'Authorization': f'Bearer {token}',
        'Content-Length': '16',
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; ASUS_Z01QD Build/QKQ1.190825.002)',
        'Host': 'clientbp.ggblueshark.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip'
    }
    data = bytes.fromhex(encrypt_api(f'08{Encrypt_ID(id)}12024d45'))
    
    response = requests.post(url, headers=headers, data=data, verify=False)  # verify=False to ignore SSL certificate warnings
    
    print(response.status_code)
    print(response.text)
    
    if response.status_code == 200:
        successful_count += 1  # Increment the counter if the request is successful
    
    return response.status_code
