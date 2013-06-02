curl -H "Content-Type: application/json"\
     -XPUT localhost:8000/api/v1/profile/15/\
     -d '{"name": "sample", 
          "email": "user@user.com",
          "password": "foobar"}'
