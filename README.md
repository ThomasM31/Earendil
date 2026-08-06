<h1 align="center">Earendil</h1>
<a id="top"></a>
<div align="center">

[![GitHub repo](https://img.shields.io/badge/github-repo-green)](https://github.com/ThomasM31/Earendil)
<a href="https://github.com/ThomasM31/Earendil"><img src="https://img.shields.io/github/stars/ThomasM31/Earendil" alt="Stars Badge"/></a>
<a href="https://github.com/ThomasM31/Earendil/graphs/contributors?from=10%2F19%2F2024"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/ThomasM31/Earendil?color=2b9348"></a>
<a href="https://github.com/ThomasM31/Earendil/pulls"><img src="https://img.shields.io/github/issues-pr/ThomasM31/Earendil" alt="Pull Requests Badge"/></a>
<a href="https://github.com/ThomasM31/Earendil/issues"><img src="https://img.shields.io/github/issues/ThomasM31/Earendil" alt="Issues Badge"/></a>

An LLM-powered research assistant application. Upload papers and ask questions to recieve cited answers. (NotebookLM/ChatPDF-esque) Simply create an account, upload your research papers (PDF), ask questions about the papers and recieve answers with citations. 
<!--- 
[![Tests](https://github.com/ThomasM31/Earendil/workflows/Test/badge.svg)](https://github.com/ThomasM31/Earendil/actions?query=workflow%3ATest)
--->

</div>

### STACK: 
- Python
- FastAPI
  - PostGreSQL for chats/users (with Alembic for migration)
  - Azure for PDF storage 
  - JWT for authentication 
- React for frontend
- Docker for containerization
- GitHub actions for CI/CD

<!--- 
Document Processing Service -> PDF → Text → Chunks → Embeddings
-> pgvector (or Azure AI Search) -> OpenAI / Azure OpenAI
-> Answer + Citations
--->
