from pydantic import BaseModel

class DNA(BaseModel):
  dna: list[str]

class DNADoc(BaseModel):
  dna: DNA
  is_mutant: bool