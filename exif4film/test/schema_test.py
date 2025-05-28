import unittest
import json
from jsonschema import validate, ValidationError, SchemaError


class SchemaTests(unittest.TestCase):
    def test_schema_validation(self):
        # Load the schema
        with open('../exif4film.schema.json', 'r') as schema_file:
            schema = json.load(schema_file)
        with open('./resources/basic_film.json', 'r') as basic_film_file:
            basic_film = json.load(basic_film_file)

        self.assertTrue(schema, "Schema should not be empty")
        self.assertTrue(basic_film, "Basic film data should not be empty")
        try:
            validate(basic_film, schema)
        except ValidationError as e:
            self.fail(f"Schema validation failed: {e.message}")
        except SchemaError as e:
            self.fail(f"Schema is invalid: {e.message}")


if __name__ == '__main__':
    unittest.main()
