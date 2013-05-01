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
    
    def __init__(self, tester):
        self.client = Client()
        self.tester = tester

    def getOK(self,url):
        response = self.client.get(url)
        self.tester.assertEqual(response.status_code, OK)
        return fromJson(response.content)

    def postOK(self, url, data):
        json = toJson(data)
        response = self.client.post(url, json, content_type="application/json")
        if (response.status_code != CREATED):
            print response.content
        self.tester.assertEqual(response.status_code, CREATED)
        return response["Location"]

    def postBad(self, url, data):
        json = toJson(data)
        response = self.client.post(url, json, content_type="application/json")
        self.tester.assertEqual(response.status_code, BAD_REQUEST)

    def deleteOK(self, url):
        # Ensure Delete Works
        response = self.client.delete(url)
        self.tester.assertEqual(response.status_code, NO_CONTENT)

        # Try to get it again, just to make sure
        response = self.client.delete(url)
        self.tester.assertEqual(response.status_code, NOT_FOUND)

    def putOK(self, url, data):
        json = toJson(data)
        response = self.client.put(url, json, content_type="application/json")
        self.tester.assertEqual(response.status_code, NO_CONTENT)

    def fields_match(self, dict1, dict2, fields):
        for field in fields:
            self.tester.assertEqual(dict1[field], dict2[field])
