from deepface import DeepFace
#DeepFace.stream("database")


def DeepFaceRecog(faces, image):
    true_face_dict = {}
    model_name = "Facenet"
    for face in faces:
        result = DeepFace.verify(face.image_base64, image, model_name=model_name)
        print(result)
        if result['verified']:
            true_face_dict[face] = result['distance']

    if true_face_dict:
        verified_face = max(true_face_dict.keys(), key=(lambda k: true_face_dict[k]))
        return verified_face.profile
    else:
        return None



