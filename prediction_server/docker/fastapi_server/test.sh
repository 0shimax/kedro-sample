curl -X POST \
  http://localhost/predict \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 9a75cc9b-f940-40a0-9cb0-f02986e1e16d' \
  -H 'cache-control: no-cache' \
  -H 'token: 1337' \
  -d '
{
	"float_features": [
		{
			"engines": 2,
			"passenger_capacity": 4,
			"crew": 3,
			"company_rating": 1,
			"review_scores_rating": 96
		},
		{
			"engines": 4,
			"passenger_capacity": 8,
			"crew": 5,
			"company_rating": 1,
			"review_scores_rating": 100
		},
		{
			"engines": 2,
			"passenger_capacity": 4,
			"crew": 3,
			"company_rating": 1,
			"review_scores_rating": 96
		},
		{
			"engines": 4,
			"passenger_capacity": 8,
			"crew": 5,
			"company_rating": 1,
			"review_scores_rating": 100
		},
		{
			"engines": 2,
			"passenger_capacity": 4,
			"crew": 3,
			"company_rating": 1,
			"review_scores_rating": 96
		},
		{
			"engines": 4,
			"passenger_capacity": 8,
			"crew": 5,
			"company_rating": 1,
			"review_scores_rating": 100
		},
		{
			"engines": 2,
			"passenger_capacity": 4,
			"crew": 3,
			"company_rating": 1,
			"review_scores_rating": 96
		},
		{
			"engines": 4,
			"passenger_capacity": 8,
			"crew": 5,
			"company_rating": 1,
			"review_scores_rating": 100
		}
	],
	"categorical_features": [
		{
			"d_check_complete": "False",
			"moon_clearance_complete": "False",
			"iata_approved": "True"
		},
		{
			"d_check_complete": "True",
			"moon_clearance_complete": "False",
			"iata_approved": "False"
		},
		{
			"d_check_complete": "False",
			"moon_clearance_complete": "False",
			"iata_approved": "True"
		},
		{
			"d_check_complete": "True",
			"moon_clearance_complete": "False",
			"iata_approved": "False"
		},
		{
			"d_check_complete": "False",
			"moon_clearance_complete": "False",
			"iata_approved": "True"
		},
		{
			"d_check_complete": "True",
			"moon_clearance_complete": "False",
			"iata_approved": "False"
		},
		{
			"d_check_complete": "False",
			"moon_clearance_complete": "False",
			"iata_approved": "True"
		},
		{
			"d_check_complete": "True",
			"moon_clearance_complete": "False",
			"iata_approved": "False"
		}
	]
}
'