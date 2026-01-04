import requests

def main():
    show = input("Enter show name: ")
    url = f"https://api.tvmaze.com/search/shows?q={show}"
    
    response = requests.get(url)
    data = response.json()
    
    if len(data) == 0:
        print("No shows found.")
        return
    
    first_result = data[0]
    show_info = first_result['show']
    
    name = show_info['name']
    premiered = show_info['premiered']
    summary = show_info['summary']
    
    print(f"Name: {name}")
    print(f"Premiered: {premiered}")
    print(f"Summary: {summary}")

if __name__ == "__main__":
    main()
