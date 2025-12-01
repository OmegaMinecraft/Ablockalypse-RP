#!/usr/bin/env python3
"""Create missing candle block models."""

import json
from pathlib import Path

# Mapping of item model references to block model names
candle_models = {
    "purple_candle": "purple_candle",
    "lime_candle": "lime_candle",
    "red_candle": "red_candle",
    "pink_candle": "pink_candle",
    "blue_candle_black": "blue_candle",
    "black_candle_clear_white": "black_candle",
    "orange_candle_clean_thin": "orange_candle",
    "cyan_candle_clean": "cyan_candle",
    "magenta_candle_white": "magenta_candle",
    "brown_candle_white": "brown_candle",
    "green_candle_black": "green_candle",
    "yellow_candle_white": "yellow_candle",
    "light_blue_candle_white": "light_blue_candle",
}

block_models_dir = Path("assets/minecraft/models/block")
block_models_dir.mkdir(parents=True, exist_ok=True)

for model_name, texture_name in candle_models.items():
    model_path = block_models_dir / f"{model_name}.json"
    
    model_data = {
        "parent": "minecraft:block/candle_one_candle",
        "textures": {
            "candle": f"minecraft:block/{texture_name}",
            "particle": f"minecraft:block/{texture_name}"
        }
    }
    
    with open(model_path, 'w') as f:
        json.dump(model_data, f, indent=2)
    
    print(f"✓ Created {model_name}.json")

print(f"\nCreated {len(candle_models)} candle block models")
