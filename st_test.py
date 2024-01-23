import streamlit as st

def main():
    st.title("Multiple Image Interaction Demo")

    # Create two columns
    col1, col2 = st.columns(2)

    # List to store images
    images_col1 = [
        "Screen Shot 2024-01-22 at 6.09.23 PM.png",
        "Screen Shot 2024-01-22 at 6.09.31 PM.png",
        # Add more image URLs as needed
    ]

    images_col2 = []

    # Display checkboxes for each image in column 1
    selected_images_col1 = [col1.checkbox(f"Select Image {i+1}") for i in range(len(images_col1))]

    # Move selected images to column 2
    if col1.button("Add to Column 2"):
        selected_indices = [i for i, selected in enumerate(selected_images_col1) if selected]
        selected_indices.reverse()  # Reverse the list to avoid index issues
        for i in selected_indices:
            if i < len(images_col1):
                images_col2.append(images_col1.pop(i))
        st.success("Images added to Column 2!")

    # Display images in the first column
    for image_url in images_col1:
        col1.image(image_url, caption=f"Column 1: Image", use_column_width=True)

    # Display images in the second column
    for image_url in images_col2:
        col2.image(image_url, caption=f"Column 2: Image", use_column_width=True)

    # Remove from column button for the second column
    if col2.button("Remove from Column 2"):
        if images_col2:
            # Remove the last image from column 2
            removed_image = images_col2.pop()
            st.success("Image removed from Column 2!")
            # Add the removed image back to column 1
            images_col1.append(removed_image)

if __name__ == "__main__":
    main()