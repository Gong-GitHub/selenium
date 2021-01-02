# Gong
from selenium1.selenium_qywx_main.page.main_interface import Main


class TestAddMember:

    def setup(self):
        self.main = Main()

    def test_add_menber(self):
        add_member = self.main.goto_add_member()
        add_member.add_member()
        # 设置简单断言，用userid查询
        assert add_member.get_menber('9')


