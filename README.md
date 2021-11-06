# PhishDetector
This module was made so you can check a URL and see if it's in discord's official list of phishing and suspicious URLs.

## Usage
```python
import core
detector = core.PhishDetector()

results = detector.check("https://ds-nitro.com/log") # True
results_2 = detector.check("https://discord.com") # False
```