
Para criar um ambiente virtual para a aplicação funcionar, você pode seguir estes passos:

Crie um novo diretório para o projeto, se ainda não tiver um.
Abra um terminal e navegue até o diretório do projeto.
Execute o seguinte comando para criar um ambiente virtual:

python3 -m venv venv

Isso criará um ambiente virtual chamado venv no diretório do projeto.

Ative o ambiente virtual. No Linux ou MacOS, use:

source venv/bin/activate
No Windows, use:

venv\Scripts\activate

Com o ambiente virtual ativado, instale as dependências necessárias. Crie um arquivo chamado requirements.txt no diretório do projeto e adicione as seguintes linhas:

Copy code
kivy==2.0.0
kivymd==0.104.2
Pillow==9.0.1
colorgram.py==1.2.2
Depois de adicionar as dependências ao requirements.txt, instale-as usando o pip:

pip install -r requirements.txt

Isso instalará todas as dependências necessárias para o projeto funcionar dentro do ambiente virtual.

# pj-espectofotometro
