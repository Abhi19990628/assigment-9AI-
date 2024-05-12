import secrets
from fastapi import FastAPI, HTTPException, Request
from models import BlogPost, Comment, LikeDislike
from database import create_post, read_post, update_post, delete_post, create_comment, read_comments, like_post




app = FastAPI()


# Create endpoints for CRUD operations on blog posts, comments, and likes/dislikes
@app.post("/posts/")
def create_new_post(post: BlogPost):
    return create_post(post)

@app.get("/posts/{post_id}")
async def read_post_by_id(post_id: str):
    return read_post(post_id)

@app.put("/posts/{post_id}")
async def update_post_by_id(post_id: str, post: BlogPost):
    return update_post(post_id, post)

@app.delete("/posts/{post_id}")
async def delete_post_by_id(post_id: str):
    return delete_post(post_id)

@app.post("/posts/{post_id}/comments/")
async def create_new_comment(post_id: str, comment: Comment):
    return create_comment(post_id, comment)

@app.get("/posts/{post_id}/comments/")
async def read_comments_for_post(post_id: str):
    return read_comments(post_id)

@app.post("/posts/{post_id}/like/")
async def like_post_by_id(post_id: str, like: LikeDislike):
    return like_post(post_id, like)


