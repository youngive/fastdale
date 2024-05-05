from pydantic import BaseModel, constr, field_validator
from pathlib import Path


class FilenameValidator(BaseModel):
    filename: constr(max_length=255, pattern=r"[^'\\?*&<\";:+\[\]=!@#$%^(){}]+")

    @classmethod
    def validate_name(cls, v):
        valid_extensions = {'swf', 'png', 'jpg'}
        extension = Path(v).suffix[1:]  # Получаем расширение файла
        if extension not in valid_extensions:
            raise ValueError("Invalid file extension")

        return v
