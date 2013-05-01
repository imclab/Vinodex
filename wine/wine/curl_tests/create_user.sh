curl -H "Content-Type: application/json"\
     -XPOST localhost:8000/api/v1/auth/user/\
     -d '{"username": "sampleuser", 
          "password": "password",
          "email": "sample@user.com"}'
