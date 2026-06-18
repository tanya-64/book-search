books={'One of us is lying':101, 'One of us is dead':102, 'One of us is next':103, 'One of us is guilty':104, 'One of us is innocent':105}
def search(book_id):    
    for key, value in books.items():
        if value == book_id:
            return key
    return -1
book_id = input("Enter the book ID: ")
print(search(int(book_id)))