from blog import app
from blog import db
from flask import render_template, flash, redirect, url_for
from blog.models import Posts
from blog.forms import AddForm, SearchForm





#default route in flask
@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

#add_post route it goes to the database
@app.route("/add_post", methods=['GET', 'POST'])
def add_post():
    form = AddForm()
    if form.validate_on_submit():
        post = Posts(title=form.title.data, author=form.author.data, slug=form.slug.data,
                     content=form.content.data)
        #clear form after submit            
        form.title.data = ''
        form.author.data = '' 
        form.slug.data =''
        form.content.data =''         
        #post data to database
        db.session.add(post)
        db.session.commit()
        flash("Posted!", category='success')
    return render_template('add_post.html', form=form)


#pass stuff to navbar
@app.context_processor
def base():
    form = SearchForm()
    return dict(form=form)



#create search area route or rather function
@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    posters = Posts.query
    if form.validate_on_submit():
        #get data from submitted form
        post.searched = form.searched.data

        #query the database
        posters = posters.filter(Posts.content.like('%' + post.searched + '%'))

        #how to present the search details
        posters = posters.order_by(Posts.title).all()

        
        return render_template("search.html", form=form, searched = post.searched, posters=posters)
    
    else:
        flash("ati?", category="danger")


         
        
        

#show posts in flask
@app.route("/posts")
def posts_page():
    posts = Posts.query.order_by(Posts.date_posted)
    return render_template('posts.html', posts=posts)




#show individual post in flask
@app.route('/posts/<int:id>')
def post(id):
    post = Posts.query.get_or_404(id)
    return render_template('post.html', post=post)





#edit a post in flask
@app.route('/posts/edit/<int:id>', methods=['GET', 'POST'])
def edit_post(id):
    post = Posts.query.get_or_404(id)
    form = AddForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.author = form.author.data
        post.slug = form.slug.data
        post.content = form.content.data
        #update the database
        db.session.add(post)
        db.session.commit()
        flash("Post Edited!", category="success")
        return redirect(url_for('post', id=post.id))
    
    form.title.data = post.title
    form.author.data = post.author
    form.slug.data = post.slug
    form.content.data = post.content
    return render_template('edit_post.html', form=form)


    

#Delete blog post in flask
@app.route('/posts/delete/<int:id>')
def delete_post(id):
    post_to_delete = Posts.query.get_or_404(id)
    try:
        db.session.delete(post_to_delete)
        db.session.commit()
        #return a message
        flash("Post Deleted!", category="danger")
        
        #grab all the posts from the database after deleting
        posts = Posts.query.order_by(Posts.date_posted)
        return render_template('posts.html', posts=posts)

    except:
        #retun an error message!
        flash("Whoops! There was a problem! Try again!", category="danger!")

        #grab all the posts from the database again for user to try and delete again
        posts = Posts.query.order_by(Posts.date_posted)
        return render_template('posts.html', posts=posts)