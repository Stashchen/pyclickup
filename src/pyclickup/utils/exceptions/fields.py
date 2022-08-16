
class ReadOnlyTaskField(Exception):
    """
    Raised, when there was a try of manual update of task's `id` field.
    """

class RequiredFieldMissing(Exception):
    """Raises, when requred field is missing."""

class CustomFieldNotFound(Exception):
    """Raised if raw custom field not found in raw clickup list."""

