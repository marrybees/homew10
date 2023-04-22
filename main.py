import request
def get_data (url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
          return  f"Error: {response.status_code}"
    except :

        return f"Error: ვერ მოხერხდა დაკავშირება შეგიძლიათ"


print(get_data("https://api.github.com/"))



