# Classical Computer Vision

## Table of Contents
1. [Image Formation and Camera Models](#image-formation-and-camera-models)
2. [Image Filtering and Edge Detection](#image-filtering-and-edge-detection)
3. [Feature Detection and Description](#feature-detection-and-description)
4. [Feature Matching and Geometric Verification](#feature-matching-and-geometric-verification)
5. [Stereo Vision and Depth](#stereo-vision-and-depth)
6. [Optical Flow and Motion](#optical-flow-and-motion)
7. [Structure from Motion and SLAM](#structure-from-motion-and-slam)

---

## Image Formation and Camera Models

### Pinhole Camera Model
Maps 3D world point X = (X,Y,Z)ᵀ to 2D image point x = (u,v)ᵀ:

x = K [R | t] X  (in homogeneous coordinates)

**Intrinsic matrix K:**
K = [[fx, s, cx], [0, fy, cy], [0, 0, 1]]
- fx, fy: focal lengths in pixels
- cx, cy: principal point
- s: skew (usually 0)

**Extrinsic [R|t]:** Rotation R (3×3 orthogonal) + translation t (3×1) from world to camera.

### Lens Distortion
- **Radial:** r' = r(1 + k₁r² + k₂r⁴ + k₃r⁶) — barrel/pincushion
- **Tangential:** from lens not parallel to image plane
- Calibration: Use checkerboard pattern → Zhang's method (OpenCV `calibrateCamera`)

### Homogeneous Coordinates
Point (x,y) → (x,y,1). Enables representing projection, translation as matrix multiplication.
Points at infinity: (x,y,0). Lines: lᵀx = 0.

---

## Image Filtering and Edge Detection

### Convolution
(f * g)(x,y) = ΣΣ f(x-i, y-j) · g(i,j)

Key filters:
- **Gaussian blur:** G(x,y) = (1/2πσ²)exp(-(x²+y²)/2σ²) — smoothing, noise reduction
- **Sobel:** Gradient approximation. Gx = [[-1,0,1],[-2,0,2],[-1,0,1]], Gy = Gxᵀ
- **Laplacian:** ∇²f = ∂²f/∂x² + ∂²f/∂y² — second derivative, blob detection
- **Laplacian of Gaussian (LoG):** Combine smoothing + edge detection

### Canny Edge Detector
1. Gaussian smoothing
2. Gradient magnitude and direction (Sobel)
3. Non-maximum suppression (thin edges)
4. Hysteresis thresholding (high/low thresholds)

### Hough Transform
Detect parametric shapes (lines, circles) by voting in parameter space.
- **Lines:** (x,y) → curve in (ρ,θ) space. Peak = line.
- **Circles:** (x,y) → cone in (a,b,r) space.
- **Generalized Hough:** Arbitrary shapes via R-table.

### Morphological Operations
- **Erosion:** Shrinks foreground. Removes noise.
- **Dilation:** Expands foreground. Fills gaps.
- **Opening:** Erosion then dilation. Removes small noise.
- **Closing:** Dilation then erosion. Fills small holes.

---

## Feature Detection and Description

### Harris Corner Detector
Detect corners by analyzing intensity change in all directions.

Structure tensor M at pixel (x,y):
M = Σ w(u,v) [[Ix², IxIy], [IxIy, Iy²]]

Corner response: R = det(M) - k·trace(M)² where k ≈ 0.04-0.06.
- R large positive → corner
- R large negative → edge
- |R| small → flat

### SIFT (Scale-Invariant Feature Transform)
1. **Scale-space extrema:** Difference-of-Gaussians (DoG) across octaves
2. **Keypoint localization:** Sub-pixel refinement, reject low contrast / edges
3. **Orientation assignment:** Gradient histogram → dominant orientation
4. **Descriptor:** 4×4 grid of 8-bin orientation histograms → 128-dim vector

Properties: Invariant to scale, rotation, partially invariant to illumination/viewpoint.

### SURF (Speeded Up Robust Features)
Approximates SIFT using box filters and integral images. ~3× faster than SIFT.

### ORB (Oriented FAST and Rotated BRIEF)
- Detection: FAST corners + Harris score filtering
- Description: Rotated BRIEF (binary descriptor, 256 bits)
- Very fast, no patent restrictions. Default in OpenCV for real-time.

### Feature Descriptor Comparison
| Detector | Descriptor Dim | Invariance | Speed | Patent |
|----------|---------------|------------|-------|--------|
| SIFT | 128 float | Scale + rotation | Slow | Expired |
| SURF | 64 float | Scale + rotation | Medium | Patented |
| ORB | 256 binary | Rotation | Fast | Free |
| AKAZE | Variable | Scale + rotation | Medium | Free |
| SuperPoint | 256 float | Learned | GPU-fast | Open |

---

## Feature Matching and Geometric Verification

### Matching Strategies
- **Brute-force:** Compare every pair. O(n·m·d).
- **FLANN:** Approximate nearest neighbor. Much faster for large sets.
- **Ratio test (Lowe's):** Accept match only if dist(best)/dist(2nd best) < 0.7.

### RANSAC (Random Sample Consensus)
Robust fitting in presence of outliers:
1. Randomly sample minimum points (e.g., 4 for homography)
2. Fit model to sample
3. Count inliers (points consistent with model within threshold)
4. Repeat N times, keep best model
5. Re-fit on all inliers

Number of iterations: N = log(1-p) / log(1-(1-ε)ˢ)
where p = desired probability, ε = outlier ratio, s = sample size.

### Homography
Maps points between two planes: x' = Hx (3×3 matrix, 8 DoF).
Requires 4 point correspondences (minimum).
Used for: panorama stitching, planar object detection, augmented reality.

### Fundamental Matrix
Encodes epipolar geometry: x'ᵀFx = 0 for corresponding points.
- 7 DoF (3×3 rank-2 matrix, up to scale)
- Minimum 7 point correspondences (or 8 with 8-point algorithm)
- Relates uncalibrated camera pairs

### Essential Matrix
E = [t]× R = K'ᵀFK
- 5 DoF (rotation + direction of translation)
- Requires calibrated cameras
- Extract R, t from E (4 solutions, 1 physically valid)

---

## Stereo Vision and Depth

### Epipolar Geometry
- **Epipole:** Projection of one camera center onto the other image
- **Epipolar line:** For a point in image 1, the corresponding point in image 2 lies on a line
- **Epipolar constraint:** x'ᵀFx = 0 reduces 2D search to 1D

### Stereo Matching
Given rectified stereo pair (epipolar lines = horizontal scanlines):
- **Disparity:** d = x_left - x_right. Depth Z = fB/d (f=focal, B=baseline)
- **Block matching:** Compare windows along scanlines (SAD, SSD, NCC)
- **Semi-Global Matching (SGM):** Dynamic programming along multiple paths. Best classical method.
- **Deep stereo:** PSMNet, RAFT-Stereo, CREStereo — learned cost volumes

### Depth Map Quality Metrics
- Bad pixel rate: % pixels with |d_pred - d_gt| > threshold
- End-point error (EPE): Mean absolute disparity error
- D1-all: % pixels with error > max(3px, 5% of ground truth)

---

## Optical Flow and Motion

### Definition
Dense correspondence between frames: (u(x,y), v(x,y)) = pixel displacement.

### Brightness Constancy Assumption
I(x,y,t) = I(x+u, y+v, t+1)
Taylor expansion → Ix·u + Iy·v + It = 0 (optical flow constraint equation)
One equation, two unknowns → need additional constraint.

### Lucas-Kanade (Sparse)
Assumes constant flow in local window. Solve overdetermined system via least squares.
Good for tracking sparse features. Fails for large motions.

### Horn-Schunck (Dense)
Add global smoothness constraint: minimize ∫∫ (Ix·u + Iy·v + It)² + α(|∇u|² + |∇v|²) dxdy

### Modern Deep Optical Flow
- **FlowNet/FlowNet2:** First CNN approaches
- **RAFT:** Recurrent All-Pairs Field Transforms — iterative updates on correlation volumes
- **GMFlow/FlowFormer:** Transformer-based, global matching
- **UniMatch:** Unified model for flow + stereo + depth

---

## Structure from Motion and SLAM

### Structure from Motion (SfM) Pipeline
1. **Feature extraction:** SIFT/SuperPoint on all images
2. **Feature matching:** Pairwise matching + geometric verification
3. **Incremental reconstruction:** Initialize with 2-view, add images one at a time
4. **Triangulation:** Compute 3D points from 2+ views
5. **Bundle adjustment:** Jointly optimize all camera poses + 3D points (minimize reprojection error)
6. **Dense reconstruction:** MVS (Multi-View Stereo) for dense point cloud

Tools: COLMAP (open-source, gold standard), OpenSfM, VisualSFM.

### Bundle Adjustment
Minimize: Σ_i Σ_j ‖x_ij - π(C_i, X_j)‖²
over camera parameters C_i and 3D points X_j.
- Non-linear least squares (Levenberg-Marquardt)
- Exploits sparsity of Jacobian (Schur complement trick)
- Typically the most expensive step

### Visual SLAM
Real-time SfM with loop closure:
- **ORB-SLAM3:** Feature-based, supports mono/stereo/RGB-D + IMU
- **LSD-SLAM:** Direct (photometric) method
- **VINS-Mono:** Visual-inertial odometry
- **DROID-SLAM:** Deep learning SLAM (differentiable BA)

Key components:
1. **Tracking:** Estimate current pose from frame-to-frame matches
2. **Local mapping:** Triangulate new points, local bundle adjustment
3. **Loop closing:** Detect revisited places (bag-of-words), correct drift
4. **Relocalization:** Recover from tracking failure
