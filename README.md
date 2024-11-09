# Mercadolibre Exam - GenAI & FFB Team

Welcome MELI Team!

## Usage

The API is currently deployed on [Vercel](https://vercel.com/) under this [link](https://meli-challenge-ncinzer.vercel.app/)

[https://meli-challenge-ncinzer.vercel.app/](https://meli-challenge-ncinzer.vercel.app/)

## Endpoints
### [Mutant Request](https://meli-challenge-ncinzer.vercel.app/mutant)

`POST /mutant`

#### Mutant request
```
Body 
{ "dna": [ "ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTA"] }
```

### Response

    HTTP/1.1 200 OK
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Location: /mutant

    { "success": true, "dna": ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTA"] }

----
#### Not mutant request
```
Body 
{ "dna": [ "ATGCGA", "CAGTGC", "TTATTT", "AGAAGG", "CTCCTA", "TCACTA"] }
```

### Response

    HTTP/1.1 403 Forbidden
    Status: 403 Forbidden
    Connection: close
    Content-Type: application/json
    Location: /mutant

    { "detail": "Its a human! Abort!" }

---
### [Stats Request](https://meli-challenge-ncinzer.vercel.app/stats)

`GET /stats`

### Response

    HTTP/1.1 200 OK
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Location: /mutant

    { "count_human_dna": 0, "count_mutant_dna": 0, "ratio": 0.0 }

---
## Stack

- API: [FastAPI](https://fastapi.tiangolo.com/)
- Deploy: [Vercel](https://vercel.com/)
- Database: [MongoDB Atlas](https://cloud.mongodb.com/)
