import pandas as pd
import numpy as np
import pickle

authors = pd.DataFrame(
    {"author_id": [1, 2, 3], "author_name": ["Тургенев", "Чехов", "Островский"]},
    columns=["author_id", "author_name"],
)
print(authors)

book = pd.DataFrame(
    {
        "author_id": [1, 1, 1, 2, 2, 3, 3],
        "book_title": [
            "Отцы и дети",
            "Рудин",
            "Дворянское гнездо",
            "Толстый и тонкий",
            "Дама с собачкой",
            "Гроза",
            "Таланты и поклонники",
        ],
        "price": [450, 300, 350, 500, 450, 370, 290],
    },
    columns=["author_id", "book_title", "price"],
)
print(book)

authors_price = authors.merge(book, on="author_id")
print(authors_price)

top5 = authors_price.sort_values("price", ascending=False)[0:5]
print(top5)

authors_stat = (
    authors_price.groupby("author_name")["price"]
    .agg(("min", "max", "mean"))
    .reset_index()
)
authors_stat.rename(
    columns={"min": "min_price", "max": "max_price", "mean": "mean_price"}, inplace=True
)
print(authors_stat)

authors_price["cover"] = [
    "твердая",
    "мягкая",
    "мягкая",
    "твердая",
    "твердая",
    "мягкая",
    "мягкая",
]
print(authors_price)

book_info = pd.pivot_table(
    authors_price,
    values="price",
    index=["author_name"],
    columns=["cover"],
    aggfunc=np.sum,
).fillna(0)
print(book_info)

with open("book_info.pkl", "wb") as handle:
    pickle.dump(book_info, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open("book_info.pkl", "rb") as handle:
    book_info2 = pickle.load(handle)

print(any(book_info == book_info2))
