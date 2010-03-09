# -*- coding: utf-8 -*-

import grok
from uvc.layout.layout import IUVCLayer
from grokcore.message import receive
from dolmen.app.layout.viewlets import FlashMessages


class Messages(FlashMessages):
    grok.layer(IUVCLayer)

    def display_messages(self):
        for message in self.messages:
            yield dict(css=message.type.replace('.', '-'),
                       type=message.type,
                       message=message.message)

    def update(self):
        self.messages = receive()