curl -H "Content-Type: application/json"\
     -XPOST localhost:8000/api/v1/profile/\
     -d '{"name": "sample", 
          "email": "user@user.com",
          "password": "foobar"}'
