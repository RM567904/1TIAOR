# 🌾 FarmTech Solutions - Sistema de Gestão Agrícola Digital

## 📋 Visão Geral do Projeto

Sistema completo de gestão agrícola desenvolvido para a **FarmTech Solutions**, focado em agricultura digital para culturas de **Café** e **Soja** (principais culturas de São Paulo). O sistema permite gerenciar áreas de plantio, calcular manejo de insumos e realizar análises estatísticas dos dados.

## 🎯 Funcionalidades Principais

### Sistema Python
- **Gestão de Áreas de Plantio**
  - Café: cálculo de área retangular
  - Soja: cálculo de área circular (pivô central)
  - Cálculo automático de número de ruas

- **Manejo de Insumos**
  - Pulverização (mL/m²)
  - Adubação sólida (kg/hectare)
  - Cálculo de quantidade total necessária
  - Distribuição por rua de plantio

- **Operações CRUD Completas**
  - Cadastro de dados
  - Visualização de relatórios
  - Atualização de registros
  - Deleção com confirmação
  - Exportação para CSV

### Análise em R
- Estatísticas descritivas (média, desvio padrão, mediana)
- Análise por cultura e tipo de insumo
- Geração de gráficos automatizados
- **Bônus**: Integração com API meteorológica

## 🚀 Como Executar

### Pré-requisitos
- Python 3.7+
- R 4.0+
- Git (para versionamento)

### 1. Executar o Sistema Python

```bash
# Salvar o código Python como farmtech_system.py
python farmtech_system.py
```

**Menu Principal:**
1. Cadastre áreas de plantio (opção 1)
2. Cadastre manejos de insumos (opção 2)
3. Visualize os dados cadastrados (opção 3)
4. Exporte os dados para CSV (opção 6)

### 2. Executar Análise em R

```bash
# Salvar o código R como analise_farmtech.R
Rscript analise_farmtech.R
```

Ou no RStudio:
```r
source("analise_farmtech.R")
```

## 📊 Estrutura de Dados

### Vetores Principais (Python)
- `areas_plantio[]` - Armazena todas as áreas cadastradas
- `manejos_insumos[]` - Armazena todos os manejos de insumos
- `historico_operacoes[]` - Registra todas as operações realizadas

### Arquivos Gerados
- `areas_plantio.csv` - Dados das áreas para análise
- `manejos_insumos.csv` - Dados de manejo para análise
- `analise_areas_cultura.png` - Gráfico de áreas por cultura
- `analise_manejo_insumos.png` - Gráfico de distribuição de insumos
- `relatorio_farmtech.txt` - Relatório completo de análise

## 🔧 Configuração do GitHub

### Estrutura de Branches
```
main/
├── develop/
│   ├── feature/python-system
│   ├── feature/r-analysis
│   └── feature/weather-api
```

### Comandos Git Essenciais

```bash
# Inicializar repositório
git init
git add .
git commit -m "Initial commit - FarmTech Solutions"

# Criar branch de desenvolvimento
git checkout -b develop

# Criar feature branch
git checkout -b feature/python-system

# Após completar feature
git add .
git commit -m "feat: implementação do sistema Python"
git checkout develop
git merge feature/python-system

# Push para GitHub
git remote add origin https://github.com/seu-usuario/farmtech-solutions.git
git push -u origin main
```

### Arquivo .gitignore Recomendado
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/

# R
.Rhistory
.RData
.Rproj.user/

# IDE
.vscode/
.idea/
*.swp
```

## 📈 Exemplos de Uso

### Cadastro de Área de Café
1. Selecione "1" no menu principal
2. Escolha "Café" como cultura
3. Informe nome da área: "Talhão Norte"
4. Comprimento: 500 metros
5. Largura: 200 metros
6. Sistema calcula: 100.000 m² (10 hectares), 57 ruas

### Manejo de Fosfato no Café
1. Selecione "2" no menu principal
2. Escolha a área cadastrada
3. Selecione "Fosfato" como insumo
4. Tipo: Pulverização
5. Dosagem: 500 mL/m²
6. Sistema calcula: 50.000 litros totais, 877 litros/rua

## 🌤️ API Meteorológica (Bônus)

Para ativar dados meteorológicos reais no R:

1. Cadastre-se em [OpenWeatherMap](https://openweathermap.org/api)
2. Obtenha sua API key gratuita
3. No arquivo R, substitua `YOUR_API_KEY_HERE` pela sua chave
4. Descomente o código da API (linhas marcadas)

## 📝 Resumo do Artigo (Formação Social)

### Orientações para o Resumo
- **Artigo**: Capítulo 8 - Agricultura Digital (Embrapa)
- **Formato**: 1 página A4
- **Fonte**: Arial 11
- **Espaçamento**: 1 entre linhas
- **Margens**: 2cm (direita e esquerda)

### Estrutura Sugerida do Resumo
1. **Introdução** (2-3 linhas): Contexto da agricultura digital
2. **Principais Conceitos** (5-6 linhas): Tecnologias apresentadas
3. **Benefícios** (4-5 linhas): Vantagens da digitalização
4. **Desafios** (3-4 linhas): Obstáculos à implementação
5. **Conclusão** (2-3 linhas): Perspectivas futuras

## 🏆 Critérios de Avaliação Atendidos

✅ **Python**
- Suporte a 2 culturas (Café e Soja)
- Cálculo de área com diferentes geometrias
- Cálculo de manejo de insumos
- Dados organizados em vetores
- Menu completo com CRUD
- Loops e estruturas de decisão

✅ **R**
- Análise estatística (média, desvio padrão)
- Importação de dados do Python
- Geração de gráficos

✅ **Extras**
- GitHub para versionamento
- API meteorológica em R
- Sistema profissional e escalável

## 👥 Trabalho em Equipe

### Divisão Sugerida de Tarefas
1. **Dev 1**: Sistema Python base (menu, CRUD)
2. **Dev 2**: Cálculos agrícolas (áreas, insumos)
3. **Dev 3**: Análise em R e gráficos
4. **Dev 4**: Integração API e documentação
5. **Todos**: Testes, revisão e resumo do artigo

## 📞 Suporte

Para dúvidas sobre o sistema:
- Consulte este README
- Revise os comentários no código
- Teste com dados de exemplo fornecidos

## 🎓 Observações Acadêmicas

Este projeto demonstra:
- Programação estruturada em Python
- Análise de dados em R
- Versionamento com Git
- Trabalho colaborativo
- Aplicação prática em agronegócio
- Integração com APIs externas

---

## Videos demonstrando o funcionamento

[Farmtech em R](https://youtu.be/zSGKp3eRCbI)

[Farmtech em Python](https://youtu.be/N1GVMDp3FRA)

---

*Desenvolvido para o curso de Engenharia de Software - FIAP*

**FarmTech Solutions** - Transformando a agricultura através da tecnologia 🌱