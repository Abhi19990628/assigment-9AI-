# FASTAPI web framework Server for blog


This FAST API server provides endpoints to retrieve Blog information, with support for adding new branches. It uses Mongo db as the database backend.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://https://github.com/Abhi19990628/assigment-9AI.git
   cd assignment

2. **Install dependencies**:
   ```bash

   pip install unicone
   pip install fastapi
   pip install pymongo

3. **Database Configuration**:
    * Make sure you have mongodb installed and running.
    * Create a new mongodb database for the project.
4. **Set Database Credentials**:
   * client = MongoClient("mongodb://localhost:27017/")
   * db = client["blog_database"]
  

5. **Run the Server**:
   ```bash
   uvicorn app:app --reload
   http://127.0.0.1:8000/docs


## Endpoints

 * @app.post("/posts/"): GET endpoint to retrieve create new blog post.
 * @app.get("/"): GET endpoint to retrieve a list of all blogs.
 * @app.get("/posts/{post_id}")/: GET endpoint to retrieve details of a specific blog identified by id.
 * @app.put("/posts/{post_id}"):GET endpoint to retrieve details of a specific blog identified by id and you can update
 * @app.delete("/posts/{post_id}"):GET endpoint to retrieve deltails of a specific blog identified by id and you can delete
 * @app.post("/posts/{post_id}/comments/"): GET endpoint and u can add comment on specific blog
 * @app.post("/posts/{post_id}/like/") : GET endpoint and u can add  like on post ,
