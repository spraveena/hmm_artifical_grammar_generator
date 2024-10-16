import numpy as np
from fractions import Fraction
import pandas as pd

pitch_probability = [0.45,0.35,0.20]
states = np.array([1,2,3,4,5,6,7,8,9]) 


#increase chords 2 and 3 - done
#decrease probability of repeating in stage 2 - done

#take in frequency output sine waves

#for last chord - increase probability of ending at 0 [85,10,6] - done

#decrease repetition of same pitch being chosen within one sequence

#ASDR envelope

transition_matrix = [
[0.2,  0.48, 0, 0.04, 0.08,   0.16, 0, 0.04,   0.  ],
 [0.,   0.4,   0.48,   0,  0.,   0,  0.12,  0.,   0.  ],
 [0.,   0.,   0.4,   0,  0.,   0,  0,  0.,   0.6  ],
 [0.,   0.6,   0.,   0,  0.3, 0.1,   0.,   0, 0.  ],
 [0.,   0.24,   0.48,   0.,   0.16, 0.,   0.12,   0, 0 ],
 [0.,   0.,   0.48,   0, 0.24, 0.16, 0.12,   0, 0.  ],
 [0.,   0.,   0.24,   0.,   0,   0, 0.16, 0, 0.6  ],
 [0.,   0.6,   0.,   0.,   0.3,   0.1,   0.,   0,  0 ],
 [1.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.  ]]

chords = np.array([
[0,6,10],
[0,4,7],
[3,7,10],
[1,7,11],
[3,8,12],
[4,10,13],
[7,10,13],
[5,9,12],
[0,6,10]
])


def generate_chord_sequence(length):
	
	chord_sequence = list()
	chord_sequence.append(1)
	sequence_probability = 1
	
	for j in range(length):
		next_state = np.random.choice(states,p=transition_matrix[chord_sequence[j]-1])
		if next_state == 9:
			break
		chord_sequence.append(next_state)
		probability = transition_matrix[chord_sequence[j]-1][next_state-1]

		#For debugging purposes
		# print('From {prev_state} to {next_state}'.format(prev_state = chord_sequence[j],next_state = next_state))
		# print('Probabilty: {p}'.format(p=probability))

		
		sequence_probability *= transition_matrix[chord_sequence[j]-1][next_state-1]


	return chord_sequence,sequence_probability

def pitch_from_chord_sequence(chord_sequence):
	pitch_sequence = list()
	n = 100000
	j = 0
	for i in range(len(chord_sequence)):
		if i == len(chord_sequence)-1:
			pitch = np.random.choice(chords[chord_sequence[i]-1],p=[0.85,0.10,0.05])
		else:
			pitch = np.random.choice(chords[chord_sequence[i]-1],p=pitch_probability)
			print('Old pitch: {pitch}'.format(pitch=pitch))
			print('Number of occurrences of pitch: {pitch_count}'.format(pitch_count=pitch_sequence.count(pitch)))
			while pitch_sequence.count(pitch)>1 and j<= n:
				pitch = np.random.choice(chords[chord_sequence[i]-1],p=pitch_probability)
				j = j+1
			print('New pitch: {pitch}'.format(pitch=pitch))
			print("--------------------------------------------------------------------------------------------------")
		
		pitch_sequence.append(pitch)

	return pitch_sequence


def main():

	number_of_sequences = 12000
	list_of_pitch_sequences = list()
	list_of_chord_sequences = list()
	sequence_count = 0
	for i in range(number_of_sequences):
		length_of_seq = np.random.randint(7,9)
		[chord_sequence,sequence_probability] = generate_chord_sequence(length_of_seq-1)

		if sequence_probability == 0 or chord_sequence[-1] !=3 and chord_sequence[-1] !=7 or len(chord_sequence) < 6:
			continue
		chord_sequence.append(9) #force sequences to end with 1		
		pitch_sequence = pitch_from_chord_sequence(chord_sequence)
		
		while pitch_sequence in list_of_pitch_sequences: #come up wtih another combination of pitches if pitch sequence already exists
			pitch_sequence = pitch_from_chord_sequence(chord_sequence)

		#For debugging purposes
		# print('Chord sequence {i}: {chord_sequence}'.format(i = sequence_count + 1,chord_sequence = str(chord_sequence)))
		# print('Probability of Chord sequence {i}: {probability}'.format(i = i,probability = str(sequence_probability)))
		# print('Music sequence {i}: {pitch_sequence}'.format(i = sequence_count + 1,pitch_sequence = str(pitch_sequence)))
		# print("----------------------------------------------------------------------")

		if pitch_sequence in list_of_pitch_sequences:
			continue
		
		list_of_pitch_sequences.append(pitch_sequence)
		list_of_chord_sequences.append(chord_sequence)
		sequence_count += 1

	output = list(zip(list_of_chord_sequences,list_of_pitch_sequences))
	df = pd.DataFrame(output,index=None)
	df.to_csv("1st_grammar_sequences.txt",header=["chord_sequence","pitch_sequence"],sep="\t",index=None)
	print('Number of sequences: {i}'.format(i = sequence_count))


	return list_of_chord_sequences


if __name__ == "__main__":
	main()



