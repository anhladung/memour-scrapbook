"""
Computer Vision Sticker Segmentation Engine
Author: AI Engineer & CV Specialist (MEMOUR Studio)
"""

import os
import cv2
import numpy as np
from PIL import Image
import io
import base64

def detect_background_color(img_bgr):
    """
    Sample border pixels to reliably detect sheet background color.
    """
    h, w = img_bgr.shape[:2]
    border_pixels = []
    
    # Sample top & bottom borders
    border_pixels.append(img_bgr[0:max(3, int(h*0.02)), :].reshape(-1, 3))
    border_pixels.append(img_bgr[h-max(3, int(h*0.02)):h, :].reshape(-1, 3))
    # Sample left & right borders
    border_pixels.append(img_bgr[:, 0:max(3, int(w*0.02))].reshape(-1, 3))
    border_pixels.append(img_bgr[:, w-max(3, int(w*0.02)):w].reshape(-1, 3))
    
    all_borders = np.vstack(border_pixels)
    median_bg = np.median(all_borders, axis=0).astype(np.uint8)
    return median_bg

def segment_sticker_sheet(image_path_or_bytes, min_area_ratio=0.015, max_stickers=50):
    """
    Main Computer Vision Pipeline:
    1. Reads uploaded image.
    2. Detects background color and creates color-distance mask.
    3. Finds distinct sticker contours/objects (not bound to any grid).
    4. For each sticker:
       - Extracts exact RGBA mask with transparent background.
       - Preserves white borders, colored borders, textures and shadows.
       - Auto-crops with 6% safe padding.
       - Generates preview image and bounding box.
    """
    if isinstance(image_path_or_bytes, str):
        img_bgr = cv2.imread(image_path_or_bytes)
    elif isinstance(image_path_or_bytes, bytes):
        nparr = np.frombuffer(image_path_or_bytes, np.uint8)
        img_bgr = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    else:
        raise ValueError("Invalid image input format")

    if img_bgr is None:
        raise ValueError("Could not decode image")

    h, w = img_bgr.shape[:2]
    total_area = h * w
    min_area = total_area * min_area_ratio

    # 1. Background color detection
    bg_color = detect_background_color(img_bgr)
    
    # 2. Compute color distance in CIELAB space for perceptual accuracy
    img_lab = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2LAB)
    bg_lab = cv2.cvtColor(np.uint8([[bg_color]]), cv2.COLOR_BGR2LAB)[0][0]
    
    # Euclidean distance in LAB space
    diff_lab = np.linalg.norm(img_lab.astype(np.float32) - bg_lab.astype(np.float32), axis=2)
    
    # Also check RGB distance
    diff_bgr = np.linalg.norm(img_bgr.astype(np.float32) - bg_color.astype(np.float32), axis=2)
    
    # Combined foreground mask
    threshold_lab = 16.0
    threshold_bgr = 22.0
    fg_mask = (diff_lab > threshold_lab) | (diff_bgr > threshold_bgr)
    fg_mask = (fg_mask * 255).astype(np.uint8)

    # 3. Morphological cleaning to close internal gaps while preserving artwork borders
    kernel_close = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
    fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_CLOSE, kernel_close, iterations=2)

    # Fill internal holes inside objects
    contours_holes, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    filled_mask = np.zeros_like(fg_mask)
    for c in contours_holes:
        if cv2.contourArea(c) > min_area * 0.2:
            cv2.drawContours(filled_mask, [c], -1, 255, thickness=cv2.FILLED)

    # 4. Find all distinct object contours
    contours, hierarchy = cv2.findContours(filled_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Filter valid stickers by area
    valid_contours = []
    for c in contours:
        area = cv2.contourArea(c)
        if area >= min_area:
            valid_contours.append(c)

    # If no contour found (e.g. subtle single object), fallback to largest central region
    if not valid_contours and contours:
        valid_contours = [max(contours, key=cv2.contourArea)]
    elif not valid_contours:
        valid_contours = [np.array([[[0, 0]], [[w, 0]], [[w, h]], [[0, h]]])]

    # Sort contours top-to-bottom, left-to-right
    def get_sort_key(cnt):
        x, y, cw, ch = cv2.boundingRect(cnt)
        return (y // (h // 4)) * 10000 + x

    valid_contours.sort(key=get_sort_key)
    valid_contours = valid_contours[:max_stickers]

    segmented_stickers = []

    # Original RGB image for cropping
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    for idx, cnt in enumerate(valid_contours, start=1):
        x, y, cw, ch = cv2.boundingRect(cnt)
        
        # Add 6% safe padding around sticker
        pad_x = int(cw * 0.06) + 4
        pad_y = int(ch * 0.06) + 4
        
        x0 = max(0, x - pad_x)
        y0 = max(0, y - pad_y)
        x1 = min(w, x + cw + pad_x)
        y1 = min(h, y + ch + pad_y)
        
        crop_rgb = img_rgb[y0:y1, x0:x1]
        crop_mask = filled_mask[y0:y1, x0:x1]

        # Refine Alpha Channel: Soft anti-aliased edge
        alpha_channel = crop_mask.copy()
        alpha_channel = cv2.GaussianBlur(alpha_channel, (3, 3), 0)

        # Create RGBA Image
        r, g, b = cv2.split(crop_rgb)
        rgba_mat = cv2.merge([r, g, b, alpha_channel])
        
        # Convert to PIL Image
        pil_rgba = Image.fromarray(rgba_mat, 'RGBA')

        # Encode to Base64 for web preview
        buffer = io.BytesIO()
        pil_rgba.save(buffer, format="PNG")
        png_bytes = buffer.getvalue()
        b64_str = base64.b64encode(png_bytes).decode('utf-8')
        data_url = f"data:image/png;base64,{b64_str}"

        # Bounding box on original image
        bbox = {
            'x': int(x0),
            'y': int(y0),
            'width': int(x1 - x0),
            'height': int(y1 - y0),
            'original_w': w,
            'original_h': h
        }

        segmented_stickers.append({
            'index': idx,
            'bbox': bbox,
            'png_bytes': png_bytes,
            'data_url': data_url,
            'width': int(x1 - x0),
            'height': int(y1 - y0),
            'aspect_ratio': round(float(x1 - x0) / max(1, float(y1 - y0)), 3)
        })

    # Generate visual overlay of original image with bounding boxes
    overlay_bgr = img_bgr.copy()
    for item in segmented_stickers:
        bx, by, bw, bh = item['bbox']['x'], item['bbox']['y'], item['bbox']['width'], item['bbox']['height']
        idx = item['index']
        # Draw neo-brutalist bounding box
        cv2.rectangle(overlay_bgr, (bx, by), (bx + bw, by + bh), (55, 19, 136), 3)
        # Draw label tag
        label_text = f"Sticker {idx:02d}"
        cv2.rectangle(overlay_bgr, (bx, max(0, by - 24)), (bx + 110, by), (55, 19, 136), -1)
        cv2.putText(overlay_bgr, label_text, (bx + 8, by - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 2)

    overlay_rgb = cv2.cvtColor(overlay_bgr, cv2.COLOR_BGR2RGB)
    pil_overlay = Image.fromarray(overlay_rgb)
    overlay_buf = io.BytesIO()
    pil_overlay.save(overlay_buf, format="JPEG", quality=90)
    overlay_b64 = base64.b64encode(overlay_buf.getvalue()).decode('utf-8')
    overlay_data_url = f"data:image/jpeg;base64,{overlay_b64}"

    return {
        'total_detected': len(segmented_stickers),
        'overlay_data_url': overlay_data_url,
        'stickers': segmented_stickers
    }
