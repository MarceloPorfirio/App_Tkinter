import flet
from flet import Text,TextField, FilledButton, Row , Banner, colors, Icon, icons, TextButton

def main(page):

    dict_values = {
        'contratante': '',
        'medida_judicial': '',
        'outra_parte': '',
        'prolabore':'',
        'exito':'',
        'foro':'',
        'data':''
    }
    def gera_contrato(e):

        dict_values['contratante'] = contratante.value
        dict_values['medida_judicial'] = medida_judicial.value
        dict_values['outra_parte'] = outra_parte.value
        dict_values['prolabore'] = prolabore.value
        dict_values['exito'] = exito.value
        dict_values['foro'] = foro.value
        dict_values['data'] = data.value

        for values in dict_values.values():
            if not values:
                page.banner.open=True
                page.update()
                return
        print('Já é possível gerar o contrato')
    
    def fecha_banner(e):
        page.banner.open=False
        page.update()

    page.banner = Banner(
        bgcolor=colors.AMBER_100,
        leading=Icon(
            icons.DANGEROUS_SHARP,
            color = colors.RED_400,
            size=40

        ),
        content=Text('Ops, Todos os campos devem ser preenchidos'),
        actions=[
            TextButton(
                'Ok',
                on_click=fecha_banner
            )
        ]
    )


    titulo = Text(value='Gerador de Contrato de Prestação de Serviços Advocatícios',size=20,weight='bold')
    contratante = TextField(label='Nome do Contratante',autofocus=True)
    medida_judicial = TextField(label='Medida Judicial')
    outra_parte = TextField(label='Outra Parte')
    prolabore = TextField(label='Prolabore',prefix_text= 'R$ ')
    exito = TextField(label='Exito',suffix_text=' %')
    foro = TextField(label='Foro')
    data = TextField(label='Data do Contrato')
    btn_gerar = FilledButton(text='Gerar Contrato',on_click=gera_contrato)

    # Definir os widgets na tela
    page.add(
        # Primeira linha
        Row(
            controls= [
                titulo
            ]
        ),
        Row(
            controls=[
                contratante,
            ]
        ),
        Row(
            controls=[
                medida_judicial,outra_parte
            ]
        ),
        Row(
            controls=[
                prolabore,exito
            ]
        ),
        Row(
            controls=[
                foro,data
            ]
        ),
        Row(
            controls = [
                btn_gerar
            ]
        )
    )

flet.app(target=main)