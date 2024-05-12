# CRUD operations for blog posts Everything is working you can check 
from bson import ObjectId
from pymongo import MongoClient
from models import BlogPost, Comment

client = MongoClient("mongodb://localhost:27017/")
db = client["blog_database"]
blog_posts_collection = db["blog_posts"]
comments_collection = db["comments"]

def create_post(post: BlogPost) -> str:
    inserted_id = str(blog_posts_collection.insert_one(post.dict()).inserted_id)
    return inserted_id

def read_all_posts() -> list:
    posts = blog_posts_collection.find()
    return [BlogPost(**post) for post in posts]

def read_post(post_id: str) -> BlogPost:
    try:
        post_data = blog_posts_collection.find_one({"_id": ObjectId(post_id)})
     
        if post_data:
            return [BlogPost(**post_data)]
        else:
            return None
    except Exception as e:
        print(f"Error occurred while reading post: {e}")
        return None


def update_post(post_id: str, post: BlogPost) -> bool:
    result = blog_posts_collection.replace_one({"_id":ObjectId( post_id)}, post.dict())
    return result.modified_count > 0

def delete_post(post_id: str) -> bool:
    result = blog_posts_collection.delete_one({"_id": ObjectId(post_id)})
    return result.deleted_count > 0

def create_comment(post_id: str, comment: Comment) -> str:
    comment_data = comment.dict()
    comment_data["post_id"] = post_id
    inserted_id = str(comments_collection.insert_one(comment_data).inserted_id)
    return inserted_id

def read_comments(post_id: str) -> list:
    comments = comments_collection.find({"post_id": post_id})
    return [Comment(**comment) for comment in comments]


# Like a post
def like_post(post_id: str) -> bool:
    result = blog_posts_collection.update_one({"_id": post_id}, {"$inc": {"likes": 1}})
    return result.modified_count > 0
