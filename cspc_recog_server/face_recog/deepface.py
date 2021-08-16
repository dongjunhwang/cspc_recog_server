from deepface import DeepFace
#DeepFace.stream("database")
import base64

def DeepFaceRecog(faces, image):
    true_face_dict = {}
    backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface']
    model_name = "Facenet"
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
        result = DeepFace.verify("data:image/jpeg;base64,"+face.image_base64,
                                   "data:image/jpeg;base64,"+image,
                                 model_name=model_name, detector_backend=backends[4])
        print(result)
        if result['verified']:
            true_face_dict[face] = result['distance']

    if true_face_dict:
        verified_face = max(true_face_dict.keys(), key=(lambda k: true_face_dict[k]))
        return verified_face.profile
    else:
        return None



