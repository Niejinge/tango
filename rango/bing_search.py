# _*_ coding: utf-8 _*_
import requests


def read_bing_key():
    bing_api_key = None

    try:
        with open(r'C:\Users\jinie\Desktop\practice\tango\bing.key', 'r') as f:
            bing_api_key = f.readline()
    except:
        raise IOError('bing.key file not found')

    return bing_api_key


def run_query(search_terms):
    bing_api_key = read_bing_key()
    if not bing_api_key:
        raise KeyError("Bing Key Not Found")
    search_url = "https://api.cognitive.microsoft.com/bing/v7.0/search"

    count = 10
    offset = 0

    headers = {'Ocp-Apim-Subscription-Key': bing_api_key, 'Accept': 'application/json'}
    params = {"q": search_terms, 'count': count, 'offset': offset, }
    results = []

    try:
        response = requests.get(search_url, headers=headers, params=params)
        json_response = response.json()
        for result in json_response['webPages']['value']:
            results.append({'title': result['name'],
                            'link': result['url'],
                            'summary': result['snippet']})
    except Exception as e:
        print("Error when querying the Bing API:", e)
    return results


def main():
    run_query('curry')


if __name__ == '__main__':
    main()
