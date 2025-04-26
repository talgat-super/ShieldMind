import random

# Simulated simple ML model
attack_types = ["DDoS", "SQL Injection", "XSS", "Brute Force", "Phishing"]

def predict_attack(source_ip: str, destination_ip: str) -> dict:
    # Randomly pick an attack type
    attack_type = random.choice(attack_types)

    # Generate a random risk score between 0.3 and 1.0
    risk_score = round(random.uniform(0.3, 1.0), 2)

    return {
        "attack_type": attack_type,
        "risk_score": risk_score
    }
