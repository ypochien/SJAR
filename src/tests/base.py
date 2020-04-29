from unittest import IsolatedAsyncioTestCase

import shioaji as sj


class BaseTestCase(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.api = sj.Shioaji()
