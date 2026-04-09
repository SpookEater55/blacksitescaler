import gradio as gr
from PIL import Image
import os

css = """
body, .gradio-container { background: #0a0a0a !important; color: #ffffff !important; font-family: 'Inter', system-ui, sans-serif; }
.gradio-container { max-width: 1100px; margin: 0 auto; padding: 20px; }
h1 { font-size: 48px !important; font-weight: 900; background: linear-gradient(90deg, #c026d3, #a855f7); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center; margin-bottom: 8px; text-shadow: 0 0 30px rgba(192, 38, 211, 0.5); }
h2 { color: #aaaaaa; text-align: center; font-weight: 400; margin-bottom: 30px; }
.button { background: #111111 !important; border: 2px solid #c026d3 !important; color: #c026d3 !important; font-weight: 700; font-size: 18px; padding: 16px 32px; border-radius: 9999px; transition: all 0.3s ease; }
.button:hover { background: #c026d3 !important; color: #000000 !important; transform: scale(1.05); box-shadow: 0 0 25px #c026d3; }
.upload-box { border: 2px dashed #c026d3 !important; border-radius: 16px; background: #1a1a1a; }
.output-image { border-radius: 16px; border: 1px solid #222; }
"""

def upscale_image(image, mode):
    if image is None:
        return None
    return image

with gr.Blocks(css=css, title="blacksite scaler") as demo:
    # 🔥 RICHADS PUSH SCRIPT
    gr.HTML('''<script type="module" src="https://richinfo.co/richpartners/push/js/rp-cl-ob.js?pubid=1007787&siteid=393464&niche=33" async data-cfasync="false"></script>''')
    
    gr.Markdown("# BLACKSITE SCALER")
    gr.Markdown("## Dual-Mode AI Image Upscaler")
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### Standard Upscale (×4)")
            btn_standard = gr.Button("4× UPSCALE", size="large", elem_classes=["button"])
        with gr.Column(scale=1):
            gr.Markdown("### Premium Upscale (×8) ✨")
            btn_premium = gr.Button("8× UPSCALE", size="large", elem_classes=["button"])
    
    with gr.Row():
        with gr.Column():
            input_image = gr.Image(label="Upload Source Image", type="pil", height=500, elem_classes=["upload-box"])
        with gr.Column():
            output_image = gr.Image(label="Upscaled Result", height=500, elem_classes=["output-image"])
    
    gr.Markdown('<div style="text-align: center; margin-top: 20px; padding: 10px; opacity: 0.65;"><p style="margin: 0; font-size: 16pt;">created by 6nova / powered by gradio</p></div>')

    btn_standard.click(fn=lambda img: upscale_image(img, "4x"), inputs=input_image, outputs=output_image)
    btn_premium.click(fn=lambda img: upscale_image(img, "8x"), inputs=input_image, outputs=output_image)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=int(os.getenv("PORT", 7860)), share=False, show_error=True)
