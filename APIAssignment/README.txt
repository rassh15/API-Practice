To access this API

1. First runserver 
2. This is token based API. Either use user detail (username: user03, password:user03) 
    or register new user. 
3. You can register user using url(http://127.0.0.1:8000/api/register/)
4. Token is generated after registering user or after successfull login.
5. There are two API (Create API and Update API).
5. Use that token to access message create api(http://127.0.0.1:8000/create)
with the form data in format
    {
        msg : 'Message to be sent'
    }

6. Update message api.
To access this view you can use url (/<int:pk>).
Here you provide message id to access that message
with the form data in format
(
    {
        msg : 'Message to be sent'
    }
)

7. User can only have 10 request per hour.
