from http.client import responses

import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re

from numpy.ma.extras import unique


# requests для работы с API
# pandas для обработки данных
# matplotlib для визуализации

class UserSalesAnalyzer:
    def __init__(self, api_url):
        self.api_url = api_url
        self.users = []
        self.sales = []

    def fetch_data(self):
        try:
            # Получение данных о пользователях
            response = requests.get(f"{self.api_url}/users")    # Отправляет GET-запрос к API
            response.raise_for_status()                         # Был ли запрос успешен
            self.users = response.json()                        # Преобразует тело ответа из JSON в Python-объект

            # Получение данных о продажах
            response = requests.get(f"{self.api_url}/sales")
            response.raise_for_status()
            self.sales = response.json()
        except requests.RequestException as e:
            print(f"Ошибка при получении данных из API: {e}")

    def process_user_data(self):
        try:
            user_stats = {
                "total_users": len(self.users),
                # Суммирование последовательности единиц для каждого активного пользователя
                "active_users": sum(1 for user in self.users if user.get("is_active", False)),
                "average_age": sum(user.get("age", 0) for user in self.users) / len(self.users) if self.users else 0
            }
            return user_stats
        except Exception as e:
            print(f"Ошибка при обработке данных пользователей: {e}")
            return {}

    def process_sales_data(self):
        try:
            sales_df = pd.DataFrame(self.sales)                         # Создание DataFrame из списка словаря
            total_revenue = sales_df["amount"].sum()                    # Суммирование столбца amount из DataFrame
            avg_sale = sales_df["amount"].mean()                        # Среднее значение столбца amount из DataFrame
            top_products = sales_df["product"].value_counts().head(5)   # 5 самых популярных продуктов и количество их продаж
            return {
                "total_revenue": total_revenue,
                "average_sale": avg_sale,
                "top_products": top_products.to_dict()
            }
        except Exception as e:
            print(f"Ошибка при обработке данных о продажах: {e}")
            return {}

    def visualize_data(self, user_stats, sales_stats):
        try:
            # Визуализация статистики пользователей
            plt.figure(figsize=(12,6))                  # Создание новой фигуры(окна)
            plt.subplot(121)                            # Подграфик в сетке 1x2 и выбор 1 позиции
            # столбчатая диаграмма для статистики пользователей
            plt.bar(["Total Users", "Active Users"], [user_stats["total_users"], user_stats["active_users"]])
            plt.title("User Statistics")

            # Визуализация топ-5 продуктов
            plt.subplot(122)                            # 2 позиция
            # Извлечение названий продуктов и их продаж
            products = list(sales_stats["top_products"].keys())
            values = list(sales_stats["top_products"].values())
            plt.bar(products, values)
            plt.title("Top-5 products")
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()                          # Регулирование параметров под графиков
            plt.savefig("sales_analysis.png")
            print("Визуализация сохранена в файле 'sales_analysis.png'")
        except Exception as e:
            print(f"Ошибка при визуализации данных: {e}")

    def analyze_text_data(self, text):
        try:
            words = re.findall(r'\w+', text.lower())    # Список всех слов в тексте через регулярное выражение
            word_count = len(words)
            unique_words = len(set(words))
            most_common = Counter(words).most_common(5)        # Объект Counter подсчитывает частоту каждого слова
            return {
                "word_count": word_count,
                "unique_words": unique_words,
                "most_common": most_common
            }
        except Exception as e:
            print(f"Ошибка при анализе текста: {e}")
            return {}

    def generate_report(self, user_stats, sales_stats, text_analysis):
        try:
            report = f"""
                    Отчет по анализу данных:

                    Статистика пользователей:
                    - Всего пользователей: {user_stats['total_users']}
                    - Активных пользователей: {user_stats['active_users']}
                    - Средний возраст: {user_stats['average_age']:.2f}

                    Статистика продаж:
                    - Общая выручка: ${sales_stats['total_revenue']:.2f}
                    - Средняя сумма продажи: ${sales_stats['average_sale']:.2f}
                    - Топ-5 продуктов:
                      {json.dumps(sales_stats['top_products'], indent=2)}

                    Анализ текста:
                    - Количество слов: {text_analysis['word_count']}
                    - Уникальных слов: {text_analysis['unique_words']}
                    - Самые частые слова: {text_analysis['most_common']}
                    """

            with open("analysis_report.txt", "w") as f:
                f.write(report)
            print("Отчет сохранен в файле 'analysis_report.txt'")
        except Exception as e:
            print(f"Ошибка при генерации отчета: {e}")

def main():
    analyzer = UserSalesAnalyzer("http://localhost:3000")
    analyzer.fetch_data()

    user_stats = analyzer.process_user_data()
    sales_stats = analyzer.process_sales_data()
    analyzer.visualize_data(user_stats, sales_stats)

    sample_text = """
        Пример текста для анализа.
        Грачи прилетели сегодня рано утром. Мы сначала их не заметили. Черные птицы беспорядочно расселись на поле.
        На темной пахоте их нелегко было заметить. А затем грачи взлетели на белоствольные березы, 
        и началась шумная птичья конференция об устройстве гнезд. 
        И тут все увидели, что прилетели грачи — гонцы наступившей весны.
        """
    text_analysis = analyzer.analyze_text_data(sample_text)

    analyzer.generate_report(user_stats, sales_stats, text_analysis)

if __name__ == "__main__":
    main()