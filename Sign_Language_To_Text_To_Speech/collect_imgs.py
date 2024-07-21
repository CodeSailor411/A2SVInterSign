import os
import cv2

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 7  # Update with the number of classes in your existing dataset
dataset_size = 100  # Number of images you want to collect for each class

cap = cv2.VideoCapture(0)

for j in range(number_of_classes):
    class_dir = os.path.join(DATA_DIR, str(j))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    # Get the number of existing images in the class directory
    existing_images = len([name for name in os.listdir(class_dir) if os.path.isfile(os.path.join(class_dir, name))])
    remaining_images = dataset_size - existing_images

    if remaining_images <= 0:
        print(f'Class {j} already has enough images. Skipping...')
        continue

    print(f'Collecting data for class {j}. {remaining_images} more images needed.')

    done = False
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Ready? Press "Q" to start collecting!', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break

    counter = existing_images
    while counter < dataset_size:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(1)
        image_path = os.path.join(class_dir, '{}.jpg'.format(counter))
        cv2.imwrite(image_path, frame)
        print(f'Saved {image_path}')
        counter += 1

cap.release()
cv2.destroyAllWindows()
