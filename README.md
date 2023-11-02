# downtube
My npm dependecy to download youtube video, even a plylist.

# Exemplo de repositório

Este repositório contém exemplos de scripts em diferentes linguagens de programação.

## JavaScript


```javascript
// Importa o módulo de download
const { callPythonFunction} = require('./index');

const videoUrl = 'https://youtube.com/playlist?list=PL5IUqFIqz3QAdJsrxqsHBaBFBigxDThNF&si=GM_cUodtFYy72sYG'; // Substitua VIDEO_ID pela ID do vídeo

callPythonFunction(videoUrl)
  .then((result) => {
    console.log(result);
  })
  .catch((error) => {
    console.error(`Erro na solicitação de download: ${error}`);
  });
