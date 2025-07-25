
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
5. Customization: You can change relics and rewards by editing the `RELICS` dictionary in `app.py`.

## Technologies Used
- Python (Flask)
- HTML, CSS, JavaScript

## How to Run
1. Make sure you have Python installed.
2. Make sure Python and pip are added to your system PATH (so you can run `python` and `pip` from any folder).
3. Install Flask:
   ```
   pip install flask
   ```
4. Run the app:
   ```
   python app.py
   ```
5. Open your browser and go to `http://localhost:5000`

## Things to Consider When Running the Webapp
- If you see an error like "python is not recognized as an internal or external command", you need to add Python to your PATH or restart your computer after installing Python.
- If `pip` is not found, you may need to install it or add it to your PATH.
- You may need to run the command prompt as administrator to install packages.
- If the app does not start, check for error messages and make sure Flask is installed.
- The script `run_first_time.bat` can help automate setup, but you may need to confirm prompts or fix PATH issues manually.

## Customization
You can change relics and rewards by editing the `RELICS` dictionary in `app.py`.

## License
MIT License. See LICENSE file for details.

---
This is a fan-made tool and not affiliated with Digital Extremes. Warframe is a registered trademark of Digital Extremes.
