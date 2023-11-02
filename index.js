const { PythonShell } = require('python-shell');


function callPythonFunction(url) {
  return new Promise((resolve, reject) => {
    const options = {
      scriptPath: './python_code',
      args: ["download_video", url,"downloads"],
    };
    const pythonShell = new PythonShell('main.py', options);

    pythonShell.on('message', (message) => {
      // Exibe a mensagem no console
      console.log(message);
    });

  });
}

module.exports = { callPythonFunction };
