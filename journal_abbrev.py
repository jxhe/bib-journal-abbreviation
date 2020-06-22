import sys
import json
import re
import argparse

def abbreviate(line, journal_to_abbr):
    if re.search('".*"', line) is not None:
        journal_name_template = '"{}"'
        journal_str = re.search('".*"', line).group(0)
    elif re.search('{.*}', line) is not None:
        journal_name_template = '{{{}}}'
        journal_str = re.search('{.*}', line).group(0)
    else:
        raise ValueError('the format "{}" is not valid'.format(line))

    journal_name_strip = journal_str[1:-1]
    journal_name = journal_name_strip.replace('{','').replace('}','')
    journal_name = journal_to_abbr.get(journal_name, journal_name_strip)
    journal_name = journal_name_template.format(journal_name)

    return line.replace(journal_str, journal_name)




def main(journal_to_abbr):
    for line in sys.stdin:
        line_strip = line.strip()
        if line_strip.startswith('journal'):
            new_line = abbreviate(line, journal_to_abbr)
            print(new_line.rstrip())
        else:
            print(line.rstrip())
            

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Journal abbreviation")
    parser.add_argument('--user-json', type=str, default=None, help="customized json file")
    args = parser.parse_args()

    with open('journals.json') as fin:
        journal_to_abbr = json.load(fin)

    if args.user_json is not None:
        with open(args.user_json) as fin:
            customize_json = json.load(fin)
        journal_to_abbr.update(customize_json)

    main(journal_to_abbr)
