import core

detector = core.PhishDetector()

results = detector.check("https://ds-nitro.com/log")
print(results, "https://ds-nitro.com/log")
results_2 = detector.check("https://discord.com")
print(results_2, "https://google.com")