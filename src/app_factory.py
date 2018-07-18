# -*- coding: utf-8 -*-
from vibora import Vibora
from vibora.router import RouterStrategy
from src.views.api import bp_api

from src.settings import app_config
from src.log.config import logger
from redis import StrictRedis
from rq import Queue


def create_app():
    app = Vibora(router_strategy=RouterStrategy.CLONE)
    # app.configure_static_files()
    app.add_blueprint(bp_api)
    app.logger = logger

    job_queue = Queue(connection=StrictRedis.from_url(app_config.redis_conn))
    app.components.add(job_queue)

    return app
