from json.encoder import JSONEncoder
from json.decoder import JSONDecoder

toJson = JSONEncoder().encode
fromJson = JSONDecoder().decode

def getOK(url, client, tester):
    response = client.get(url)
    tester.assertEqual(response.status_code, 200)
    return fromJson(response.content)

def postOK(url, data, client, tester):
    json = toJson(data)
    response = client.post(url, json, content_type="application/json")
    tester.assertEqual(response.status_code, 201)
    return response["Location"]

def deleteOK(url, client, tester):
    # Ensure Delete Works
    response = client.delete(url)
    tester.assertEqual(response.status_code, 204)

    # Try to get it again, just to make sure
    response = client.delete(url)
    tester.assertEqual(response.status_code, 404)

def both_contain(dict1, dict2, fields, tester):
    for field in fields:
        tester.assertEqual(dict1[field], dict2[field])
