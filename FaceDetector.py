import cv2
import mediapipe as mp
from threading import Thread
import math

import Hardcodes


class FaceInterface():
    def __init__(self):
        self.mp_face_mesh = mp.solutions.face_mesh
        self.draw_ut = mp.solutions.drawing_utils
        self.draw_st = mp.solutions.drawing_styles
        self.cam = None
        self.stopped = False
        self.hasStarted = False
        self.lastFrame = None
        self.info = None

        # The camera thread
        t = Thread(target=self.updateWebcam, args=())
        t.daemon = True
        t.start()

    def updateWebcam(self):
        # Start the camera
        self.cam = cv2.VideoCapture(0)
        # Camera loop
        while not self.stopped:
            # Read the camera
            ret, frame = self.cam.read()
            frame = cv2.flip(frame, 1)
            # And start the detection!
            with self.mp_face_mesh.FaceMesh(max_num_faces=1, refine_landmarks=False) as face_mesh:
                # Process the frame
                frame.flags.writeable = False
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = face_mesh.process(frame)
                frame.flags.writeable = True
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

                # If it detects a face
                if results.multi_face_landmarks:
                    self.updateInfo(results.multi_face_landmarks[0])
                    # For every face in the screen (even though there is only one)
                    for face_landmarks in results.multi_face_landmarks:
                        # Draw the face tesselation
                        self.draw_ut.draw_landmarks(frame, face_landmarks, self.mp_face_mesh.FACEMESH_TESSELATION,
                                                  self.draw_ut.DrawingSpec(color=(255, 0, 0), thickness=1,
                                                                         circle_radius=2),
                                                  self.draw_st.get_default_face_mesh_tesselation_style())
                        # And the face contour
                        self.draw_ut.draw_landmarks(frame, face_landmarks, self.mp_face_mesh.FACEMESH_CONTOURS,
                                                      None,
                                                      self.draw_st.get_default_face_mesh_contours_style())

            # And set the last frame of the camera
            self.lastFrame = frame

            # This is for knowing when to start the game
            self.hasStarted = True

    def getImage(self):
        if self.lastFrame is None:
            return
        # Show the last frame to a window
        frame = self.lastFrame
        if Hardcodes.showcamera:
            cv2.imshow('webCam', frame)

    def closeCam(self):
        # Stop everything
        self.stopped = True
        self.cam.release()
        cv2.destroyAllWindows()

    def updateInfo(self, points):
        # Calculate the angle of the face based on two points
        A = points.landmark[151]
        B = points.landmark[152]
        angle = math.degrees(math.atan2(B.y - A.y, B.x - A.x)) - 90.0
        # And calculate if the mouth is open
        lipup = points.landmark[13]
        lipdown = points.landmark[14]
        shoot = math.sqrt((lipdown.x - lipup.x)**2 + (lipdown.y - lipup.y)**2) > 0.02

        self.info = [angle, shoot]

