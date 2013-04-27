from json.encoder import JSONEncoder
from json.decoder import JSONDecoder
from django.test.client import Client

toJson = JSONEncoder().encode
fromJson = JSONDecoder().decode

class UnitTestHelper(object):
    
    def __init__(self, tester):
        self.client = Client()
        self.tester = tester

    def getOK(self,url):
        response = self.client.get(url)
        self.tester.assertEqual(response.status_code, 200)
        return fromJson(response.content)

    def postOK(self, url, data):
        json = toJson(data)
        response = self.client.post(url, json, content_type="application/json")
        self.tester.assertEqual(response.status_code, 201)
        return response["Location"]

    def deleteOK(self, url):
        # Ensure Delete Works
        response = self.client.delete(url)
        self.tester.assertEqual(response.status_code, 204)

        # Try to get it again, just to make sure
        response = self.client.delete(url)
        self.tester.assertEqual(response.status_code, 404)

    def putOK(self, url, data):
        json = toJson(data)
        response = self.client.put(url, json, content_type="application/json")
        self.tester.assertEqual(response.status_code, 204)

    def fields_match(self, dict1, dict2, fields):
        for field in fields:
            self.tester.assertEqual(dict1[field], dict2[field])
