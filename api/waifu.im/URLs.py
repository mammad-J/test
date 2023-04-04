class URLs:
    def __init__(self):

        self.base_url = "https://api.waifu.im/"
        
        self.tags = "tags/"
        self.search = "search/"
    
    def base_url(self):
        return self.base_url
    
    def tags_list(self):
        return self.base_url + self.tags
    def search_url():
        return self.base_url + self.search

