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
    """Testing register page"""
    response = app.test_client().get("/register")
    assert b"Email" in response.data
    assert b"Username" in response.data
    assert b"Password" in response.data
    assert b"Confirm password" in response.data
    assert b"Register!" in response.data


def test4():
    """Testing Log In page"""
    response = app.test_client().get("/login")
    assert b"Email" in response.data
    assert b"Password" in response.data
    
    
def test5():
    """Testing About us section """
    response = app.test_client().get("/info")
    assert b"Welcome to Team 1" in response.data
    assert b"Copyright 2022 CUNY TTP - Winter 22 Bootcamp. All Rights Reserved." in response.data
    
def test6():
    """Testing Home section """
    response = app.test_client().get("/")
    assert b"Movies Review Blog" in response.data
    
    
    


    

    
    

    

