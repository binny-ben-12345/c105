import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)

frame= cv2.imread(images[0])

height, width, channels= frame.shape

size=(width, height)

out=cv2.VideoWriter("Project.mp4", cv2.VideoWriter_fourcc(*'DIVX'), 5, (1080,1080))
#fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
#out = cv2.VideoWriter('C:/Users/binny ben/OneDrive/Desktop/c105/Videos/output.mp4',fourcc, 5, (1080,1080))

for i in range(count-1, 0, -1):
    frame= cv2.imread(images[i])
    out.write(frame)

out.release()    
print("done")