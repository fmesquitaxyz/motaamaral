import requests
from bs4 import BeautifulSoup
import os

def download_links(url, output_folder, cookies=None):
    # Send an HTTP request to the URL with cookies
    response = requests.get(url, cookies=cookies)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the links in the page
        links = soup.find_all('a', href=True)

        # Create the output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Download each link
        for link in links:
            href = link['href']
            # Construct the absolute URL if it's a relative URL
            absolute_url = href if 'http' in href else f"{url.rstrip('/')}/{href.lstrip('/')}"
            
            # Download the content of the link
            link_response = requests.get(absolute_url, cookies=cookies)
            
            # Get the filename from the URL
            filename = os.path.join(output_folder, os.path.basename(href))
            
            # Save the content to a file
            with open(filename, 'wb') as file:
                file.write(link_response.content)

            print(f"Downloaded: {absolute_url} => {filename}")

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}. {response.text}")



# Example usage:
subscription_cookies = {"cf_clearance": "JZw5cIE20tbzDciJ13LkgAPthVSWTdJgEXEgSxKue.A-1703607775-0-2-99c2b4c2.467ceb02.cec3eb22-0.2.1703607775",
                        "_rmMeToken_" : "YTozOntzOjU6InRva2VuIjtzOjM2OiI3Njc5NTc0Ni1jZDM0LTRmZDktOTc3My0zN2Y5YjgzZDI2NTgiO3M6ODoidXNlcm5hbWUiO3M6MTI6ImZtZ0BkdWNrLmNvbSI7czo4OiJzZXJpZXNJZCI7czozNjoiM2M2OTliNGUtN2FmMi00ZTc0LTg2OWUtN2M0MjVhYmRiYmQzIjt9",
                        "ACORIANO_SID" : "osnub40vcd9p0u5gbmet3q4na5"}  # Replace with your subscription 
url_to_download = "https://www.acorianooriental.pt/pagina/edicao-impressa/2023-09-19/opiniao"
output_directory = "downloaded_files"
download_links(url_to_download, output_directory, subscription_cookies)


# Cookie
# 	=; =; =; 64de97fd17707bf63fe648c0172eb92f=1