from unittest import IsolatedAsyncioTestCase

import shioaji

class BaseTestCase(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.api = sj.Shioaji()


