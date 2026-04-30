# Generative Models: Diffusion, VAEs, GANs

## Table of Contents
1. [Diffusion Models](#diffusion-models)
2. [Variational Autoencoders](#variational-autoencoders)
3. [Generative Adversarial Networks](#generative-adversarial-networks)
4. [Normalizing Flows](#normalizing-flows)
5. [Latent Diffusion and Stable Diffusion](#latent-diffusion-and-stable-diffusion)

---

## Diffusion Models

### Forward Process (Adding Noise)
Given data x₀, gradually add Gaussian noise over T steps:
q(x_t | x_{t-1}) = N(x_t; √(1-β_t) x_{t-1}, β_t I)

where β_t is the noise schedule (small values, e.g., β₁=10⁻⁴ to β_T=0.02).

**Closed-form for any timestep t:**
q(x_t | x₀) = N(x_t; √ᾱ_t x₀, (1-ᾱ_t)I)
where α_t = 1-β_t and ᾱ_t = Π_{s=1}^{t} α_s

At t=T, x_T ≈ N(0, I) (pure noise).

### Reverse Process (Denoising)
Learn to reverse: p_θ(x_{t-1} | x_t) = N(x_{t-1}; μ_θ(x_t, t), Σ_θ(x_t, t))

**DDPM parameterization:** Instead of predicting μ directly, predict the noise ε:
μ_θ(x_t, t) = (1/√α_t)(x_t - (β_t/√(1-ᾱ_t)) ε_θ(x_t, t))

**Training loss (simplified):**
L = E_{t, x₀, ε} [‖ε - ε_θ(√ᾱ_t x₀ + √(1-ᾱ_t)ε, t)‖²]

Just MSE between true noise and predicted noise.

### Score Matching Perspective
The score function ∇_x log p(x) points toward higher density.

Score matching: train s_θ(x, t) ≈ ∇_{x_t} log q(x_t)
Connection: ε_θ(x_t, t) = -√(1-ᾱ_t) · s_θ(x_t, t)

This connects DDPM to score-based generative models (Song & Ermon).

### DDIM (Denoising Diffusion Implicit Models)
Deterministic sampling process (same noise → same output):
x_{t-1} = √ᾱ_{t-1} · predicted_x₀ + √(1-ᾱ_{t-1}) · direction_to_x_t

Key benefit: Can skip steps (e.g., 1000→50 steps) with minimal quality loss.

### Classifier-Free Guidance
Train model both conditional and unconditional (randomly drop conditioning).
At inference, amplify the conditional signal:
ε̃ = ε_uncond + w · (ε_cond - ε_uncond)

where w > 1 is the guidance scale (typically 7-15).
Higher w → more adherence to prompt, less diversity.

### U-Net Architecture (for diffusion)
- Encoder: downsample with ResBlocks + self-attention
- Bottleneck: attention at lowest resolution
- Decoder: upsample with ResBlocks + cross-attention (to text embeddings)
- Skip connections between encoder and decoder
- Time embedding: sinusoidal → MLP → add to each ResBlock
- Text conditioning: CLIP text embeddings → cross-attention

### DiT (Diffusion Transformer)
Replace U-Net with a transformer:
- Patch input → sequence of tokens
- AdaLN-Zero for time/class conditioning
- Standard transformer blocks with self-attention
- Scales better than U-Net at large compute budgets

---

## Variational Autoencoders

### Architecture
- **Encoder** q_φ(z|x): Maps input x to distribution over latent z
- **Decoder** p_θ(x|z): Maps latent z back to reconstruction

### Evidence Lower Bound (ELBO)
log p(x) ≥ E_{q(z|x)}[log p(x|z)] - KL(q(z|x) || p(z))

= Reconstruction loss - KL divergence (regularization)

### Reparameterization Trick
To backpropagate through sampling z ~ N(μ, σ²):
z = μ + σ ⊙ ε, where ε ~ N(0, I)

Gradients flow through μ and σ (deterministic path), not through the sampling.

### VQ-VAE (Vector Quantized)
Replace continuous latent with discrete codebook:
1. Encoder outputs continuous z_e
2. Quantize to nearest codebook entry: z_q = argmin_k ‖z_e - e_k‖
3. Decoder reconstructs from z_q

**Straight-through estimator:** Copy gradients from z_q to z_e (not differentiable otherwise).
**Used in:** DALL-E (original), audio generation (SoundStream), video tokenization.

### β-VAE
Scale the KL term: L = Reconstruction - β · KL
- β > 1: More disentangled latent factors, worse reconstruction
- β < 1: Better reconstruction, less structured latent space

---

## Generative Adversarial Networks

### Min-Max Game
min_G max_D V(D, G) = E_{x~p_data}[log D(x)] + E_{z~p_z}[log(1 - D(G(z)))]

- **Generator G:** Maps noise z → fake data. Tries to fool D.
- **Discriminator D:** Classifies real vs fake. Tries to distinguish.

### Training Instabilities
- **Mode collapse:** G produces limited variety (maps many z to same output)
- **Vanishing gradients:** If D is too good, G gets no useful gradient
- **Non-convergence:** Oscillation between G and D

### Wasserstein GAN (WGAN)
Replace JS divergence with Wasserstein distance:
min_G max_{D∈1-Lipschitz} E_{x~p_data}[D(x)] - E_{z~p_z}[D(G(z))]

- Lipschitz constraint: gradient penalty (WGAN-GP) or spectral normalization
- More stable training, meaningful loss curve

### StyleGAN Architecture
1. Mapping network: z → w (intermediate latent space via 8 FC layers)
2. Synthesis network: w controls style at each resolution via AdaIN
3. Progressive training: start low-res, gradually add higher-res layers
4. Stochastic variation: per-pixel noise injection for fine details

### Key GAN Variants
| Model | Innovation | Application |
|-------|-----------|-------------|
| DCGAN | Convolutional GAN, batch norm | Image generation |
| CycleGAN | Unpaired image-to-image translation | Style transfer |
| Pix2Pix | Paired image-to-image with conditional GAN | Edges→photos |
| StyleGAN 2/3 | State-of-the-art face generation | Synthesis |
| GigaGAN | Scaling GAN to 1B params | Text-to-image |

---

## Normalizing Flows

### Idea
Transform simple distribution (N(0,I)) through a chain of invertible functions:
x = f_K ∘ f_{K-1} ∘ ... ∘ f_1(z)

Exact likelihood: log p(x) = log p(z) - Σ log |det(∂f_k/∂z_k)|

**Key constraint:** Each f_k must be invertible with tractable Jacobian determinant.

### Flow Types
- **RealNVP:** Affine coupling layers. Half variables transform the other half.
- **Glow:** 1×1 invertible convolutions + affine coupling.
- **Continuous flows (FFJORD):** Neural ODE-based. Exact likelihood via Hutchinson trace estimator.
- **Flow matching:** Learn velocity field for ODE. Used in Stable Diffusion 3.

---

## Latent Diffusion and Stable Diffusion

### Latent Diffusion Model (LDM)
Key insight: Run diffusion in a compressed latent space, not pixel space.

1. **VAE encoder** compresses 512×512×3 → 64×64×4 (8× spatial compression)
2. **Diffusion** operates in this 64×64×4 latent space
3. **VAE decoder** reconstructs 64×64×4 → 512×512×3

Benefits: ~64× less computation than pixel-space diffusion.

### Stable Diffusion Pipeline
1. **Text encoder (CLIP):** "A cat on a beach" → text embeddings
2. **Noise scheduler:** Initialize with pure noise latent
3. **U-Net denoiser:** Iteratively denoise, conditioned on text via cross-attention
4. **VAE decoder:** Latent → pixel image

### Stable Diffusion Versions
| Version | Text Encoder | Denoiser | Key Improvement |
|---------|-------------|----------|-----------------|
| SD 1.5 | CLIP ViT-L/14 | U-Net | Base model |
| SD 2.1 | OpenCLIP ViT-H | U-Net | Better text understanding |
| SDXL | Dual CLIP encoders | Larger U-Net | 1024×1024, better quality |
| SD 3 | T5 + CLIP (×2) | DiT (MM-DiT) | Flow matching, transformer backbone |
| FLUX | T5 + CLIP | DiT variant | Black Forest Labs, state-of-the-art |

### ControlNet
Add spatial control to diffusion models:
- Copy U-Net encoder, add zero-conv connections to original U-Net
- Condition on: edges (Canny), depth, pose, segmentation maps
- "Locked copy" preserves pretrained quality while learning new conditions
