num_frames = 16
fps = 24 // 3
image_size = (256, 256)

# Define model
model = dict(
    type="STDiT-XL/2",
    space_scale=0.5,
    time_scale=1.0,
    enable_flashattn=True,
    enable_layernorm_kernel=True,
    from_pretrained="PRETRAINED_MODEL",
)
vae = dict(
    type="VideoAutoencoderKL",
    from_pretrained="stabilityai/sd-vae-ft-ema",
)
text_encoder = dict(
    type="t5",
    from_pretrained="./pretrained_models/t5_ckpts",
    model_max_length=120,
)
scheduler = dict(
    type="iddpm",
    num_sampling_steps=100,
    cfg_scale=7.0,
)
dtype = "fp16"

# Others
batch_size = 2
seed = 42
prompt_path = "./assets/texts/t2v_samples.txt"
save_dir = "./outputs/samples/"
