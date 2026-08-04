<h1 align="center">Earendil</h1>
<a id="top"></a>
<div align="center">

[![GitHub repo](https://img.shields.io/badge/github-repo-green)](https://github.com/ThomasM31/Earendil)
<a href="https://github.com/ThomasM31/Earendil"><img src="https://img.shields.io/github/stars/ThomasM31/Earendil" alt="Stars Badge"/></a>
<a href="https://github.com/ThomasM31/Earendil/graphs/contributors?from=10%2F19%2F2024"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/ThomasM31/Earendil?color=2b9348"></a>
<a href="https://github.com/ThomasM31/Earendil/pulls"><img src="https://img.shields.io/github/issues-pr/ThomasM31/Earendil/" alt="Pull Requests Badge"/></a>
<a href="https://github.com/ThomasM31/Earendil/issues"><img src="https://img.shields.io/github/issues/ThomasM31/Earendil/" alt="Issues Badge"/></a>

An LLM-powered research assistant application. Upload papers and ask questions to recieve cited answers. (NotebookLM/ChatPDF-esque)
<!--- 
[![Tests](https://github.com/ThomasM31/Earendil/workflows/Test/badge.svg)](https://github.com/ThomasM31/Earendil/actions?query=workflow%3ATest)
--->

</div>

### STACK: 
- FASTapi REST API
  - PostGreSQL for chats/users
  - Azure for PDF storage 
  - JWT for authentication 
- React for frontend
- Docker 
- GitHub actions for CI/CD

### GOAL:
A web application where users can:
- Sign in
- Upload research papers (PDFs)
- Ask questions about the uploaded papers
- Receive answers with citations
- View previous chats
- Manage their document library

### NOTES:
            Document Processing Service

                         │

          PDF → Text → Chunks → Embeddings

                         │

            pgvector (or Azure AI Search)

                         │

                OpenAI / Azure OpenAI

                         │

                 Answer + Citations
