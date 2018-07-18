# -*- coding: utf-8 -*-
import time

from vibora.responses import JsonResponse
from vibora.blueprints import Blueprint
from rq import Queue

from src.log.config import logger
from src.job.word import count_words

bp_api = Blueprint()


@bp_api.route('/time')
async def get_time(job_queue: Queue):
    logger.info('get user request')

    job_queue.enqueue(count_words, str(time.time()))
    return JsonResponse({'time': str(time.time())})
