#!/usr/bin/env python3
from flask import Flask, render_template, request, jsonify, send_file
import random
import time
import json
import os

app = Flask(__name__)

RELICS = {
    "Lith A1": {
        "Common": ["Forma Blueprint", "Loki Prime Neuroptics", "Bo Prime Handle"],
        "Uncommon": ["Wyrm Prime Cerebrum", "Odonata Prime Wings"],
        "Rare": ["Loki Prime Blueprint"]
    },
    "Meso B1": {
        "Common": ["Forma Blueprint", "Ember Prime Neuroptics", "Glaive Prime Blade"],
        "Uncommon": ["Soma Prime Stock", "Hikou Prime Pouch"],
        "Rare": ["Frost Prime Systems"]
    },
    "Neo C1": {
        "Common": ["Forma Blueprint", "Rhino Prime Chassis", "Boltor Prime Barrel"],
        "Uncommon": ["Scindo Prime Blade", "Lex Prime Receiver"],
        "Rare": ["Nyx Prime Blueprint"]
    },
    "Axi D1": {
        "Common": ["Forma Blueprint", "Saryn Prime Chassis", "Vasto Prime Barrel"],
        "Uncommon": ["Nikana Prime Blade", "Vauban Prime Neuroptics"],
        "Rare": ["Ivara Prime Blueprint"]
    },
    "Axi Y1": {
        "Common": ["Forma Blueprint", "Paris Prime String", "Carrier Prime Cerebrum"],
        "Uncommon": ["Akstiletto Prime Barrel", "Vauban Prime Chassis"],
        "Rare": ["Ymir Prime Blueprint"]
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