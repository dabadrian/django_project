from django.core.exceptions import ValidationError

def validate_nota(value):
    if value < 0 or value > 100:
        raise ValidationError(
            "%(value)s no es una nota inválida",
            params={"value": value},
        )

def validate_ci(value):
    if  not value.isdigit():
        raise ValidationError(
            "El campo CI sólo puede tener números"
        )
        
