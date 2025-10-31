from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "science"},
    {"title": "Title Two", "author": "Author Two", "category": "science"},
    {"title": "Title Three", "author": "Author Three", "category": "history"},
    {"title": "Title Four", "author": "Author Four", "category": "math"},
    {"title": "Title Five", "author": "Author Five", "category": "math"},
    {"title": "Title Six", "author": "Author Two", "category": "math"},
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book["title"].casefold() == book_title.casefold():
            return book


@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book["category"].casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{book_author}/")
def read_author_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if (
            book["author"].casefold() == book_author.casefold()
            and book["category"].casefold() == category.casefold()
        ):
            books_to_return.append(book)
    return books_to_return


@app.post("/book/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.delete("/book/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i]["title"].casefold() == book_title.casefold():
            del BOOKS[i]
            return {"message": f"Book '{book_title}' deleted successfully"}
    return {"message": f"Book '{book_title}' not found"}
