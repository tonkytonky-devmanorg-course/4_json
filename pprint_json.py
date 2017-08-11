import json
import sys


def load_json(filepath):
    with open(filepath, encoding='utf-8') as input_file:
        return json.load(input_file)


def pretty_print_json(loaded_json):
    print(json.dumps(loaded_json, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': ')))


def main():
    try:
        pretty_print_json(load_json(sys.argv[1]))
    except IndexError:
        print(
            'Please, call the script with a path to a JSON file. '
            'You need to specify the path as the first script argument.'
        )


if __name__ == '__main__':
    main()
