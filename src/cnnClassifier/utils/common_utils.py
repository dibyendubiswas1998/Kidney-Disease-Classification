import os
import shutil
import json
import yaml
import joblib
from pathlib import Path
from box.exceptions import BoxValueError
from box import ConfigBox
from ensure import ensure_annotations
from typing import Any
import base64


@ensure_annotations
def read_params(config_path: Path) -> ConfigBox:
    """
        Read the YAML file at the specified path and return its contents as a dictionary.

        Args:
            config_path (str): The path to the YAML file.

        Returns:
            ConfigBox: ConfigBox type

        Raises:
            Exception: If there is an error while reading the file.
    """
    try:
        with open(config_path) as yaml_file:
            config = yaml.safe_load(yaml_file)
        return ConfigBox(config)
    
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as ex:
        raise ex


@ensure_annotations
def clean_prev_dirs_if_exis(dir_path: str) -> None:
    """
        Clean up a directory by removing it if it exists.

        Args:
            dir_path (str): The path to the directory that needs to be cleaned up.

        Returns:
            None

        Raises:
            Any exception that occurs during the removal process is caught and ignored.
    """
    try:
        if os.path.isdir(dir_path):
            shutil.rmtree(dir_path)
    except Exception as ex:
        raise ex


@ensure_annotations
def create_dir(dirs: list) -> None:
    """
        Create directories specified in a list.

        Args:
            dirs (list): A list of directory names to be created.

        Raises:
            Exception: If any exception occurs during the creation of directories.

        Example Usage:
            create_dir(['dir1', 'dir2'])
    """
    try:
        for dir in dirs:
            os.makedirs(dir, exist_ok=True)
    except Exception as e:
        raise e


@ensure_annotations
def save_report(file_path: Path, report: dict) -> None:
    """
        Saves the report dictionary to a file in JSON format.

        Args:
            file_path (str): The path of the file where the report will be saved.
            report (dict): The report data that will be written to the file.

        Raises:
            Exception: If any error occurs during the file writing process.

        Example:
            save_report('report.json', {'name': 'John', 'age': 25})
    """
    try:
        with open(file_path, 'a+') as f:
            json.dump(report, f, indent=4)
    except Exception as e:
        raise e


@ensure_annotations
def load_report(file_path:Path) -> ConfigBox:
    """
        Load a report from a file and return a ConfigBox object.

        Args:
            file_path (Path): The path to the file containing the report.

        Returns:
            ConfigBox: A ConfigBox object representing the content of the file.

        Raises:
            Exception: If there is an error while loading the report.

        Example Usage:
            file_path = Path("report.json")
            report = load_report(file_path)
    """
    try:
        with open(file_path) as f:
            content = json.load(f)
        return ConfigBox(content)

    except Exception as ex:
        raise ex


@ensure_annotations
def save_binary_file(data: Any, file_path: Path) -> None:
    """
        Save binary file.

        This function saves the provided data as a binary file at the specified file path using the joblib.dump method.
        If an exception occurs during the saving process, the exception is re-raised.

        :param data: The data to be saved as a binary file.
        :param file_path: The path where the binary file will be saved.
        :return: None
    """
    try:
        joblib.dump(value=data, filename=file_path)

    except Exception as ex:
        raise ex


@ensure_annotations
def load_binary_file(file_path: Path) -> Any:
    """
        Load binary file from the specified file path.

        Args:
            file_path (Path): The path to the binary file to be loaded.

        Returns:
            Any: The loaded data from the binary file.

        Raises:
            Exception: If an error occurs during the loading process.
    """
    try:
        data = joblib.load(file_path)
        return data

    except Exception as ex:
        raise ex


@ensure_annotations
def get_size(file_path: Path) -> str:
    """
        Returns the size of a file in kilobytes as a string.

        Args:
            file_path (Path): The path to the file for which the size needs to be determined.

        Returns:
            str: The size of the file in kilobytes as a string with the "~" symbol and "KB" suffix.

        Raises:
            Exception: If an error occurs while getting the file size.

        Example Usage:
            file_path = Path("path/to/file.txt")
            size = get_size(file_path)
            print(size)
    """
    try:
        size_in_kb = round(os.path.getsize(file_path)/1024)
        return "~ {size_in_kb} KB".format(size_in_kb)

    except Exception as ex:
        raise ex


def decode_image(img_string, file_name):
    """
        Decode a base64 encoded image string and save it as a file.

        Args:
            img_string (str): The base64 encoded image string.
            file_name (str): The name of the file to save the decoded image.

        Raises:
            Exception: If an error occurs during the decoding or file writing process.

        Returns:
            None
    """
    try:
        img_data = base64.b64decode(img_string)
        with open(file_name, 'wb') as f:
            f.write(img_data)
            f.close()

    except Exception as ex:
        raise ex


def encode_image_into_base64(cropped_img_path):
    """
        Encodes an image file into base64 format.

        Args:
            cropped_img_path (str): The path of the image file to be encoded.

        Returns:
            bytes: The base64 encoded version of the image.

        Raises:
            Exception: If there is an error while encoding the image.

        Example:
            encoded_image = encode_image_into_base64("image.jpg")
            print(encoded_image)
    """
    try:
        with open(cropped_img_path, "rb") as f:
            return base64.b64encode(f.read())

    except Exception as ex:
        raise ex




if __name__ == "__main__":
    pass
