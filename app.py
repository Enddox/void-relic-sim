#!/usr/bin/env python3
from flask import Flask, render_template, request, jsonify, send_file
import random
import time
import json
import os

app = Flask(__name__)

# Base de datos de reliquias (puede ser expandida)
RELIQUIAS = {
    "Lith A1": {
        "Comunes": ["Forma Blueprint", "Loki Prime Neuroptics", "Bo Prime Handle"],
        "Incomunes": ["Wyrm Prime Cerebrum", "Odonata Prime Wings"],
        "Raros": ["Loki Prime Blueprint"]
    },
    "Meso B1": {
        "Comunes": ["Forma Blueprint", "Ember Prime Neuroptics", "Glaive Prime Blade"],
        "Incomunes": ["Soma Prime Stock", "Hikou Prime Pouch"],
        "Raros": ["Frost Prime Systems"]
    },
    "Neo C1": {
        "Comunes": ["Forma Blueprint", "Rhino Prime Chassis", "Boltor Prime Barrel"],
        "Incomunes": ["Scindo Prime Blade", "Lex Prime Receiver"],
        "Raros": ["Nyx Prime Blueprint"]
    },
    "Axi D1": {
        "Comunes": ["Forma Blueprint", "Saryn Prime Chassis", "Vasto Prime Barrel"],
        "Incomunes": ["Nikana Prime Blade", "Vauban Prime Neuroptics"],
        "Raros": ["Ivara Prime Blueprint"]
    }
    ,
    "Axi Y1": {
        "Comunes": ["Forma Blueprint", "Paris Prime String", "Carrier Prime Cerebrum"],
        "Incomunes": ["Akstiletto Prime Barrel", "Vauban Prime Chassis"],
        "Raros": ["Ymir Prime Blueprint"]
    }
}

PROBABILIDADES = {
    "Intacto": {"Comunes": 76, "Incomunes": 22, "Raros": 2},
    "Excepcional": {"Comunes": 70, "Incomunes": 26, "Raros": 4},
    "Impecable": {"Comunes": 60, "Incomunes": 34, "Raros": 6},
    "Radiante": {"Comunes": 50, "Incomunes": 40, "Raros": 10}
}

@app.route('/')
def index():
    return render_template('index.html', relics=list(RELIQUIAS.keys()))

@app.route('/simulate', methods=['POST'])
def simulate():
    data = request.json
    players = data['players']
    results = []
    # Simular apertura para cada jugador
    for player in players:
        relic_name = player['relic']
        refinement = player['refinement']
        if relic_name not in RELIQUIAS:
            return jsonify({"error": f"Reliquia {relic_name} no encontrada"}), 400
        relic = RELIQUIAS[relic_name]
        probs = PROBABILIDADES[refinement]
        # Determinar rareza del drop
        rarity = random.choices(
            ["Comunes", "Incomunes", "Raros"],
            weights=[probs["Comunes"], probs["Incomunes"], probs["Raros"]],
            k=1
        )[0]
        # Seleccionar ítem específico
        item = random.choice(relic[rarity])
        # Color según rareza
        color = {
            "Comunes": "common",
            "Incomunes": "uncommon",
            "Raros": "rare"
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
    
    RELIQUIAS[relic_name] = {
        "Comunes": commons,
        "Incomunes": uncommons,
        "Raros": rares
    }
    
    return jsonify({"success": True, "relics": list(RELIQUIAS.keys())})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)