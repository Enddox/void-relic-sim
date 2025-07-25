# void-relic-sim

Void Relic Sim is a simple web app that simulates opening Warframe Void Relics. You can select the relic (currently only Axi Y1), choose the refinement level, and see what rewards you would get, just like in the real game.

## Features
- Simulate opening the Axi Y1 relic for up to 4 players.
- Choose refinement level: Intact, Exceptional, Flawless, or Radiant.
- See random rewards based on official drop chances and item rarities.
- Add new relics and customize their rewards directly from the web interface.
- Modern, responsive UI styled for Warframe fans.

## How It Works
1. Select the number of players (1-4).
2. For each player, choose the relic and refinement level.
3. Click "Simulate Opening" to see the results for each player.
4. Rewards are randomly selected based on the chosen refinement and official drop rates.
5. You can add new relics and their rewards using the "Add New Relic" section.

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
- You can add new relics and their rewards from the web interface.
- To change the default relics, edit the `RELICS` dictionary in `app.py`.

## License
MIT License. See LICENSE file for details.

---
This is a fan-made tool and not affiliated with Digital Extremes. Warframe is a registered trademark of Digital Extremes.
