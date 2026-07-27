# Earendil
[![GitHub repo](https://img.shields.io/badge/github-repo-green)](https://github.com/ThomasM31/Earendil)

An LLM-powered research assistant application. Upload papers and ask questions to recieve cited answers. (NotebookLM/ChatPDF-esque)

<!-- TOADD ex.
- [![Tests](https://github.com/simonw/llm/workflows/Test/badge.svg)](https://github.com/simonw/llm/actions?query=workflow%3ATest)
- ADD: Link to website with icon
-->

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
