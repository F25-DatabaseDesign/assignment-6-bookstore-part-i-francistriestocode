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
book1 = [1, 1, "Michael Jordan: The Life", "Roland Lazenby", "13-9780316194761", "20.00", "mj.jpg", 1]
book2 = [2, 1, "Lebron James: The Rise of a Star", "David Morgan", "13-9781886228740", "20.00", "lbj.jpg",0]
book3 = [3, 1, "On the Court With...Stephen Curry", "Matt Christopher", "13-9780316509589", "7.00", "steph.jpg", 1]
book4 = [4, 1, "Allen Iverson", "John N Smallwood, Jr", "13-9781476751603", "18.00", "ai.jpg", 0]

book5 = [5, 2, "Messi", "Harry Conix", "13-9781948585873", "10.00", "messi.jpg", 0]
book6 = [6, 2, "Cristiano Ronaldo", "Brianna Battista", "13-9781538344729", "10.00", "ronaldo.jpg",1]
book7 = [7, 2, "Zidane", "Patrick Fort", "13-9781785038488", "39.00", "zidane.jpg",0]
book8 = [8, 2, "Bale-The Biography", "Frank Worrall", "13-9781843583943", "19.00", "bale.jpg", 1]

book9 = [9, 3, "Sabrina Ionescu: Rising Basketball Star", "Matt Chandler", "13-9781663983626", "13.00", "sab.jpg", 1]
book10 = [10, 3, "Caitlin Clark: Basketnall Superstar", "Anthony K Hewson", "13-9781634949361", "5.00", "clark.jpg", 0]
book11 = [11, 3, "Angel Reese", "Kim Thompson", "13-9798892006330", "11.00", "reese.jpg", 0]
book12 = [12, 3, "A'Ja Wilson", "Tracy Abell", "13-9781637391273", "5.00", "wilson.jpg", 1]

book13 = [13, 4, "Simone Biles: Greatest Gymnast of All Time", "Caitie McAneney", "13-9781508160700", "10.00", "biles.jpg", 1]
book14 = [14, 4, "Faster Than Lightning: My Autobiography", "Usain Bolt", "13-9780007371426", "16.00", "bolt.jpg", 0]
book15 = [15, 4, "Roger Federer: The Biography", "Ren Stauffer", "13-9781913538910", "15.00", "fed.jpg", 1]
book16 = [116, 4, "99: Stories of the Game", "Wayne Gretzky", "13-9780735232624", "28.00", "wayne.jpg", 0]







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
