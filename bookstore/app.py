from flask import Flask, render_template, request, redirect, url_for, make_response


# instantiate the app
app = Flask(__name__)

# Create a list called categories. The elements in the list should be lists that contain the following information in this order:
#   categoryId
#   categoryName
#   An example of a single category list is: [1, "Biographies"]

# Create a list called books. The elements in the list should be lists that contain the following information in this order:
#   bookId     (you can assign the bookId - preferably a number from 1-16)
#   categoryId (this should be one of the categories in the category dictionary)
#   title
#   author
#   isbn
#   price      (the value should be a float)
#   image      (this is the filename of the book image.  If all the images, have the same extension, you can omit the extension)
#   readNow    (This should be either 1 or 0.  For each category, some of the books (but not all) should have this set to 1.
#   An example of a single category list is: [1, 1, "Madonna", "Andrew Morton", "13-9780312287863", 39.99, "madonna.png", 1]

categories = [];
category1 = [1, "NBA"]
category2 = [2, "Soccer"]
category3 = [3, "WNBA"]
category4 = [4, "Olympics"]

categories.append(category1)
categories.append(category2)
categories.append(category3)
categories.append(category4)

books = [];
book1 = [1, 1, "Michael Jordan: The Life", "Roland Lazenby", "13-9780316194761", "20.00", "mj.png", 1]
book2 = [2, 1, "



# set up routes
@app.route('/')
def home():
    #Link to the index page.  Pass the categories as a parameter
    return render_template()

@app.route('/category')
def category():
    # Store the categoryId passed as a URL parameter into a variable

    # Create a new list called selected_books containing a list of books that have the selected category

    # Link to the category page.  Pass the selectedCategory, categories and books as parameters
    return render_template()

@app.route('/search')
def search():
    #Link to the search results page.
    return render_template()

@app.errorhandler(Exception)
def handle_error(e):
    """
    Output any errors - good for debugging.
    """
    return render_template('error.html', error=e) # render the edit template


if __name__ == "__main__":
    app.run(debug = True)
