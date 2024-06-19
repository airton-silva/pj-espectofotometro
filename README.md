
## Para criar um ambiente virtual para a aplicação funcionar, você pode seguir estes passos:

* Crie um novo diretório para o projeto, se ainda não tiver um.
Abra um terminal e navegue até o diretório do projeto.

## Execute o seguinte comando para criar um ambiente virtual:

    python3 -m venv venv

* Isso criará um ambiente virtual chamado venv no diretório do projeto.

## Ative o ambiente virtual. No Linux ou MacOS, use:

    source venv/bin/activate

## No Windows, use:

    venv\Scripts\activate

## Com o ambiente virtual ativado, instale as dependências necessárias.

    pip install -r requirements.txt

Isso instalará todas as dependências necessárias para o projeto funcionar dentro do ambiente virtual.

## Observação 

* No windows pode ser que seja necessario fazer alterações em caminho onde sera carregado o arquivo.   
* Assim como o caminho da fonte no sistema, Ex:

    # fonte para sistemas o seu sistema operaciona
		font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


# pj-espectofotometro
