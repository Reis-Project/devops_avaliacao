import flet as ft

def main(page:ft.Page):
    page.bgcolor = "blue"
    page.theme_mode = "dark"
    page.title = "App Avaliação"
    page.window.width = 450
    page.window.height = 700
    page.window.maximizable = False
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    
    def btn_editar(e):
        _stack_main.controls.clear()
        page.update()
        _stack_main.controls.append(editar)
        _stack_main.update()
    
    def btn_pesquisar(e):
        _stack_main.controls.clear()
        page.update()
        _stack_main.controls.append(pesquisar)
        _stack_main.update()
        
    def btn_config(e):
        _stack_main.controls.clear()
        page.update()
        _stack_main.controls.append(config)
        _stack_main.update()
        
    def btn_compartilhar(e):
        _stack_main.controls.clear()
        page.update()
        _stack_main.controls.append(compartilhar)
        _stack_main.update()
        
    def btn_main(e):
        _stack_main.controls.clear()
        page.update()
        _stack_main.controls.append(_main)
        _stack_main.update()
    
    page.floating_action_button = ft.FloatingActionButton(icon=ft.Icons.ADD, bgcolor="blue", on_click=btn_main)
    page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED
    
    page.appbar = ft.BottomAppBar(
        bgcolor="#F6F6F6FF",
        shape = ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.Icons.EDIT, icon_color=ft.Colors.BLUE, icon_size=28, on_click=btn_editar),
                ft.IconButton(icon=ft.Icons.SEARCH, icon_color=ft.Colors.BLUE, icon_size=28, on_click=btn_pesquisar),
                ft.Container(expand=True),
                ft.IconButton(icon=ft.Icons.SETTINGS, icon_color=ft.Colors.BLUE, icon_size=28, on_click=btn_config),
                ft.IconButton(icon=ft.Icons.SHARE, icon_color=ft.Colors.BLUE, icon_size=28, on_click=btn_compartilhar),
            ]
        ),
        
    )
    
    #Container Principal
    _main = ft.Container(
        width=400,
        height=550,
        bgcolor="#F6F6F6FF",
        border_radius= 16,
        alignment=ft.alignment.center,
        shadow=ft.BoxShadow(blur_radius=10,color=ft.Colors.with_opacity(opacity=0.9,color='black')),
        content=ft.Text(
            value="INICIO",
            color="black",
            size=32
        )
    )
    
    #Container Editar
    editar = ft.Container(
        width=400,
        height=550,
        bgcolor="#F6F6F6FF",
        border_radius= 16,
        alignment=ft.alignment.center,
        shadow=ft.BoxShadow(blur_radius=10,color=ft.Colors.with_opacity(opacity=0.9,color='black')),
        content=ft.Text(
            value="EDITAR",
            color="black",
            size=32
        )
    )
    
    #Container Pesquisar
    pesquisar = ft.Container(
        width=400,
        height=550,
        bgcolor="#F6F6F6FF",
        border_radius= 16,
        alignment=ft.alignment.center,
        shadow=ft.BoxShadow(blur_radius=10,color=ft.Colors.with_opacity(opacity=0.9,color='black')),
        content=ft.Text(
            value="PESQUISAR",
            color="black",
            size=32
        )
    )
    
    #Container Configurações
    config = ft.Container(
        width=400,
        height=550,
        bgcolor="#F6F6F6FF",
        border_radius= 16,
        alignment=ft.alignment.center,
        shadow=ft.BoxShadow(blur_radius=10,color=ft.Colors.with_opacity(opacity=0.9,color='black')),
        content=ft.Text(
            value="CONFIGURAÇÕES",
            color="black",
            size=32
        )
    )
    
    #Container Compartilhar
    compartilhar = ft.Container(
        width=400,
        height=550,
        bgcolor="#F6F6F6FF",
        border_radius= 16,
        alignment=ft.alignment.center,
        shadow=ft.BoxShadow(blur_radius=10,color=ft.Colors.with_opacity(opacity=0.9,color='black')),
        content=ft.Text(
            value="COMPARTILHAR",
            color="black",
            size=32
        )
    )
    
    #Stack Principal
    _stack_main = ft. Stack(
        controls=[
            _main
        ]
    )
    
    page.add(_stack_main)
    page.update()
    
ft.app(target=main)