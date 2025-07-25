
# void-relic-sim

Void Relic Sim is a simple web app that simulates opening Warframe Void Relics. You can select the relic, choose the refinement level, and see what rewards you would get, just like in the real game.

## Features
- Simulate opening any supported relic for up to 4 players.
- Choose refinement level: Intact, Exceptional, Flawless, or Radiant.
- See random rewards based on official drop chances and item rarities.
- Simple, clean UI styled for Warframe fans.
- Drop colors: Common = bronze, Uncommon = silver, Rare = gold.

## How It Works
1. Select the number of players (1-4).
2. For each player, choose the relic and refinement level.
3. Click "Simulate Opening" to see the results for each player.
4. Rewards are randomly selected based on the chosen refinement and official drop rates.
5. To add new relics, edit the `RELICS` dictionary in `app.py` as the developer.

## Technologies Used
- Python (Flask)
- HTML, CSS, JavaScript

## How to Run
1. Make sure you have Python installed.
2. Install Flask:
   ```
   pip install flask
   ```
3. Run the app:
   ```
   python app.py
   ```
4. Open your browser and go to `http://localhost:5000`

## Customization
- To add or change relics and their rewards, edit the `RELICS` dictionary in `app.py`.

## License
MIT License. See LICENSE file for details.

---
This is a fan-made tool and not affiliated with Digital Extremes. Warframe is a registered trademark of Digital Extremes.
