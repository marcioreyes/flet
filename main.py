from flet import Page
from flet import colors
from flet import Container
from flet import RadialGradient
from flet import Alignment
from flet import app
from flet import Column
from flet import Row

def main(page: Page):

    page.window_width= 400
    page.window_height= 559
    #page.window_bgcolor = colors.GREEN
    page.window_opacity= 1.0
    page.window_border_size= 0
    page.bgcolor= colors.BLACK
    page.window_title_bar_hidden= True
    page.window_frameless= True
    page.window_left= 800
    page.window_top= 100


    #criando o container para os componentes
    main_container= Container(
        expand= True,
        gradient=RadialGradient(
            center=Alignment(0, -1.25),
            radius=1.4,
            colors=[
                "#42445f",
                "#656666",
                "#42455f",
                "#42455f",
                "#423456",
                "#42455f",
                "#42455f",
                "#42455f",
                "#42455f",
                "#444444",
            ],
        ),
        padding= 15,
        content= Column(
            expand= True,
                controls=[
                    #linha na qual os cards serao add
                    Row(
                        expand= True,
                        alignment= 'center',
                    )
                ]
        )

    )

    page.add(main_container)
    page.update()

app(target=main, assets_dir='assets')