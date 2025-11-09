import cv2
from skimage.metrics import structural_similarity as ssim

def match(path1, path2):
    # Read the images
    img1 = cv2.imread(path1)
    img2 = cv2.imread(path2)

    if img1 is None or img2 is None:
        raise ValueError("One or both image paths are invalid.")

    # Convert to grayscale
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Resize to match dimensions if different
    if img1.shape != img2.shape:
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    # Compute SSIM (Structural Similarity Index)
    similarity_index, _ = ssim(img1, img2, full=True)

    # Convert to percentage
    similarity_percentage = similarity_index * 100
    return similarity_percentage
