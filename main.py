from fastapi import FastAPI, HTTPException, status

from utils import is_mutant
from db.models import DNA, DNADoc
from db.conn import collection_dnas
from db.schemas import build_dna_doc

app = FastAPI()

db_path = '/tmp/db.json'
DNAS = 'dnas'
STATS = 'stats'
C_MUTANT = 'count_mutant_dna'
C_HUMAN = 'count_human_dna'
RATIO = 'ratio'

@app.get('/')
def home():
  return {"message": "Please, make a GET request to /stats or POST request to /mutant with dna structure as asked in the challenge."}

@app.post('/mutant')
def post_mutant(body: DNA):
  dna = body.dna

  mutant = is_mutant(dna)

  collection_dnas.insert_one(build_dna_doc(dna, mutant))

  if not mutant:
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Its a human! Abort!')
  
  return {
    "success": True,
    "dna": dna,
  }

@app.get('/stats')
def get_stats():
  dnas: list[DNADoc] = collection_dnas.find()

  stats = {
    C_HUMAN: 0,
    C_MUTANT: 0,
    RATIO: 0.0
  }

  for dna in dnas:
    if dna['is_mutant']:
      stats[C_MUTANT] += 1
    else:
      stats[C_HUMAN] += 1

  stats[RATIO] = stats[C_MUTANT] / stats[C_HUMAN] if stats[C_HUMAN] > 0 else float(stats[C_MUTANT])
  
  return stats
