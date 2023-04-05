from tqdm import tqdm
import requests
import json
import os
import random
import shutil

class WaifuIm:
    def __init__(self, is_nsfw=False, gif=False, many=False, just_link=True):
        # Tags for SFW images
        self.sfw_tags = [
            "maid",
            "waifu",
            "marin-kitagawa",
            "mori-calliope",
            "raiden-shogun",
            "oppai",
            "selfies",
            "uniform"
        ]
        # Tags for NSFW images
        self.nsfw_tags = [
            "ass",
            "hentai",
            "milf",
            "oral",
            "paizuri",
            "ecchi",
            "ero"
        ]
        # API endpoints
        self.base_url = "https://api.waifu.im/"
        self.tags_list = "https://api.waifu.im/tags/"
        self.search_url = "https://api.waifu.im/search/"
        # Settings
        self.is_nsfw = bool(is_nsfw)
        self.gif = bool(gif)
        self.many = bool(many)
        self.just_link = bool(just_link)
    
    def random(self):
        try:
            # Send request to the API with specified parameters
            response = requests.get(self.search_url + "?many=" + str(self.many) + "&is_nsfw=" + str(self.is_nsfw) + "&gif=" + str(self.gif)).json()

            if self.just_link == True:
                if self.many == True:
                    # Get URLs of multiple images
                    urls = []
                    for image in response['images']:
                        urls.append(image['url'])
                    return urls
                else:
                    # Get URL of a single image
                    url = response['images'][0]['url']
            else:
                # Return the response object containing image information
                return response

        except Exception as error:
            print(error)

    def get_by_tag(self, included_tags:str):
        try:
            # Send request to the API with specified parameters and included tags
            response = requests.get(self.search_url + "?many=" + str(self.many) + "&is_nsfw=" + str(self.is_nsfw) + "&gif=" + str(self.gif) + "&included_tags=" + included_tags).json()

            if self.just_link == True:
                if self.many == True:
                    # Get URLs of multiple images
                    urls = []
                    for image in response['images']:
                        urls.append(image['url'])
                    return urls
                else:
                    # Get URL of a single image
                    url = response['images'][0]['url']
            else:
                # Return the response object containing image information
                return response

        except Exception as error:
            print(error)
            pass
    
    def download(self, path=os.getcwd(), urls=[]):
        downloaded = []
        if not urls:
            print("No URLs to download")
            return
        for url in urls:
            try:
                # Extract filename from URL
                file_name = url.split("/")[-1]
                # Build file path
                file_path = os.path.join(path, file_name)
                # Send request to download image
                response = requests.get(url, stream=True)
                response.raise_for_status()
                # Get total file size in bytes
                total_size = int(response.headers.get('content-length', 0))
                # Set initial downloaded bytes to 0
                bytes_downloaded = 0
                # Write image to file
                with open(file_path, 'wb') as f:
                    for data in response.iter_content(chunk_size=4096):
                        # Update progress
                        bytes_downloaded += len(data)
                        progress = (bytes_downloaded / total_size) * 100

                        print("Downloaded:")
                        for pic in downloaded:
                            print(pic)

                        print(f"\n\rDownloading {file_name}: {bytes_downloaded}/{total_size} bytes ({progress:.2f}%)", end='')
                        # Write data to file
                        f.write(data)

                        os.system('cls' if os.name == 'nt' else 'clear')

                
                print(f"\nImage {file_name} downloaded successfully to {file_path}")
                downloaded.append(file_path)

            except Exception as e:
                print(f"Error downloading {url}: {e}")


# Example usage
waifu = WaifuIm(is_nsfw=True, gif=True, many=True, just_link=True)
a = waifu.random()
waifu.download(urls=a)
