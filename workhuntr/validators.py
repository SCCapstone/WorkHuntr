from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
import re

class ExtraValidators(object):
    def validate(self, password, user=None):
        if not re.findall('\d', password):
            raise ValidationError(_("Your password must contain at least one number."), code='No_Number',)
        if not re.findall('[A-Z]', password):
            raise ValidationError(_("Your password must contain at least one uppercase letter."), code='No_Uppercase')
        if not re.findall('[a-z]', password):
            raise ValidationError(_("Your password must contain at least one lowercase letter."), code='No_Lowercase')

    def get_help_text(self):
        return _("Your password must be of length 8 and contain at least one (1) of each: "
                 "number, uppercase letter, lowercase letter")
