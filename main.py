from fastapi import FastAPI, File, UploadFile
from starlette.responses import HTMLResponse
# from authtoken import auth_token
# import torch
# from torch import autocast
# from diffusers import StableDiffusionPipeline

app = FastAPI()

# modelid = "CompVis/stable-diffusion-v1-4"
# device = "cuda"
# pipe = StableDiffusionPipeline.from_pretrained(modelid, revision="fp16", torch_dtype=torch.float16, use_auth_token=auth_token) 
# pipe.to(device)

# @app.post("/generate/")
# async def generate(prompt: str):
#     with autocast(device): 
#         image = pipe(prompt, guidance_scale=8.5)["sample"][0]
#     image.save('generatedimage.png')
    # return HTMLResponse(content=open('generatedimage.png', 'rb').read(), media_type="image/png")

@app.post("/generate")
def generate(prompt: str):
    return {"prompt": prompt + " received"}


