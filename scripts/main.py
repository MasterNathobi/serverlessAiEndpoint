from flask import Flask, request, jsonify

app = Flask(__name__)

# Placeholder model loading functions
def loadStableDiffusionModel():
    print("Stable Diffusion model loaded.")
    return "StableDiffusionModel"

def loadVaceModel():
    print("VACE model loaded.")
    return "VACEModel"

# Load models once at startup
stableModel = loadStableDiffusionModel()
vaceModel = loadVaceModel()

# Placeholder inference functions
def runStableDiffusion(prompt):
    return f"Generated image from Stable Diffusion using prompt: '{prompt}'"

def runVace(prompt):
    return f"Generated video frame from VACE using prompt: '{prompt}'"

@app.route("/", methods=["POST"])
def generate():
    data = request.get_json()
    mode = data.get("mode", "").lower()
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"error": "Missing 'prompt' in request"}), 400

    if mode == "stable":
        result = runStableDiffusion(prompt)
    elif mode == "vace":
        result = runVace(prompt)
    else:
        return jsonify({"error": "Invalid mode. Use 'stable' or 'vace'."}), 400

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
