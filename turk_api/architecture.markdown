- User uploads image
- Turk Job gets created
- User gets redirected to page for result
- Someone finishes the job
- User gets result

API:

GET /requestInfo
  - Page for user to request wine

POST /job
  ARGS:
    imageUrl
  RESPONSE:
    jobId

GET /job
  ARGS: None
  RESPONSE:
    option[requestId]

GET /jobresult
  ARGS:
    requestId
  RESPONSE:
    name
    year
    winery

POST /jobresult
  ARGS:
    requestId
    name
    year
    winery
  REPONSE:
    None

*SCHEMA*

TABLE jobs
  - id pkey
  - imageUrl string 1024
  - name string 1024
  - year int
  - winery string 1024
  - status string
