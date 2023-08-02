import pytest


#
# @pytest.mark.flaky(reruns=5)
@pytest.mark.usefixtures("init_driver")
class Basetest:
    pass
