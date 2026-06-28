import os
import urllib.request

def download_piper_models():
    directory = 'piper_voices'
    base_url = "https://huggingface.co/rhasspy/piper-voices/resolve/main"

    print("Checking for missing Piper ONNX models...")
    
    for filename in os.listdir(directory):
        if filename.endswith(".onnx.json"):
            model_name = filename.replace(".onnx.json", "")
            onnx_path = os.path.join(directory, f"{model_name}.onnx")
            
            if not os.path.exists(onnx_path):
                # Parse model name (e.g., en_US-lessac-medium)
                parts = model_name.split("-")
                lang_region = parts[0]
                lang = lang_region.split("_")[0]
                voice = parts[1]
                quality = parts[2]
                
                # Construct huggingface url
                url = f"{base_url}/{lang}/{lang_region}/{voice}/{quality}/{model_name}.onnx"
                
                print(f"Downloading {model_name}.onnx (this may take a minute)...")
                try:
                    urllib.request.urlretrieve(url, onnx_path)
                    print(f"Successfully downloaded {model_name}.onnx!")
                except Exception as e:
                    print(f"Failed to download {model_name}: {e}")
            else:
                print(f"{model_name}.onnx already exists. Skipping.")

if __name__ == "__main__":
    download_piper_models()
