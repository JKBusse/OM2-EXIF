import json
import unittest

from jsonschema import validate, ValidationError, SchemaError

SCHEMA_JSON = '../exif4film.schema.json'
BASIC_FILM = './resources/basic_film.json'
BROKEN_FILM = './resources/broken_film.json'


class SchemaTests(unittest.TestCase):
    def test_schema_validation(self):
        with open(SCHEMA_JSON, 'r') as schema_file:
            schema = json.load(schema_file)
        with open(BASIC_FILM, 'r') as basic_film_file:
            basic_film = json.load(basic_film_file)

        self.assertTrue(schema, "Schema should not be empty")
        self.assertTrue(basic_film, "Basic film data should not be empty")
        try:
            validate(basic_film, schema)
        except ValidationError as e:
            self.fail(f"Schema validation failed: {e.message}")
        except SchemaError as e:
            self.fail(f"Schema is invalid: {e.message}")

    def test_invalid_film_file(self):
        with open(SCHEMA_JSON, 'r') as schema_file:
            schema = json.load(schema_file)
        with open(BROKEN_FILM, 'r') as broken_film_file:
            broken_film = json.load(broken_film_file)

        self.assertTrue(schema, "Schema should not be empty")
        self.assertTrue(broken_film, "Basic film data should not be empty")

        with self.assertRaises(ValidationError):
            validate(broken_film, schema)


if __name__ == '__main__':
    unittest.main()
