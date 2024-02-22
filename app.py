

import streamlit as st
import cv2
import numpy as np

def main():
    st.title("Image Processing App")

    # Upload an image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the image
        image = np.array(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)

        st.subheader("Original Image")
        st.image(image, channels="BGR", use_column_width=True)

        # Process image
        options = st.multiselect("Select processing options:", ["Convert to Grayscale", "Binary Thresholding", "Brightness & Contrast", "Draw Line", "Draw Rectangle", "Write Text"])
        
        processed_image = image.copy()

        for option in options:
            if option == "Convert to Grayscale":
                processed_image = cv2.cvtColor(processed_image, cv2.COLOR_BGR2GRAY)
            elif option == "Binary Thresholding":
                val = st.slider("Select a threshold value", min_value=0, max_value=255, value=127, step=1)
                max_threshold = st.slider("Select a some value", min_value=0, max_value=255, value=255, step=1)
                _, processed_image = cv2.threshold(processed_image, val, max_threshold, cv2.THRESH_BINARY)
            elif option == "Brightness & Contrast":
                alpha = st.slider("Alpha (Contrast)", 0.0, 3.0, 1.0)
                beta = st.slider("Beta (Brightness)", 0, 100, 0)
                processed_image = cv2.convertScaleAbs(processed_image, alpha=alpha, beta=beta)
            elif option == "Draw Line":
                st.write("Enter start point")
                x1 = st.number_input("(x1)", key="x1_line")
                y1 = st.number_input("(y1)", key="y1_line")
                st.write("Enter end point")
                x2 = st.number_input("(x2)", key="x2_line")
                y2 = st.number_input("(y2)", key="y2_line")
                thick = st.slider("Select thickness", 0, 50, 5)
                # Allow user to pick a color
                selected_color = st.color_picker("Choose a color", "#ff6347")
                # Convert hexadecimal color to BGR format
                selected_color_bgr = tuple(int(selected_color[i:i+2], 16) for i in (1, 3, 5))

                #adding line in the image
                processed_image = cv2.line(processed_image, (int(x1), int(y1)), (int(x2), int(y2)), selected_color_bgr, lineType= cv2.LINE_AA, thickness= thick)

            elif option == "Draw Rectangle":
                st.write("Enter start point")
                x1_rect = st.number_input("(x1_rect)", key="x1_rect")
                y1_rect = st.number_input("(y1_rect)", key="y1_rect")
                st.write("Enter end point")
                x2_rect = st.number_input("(x2_rect)", key="x2_rect")
                y2_rect = st.number_input("(y2_rect)", key="y2_rect")
                thick = st.slider("Select thickness", 0, 50, 5)
                # Allow user to pick a color
                selected_color = st.color_picker("Choose a color", "#ff6347")
                # Convert hexadecimal color to BGR format
                selected_color_bgr = tuple(int(selected_color[i:i+2], 16) for i in (1, 3, 5))

                #adding rectangle in the image
                processed_image = cv2.rectangle(processed_image, (int(x1_rect), int(y1_rect)), (int(x2_rect), int(y2_rect)), selected_color_bgr, lineType= cv2.LINE_AA, thickness= thick)

            elif option == "Write Text":
                # Text input field
                text = st.text_input("Enter Text here:")
                st.write("Enter coordinate of Text :")
                x1_text = st.number_input("(x1_text)", key="x1_text")
                y1_text = st.number_input("(y1_text)", key="y1_text")
                text_thick = st.slider("Select thickness", 0, 50, 5)
                font_sc = st.slider("Select font scale", 0, 50, 5)
                # Allow user to pick a color
                selected_color = st.color_picker("Choose a color", "#ff6347")
                # Convert hexadecimal color to BGR format
                selected_color_bgr = tuple(int(selected_color[i:i+2], 16) for i in (1, 3, 5))
                cv2.putText(processed_image, text, (int(x1_text), int(y1_text)), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=font_sc, color=selected_color_bgr, thickness=text_thick, lineType=cv2.LINE_AA)


        # Convert processed image to RGB for displaying
        processed_image_rgb = cv2.cvtColor(processed_image, cv2.COLOR_BGR2RGB)

        st.subheader("Processed Image")
        st.image(processed_image_rgb, use_column_width=True)

if __name__ == "__main__":
    main()
