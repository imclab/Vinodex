import mturkcore
m = mturkcore.MechanicalTurk()
print m.create_request("CreateHIT",
{
     "Title":                       "Classify the wine", 
     "Description":                 "Enter the wine name, year, and winery",
     "Question":                    file("classifywine.question").read(),
     "Reward": {
         "Amount":       0.25,
         "CurrencyCode": "USD"
     },
     "AssignmentDurationInSeconds": 60,
     "LifetimeInSeconds":           3600
     
})
