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
    },
    "Lith Y1": {
        "Common": [
            "Lex Prime Barrel",
            "Braton Prime Blueprint",
            "Nautilus Prime Carapace"
        ],
        "Uncommon": [
            "Zylok Prime Receiver",
            "Trumna Prime Stock"
        ],
        "Rare": [
            "Yareli Prime Neuroptics Blueprint"
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
    try:
        data = request.json
        if not data or 'players' not in data:
            return jsonify({"error": "Invalid request data"}), 400
        
        players = data['players']
        results = []
        
        # Validar que PROBABILITIES contenga el refinamiento
        valid_refinements = list(PROBABILITIES.keys())
        
        # Simulate opening for each player
        for player in players:
            if 'relic' not in player or 'refinement' not in player:
                return jsonify({"error": "Each player must have 'relic' and 'refinement' fields"}), 400
                
            relic_name = player['relic']
            refinement = player['refinement']
            
            if relic_name not in RELICS:
                return jsonify({"error": f"Relic {relic_name} not found"}), 400
            
            if refinement not in PROBABILITIES:
                return jsonify({"error": f"Invalid refinement {refinement}. Valid options: {valid_refinements}"}), 400
                
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
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '0.0.0.0')
    debug = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    app.run(host=host, port=port, debug=debug)