"""
cm_plugin Django application initialization.
"""

from django.apps import AppConfig
from edx_django_utils.plugins.constants import (
    PluginURLs, PluginSettings
)


class CmPluginConfig(AppConfig):
    """
    Configuration for the cm_plugin Django application.
    """

    name = 'cm_plugin'
    plugin_app = {

        # Configuration setting for Plugin URLs for this app.
        PluginURLs.CONFIG: {

            'lms.djangoapp': {

                # The namespace to provide to django's urls.include.
                PluginURLs.NAMESPACE: 'cm_plugin',

                # The application namespace to provide to django's urls.include.
                # Optional; Defaults to None.
                PluginURLs.APP_NAME: 'cm_plugin',

                # The regex to provide to django's urls.url.
                # Optional; Defaults to r''.
                PluginURLs.REGEX: 'cm_plugin',

                # The python path (relative to this app) to the URLs module to be plugged into the project.
                # Optional; Defaults to 'urls'.
                PluginURLs.RELATIVE_PATH: 'cm_plugin.urls',
            }
        },
        PluginSettings.CONFIG: {
            'lms.djangoapp': {

                # Configure each settings, as needed.
                'production': {

                    # The python path (relative to this app) to the settings module for the relevant Project Type and Settings Type.
                    # Optional; Defaults to 'settings'.
                    PluginSettings.RELATIVE_PATH: 'lms.envs.tutor.production',
                },
                'common': {
                    PluginSettings.RELATIVE_PATH: 'lms.envs.common',
                },
            }
        }
    }