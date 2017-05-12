# -*- coding: utf-8 -*-
"""
    flask_security.babel
    ~~~~~~~~~~~~~~~~~~~~

    I18N support for Flask-Security.
"""

from flask_babelex import Domain
import pkg_resources
from wtforms.i18n import messages_path

from .utils import config_value as cv

wtforms_domain = Domain(messages_path(), domain='wtforms')


class Translations(object):
    """Fixes WTForms translation support and uses wtforms translations."""

    def gettext(self, string):
        return wtforms_domain.gettext(string)

    def ngettext(self, singular, plural, n):
        return wtforms_domain.ngettext(singular, plural, n)


def _get_i18n_domain(app):
    return Domain(
        pkg_resources.resource_filename('flask_security', 'translations'),
        domain='flask_security'
    )
