#!/usr/bin/env python3
from flask import Flask, render_template, request, jsonify, send_file
import random
import time
import json
import os

app = Flask(__name__)

RELICS = {
    "Axi Y1": {
        "Common": [
            "Sevagoth Prime Neuroptics Blueprint",
            "Fang Prime Blueprint",
            "Forma Blueprint"
        ],
        "Uncommon": [
            "Lavos Prime Blueprint",
            "Paris Prime Upper Limb"
        ],
        "Rare": [
            "Yareli Prime Systems Blueprint"
        ]
    }
}

PROBABILITIES = {
    "Intact": {"Common": 76, "Uncommon": 22, "Rare": 2},
    "Exceptional": {"Common": 70, "Uncommon": 26, "Rare": 4},
    "Flawless": {"Common": 60, "Uncommon": 34, "Rare": 6},
    "Radiant": {"Common": 50, "Uncommon": 40, "Rare": 10}
}

@app.route('/')
def index():
    return render_template('index.html', relics=list(RELICS.keys()))

@app.route('/simulate', methods=['POST'])
def simulate():
    data = request.json
    players = data['players']
    results = []
    # Simulate opening for each player
    for player in players:
        relic_name = player['relic']
        refinement = player['refinement']
        if relic_name not in RELICS:
            return jsonify({"error": f"Relic {relic_name} not found"}), 400
        relic = RELICS[relic_name]
        probs = PROBABILITIES[refinement]
        # Determine rarity of drop
        rarity = random.choices(
            ["Common", "Uncommon", "Rare"],
            weights=[probs["Common"], probs["Uncommon"], probs["Rare"]],
            k=1
        )[0]
        # Select specific item
        item = random.choice(relic[rarity])
        # Color by rarity
        color = {
            "Common": "common",
            "Uncommon": "uncommon",
            "Rare": "rare"
        }[rarity]
        results.append({
            "relic": relic_name,
            "refinement": refinement,
            "rarity": rarity,
            "item": item,
            "color": color
        })
    return jsonify(results)

@app.route('/add_relic', methods=['POST'])
def add_relic():
    data = request.json
    relic_name = data['name']
    commons = data['commons']
    uncommons = data['uncommons']
    rares = data['rares']
    RELICS[relic_name] = {
        "Common": commons,
        "Uncommon": uncommons,
        "Rare": rares
    }
    return jsonify({"success": True, "relics": list(RELICS.keys())})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)