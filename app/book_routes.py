from app import db
from app.models.books import Book
from flask import Blueprint, jsonify, request, make_response, abort



books_bp = Blueprint("books", __name__, url_prefix="/books")

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message":f"{cls.__name__} {model_id} invalid"}, 400))

    model = cls.query.get(model_id)

    if not model:
        abort(make_response({"message":f"{cls.__name__} {model_id} not found"}, 404))

    return model

@books_bp.route("/<book_id>", methods=["GET"])
def handle_book(book_id):
    book = validate_model(Book, book_id)

    return {
        "id": book.id,
        "title": book.title,
        "description": book.description,
        "author": book.author
        }

@books_bp.route("/<book_id>", methods=["PUT"])
def update_book(book_id):
    book = validate_model(Book, book_id)

    request_body = request.get_json()

    book.title = request_body["title"]
    book.description = request_body["description"]
    book.author_id = request_body["author_id"]

    db.session.commit()

    return make_response(f"Book #{book.id} successfully updated")

@books_bp.route("/<book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = validate_model(Book, book_id)

    db.session.delete(book)
    db.session.commit()

    return make_response(f"Book #{book.id} successfully deleted")

@books_bp.route("", methods=["POST", "GET"])
def handle_books():
    if request.method == "GET":
        books = Book.query.all()
        books_response = []
        for book in books:
            books_response.append({
                "id": book.id,
                "title": book.title,
                "description": book.description,
                "author id": book.author_id
            })
        return jsonify(books_response)
    elif request.method == "POST":
        request_body = request.get_json()
        new_book = Book(
            title=request_body["title"],
            description=request_body["description"]
            )
        db.session.add(new_book)
        db.session.commit()

    return make_response(f"Book {new_book.title} successfully created", 201)


