from handlers.base import BaseHandler

import logging
logger = logging.getLogger(__name__)


class IndexHandler(BaseHandler):
    def get(self):
        self.render("index.html")