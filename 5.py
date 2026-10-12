import flet as ft
from flet import TextField, ElevatedButton, Text
from flet_core import ControlEvent

dict_ = {
    'name1': 250,
    'name2': 300,
    'name3': 1000,
    'name4': 700,
    'name5': 425,
    'name6': 575,
    'name7': 400,
    'name8': 325,
    'name9': 650,
    'name10': 800
}


class MainPage(ft.Container):
    def __init__(self):
        super().__init__()

        text_name: TextField = TextField(label='Name', text_align=ft.TextAlign.LEFT, width=200)
        text_time: TextField = TextField(label='Hours Spent', text_align=ft.TextAlign.LEFT, width=200)
        text_raw_result: Text = Text(value='Monthly Pay: 0', color=ft.colors.WHITE, size=20)
        text_ndfl: Text = Text(value='NDFL: 0', color=ft.colors.WHITE, size=20)
        text_final_result: Text = Text(value='Total: 0', color=ft.colors.WHITE, size=25)
        button_calculate: ElevatedButton = ElevatedButton(text='Calculate', width=200, disabled=True)

        def validate(e: ControlEvent) -> None:
            if all([text_name.value, text_time.value]) and text_name.value in dict_:
                button_calculate.disabled = False
            else:
                button_calculate.disabled = True

            self.update()

        def submit(e: ControlEvent) -> None:
            print('Name:', text_name.value)
            print('Hours Spent:', text_time.value)
            salary = dict_.get(text_name.value)
            print('Salary/h:', salary)

            raw_result = get_monthly_pay(dict_.get(text_name.value), int(text_time.value))
            ndfl = get_ndfl(float(raw_result))
            text_raw_result.value = f'Monthly Pay: {raw_result}'
            text_ndfl.value = f'NDFL {ndfl}'
            text_final_result.value = f'Total: {float(raw_result) - float(ndfl)}'
            print(text_raw_result.value)
            self.update()

        def get_monthly_pay(hourly_salary, time_spent):
            return str(float(hourly_salary * time_spent))

        def get_ndfl(monthly_pay):
            return str(float(monthly_pay*0.13))

        self.content = ft.Column(
            controls=[
                ft.Row([text_name, text_time, button_calculate]),
                ft.Row([text_raw_result]),
                ft.Row([text_ndfl]),
                ft.Row([text_final_result])
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
        self.result = ft.Text(value='', color=ft.colors.WHITE, size=20)

        text_name.on_change = validate
        text_time.on_change = validate
        button_calculate.on_click = submit


def main(page: ft.Page):
    page.title = "Title"
    sc = MainPage()

    page.add(sc)


ft.app(target=main)
