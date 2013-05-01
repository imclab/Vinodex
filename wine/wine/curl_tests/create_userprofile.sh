curl -H "Content-Type: application/json"\
     -XPOST localhost:8000/api/v1/profile/\
     -d '{"firstname": "sample", 
          "lastname": "user",
          "user": "/api/v1/auth/user/1/",
          "avatar": "http//sample.com/user"}'
