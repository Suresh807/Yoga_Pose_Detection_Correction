import cv2
import mediapipe as mp
import streamlit as st
from pose_detection import give_feedback, calculate_angle

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

def main():
    st.title("Yoga Pose Detection & Correction")
    st.write("Get real-time feedback on your yoga poses.")

    run = st.checkbox('Activate Webcam')
    cap = cv2.VideoCapture(0)

    if run:
        stframe = st.empty()

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Convert image to RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Process pose
            results = pose.process(rgb_frame)

            if results.pose_landmarks:
                mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
                
                # Provide feedback
                feedback = give_feedback(results.pose_landmarks.landmark)
                cv2.putText(frame, feedback, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

            # Display the frame
            stframe.image(frame, channels="BGR")

    cap.release()

if __name__ == "__main__":
    main()
    
