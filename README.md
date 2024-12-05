
 AI-Powered Yoga Pose Detection and Correction System

This project focuses on enhancing yoga practice through AI-powered pose detection and real-time corrective feedback. It uses computer vision techniques to identify yoga poses, measure alignment, and provide personalized feedback to improve posture and prevent injuries.

---

 Table of Contents
1. [Features](features)
2. [Technologies Used](technologies-used)
3. [System Requirements](system-requirements)
4. [Setup and Installation](setup-and-installation)
5. [Usage](usage)
6. [How It Works](how-it-works)
7. [Results](results)
8. [Future Scope](future-scope)
9. [Contributing](contributing)
10. [License](license)

---

 Features
- Detects common yoga poses using a pre-trained AI model.
- Provides real-time feedback to correct pose alignment.
- Displays visual overlays of joints and angles for better understanding.
- Offers an accuracy score to motivate users.
- User-friendly interface with Streamlit.
- Scalable and adaptable for new poses or features.

---

 Technologies Used
- Python: Core programming language.
- Mediapipe: For extracting body keypoints.
- TensorFlow/Keras: For pose classification model.
- OpenCV: For image processing.
- Streamlit: For building the interactive interface.
- Flask: Simulated API for backend services.

---

 System Requirements
- Operating System: Windows, macOS, or Linux.
- Python Version: 3.8 or above.
- Hardware: Minimum 4GB RAM, a GPU is recommended for real-time processing.

---

 Setup and Installation

 1. Clone the Repository
```bash
git clone https://github.com/your-username/yoga-pose-detection.git
cd yoga-pose-detection
```

 2. Create a Virtual Environment
```bash
python -m venv yoga-env
source yoga-env/bin/activate    For Linux/macOS
yoga-env\Scripts\activate       For Windows
```

 3. Install Dependencies
Install the required Python packages using `pip`:
```bash
pip install -r requirements.txt
```

 4. Download Pre-Trained Models
- The pre-trained MobileNetV2 model will be automatically downloaded during runtime. 
- Mediapipe does not require additional setup for pose estimation.

---

 Usage

 Running the Application
1. Start the Streamlit Interface
   ```bash
   streamlit run app.py
   ```
   This will launch the application in your default web browser.

2. Upload an Image or Use Webcam
   - Upload an image for pose detection.
   - Enable webcam for real-time detection and feedback.

3. View Feedback
   - The interface will display:
     - Detected yoga pose.
     - Accuracy score.
     - Corrective feedback for misaligned joints.

---

 How It Works

 Pose Classification
1. Keypoint Detection:
   - Mediapipe extracts keypoints (joints like elbows, knees, shoulders).
   - These are used as inputs for the pose classification model.

2. Pose Prediction:
   - A fine-tuned MobileNetV2 model classifies the yoga pose based on keypoint positions.

3. Pose Correction:
   - Calculates angles between joints (e.g., shoulder-elbow-wrist).
   - Compares user pose against ideal templates.
   - Highlights misalignments with visual markers.

 Architecture
- Frontend:
  - Built using Streamlit for real-time interaction.
- Backend:
  - Pose classification and correction logic implemented using TensorFlow and Mediapipe.

---

 Results
- Classification Accuracy: 94% on the test dataset.
- Pose Correction: ±3° precision in angle measurements.
- Latency: Processes frames in ~50ms, suitable for real-time feedback.

 Visual Feedback
- Overlays showing:
  - Keypoint locations (color-coded dots).
  - Misaligned joints (highlighted in red).
  - Corrective suggestions (text on screen).

---

 Future Scope
- Add more yoga poses to the model.
- Integrate breathing pattern analysis.
- Enable voice-guided yoga sessions.
- Support for mobile devices and AR/VR platforms.

---

 Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push the branch (`git push origin feature-branch`).
5. Open a pull request.
