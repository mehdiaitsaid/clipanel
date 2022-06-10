login_schema = {
    'email':
        {'type': 'string','regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', 'required': True
         },
    'password':
        {'type': 'string', 'required': True
         },
}
