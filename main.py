import json
if __name__ == '__main__':
    with open('paises.json', 'r', encoding='utf-8') as f:
        print(json.load(f))