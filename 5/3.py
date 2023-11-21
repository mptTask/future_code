import requests

def get_cat_fact():
    api_url = "https://catfact.ninja/fact"
    response = requests.get(api_url)

    if response.status_code == 200:
        cat_fact = response.json()
        return cat_fact.get('fact', None)
    else:
        return None

def main():
    print("Программа для получения фактов о кошечках.")
    print("------------------------------------------------")

    cat_fact = get_cat_fact()

    if cat_fact is not None:
        print("Вот интересный факт о кошечках:")
        print(cat_fact)
    else:
        print("Не удалось получить факт о кошечках. Пожалуйста, повторите попытку.")

if __name__ == "__main__":
    main()
