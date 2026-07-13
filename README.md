readme_content = """# 🎮 Conversor SMC para SFC (Interface Gráfica)

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue?style=flat-square)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-orange?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)

Um aplicativo desktop moderno, minimalista e eficiente para converter em massa arquivos de ROM do Super Nintendo (SNES) da extensão antiga `.smc` para a extensão padrão `.sfc`. O programa realiza uma busca **recursiva**, o que significa que ele vasculha a pasta selecionada e todas as suas subpastas automaticamente.

---

## ✨ Funcionalidades

- **🔍 Busca Recursiva:** Encontra e converte arquivos em qualquer nível de profundidade dentro de subpastas.
- **🎨 Interface Moderna:** Visual limpo, minimalista e responsivo construído com `CustomTkinter`.
- **🌓 Tema Automático:** Suporta alternância automática entre Modo Escuro (Dark Mode) e Modo Claro (Light Mode) baseado nas configurações do seu sistema operacional.
- **📜 Log em Tempo Real:** Caixa de texto estilo console que mostra exatamente quais arquivos foram alterados durante o processo.
- **🛡️ Prevenção de Erros:** O botão de conversão é desativado temporariamente enquanto o processo roda para evitar cliques duplicados e travamentos.
