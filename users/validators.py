import re

# from rest_framework.exceptions import ValidationError
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _

@deconstructible
class CPFValidator:
    terms = []
    
    def _first_check_digit(self):
        check_digit1 = sum([term * (10 - count) for count, term in enumerate(self.terms[:-2])]) % 11
        return 0 if check_digit1 < 2 else 11 - check_digit1
    
    def _second_check_digit(self):
        check_digit2 = sum([term * (11 - count) for count, term in enumerate(self.terms[:-1])]) % 11
        return 0 if check_digit2 < 2 else 11 - check_digit2
        
    
    def __call__(self, value):
        if re.fullmatch('^\d{11}$', value):
            self.terms = [int(term) for term in list(value)]
            
            if all(term == self.terms[0] for term in self.terms):
                raise ValidationError(
                    _('All digit are equals.')
                )
            
            check_digit1 = self._first_check_digit()
            check_digit2 = self._second_check_digit()
            
            if check_digit1 != self.terms[9] or check_digit2 != self.terms[10]:
                raise ValidationError(_('Is not valid.'))
        else:
            raise ValidationError(
                _('Must contain 11 digits.'),
            )
    
    def __eq__(self, other):
        return isinstance(other, CPFValidator)


@deconstructible
class DriverLicenseRegisterNumberValidator:
    terms = []
    
    def _first_check_digit(self):
        check_digit1 = sum([term * (9 - count) for count, term in enumerate(self.terms[:-2])]) % 11
        return check_digit1
    
    def _second_check_digit(self):
        check_digit2 = sum([term * count for count, term in enumerate(self.terms[:9])]) % 11
        return check_digit2
    
    def __call__(self, value):
        if re.fullmatch('^\d{9}$', value):
            self.terms = [int(term) for term in list(value)]
            
            if all(term == self.terms[0] for term in self.terms):
                raise ValidationError(
                    _('All digit are equals.')
                )
            
            check_digit1 = self._first_check_digit()
            check_digit2 = self._second_check_digit()
            
            if check_digit1 > 9:
                check_digit1 = 0
                
                if check_digit2 - 2 < 0:
                    check_digit2 += 9
                elif check_digit2 - 2 >= 0:
                    check_digit2 -= 2
            
            check_digit2 = 0 if check_digit2 > 9 else check_digit2
            
            if check_digit1 != self.terms[9] or check_digit2 != self.terms[10]:
                raise ValidationError(_('Is not valid.'))
        else:
            raise ValidationError(
                _('Must contain 9 digits.'),
            )
        
    def __eq__(self, other):
        return isinstance(other, CPFValidator)