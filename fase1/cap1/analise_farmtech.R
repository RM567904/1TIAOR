# ============================================
# FarmTech Solutions - Análise Estatística
# Sistema de Análise de Dados Agrícolas em R
# ============================================

# Limpar ambiente
rm(list = ls())

# Instalar pacotes necessários (se não estiverem instalados)
required_packages <- c("httr", "jsonlite", "ggplot2", "dplyr")
new_packages <- required_packages[!(required_packages %in% installed.packages()[,"Package"])]
if(length(new_packages)) install.packages(new_packages)

# Carregar bibliotecas
library(httr)
library(jsonlite)
library(ggplot2)
library(dplyr)

# ============================================
# PARTE 1: ANÁLISE DE DADOS AGRÍCOLAS
# ============================================

cat("========================================\n")
cat("FARMTECH SOLUTIONS - ANÁLISE ESTATÍSTICA\n")
cat("========================================\n\n")

# Função para carregar e analisar dados de áreas
analisar_areas <- function() {
  tryCatch({
    # Verificar se o arquivo existe
    if (!file.exists("areas_plantio.csv")) {
      cat("⚠️ Arquivo 'areas_plantio.csv' não encontrado.\n")
      cat("Execute o programa Python primeiro para gerar os dados.\n")
      return(NULL)
    }
    
    # Carregar dados
    dados_areas <- read.csv("areas_plantio.csv", stringsAsFactors = FALSE)
    
    cat("📊 ANÁLISE DE ÁREAS DE PLANTIO\n")
    cat("--------------------------------\n")
    
    # Estatísticas básicas
    cat(sprintf("Total de áreas cadastradas: %d\n", nrow(dados_areas)))
    cat(sprintf("Área total (m²): %.2f\n", sum(dados_areas$area_total_m2)))
    cat(sprintf("Área total (hectares): %.2f\n", sum(dados_areas$area_total_ha)))
    
    # Média e desvio padrão
    media_area <- mean(dados_areas$area_total_m2)
    desvio_area <- sd(dados_areas$area_total_m2)
    mediana_area <- median(dados_areas$area_total_m2)
    
    cat(sprintf("\n📈 Estatísticas de Área (m²):\n"))
    cat(sprintf("  Média: %.2f\n", media_area))
    cat(sprintf("  Desvio Padrão: %.2f\n", desvio_area))
    cat(sprintf("  Mediana: %.2f\n", mediana_area))
    cat(sprintf("  Mínimo: %.2f\n", min(dados_areas$area_total_m2)))
    cat(sprintf("  Máximo: %.2f\n", max(dados_areas$area_total_m2)))
    cat(sprintf("  Coeficiente de Variação: %.2f%%\n", (desvio_area/media_area)*100))
    
    # Análise por cultura
    if (length(unique(dados_areas$cultura)) > 1) {
      cat("\n🌱 Análise por Cultura:\n")
      for (cult in unique(dados_areas$cultura)) {
        areas_cultura <- dados_areas[dados_areas$cultura == cult, ]
        cat(sprintf("\n%s:\n", cult))
        cat(sprintf("  Número de áreas: %d\n", nrow(areas_cultura)))
        cat(sprintf("  Área média: %.2f m²\n", mean(areas_cultura$area_total_m2)))
        cat(sprintf("  Desvio padrão: %.2f m²\n", sd(areas_cultura$area_total_m2)))
        cat(sprintf("  Área total: %.2f hectares\n", sum(areas_cultura$area_total_ha)))
      }
    }
    
    # Criar gráfico se houver dados suficientes
    if (nrow(dados_areas) >= 2) {
      # Gráfico de barras por cultura
      cultura_summary <- dados_areas %>%
        group_by(cultura) %>%
        summarise(
          total_area = sum(area_total_ha),
          count = n()
        )
      
      # Salvar gráfico
      png("analise_areas_cultura.png", width = 800, height = 600)
      par(mfrow = c(1, 2))
      
      # Gráfico 1: Área total por cultura
      barplot(cultura_summary$total_area, 
              names.arg = cultura_summary$cultura,
              main = "Área Total por Cultura (hectares)",
              col = c("green", "gold"),
              ylab = "Área (ha)",
              xlab = "Cultura")
      
      # Gráfico 2: Distribuição das áreas
      hist(dados_areas$area_total_ha, 
           main = "Distribuição das Áreas",
           xlab = "Área (hectares)",
           ylab = "Frequência",
           col = "lightblue",
           breaks = 5)
      
      dev.off()
      cat("\n✅ Gráfico salvo como 'analise_areas_cultura.png'\n")
    }
    
    return(dados_areas)
    
  }, error = function(e) {
    cat(sprintf("❌ Erro ao analisar áreas: %s\n", e$message))
    return(NULL)
  })
}

# Função para analisar dados de manejo
analisar_manejo <- function() {
  tryCatch({
    # Verificar se o arquivo existe
    if (!file.exists("manejos_insumos.csv")) {
      cat("\n⚠️ Arquivo 'manejos_insumos.csv' não encontrado.\n")
      return(NULL)
    }
    
    # Carregar dados
    dados_manejo <- read.csv("manejos_insumos.csv", stringsAsFactors = FALSE)
    
    cat("\n💊 ANÁLISE DE MANEJO DE INSUMOS\n")
    cat("--------------------------------\n")
    
    # Estatísticas básicas
    cat(sprintf("Total de aplicações: %d\n", nrow(dados_manejo)))
    
    # Análise por tipo de aplicação
    cat("\n📊 Por Tipo de Aplicação:\n")
    for (tipo in unique(dados_manejo$tipo_aplicacao)) {
      manejos_tipo <- dados_manejo[dados_manejo$tipo_aplicacao == tipo, ]
      cat(sprintf("\n%s:\n", tipo))
      cat(sprintf("  Número de aplicações: %d\n", nrow(manejos_tipo)))
      cat(sprintf("  Quantidade média: %.2f\n", mean(manejos_tipo$quantidade)))
      cat(sprintf("  Desvio padrão: %.2f\n", sd(manejos_tipo$quantidade)))
      cat(sprintf("  Total aplicado: %.2f\n", sum(manejos_tipo$quantidade)))
    }
    
    # Análise por insumo
    cat("\n🧪 Por Tipo de Insumo:\n")
    insumo_summary <- dados_manejo %>%
      group_by(insumo) %>%
      summarise(
        aplicacoes = n(),
        quantidade_total = sum(quantidade),
        quantidade_media = mean(quantidade),
        desvio_padrao = sd(quantidade)
      )
    
    for (i in 1:nrow(insumo_summary)) {
      cat(sprintf("\n%s:\n", insumo_summary$insumo[i]))
      cat(sprintf("  Aplicações: %d\n", insumo_summary$aplicacoes[i]))
      cat(sprintf("  Quantidade total: %.2f\n", insumo_summary$quantidade_total[i]))
      cat(sprintf("  Média: %.2f\n", insumo_summary$quantidade_media[i]))
      cat(sprintf("  Desvio padrão: %.2f\n", 
                  ifelse(is.na(insumo_summary$desvio_padrao[i]), 0, insumo_summary$desvio_padrao[i])))
    }
    
    # Análise por cultura
    cat("\n🌾 Por Cultura:\n")
    cultura_manejo <- dados_manejo %>%
      group_by(cultura) %>%
      summarise(
        total_aplicacoes = n(),
        quantidade_media = mean(quantidade),
        quantidade_total = sum(quantidade)
      )
    
    for (i in 1:nrow(cultura_manejo)) {
      cat(sprintf("\n%s:\n", cultura_manejo$cultura[i]))
      cat(sprintf("  Total de aplicações: %d\n", cultura_manejo$total_aplicacoes[i]))
      cat(sprintf("  Quantidade média por aplicação: %.2f\n", cultura_manejo$quantidade_media[i]))
      cat(sprintf("  Quantidade total aplicada: %.2f\n", cultura_manejo$quantidade_total[i]))
    }
    
    # Criar gráfico se houver dados suficientes
    if (nrow(dados_manejo) >= 2) {
      png("analise_manejo_insumos.png", width = 1000, height = 600)
      par(mfrow = c(1, 2))
      
      # Gráfico 1: Quantidade por insumo
      insumo_totals <- aggregate(quantidade ~ insumo, dados_manejo, sum)
      barplot(insumo_totals$quantidade,
              names.arg = insumo_totals$insumo,
              main = "Quantidade Total por Insumo",
              ylab = "Quantidade",
              col = rainbow(nrow(insumo_totals)),
              las = 2)
      
      # Gráfico 2: Distribuição por cultura
      cultura_totals <- aggregate(quantidade ~ cultura, dados_manejo, sum)
      pie(cultura_totals$quantidade,
          labels = paste(cultura_totals$cultura, 
                        sprintf("(%.1f%%)", 
                               100 * cultura_totals$quantidade / sum(cultura_totals$quantidade))),
          main = "Distribuição de Insumos por Cultura",
          col = c("lightgreen", "lightyellow"))
      
      dev.off()
      cat("\n✅ Gráfico salvo como 'analise_manejo_insumos.png'\n")
    }
    
    return(dados_manejo)
    
  }, error = function(e) {
    cat(sprintf("❌ Erro ao analisar manejo: %s\n", e$message))
    return(NULL)
  })
}

# ============================================
# PARTE 2: DADOS METEOROLÓGICOS (IR ALÉM)
# ============================================

# Função para obter dados meteorológicos
obter_dados_meteorologicos <- function(cidade = "Guarulhos", pais = "BR") {
  cat("\n\n🌤️ DADOS METEOROLÓGICOS\n")
  cat("------------------------\n")
  
  tryCatch({
    # API OpenWeatherMap (versão gratuita)
    # Nota: Em produção, use sua própria API key
    api_key <- "YOUR_API_KEY_HERE"  # Substitua com sua chave API
    
    # Para demonstração, vamos simular dados meteorológicos
    # Em produção, descomente o código abaixo e use sua API key
    
    # url <- sprintf("http://api.openweathermap.org/data/2.5/weather?q=%s,%s&appid=%s&units=metric&lang=pt_br",
    #                cidade, pais, api_key)
    # 
    # response <- GET(url)
    # 
    # if (status_code(response) == 200) {
    #   dados <- fromJSON(content(response, "text"))
    #   
    #   cat(sprintf("📍 Local: %s, %s\n", dados$name, dados$sys$country))
    #   cat(sprintf("🌡️ Temperatura: %.1f°C\n", dados$main$temp))
    #   cat(sprintf("🌡️ Sensação térmica: %.1f°C\n", dados$main$feels_like))
    #   cat(sprintf("💧 Umidade: %d%%\n", dados$main$humidity))
    #   cat(sprintf("☁️ Condição: %s\n", dados$weather[[1]]$description))
    #   cat(sprintf("💨 Vento: %.1f m/s\n", dados$wind$speed))
    #   cat(sprintf("🌅 Nascer do sol: %s\n", 
    #               format(as.POSIXct(dados$sys$sunrise, origin = "1970-01-01"), "%H:%M")))
    #   cat(sprintf("🌇 Pôr do sol: %s\n", 
    #               format(as.POSIXct(dados$sys$sunset, origin = "1970-01-01"), "%H:%M")))
    # }
    
    # Dados simulados para demonstração
    cat(sprintf("📍 Local: %s, %s\n", cidade, pais))
    cat("⚠️ Usando dados simulados (configure sua API key para dados reais)\n\n")
    
    # Simular dados meteorológicos típicos de Guarulhos
    temp <- runif(1, 18, 28)
    umidade <- runif(1, 60, 80)
    vento <- runif(1, 2, 8)
    
    cat(sprintf("🌡️ Temperatura: %.1f°C\n", temp))
    cat(sprintf("🌡️ Sensação térmica: %.1f°C\n", temp - 2))
    cat(sprintf("💧 Umidade: %.0f%%\n", umidade))
    cat(sprintf("☁️ Condição: Parcialmente nublado\n"))
    cat(sprintf("💨 Vento: %.1f m/s\n", vento))
    cat(sprintf("☔ Probabilidade de chuva: %.0f%%\n", runif(1, 10, 60)))
    
    # Análise para agricultura
    cat("\n🌾 ANÁLISE PARA AGRICULTURA:\n")
    
    if (temp < 10) {
      cat("❄️ Temperatura muito baixa - Risco de geada\n")
    } else if (temp > 35) {
      cat("🔥 Temperatura muito alta - Aumentar irrigação\n")
    } else {
      cat("✅ Temperatura adequada para a maioria das culturas\n")
    }
    
    if (umidade < 40) {
      cat("⚠️ Umidade baixa - Considerar irrigação adicional\n")
    } else if (umidade > 85) {
      cat("⚠️ Umidade alta - Risco de doenças fúngicas\n")
    } else {
      cat("✅ Umidade em níveis adequados\n")
    }
    
    if (vento > 10) {
      cat("💨 Vento forte - Evitar pulverização\n")
    } else {
      cat("✅ Condições de vento favoráveis para pulverização\n")
    }
    
  }, error = function(e) {
    cat(sprintf("❌ Erro ao obter dados meteorológicos: %s\n", e$message))
    cat("💡 Dica: Configure sua API key do OpenWeatherMap\n")
  })
}

# ============================================
# EXECUÇÃO PRINCIPAL
# ============================================

# Menu principal
executar_analise <- function() {
  repeat {
    cat("\n========================================\n")
    cat("📊 MENU DE ANÁLISE ESTATÍSTICA\n")
    cat("========================================\n")
    cat("1. Analisar Áreas de Plantio\n")
    cat("2. Analisar Manejo de Insumos\n")
    cat("3. Análise Completa (Áreas + Manejo)\n")
    cat("4. Obter Dados Meteorológicos\n")
    cat("5. Gerar Relatório Completo\n")
    cat("6. Sair\n")
    cat("\nEscolha uma opção: ")
    
    opcao <- readline()
    
    if (opcao == "1") {
      dados_areas <- analisar_areas()
    } else if (opcao == "2") {
      dados_manejo <- analisar_manejo()
    } else if (opcao == "3") {
      dados_areas <- analisar_areas()
      dados_manejo <- analisar_manejo()
    } else if (opcao == "4") {
      obter_dados_meteorologicos()
    } else if (opcao == "5") {
      cat("\n📝 GERANDO RELATÓRIO COMPLETO...\n")
      cat("================================\n")
      
      # Criar arquivo de relatório
      sink("relatorio_farmtech.txt")
      cat("FARMTECH SOLUTIONS - RELATÓRIO DE ANÁLISE\n")
      cat(format(Sys.time(), "%d/%m/%Y %H:%M:%S"))
      cat("\n\n")
      sink()
      
      # Adicionar análises ao relatório
      sink("relatorio_farmtech.txt", append = TRUE)
      dados_areas <- analisar_areas()
      dados_manejo <- analisar_manejo()
      obter_dados_meteorologicos()
      sink()
      
      cat("\n✅ Relatório salvo como 'relatorio_farmtech.txt'\n")
    } else if (opcao == "6") {
      cat("\n👋 Encerrando análise...\n")
      cat("🌱 FarmTech Solutions - Agricultura Digital!\n")
      break
    } else {
      cat("❌ Opção inválida!\n")
    }
  }
}

# Executar o sistema
executar_analise()