from .deepface_basic import DeepFace
import time
#DeepFace.stream("database")

def DeepFaceRecog(faces, image):
    start = time.time()
    true_face_dict = {}
    backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface']
    #model_name = "Facenet"
    model_name = "Facenet"
    image_embedding = DeepFace.verify("data:image/jpeg;base64," + image,
                             model_name=model_name,
                             detector_backend='retinaface',
                             represent_option='preprocess'
                             # detector_backend='skip',
                             # normalization='Facenet',
                             )
    for face in faces:
        """
        filename = "1.jpg"
        with open(filename, 'wb') as f:
            f.write(base64.b64decode(face.image_base64))
        filename = "2.jpg"
        with open(filename, 'wb') as f:
            f.write(base64.b64decode(image))
        print("data:image/jpeg;base64,"+image)
        """
        #TODO : 일단 Retina Face Recognition을 계속 써보자.
        #모델을 선택할 수 있도록 해볼까도 생각했었는데, 어차피 detection을 app에서 할 거니까
        #그 부분은 구현 x

        identified, distance = DeepFace.customVerify(face.get_image(), image_embedding)
        print(face.profile.nick_name, identified)
        if identified:
            true_face_dict[face] = distance
    if true_face_dict:
        verified_face = min(true_face_dict.keys(), key=(lambda k: true_face_dict[k]))
        print(time.time() - start)
        return verified_face.profile
    else:
        return None

def DeepFaceAdd(image):
    model_name = "Facenet"
    result = DeepFace.verify("data:image/jpeg;base64," + image,
                             model_name=model_name,
                             detector_backend='retinaface',
                             represent_option='preprocess'
                             # detector_backend='skip',
                             # normalization='Facenet',
                             )
    return result

