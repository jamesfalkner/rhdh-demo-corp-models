#!/usr/bin/env python3
"""
${{ values.appName }} - A web application displaying data from public APIs
"""

from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

# Configuration
API_BASE_URL = "https://jsonplaceholder.typicode.com"
PORT = int(os.environ.get("PORT", 8080))

def fetch_posts():
    """Fetch sample posts from JSONPlaceholder API"""
    try:
        response = requests.get(f"{API_BASE_URL}/posts", timeout=5)
        response.raise_for_status()
        return response.json()[:10]  # Return first 10 posts
    except Exception as e:
        print(f"Error fetching posts: {e}")
        return []

def fetch_users():
    """Fetch sample users from JSONPlaceholder API"""
    try:
        response = requests.get(f"{API_BASE_URL}/users", timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching users: {e}")
        return []

@app.route('/')
def index():
    """Main page displaying posts and users"""
    posts = fetch_posts()
    users = fetch_users()
    
    # Create a user lookup dictionary
    user_dict = {user['id']: user for user in users}
    
    # Add user info to each post
    for post in posts:
        post['user'] = user_dict.get(post.get('userId'), {})
    
    return render_template('index.html', 
                         posts=posts, 
                         users=users,
                         app_name="${{ values.appName }}")

@app.route('/health')
def health():
    """Health check endpoint"""
    return {"status": "healthy", "service": "${{ values.appName }}"}, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT, debug=False)
