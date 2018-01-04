import SimpleITK as sitk  
import cv2  
#LKDS-00058,-102.655469971,108.188810974,438.759994507,12.2279986879  
if __name__ == '__main__':  
    filename = "F:/skey/correct_images/LKDS-00052.mhd"  
    ds = sitk.ReadImage(filename)  
    img_array = sitk.GetArrayFromImage(ds)  
    frame_num, width, height = img_array.shape  
  
    outpath = "F:/cancer_solution/out/train/LKDS-00058"  
    index = -1  
    for img_item in img_array:  
        index = index + 1  
        cv2.imwrite("%s/%d.png"%(outpath,index),img_item)  
  
    print("done!")