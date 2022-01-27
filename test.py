from app import app

#running a test 
def test1():
    
    """
    This function test that the flask application has a 
    correct response code when the application goes live 
    """
    response = app.test_client().get("/")
    assert response.status_code == 200


def test2():
    """A dummy docstring"""
    response = app.test_client().get("/register")
    assert response.status_code == 200
    
      
def test3():
    """Testing Home page """
    response = app.test_client().get("/")
    assert b"Puppy Company Blog" in response.data
    assert b"test" in response.data
    assert b"brand new title" in response.data
    assert b"my first six blog post" in response.data
    assert b"my test post" in response.data
    assert b"three title" in response.data
    assert b"asdf" in response.data
    assert b"Read Blog Post" in response.data
    
def test4():
    """Testing register page"""
    response = app.test_client().get("/register")
    assert b"Email" in response.data
    assert b"Username" in response.data
    assert b"Password" in response.data
    assert b"Confirm password" in response.data
    assert b"Register!" in response.data
    
def test5():
    """Testing Log In page"""
    response = app.test_client().get("/login")
    assert b"Email" in response.data
    assert b"Password" in response.data
    assert b"Log In!" in response.data
    
def test5():
    """Testing info section """
    response = app.test_client().get("/info")
    assert b"Info about our Company" in response.data
  
