# 🎵 Artificial Grammar-Based Chord Sequence Generator

This repository contains a Hidden Markov Model (HMM)-based Python tool for generating musically informed chord and pitch sequences. It simulates probabilistic musical grammar, with an emphasis on realistic transitions, constrained pitch repetition, and harmonically meaningful sequences — suitable for auditory neuroscience, BCI stimulus creation, or music cognition experiments.

---

## 🧠 Purpose

To generate synthetic chord sequences governed by a structured probabilistic grammar. These sequences can be used as stimuli for behavioral or neuroimaging studies investigating musical expectation, prediction, or perception.

---

## 🚀 Features

- Hidden Markov model (HMM)–based state transitions between chords
- Transition matrix tailored to reflect harmonic structure
- Constrained pitch selection with probabilistic weighting
- Repetition-avoidance logic for pitch realism
- Output in both **chord sequences** and **flattened pitch sequences**
- Probabilistic weighting favors cadences and closure on final chords

---

## 📜 Script Overview

### `1st_grammar_seq_generator.py`

This script includes:

- `generate_chord_sequence(length)`:  
  Constructs a sequence of chords based on an HMM-like transition matrix.

- `pitch_from_chord_sequence(chord_sequence)`:  
  Samples pitches from each chord with weighted probabilities and repetition suppression.

- `main()`:  
  Generates a batch of sequences and stores them in memory. Configurable for experimental batch runs.

---


## 💡 Future Directions

- MIDI/audio export of sequences
- Integration with timbre synthesis engines
- Visualization of transition probabilities
- Extension to polyphonic or rhythmic structures

## 📖 Citation 

If you use this tool in your own work, please cite:

```
spraveena. (2024). spraveena/ArtificialGrammarGenerator: Hidden Markov Model (HMM) for
Chord Sequence Generation (v1.0.0). Zenodo. https://doi.org/10.5281/zenodo.13937536
```
the Bibtex format is as follows:
```
@software{spraveena_2024_13937536,
  author       = {spraveena},
  title        = {spraveena/ArtificialGrammarGenerator: Hidden
                   Markov Model (HMM) for Chord Sequence Generation
                  },
  month        = oct,
  year         = 2024,
  publisher    = {Zenodo},
  version      = {v1.0.0},
  doi          = {10.5281/zenodo.13937536},
  url          = {https://doi.org/10.5281/zenodo.13937536},
}
```
