# README

This is the Quick Start tutorial from the DRF docs.

## Steps

1. Write serializers.
2. Write views.
3. Wire up API URLs.

## Notes

Make request to API

    curl -H 'Accept: application/json; indent=4' -u root:password123 http://127.0.0.1:8000/users/

You can also open this url in your browser.  Add a pk this time:

    # Be sure to login using control in upper right corner
    (browser) http://127.0.0.1:8000/users/

### Serialization

Serialization - Convert a Python/Django object into a JSON object.
Deserialization - Convert a JSON object into a Python/Django object.

The client sends JSON data to the server in an HTTP request. The server PARSES the data and de-serializes it into a Python/Django object.

The server RENDERS the outgoing Python/Django object, serializes it into JSON, and returning it to the client in an HTTP response.

    client -> server: parse + de-serialize          Use BytesIO and JSONParser
    server -> client: render + serialize            Use SubjectSerializer and JSONRenderer

## Check if username is taken

I modified the code in this tutorial so that I have an endpoint that will check to see if a particular username is in taken.  It required commenting out the registering of a 'users' route in urls.py and then replacing the original UserViewSet class in views.py with another version that contained a method to handle ```GET```.  Here is the URL for this new endpoint:

    (browser) http://127.0.0.1:8000/users/<username>/

## References

[Quickstart Tutorial](https://www.django-rest-framework.org/tutorial/quickstart/#quickstart)
[Django REST Framework](https://www.django-rest-framework.org/)
[jakubroztocil/httpie](https://github.com/jakubroztocil/httpie) -- cURL alternative
[The Ultimate Tutorial for Django REST Framework: CRUD (Part 1)](https://sunscrapers.com/blog/ultimate-tutorial-django-rest-framework-part-1/)