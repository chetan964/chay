import os
from recommender.content_based import BookRecommender

base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, 'data', 'books.csv')

recommender = BookRecommender(csv_path)

while True:
    print("\nEnter a book title (or type 'exit' to quit):")
    title = input("> ")
    if title.lower() == 'exit':
        break

    recommendations = recommender.recommend(title)
    if recommendations:
        print("\nRecommended Books:")
        for book in recommendations:
            print("-", book)
