# Cocktail Party Problem using ICA

## Overview

This project implements the Cocktail Party Problem, where multiple audio sources are mixed together and need to be separated into their original signals.

We use Independent Component Analysis (ICA), an unsupervised machine learning algorithm, to perform blind source separation on two mixed audio inputs.

---

## How it works

* Two microphones record mixed audio signals
* Each recording contains a different combination of the same sources
* ICA assumes the original sources are statistically independent
* The algorithm separates the mixed signals into independent components

---

## Project Structure

```bash
cocktail_ica/
│
├── mic1.mp3
├── mic2.mp3
├── src/
│   └── main.py
├── requirements.txt
└── .gitignore
```

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## How to Run

```bash
cd src
python main.py
```

---

## Input

* `mic1.mp3` → mixed audio signal 1
* `mic2.mp3` → mixed audio signal 2

Both inputs must be mixtures of the same sources, not separate clean audio files.

---

## Output

* `source1.mp3` → separated signal
* `source2.mp3` → separated signal

---

## Example Concept

```text
mic1 = speaker1 + speaker2
mic2 = speaker1 + speaker2 (different mix)

↓ ICA ↓

source1 ≈ speaker1
source2 ≈ speaker2
```

---

## Machine Learning Used

* Type: Unsupervised Learning
* Algorithm: FastICA
* Library: scikit-learn

---

## Applications

* Speech separation
* Noise reduction
* Audio signal processing
* Hearing aids
* Surveillance systems

---

## Limitations

* Output signals may be swapped or inverted
* Works best when sources are independent
* Performance depends on input quality

---

## Future Improvements

* Improve separation using deep learning models
* Add visualization of signals
* Support real-time audio processing

---

## Author

Vaidehi Gupta

