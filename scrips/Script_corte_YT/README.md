
## Documentação🔧

Problema: Selecionar trechos para complementar apresentações e automação com precisão temporal. 

Objetivo: Descrever o que é o código e as suas funções.


| **Item do Código** | **Explicação** |
|-------------------|----------------|
| `#Script para fazer cortes no YouTube` | **Comentário**: Descreve o propósito geral do script - fazer cortes/recortes em vídeos do YouTube. |
| `from pytubefix import YouTube` | **Import específico**: Importa apenas a classe `YouTube` da biblioteca `pytubefix`, que é usada para baixar vídeos do YouTube. A `pytubefix` é um fork melhorado da biblioteca `pytube` original. |
| `import os` | **Import do sistema**: Importa o módulo `os` do Python, que fornece funções para interagir com o sistema operacional (ex: manipular arquivos, remover arquivos). |
| `import subprocess` | **Import para comandos externos**: Importa o módulo `subprocess`, que permite executar comandos externos (como o FFmpeg) diretamente a partir do Python. |
| `url = input("URL: ").strip()` | **Entrada do usuário**: Solicita ao usuário que digite a URL do vídeo do YouTube, armazena na variável `url` e remove espaços em branco no início/fim com `.strip()` para evitar erros. |
| `inicio = input("Início (HH:MM:SS): ").strip()` | **Entrada de tempo**: Pede o horário de início do recorte no formato HH:MM:SS (ex: 01:30:45), armazena em `inicio` e remove espaços extras. |
| `fim = input("Fim (HH:MM:SS): ").strip()` | **Entrada de tempo**: Pede o horário de fim do recorte no mesmo formato, armazena em `fim` e remove espaços extras. |
| `def segundos(t):` | **Definição de função**: Define uma função personalizada chamada `segundos` que recebe um parâmetro `t` (string representando tempo). |
| `parts = [int(p) for p in t.split(':')]` | **List comprehension**: Divide a string `t` nos dois-pontos `:` usando `.split(':')` e converte cada parte em inteiro, criando uma lista `parts`. Exemplo: "01:02:03" → [1, 2, 3]. |
| `return parts[0]*3600 + parts[1]*60 + parts[2] if len(parts)==3 else parts[0]*60 + parts[1] if len(parts)==2 else parts[0]` | **Operador ternário aninhado**: Converte tempo para segundos totais. Se for HH:MM:SS (3 partes), calcula `horas×3600 + minutos×60 + segundos`. Se for MM:SS (2 partes), calcula `minutos×60 + segundos`. Se for apenas segundos (1 parte), retorna o valor. |
| `inicio_s, fim_s = segundos(inicio), segundos(fim)` | **Atribuição múltipla**: Chama a função `segundos()` para converter os tempos de início e fim em segundos totais e armazena nas variáveis `inicio_s` e `fim_s` simultaneamente. |
| `yt = YouTube(url)` | **Instanciação de objeto**: Cria um objeto `YouTube` usando a URL fornecida, que representa o vídeo do YouTube e permite acessar suas propriedades e streams. |
| `yt.streams.get_highest_resolution().download(filename="temp.mp4")` | **Download do vídeo**: Acessa todas as streams disponíveis (`.streams`), seleciona a de maior resolução (`.get_highest_resolution()`), e baixa o vídeo salvando como "temp.mp4" na pasta atual. |
| `subprocess.run(['ffmpeg', '-i', 'temp.mp4', '-ss', str(inicio_s), '-to', str(fim_s), '-c', 'copy', '-y', 'video_recortado.mp4'], capture_output=True)` | **Execução do FFmpeg**: Executa o comando FFmpeg com parâmetros: `-i` define arquivo de entrada, `-ss` marca o início do corte, `-to` marca o fim, `-c copy` copia streams sem re-encoding (mais rápido), `-y` sobrescreve arquivo existente. `capture_output=True` captura a saída do comando. |
| `os.remove("temp.mp4")` | **Limpeza de arquivos**: Remove o arquivo temporário "temp.mp4" do disco após o recorte ser concluído, liberando espaço de armazenamento. |
| `print("✅ Vídeo recortado pronto!")` | **Feedback visual**: Exibe uma mensagem de sucesso no console com emoji para informar ao usuário que o processo foi concluído. |
| `files.download("video_recortado.mp4")` | **Download específico do ambiente**: **⚠️ Atenção**: Esta linha funciona apenas em ambientes como Google Colab ou Jupyter notebooks. Em scripts locais, `files` não existe e causará erro. Serve para baixar o arquivo final para o computador do usuário. |


## Fluxo

Coleta -> Converte-> Baixa -> Recorta -> Limpa -> Finaliza  
