from flask import Flask, Blueprint, render_template, session, url_for, flash, redirect, request
from app.models import Blog, User, db

Blog_bp = Blueprint('blog', __name__)

@Blog_bp.route('/')
def home():
    if 'user' not in session:
        return redirect(url_for('auth.login'))  
    blogs = Blog.query.order_by(Blog.date_posted.desc()).all()
    return render_template('blog.html', blogs=blogs)

@Blog_bp.route('/add', methods=['POST','GET'])
def add_Blog():
    if 'user' not in session:
        flash("You need to login to post a blog",'error')
        return redirect(url_for('auth.login'))
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')

        if not title or not content:
            flash("Title or Content is need for a blog",'error')
            return redirect(url_for('blog.add_Blog'))
        new_blog= Blog(title=title,content=content,user_id=session['user'])
        db.session.add(new_blog)
        db.session.commit()
        flash('Blog added successfully','success')
        return redirect(url_for('blog.home'))
    return render_template('add_blog.html')

@Blog_bp.route('/edit/<int:blog_id>',methods=['POST','GET'])
def edit_blog(blog_id):
    if 'user' not in session:
        flash("You need to login to edit a blog",'error')
        return redirect('auth.login')
    blog = Blog.query.get_or_404(blog_id)
    if blog.user_id != session['user']:
        flash("You can only edit your blogs",'error')
        return redirect(url_for('blog.home'))
    if request.method=='POST':
        blog.title = request.form.get('title')
        blog.content = request.form.get('content')
        db.session.commit()
        flash("Blog updated successfully",'success')
        return redirect(url_for('blog.home'))
    return render_template('edit_blog.html', blog=blog)

@Blog_bp.route('/myblogs')
def my_blogs():
    if 'user' not in session:
        flash('Please login to view your blogs.', 'error')
        return redirect(url_for('auth.login'))

    user_id = session['user']
    blogs = Blog.query.filter_by(user_id=user_id).order_by(Blog.date_posted.desc()).all()
    return render_template('my_blog.html', blogs=blogs)


@Blog_bp.route('/delete/<int:blog_id>', methods=['POST'])  
def delete_blog(blog_id):
    if 'user' not in session:
        flash('Please log in first.', 'error')
        return redirect(url_for('auth.login'))  

    blog = Blog.query.get_or_404(blog_id)

    if blog.user_id != session['user']:
        flash('You can only delete your own blog.', 'error')
        return redirect(url_for('blog.home'))

    db.session.delete(blog)
    db.session.commit()
    flash('Blog deleted successfully!', 'success')
    return redirect(url_for('blog.home'))

@Blog_bp.route("/view/<int:blog_id>")
def view_blog(blog_id):

    blog = Blog.query.get_or_404(blog_id)
    return render_template("view_blog.html", blog=blog)

@Blog_bp.route("/comment/<int:blog_id>", methods=["POST"])
def add_comment(blog_id):
    if 'user' not in session:
        flash("You must be logged in to comment.", 'error')
        return redirect(url_for('auth.login'))

    content = request.form.get("content")
    if not content:
        flash("Comment cannot be empty.", 'error')
        return redirect(url_for('blog.view_blog', blog_id=blog_id))

    from app.models import Comment  

    new_comment = Comment(content=content, blog_id=blog_id, user_id=session['user'])
    db.session.add(new_comment)
    db.session.commit()

    flash("Comment added successfully.", 'success')
    return redirect(url_for('blog.view_blog', blog_id=blog_id))


