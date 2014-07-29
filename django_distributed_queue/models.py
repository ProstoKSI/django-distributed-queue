from django.conf import settings

from distributed_queue import setup_dq_environment

# I use models.py because they are loaded after django settings are ready and
# before models are loaded.
# Django doesn't have a good spot yet for this.
setup_dq_environment(settings.DQ_QUEUES_SETTINGS, settings.DQ_TASKS)
