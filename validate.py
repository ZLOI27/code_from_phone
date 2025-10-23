    def __init__(self,
             min_len=OPTIONS['min_len'],
             contain_numbers=OPTIONS['contain_numbers'],
             **kwargs
             ):
        self.min_len = min_len
        self.contain_numbers = contain_numbers


    def validate(self, password: str) -> dict:
        result = {}
        if len(password) < self.min_len:
            result['min_len'] = 'too small'
        if not self._has_number(password) and self.contain_numbers:
            result['contain_numbers'] = 'should contain at least one number'
        return result
