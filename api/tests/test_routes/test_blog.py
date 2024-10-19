from tests.utils.blog import create_random_blog

def test_should_fetch_blog_created(client, db_session):
    blog = create_random_blog(db=db_session)
    assert blog.id is not None, "Blog creation failed, no ID assigned."
    response = client.get(f"/blog/{blog.id}/")
    if response.status_code !=200:
        print(f"Failed to fetch blog. Status code: {response.status_code}")
        print(f"Response content: {response.json()}")    
    assert response.status_code == 200
    assert response.json()["title"] == blog.title