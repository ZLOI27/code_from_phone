def __init__(self,
             min_len=self.OPTIONS['min_len'],
             contain_numbers=self.OPTIONS['contain_numbers'],
             **kwargs
             ):
    self.min_len = min_len
    self.contain_numbers = contain_numbers


def validate(password: str) -> dict:
    result = {}
    if len(password) < self.min_len:
        result['min_len'] = 'too small'
    elif _has_number(password):
        result['contain_numbers'] = 'should contain at least one number'
    return result
