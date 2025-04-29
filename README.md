<!DOCTYPE html>
<html lang="pt-BR">
  <h1>🐾 Furia Fan - Bot Discord</h1>
  
  <p>O <strong>Furia Fan</strong> é um bot feito especialmente para os fãs do time de CS2 da FURIA! Com ele, você pode obter estatísticas, informações dos jogadores, rotas em game, replays e ainda se divertir com um quiz exclusivo sobre o time!</p>

  <h2>🚀 Tecnologias Utilizadas</h2>
  <ul>
    <li><strong>Python</strong> – Linguagem principal do bot.</li>
    <li><strong>Parsel</strong> – Utilizada para extrair informações de páginas da web (web scraping).</li>
    <li><strong>Cloudscraper</strong> – Lida com sites protegidos por Cloudflare para scraping.</li>
    <li><strong>OpenAI</strong> – Geração automática de perguntas para o quiz (uso limitado devido à versão gratuita da API).</li>
  </ul>

  <h2>🐳 Como rodar o projeto com Docker</h2>

  <h3>Pré-requisitos</h3>
  <p>Docker instalado: <a href="https://www.docker.com/get-started" target="_blank">https://www.docker.com/get-started</a></p>

  <h3>Passos:</h3>
  <ol>
    <li>Adicione o bot no seu servidor:
      <a href="https://discord.com/developers/applications/1364986522977173565/installation" class="discord-btn" target="_blank">Bot Invite</a>
    </li>
    <li>Execute o Docker e faça login:
      <pre><code>docker login</code></pre>
    </li>
    <li>Baixe a imagem:
      <pre><code>docker pull emmillyf/furiafan:latest</code></pre>
    </li>
    <li>Execute:
    <pre><code>docker build -t seu_usuario/furiafan -f Dockerfile ./app
    docker run --env-file .env furia-fan</code></pre>
    </li>
  </ol>

  <h2>🧠 Comandos Disponíveis</h2>

  <table border="1" cellspacing="0" cellpadding="8">
    <thead>
      <tr>
        <th>Comando</th>
        <th>Descrição</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>/jogador</td><td>Informações e estatísticas de um jogador</td></tr>
      <tr><td>/jogadores</td><td>Lista todos os jogadores do time FURIA</td></tr>
      <tr><td>/quiz</td><td>Inicia um quiz com perguntas sobre o time FURIA</td></tr>
      <tr><td>/redesocial</td><td>Mostra as redes sociais oficiais da FURIA</td></tr>
      <tr><td>/replay</td><td>Apresenta replays das melhores jogadas</td></tr>
      <tr><td>/rotas</td><td>Explica as rotas dos jogadores</td></tr>
      <tr><td>/time</td><td>Mostra informações gerais sobre o time FURIA</td></tr>
      <tr><td>/estatísticas</td><td>Estatísticas gerais do time</td></tr>
      <tr><td>/inventario</td><td>Mostra o inventário de um jogador</td></tr>
    </tbody>
  </table>

  <p><strong>⚠️ Obs:</strong> O comando <code>/quiz</code> depende da API da OpenAI e pode estar sujeito a limitações de uso.</p>

  <h2>☁️ Hospedagem com Discloud</h2>
  <p>O bot está hospedado gratuitamente usando a plataforma <a href="https://discloud.com/" target="_blank">Discloud</a>, ideal para projetos Discord de pequeno e médio porte.</p>

  <h2>🔗 Convide o Bot para o seu servidor</h2>
  <p>👉 <a href="https://discord.com/oauth2/authorize?client_id=1364986522977173565" target="_blank">Adicionar o Furia Fan ao seu servidor</a></p>

</body>
</html>
