from db.models import DNA

def is_mutant(dna: DNA):
  n = len(dna)
  total_sequences = 0
  sequence_length = 4
  range_seq = range(sequence_length)

  for row in range(n):
    if total_sequences > 1:
      return True

    for col in range(n):
      if col <= n - sequence_length:
        horizontal_sequence = dna[row][col:col + sequence_length]
        total_sequences = check_seq(horizontal_sequence, total_sequences)

      # Eg. (0,0) -> (1,1) -> (2,2) -> (3,3)... (++,++) ↘
      if row <= n - sequence_length and col <= n - sequence_length:
        diagonal_sequence = [dna[row + i][col + i] for i in range_seq]
        total_sequences = check_seq(diagonal_sequence, total_sequences)

      # Eg. (4,0) -> (3,1) -> (2,2) -> (1,3)... (--,++) ↗
      if row >= sequence_length - 1 and col <= n - sequence_length:
        diagonal_sequence = [dna[row - i][col + i] for i in range_seq]
        total_sequences = check_seq(diagonal_sequence, total_sequences)

      if row <= n - sequence_length:
        vertical_sequence = [dna[row + i][col] for i in range_seq]
        total_sequences = check_seq(vertical_sequence, total_sequences)

  return False 

def check_seq(seq, total_sequences):
  if len(set(seq)) == 1:
    total_sequences += 1
  
  return total_sequences

