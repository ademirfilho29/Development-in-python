import os 
from PIL import Image

if __name__ == "__main__":

    pasta_fotos_para_alterar= "C:\\Users\\USER\\Desktop\\fotos editadas 5x5 cm - Copy"
        
    # caminho_pasta_salvar= "C:\\Users\\USER\\Desktop\\fotos editadas"

    #alterar a resolução das imagens 

    #formula para a resolucao em cm = (cm x dpi das fotos)/2.54
    
    nova_resu = (480,530)

    #iterar sobre cada foto da pasta 
    for foto in os.listdir(pasta_fotos_para_alterar):

        #procurar se todas são no formato png, jpg ou jpeg
        if foto.lower().endswith(('png', 'jpg', 'jpeg')):

            caminho_da_imagem =  os.path.join(pasta_fotos_para_alterar, foto)

            with Image.open(caminho_da_imagem) as img:

                if img.mode != 'RGB':

                    img = img.convert('RGB')

                    pass

                img_redimensionada = img.resize(nova_resu)

                salvar_nome = f"imagem_editada"
                img_redimensionada.save(caminho_da_imagem)

                print(f"Imagem {foto} redimensionada e salva como {salvar_nome}")


                pass

            pass

        pass

    pass