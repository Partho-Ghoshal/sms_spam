def track_blog_view(blog_id):
    # Increment view count for the blog
    query = "UPDATE user_blogs SET view_count = view_count + 1 WHERE blog_id = %s"
    session.execute(query, (blog_id,))
