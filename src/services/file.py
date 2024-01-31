import base64
import os


class ServiceFile:
    def image_convert_to_binari(file_path: str, file_name: str):
        try:
            target_path = os.path.join(file_path, file_name)
            with open(target_path, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode("utf-8")
                mime_type = "image/png"
                data_url = f"data:{mime_type};base64,{encoded_image}"
                return data_url
        except Exception as e:
            print(e)
            return ""
