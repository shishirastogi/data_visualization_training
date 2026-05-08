import json
import os

def process_config(filepath):
    """Reads a config, modifies it, and saves as JSON."""
    default_config = {
        "app_name": "DataVizTraining",
        "version": "1.0",
        "debug_mode": False
    }
    
    # Write default
    print("Writing default config...")
    with open(filepath, "w") as f:
        json.dump(default_config, f, indent=4)
        
    # Read and update
    try:
        with open(filepath, "r") as f:
            config = json.load(f)
            
        print(f"Loaded config for {config['app_name']}")
        config["debug_mode"] = True
        config["version"] = "1.1"
        
        with open(filepath, "w") as f:
            json.dump(config, f, indent=4)
        print("Config updated successfully.")
        
    except FileNotFoundError:
        print(f"Error: {filepath} not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")

if __name__ == "__main__":
    process_config("app_config.json")
