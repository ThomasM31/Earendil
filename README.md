# Earendil
An LLM-powered research assistant application. Upload papers and ask questions to recieve cited answers. (NotebookLM/ChatPDF-esque)

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
