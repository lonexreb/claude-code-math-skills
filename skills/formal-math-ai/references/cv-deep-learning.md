# Deep Learning for Computer Vision

## Table of Contents
1. [CNN Foundations](#cnn-foundations)
2. [Image Classification Architectures](#image-classification-architectures)
3. [Object Detection](#object-detection)
4. [Semantic and Instance Segmentation](#semantic-and-instance-segmentation)
5. [Vision Transformers](#vision-transformers)
6. [3D Vision and Neural Rendering](#3d-vision-and-neural-rendering)
7. [Self-Supervised and Foundation Models](#self-supervised-and-foundation-models)

---

## CNN Foundations

### Convolutional Layer
Output[i,j] = Σ_m Σ_n Input[i+m, j+n] · Kernel[m,n] + bias

**Parameters:** Kernel size K, stride S, padding P, dilation D.
Output size: floor((W + 2P - D(K-1) - 1) / S) + 1

**Key properties:**
- Parameter sharing: same kernel across spatial locations
- Translation equivariance: shift input → shift output
- Local connectivity: each output depends on local receptive field

### Pooling
- **Max pooling:** Take max in window. Most common. Translation invariance.
- **Average pooling:** Take mean. Used in final layers (global average pooling).
- **Stride-2 convolution** often replaces pooling in modern architectures.

### Batch Normalization
For each channel: x̂ = (x - μ_B) / √(σ²_B + ε), then y = γx̂ + β
- μ_B, σ²_B: batch statistics (training) / running statistics (inference)
- γ, β: learned affine parameters
- Enables higher learning rates, acts as regularizer

### Common Building Blocks
- **Residual connection:** y = F(x) + x (skip connection). Enables training very deep nets.
- **Bottleneck block:** 1×1 → 3×3 → 1×1 convolutions. Reduces parameters.
- **Depthwise separable:** Depthwise conv (per-channel) + pointwise 1×1. MobileNet.
- **Squeeze-and-Excitation:** Channel attention via global pool → FC → sigmoid → rescale.

---

## Image Classification Architectures

| Architecture | Year | Key Innovation | Top-1 (ImageNet) | Params |
|-------------|------|----------------|-------------------|--------|
| AlexNet | 2012 | ReLU, dropout, GPU training | 63.3% | 60M |
| VGGNet | 2014 | Very deep (16-19 layers), 3×3 only | 74.5% | 138M |
| GoogLeNet/Inception | 2014 | Inception modules, 1×1 convs | 74.8% | 6.8M |
| ResNet | 2015 | Residual connections | 76.3% (50L) | 25.6M |
| DenseNet | 2017 | Dense connections (each layer → all subsequent) | 77.2% | 20M |
| EfficientNet | 2019 | Compound scaling (depth × width × resolution) | 84.4% (B7) | 66M |
| ConvNeXt | 2022 | Modernized ResNet matching ViT | 87.8% (XL) | 350M |

### ResNet Deep Dive
**Problem:** Very deep networks suffer from degradation (not vanishing gradients).
**Solution:** Learn residual F(x) = H(x) - x instead of H(x) directly.

Block: y = F(x, {W_i}) + x
- If F = 0 is optimal, just learn zero weights (easy)
- Identity shortcuts: no extra parameters, no extra computation
- Enables training 100+ layer networks

**Variants:** ResNet-50 (bottleneck), ResNeXt (grouped convolutions), Wide ResNet.

---

## Object Detection

### Two-Stage Detectors
**Faster R-CNN pipeline:**
1. Backbone (ResNet/FPN) extracts features
2. Region Proposal Network (RPN): propose ~2000 candidate boxes
3. RoI Pooling/Align: extract fixed-size features per proposal
4. Classification head + bounding box regression

**Feature Pyramid Network (FPN):** Multi-scale feature maps via top-down pathway + lateral connections. Essential for detecting objects at different scales.

### Single-Stage Detectors
**YOLO (You Only Look Once):**
- Divide image into S×S grid
- Each cell predicts B boxes + confidence + class probabilities
- Single forward pass → real-time detection
- YOLOv8/YOLO11: current SOTA for speed-accuracy tradeoff

**SSD:** Multi-scale detection from multiple feature map levels.
**RetinaNet:** Focal loss to address class imbalance: FL(p) = -α(1-p)^γ log(p)

### Transformer-Based Detection
**DETR (Detection Transformer):**
- No anchors, no NMS, no hand-designed components
- Set prediction: Hungarian matching for loss
- Encoder-decoder transformer on CNN features
- Object queries (learned embeddings) → predictions

**RT-DETR, DINO, Co-DETR:** Improved DETR variants with faster convergence.

### Metrics
- **IoU (Intersection over Union):** |A∩B| / |A∪B|
- **AP (Average Precision):** Area under precision-recall curve at IoU threshold
- **mAP:** Mean AP across classes. mAP@0.5, mAP@0.5:0.95 (COCO metric)
- **AR (Average Recall):** Max recall at fixed number of detections

---

## Semantic and Instance Segmentation

### Semantic Segmentation (per-pixel class)
- **FCN:** Fully Convolutional Network. Replace FC layers with conv. Upsample with transposed conv.
- **U-Net:** Encoder-decoder with skip connections. Gold standard for medical imaging.
- **DeepLab v3+:** Atrous spatial pyramid pooling (ASPP) + encoder-decoder.
- **SegFormer:** Transformer encoder + lightweight MLP decoder.

### Instance Segmentation (per-object mask)
- **Mask R-CNN:** Faster R-CNN + parallel mask branch (per-RoI binary mask).
- **YOLACT:** Real-time instance segmentation via prototype masks.
- **Segment Anything (SAM):** Foundation model for promptable segmentation. Zero-shot.

### Panoptic Segmentation
Unifies semantic (stuff) + instance (things). Every pixel gets class + instance ID.
- **Panoptic FPN:** Combines FPN detection + semantic segmentation.
- **Mask2Former:** Unified transformer architecture for all three segmentation tasks.

### Loss Functions
- **Cross-entropy:** Standard per-pixel classification loss
- **Dice loss:** 2|A∩B| / (|A|+|B|). Good for imbalanced classes.
- **Focal loss:** Down-weights easy examples. Addresses class imbalance.
- **Lovász-Softmax:** Smooth extension of IoU loss. Directly optimizes IoU.

---

## Vision Transformers

### ViT (Vision Transformer)
1. Split image into 16×16 patches
2. Linear embedding of each patch → sequence of tokens
3. Add learnable position embeddings + [CLS] token
4. Standard transformer encoder (multi-head self-attention + MLP)
5. [CLS] token → classification head

**Key insight:** With enough data (JFT-300M), pure transformers match/beat CNNs.
**Limitation:** Quadratic attention cost O(n²) in number of patches.

### Efficient Vision Transformers
- **DeiT:** Data-efficient training via distillation + strong augmentation
- **Swin Transformer:** Shifted window attention — local attention + cross-window info flow. Linear complexity.
- **PVT/PVTv2:** Pyramid vision transformer. Spatial reduction in attention.

### Hybrid Approaches
- **ConvNeXt:** Pure CNN that matches Swin Transformer. "Modernized ResNet."
- **CoAtNet:** Combine depthwise conv (local) + attention (global) in different stages.
- **EfficientViT:** Efficient multi-scale attention for mobile deployment.

---

## 3D Vision and Neural Rendering

### NeRF (Neural Radiance Fields)
Represent scene as continuous function: F(x,y,z,θ,φ) → (color, density)
- MLP maps 5D input (3D position + 2D viewing direction) → RGB + σ
- Volume rendering: C(r) = ∫ T(t)σ(t)c(t) dt where T(t) = exp(-∫σ(s)ds)
- Train from multi-view images only (no 3D supervision)

**Variants:** Instant-NGP (hash encoding, real-time), Mip-NeRF 360, Zip-NeRF, Nerfacto.

### 3D Gaussian Splatting
Represent scene as millions of 3D Gaussians:
- Each Gaussian: position, covariance, opacity, spherical harmonics (color)
- Differentiable rasterization (no ray marching)
- 30-100× faster rendering than NeRF. Real-time at 1080p.

### Monocular Depth Estimation
Single image → depth map:
- **MiDaS/DPT:** Relative depth from transformer encoder
- **ZoeDepth/Depth Anything:** Metric depth estimation
- **Marigold:** Diffusion-based depth, state-of-the-art zero-shot

---

## Self-Supervised and Foundation Models

### Contrastive Learning
- **SimCLR:** Augmented views of same image should be close, different images far
- **MoCo:** Momentum encoder for large negative queue
- **BYOL/SimSiam:** No negatives needed — stop-gradient prevents collapse

### Masked Image Modeling
- **MAE (Masked Autoencoders):** Mask 75% of patches, reconstruct pixels
- **BEiT:** Mask patches, predict visual tokens (dVAE)
- **I-JEPA:** Predict representations (not pixels) of masked regions

### Vision-Language Models
- **CLIP:** Contrastive learning on 400M image-text pairs. Zero-shot classification.
- **SigLIP:** Sigmoid loss variant of CLIP. Better scaling.
- **Florence-2:** Unified model for captioning, detection, segmentation, OCR.

### Segment Anything (SAM/SAM 2)
Promptable segmentation foundation model:
- Trained on 11M images, 1.1B masks
- Input: points, boxes, masks, or text prompts → output: segmentation mask
- SAM 2: extends to video segmentation with memory
