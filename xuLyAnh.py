import cv2 as cv
import numpy as np
import urllib.request

def load_image_from_url(url):
    req = urllib.request.urlopen(url)
    img_rw = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv.imdecode(img_rw, 1)
    return img

def add_noise(img):
    mean = 0
    sigma = 50
    noisy = np.random.normal(mean, sigma, img.shape)
    new_img = np.clip(img + noisy, 0, 255).astype(np.uint8)
    return new_img

def add_muoi_tieu(img, ratio = 0.02):
    nosy = img.copy()
    soLuong = int(ratio*img.size)
    #cho muoi vao 
    toado = [np.random.randint(0, img.shape[0]-1, soLuong) for i in img.shape]
    nosy [toado[0], toado[1], :] = 255
    #cho tieu vao
    toado = [np.random.randint(0, img.shape[0]-1, soLuong) for i in img.shape]
    nosy [toado[0], toado[1], :] = 0

    return nosy

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/opencv/opencv/refs/heads/4.x/samples/data/lena.jpg"
    img = load_image_from_url(url)
    cv.imshow('Loaded Image', img)
    cv.waitKey(0)
    cv.destroyAllWindows()

    # img2 = add_noise(img)
    # cv.imshow("img2", img2)
    # cv.waitKey(0)
    # cv.destroyAllWindows()
    
    # img3 = np.concatenate((img, img2), axis=1)
    # cv.imshow("img3", img3)
    # cv.waitKey(0)
    # cv.destroyAllWindows()

    img_mieu_tieu = add_muoi_tieu(img, ratio=0.03)
    cv.imshow("img_mieu_tieu", img_mieu_tieu)
    cv.waitKey(0)       
    cv.destroyAllWindows()
    
    img4 = np.concatenate((img, img_mieu_tieu), axis=1)
    cv.imshow("img4", img4)     
    cv.waitKey(0)
    cv.destroyAllWindows()