from pydantic import BaseModel

class BlogPost(BaseModel):
    title: str
    content: str
    author: str

class Comment(BaseModel):
    text: str
    author: str

class LikeDislike(BaseModel):
    type: str  # 'like' or 'dislike'
    user_id: int  
