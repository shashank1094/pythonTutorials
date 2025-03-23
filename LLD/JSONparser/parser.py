# https://notes.eatonphil.com/writing-a-simple-json-parser.html

JSON_LEFT_BRACKET = '['
JSON_RIGHT_BRACKET = ']'
JSON_LEFT_BRACE = '{'
JSON_RIGHT_BRACE = '}'
JSON_COMMA = ','
JSON_COLON = ':'
JSON_WHITESPACE = [' ', '\n', '\t', '\r']
JSON_SYNTAX = [JSON_LEFT_BRACE, JSON_LEFT_BRACKET, JSON_COLON, JSON_RIGHT_BRACKET, JSON_RIGHT_BRACE, JSON_COMMA]
JSON_QUOTE = '"'
NULL_LEN = len('null')
TRUE_LEN = len('true')
FALSE_LEN = len('false')

def lex_string(string):
    json_string = ''
    if string[0] == JSON_QUOTE:
        string = string[1:]
    else:
        return None, string
    for c in string:
        if c == JSON_QUOTE:
            return json_string, string[len(json_string)+1:]
        else:
            json_string += c
    raise Exception('Expected end-of-string quote')

def lex_number(string):
    json_number = ''
    number_characters = [str(d) for d in range(0, 10)] + ['-', 'e', '.']
    for c in string:
        if c in number_characters:
            json_number += c
        else:
            break
    rest = string[len(json_number):]
    if not len(json_number):
        return None, string
    if '.' in json_number:
        return float(json_number), rest
    return int(json_number), rest

def lex_bool(string):
    string_len = len(string)
    if string_len >= TRUE_LEN and \
       string[:TRUE_LEN] == 'true':
        return True, string[TRUE_LEN:]
    elif string_len >= FALSE_LEN and \
         string[:FALSE_LEN] == 'false':
        return False, string[FALSE_LEN:]
    return None, string

def lex_null(string):
    string_len = len(string)
    if string_len >= NULL_LEN and \
       string[:NULL_LEN] == 'null':
        return True, string[NULL_LEN:]
    return None, string

def get_tokens_from_lexical_analysis(string):
    tokens = []
    while len(string):
        json_string, string = lex_string(string)
        if json_string is not None:
            tokens.append(json_string)
            continue
        json_number, string = lex_number(string)
        if json_number is not None:
            tokens.append(json_number)
            continue
        json_bool, string = lex_bool(string)
        if json_bool is not None:
            tokens.append(json_bool)
            continue
        json_null, string = lex_null(string)
        if json_null is not None:
            tokens.append(None)
            continue
        if string[0] in JSON_WHITESPACE:
            string = string[1:]
        elif string[0] in JSON_SYNTAX:
            tokens.append(string[0])
            string = string[1:]
        else:
            raise Exception('Unexpected character: {}'.format(string[0]))
    return tokens

def parse_array(tokens):
    json_array = []
    _curr_token = tokens[0]
    if _curr_token == JSON_RIGHT_BRACKET:
        return json_array, tokens[1:]
    while True:
        _json, tokens = parse(tokens)
        json_array.append(_json)
        _curr_token = tokens[0]
        if _curr_token == JSON_RIGHT_BRACKET:
            return json_array, tokens[1:]
        elif _curr_token != JSON_COMMA:
            raise Exception('Expected comma after object in array')
        else:
            tokens = tokens[1:]

def parse_object(tokens):
    json_object = {}
    t = tokens[0]
    if t == JSON_RIGHT_BRACE:
        return json_object, tokens[1:]
    while True:
        json_key = tokens[0]
        if type(json_key) is str:
            tokens = tokens[1:]
        else:
            raise Exception('Expected string key, got: {}'.format(json_key))
        if tokens[0] != JSON_COLON:
            raise Exception('Expected colon after key in object, got: {}'.format(t))
        json_value, tokens = parse(tokens[1:])
        json_object[json_key] = json_value
        t = tokens[0]
        if t == JSON_RIGHT_BRACE:
            return json_object, tokens[1:]
        elif t != JSON_COMMA:
            raise Exception('Expected comma after pair in object, got: {}'.format(t))
        tokens = tokens[1:]

def parse(tokens):
    curr_token = tokens[0]
    if curr_token == JSON_LEFT_BRACKET:
        return parse_array(tokens[1:])
    elif curr_token == JSON_LEFT_BRACE:
        return parse_object(tokens[1:])
    else:
        return curr_token, tokens[1:]

if __name__ == '__main__':
    student = {'age': 17, 'name': 'first last' ,'subjects': [
        {'name': 'English', 'marks': 93.5}, {'name': 'Maths', 'marks': 95}
    ], 'bad_habits': None, 'is_voter': False, 'hobbies': ['playing football', 'dancing']}
    import json
    json_student = json.dumps(student)
    print("Original JSON : ", json_student)
    _tokens = get_tokens_from_lexical_analysis(json_student)
    print("Tokens after lexical analysis : ", _tokens)
    json_dict = parse(_tokens)
    print("Parsed JSON : ",json_dict[0])
