cat > test_chatterbox.py << 'EOF'
#!/usr/bin/env python3
import os
import torch

# KRITICKÁ OPRAVA: Nastavení pro CPU před importem
os.environ['CUDA_VISIBLE_DEVICES'] = ''
torch.set_default_tensor_type(torch.FloatTensor)

from chatterbox.tts import ChatterboxTTS
import torchaudio as ta

# Patch torch.load
original_load = torch.load
def patched_load(*args, **kwargs):
    kwargs['map_location'] = 'cpu'
    return original_load(*args, **kwargs)
torch.load = patched_load

try:
    print("Načítám model...")
    model = ChatterboxTTS.from_pretrained(device='cpu')
    print("Model načten úspěšně!")
    
    text = "Dobrý den, toto je test českého textu."
    print("Generuji řeč...")
    wav = model.generate(text)
    ta.save("test.wav", wav, model.sr)
    print("Test úspěšný! Soubor test.wav byl vytvořen.")
    
finally:
    torch.load = original_load
    
EOF