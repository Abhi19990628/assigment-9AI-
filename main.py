
import secrets
from fastapi import FastAPI, HTTPException, Request
from models import BlogPost, Comment, LikeDislike
from database import create_post, update_post, delete_post, create_comment, read_comments, like_post, read_all_posts , read_post

# Secret key for signing CSRF tokens
SECRET_KEY = "your_secret_key"

# Function to generate CSRF token
def generate_csrf_token() -> str:
    return secrets.token_hex(32)

app = FastAPI()

# Middleware to add CSRF token to response cookies
@app.middleware("http")
async def add_csrf_token(request: Request, call_next):
    response = await call_next(request)
    csrf_token = generate_csrf_token()
    response.set_cookie(key="csrf_token", value=csrf_token, httponly=True, secure=True)
    return response

# Function to verify CSRF token in requests
def verify_csrf_token(request: Request) -> None:
    csrf_token = request.cookies.get("csrf_token")
    if not csrf_token:
        raise HTTPException(status_code=403, detail="CSRF token missing")
    # Perform CSRF token verification logic here

# Example endpoint protected by CSRF
@app.post("/protected/")
async def protected_endpoint(request: Request):
    verify_csrf_token(request)
    return {"message": "CSRF token verified successfully"}

# Create endpoints for CRUD operations on blog posts, comments, and likes/dislikes
@app.post("/posts/")
def create_new_post(post: BlogPost):
    return create_post(post)

@app.get("/")
async def read_all_posts_endpoint():
    return read_all_posts()

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
