import random

# Имитационная простая модель МО
attack_types = ["DDoS", "SQL Injection", "XSS", "Brute Force", "Phishing"]

def predict_attack(source_ip: str, destination_ip: str) -> dict:
   # Случайным образом выбрать тип атаки
    attack_type = random.choice(attack_types)

    # Сгенерировать случайную оценку риска от 0,3 до 1,0
    risk_score = round(random.uniform(0.3, 1.0), 2)

    return {
        "attack_type": attack_type,
        "risk_score": risk_score
    }
