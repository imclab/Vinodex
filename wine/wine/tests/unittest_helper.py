from json.encoder import JSONEncoder
from json.decoder import JSONDecoder
from django.test.client import Client

toJson = JSONEncoder().encode
fromJson = JSONDecoder().decode

OK = 200
CREATED = 201
NO_CONTENT = 204
NOT_FOUND = 404
BAD_REQUEST = 400


class UnitTestHelper(object):
    """ This helper class is used to make it easier to make 
        HTTP Requests that can be used to verify the functionality
        of the API """
    
    def __init__(self, tester):
        """ Initializes a client that can make HTTP requests to our
            test server, and registers a tester that can be used
            to raise assertionErrors"""

        self.client = Client()
        self.tester = tester

    def getOK(self,url):
        """ Makes a GET request, and returns a dictionary with 
            the object that was received. If the server does not
            respond with the HTTP 200 OK code, an error is thrown """
        response = self.client.get(url)
        self.tester.assertEqual(response.status_code, OK)
        return fromJson(response.content)

    def postOK(self, url, data):
        """ Makes a POST request to the given url. This method will JSON
            encode the data and send it as JSON to the server. If the server
            does not respond with the HTTP 201 CREATED code, an error is
            thrown. This method returns the URL that can be accessed to 
            get the created content """
        json = toJson(data)
        response = self.client.post(url, json, content_type="application/json")
        if (response.status_code != CREATED):
            print response.content
        self.tester.assertEqual(response.status_code, CREATED)
        return response["Location"]

    def postBad(self, url, data):
        """ Makes A POST request to the given URL. This method will 
            JSON-ENCODE the data and send it a JSON to the server. This method
            should be used to ensure that the server will reject bad data. """
        json = toJson(data)
        response = self.client.post(url, json, content_type="application/json")
        self.tester.assertEqual(response.status_code, BAD_REQUEST)

    def deleteOK(self, url):
        """ This code ensures that a given piece of content can be deleted.
            Sends a DELETE request to the server, and ensures that the
            NO_CONTENT code is received. Then, it makes a GET request for the
            same piece of content, and ensures that it receives NOT_FOUND 
            from the server """
        # Ensure Delete Works
        response = self.client.delete(url)
        self.tester.assertEqual(response.status_code, NO_CONTENT)

        # Try to get it again, just to make sure
        response = self.client.delete(url)
        self.tester.assertEqual(response.status_code, NOT_FOUND)

    def putOK(self, url, data):
        """ This server makes a PUT request to the given url. The data will
            be JSON encoded and sent in the body of the request. An 
            AssertionError is thrown if the server does not respond with
            NO_CONTENT """
        json = toJson(data)
        response = self.client.put(url, json, content_type="application/json")
        self.tester.assertEqual(response.status_code, NO_CONTENT)

    def fields_match(self, dict1, dict2, fields):
        """ This method ensures that the given fields in two dictionaries match """
        for field in fields:
            self.tester.assertEqual(dict1[field], dict2[field])
