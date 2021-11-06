# PhishDetector
This module was made so you can check a URL and see if it's in discord's official list of phishing and suspicious URLs.

## Installation
``pip install phish-detector``

## Usage
```python
from phish_detector import PhishDetector

detector = PhishDetector()

results = detector.check("https://ds-nitro.com/log")
print(results, "https://ds-nitro.com/log") # True
results_2 = detector.check("https://discord.com")
print(results_2, "https://google.com") # False
```