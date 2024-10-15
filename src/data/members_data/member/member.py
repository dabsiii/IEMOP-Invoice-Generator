from src.data.members_data.member.member_interface import IMember


class Member(IMember):

    def name_shortname(self):
        return super().name_shortname()

    def stl_id(self):
        return super().stl_id()

    def billing_id(self):
        return super().billing_id()

    def bussiness_style(self):
        return super().bussiness_style()

    def tin_number(self):
        return super().tin_number()

    def bir_address(self):
        return super().bir_address()
