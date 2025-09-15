"""
Sistema de Gestão Agrícola - FarmTech Solutions
Culturas: Café e Soja (principais culturas de São Paulo)
Desenvolvido para agricultura digital
"""

import math
import json
from datetime import datetime
from typing import List, Dict, Any

class SistemaAgricola:
    def __init__(self):
        """Inicializa o sistema com vetores para armazenar dados"""
        self.culturas_disponiveis = ["Café", "Soja"]
        
        # Vetores principais para armazenamento de dados
        self.areas_plantio = []  # Lista de dicionários com dados de área
        self.manejos_insumos = []  # Lista de dicionários com dados de manejo
        self.historico_operacoes = []  # Lista para rastreamento de operações
        
        # Parâmetros padrão para cada cultura
        self.parametros_culturas = {
            "Café": {
                "espacamento_ruas": 3.5,  # metros entre ruas
                "espacamento_plantas": 0.8,  # metros entre plantas
                "insumos_recomendados": ["Fosfato", "Nitrogênio", "Potássio", "Fungicida"],
                "formato_area": "retangular"
            },
            "Soja": {
                "espacamento_ruas": 0.45,  # metros entre ruas
                "espacamento_plantas": 0.10,  # metros entre plantas
                "insumos_recomendados": ["Calcário", "Fósforo", "Herbicida", "Inseticida"],
                "formato_area": "circular"
            }
        }
    
    def calcular_area_retangular(self, comprimento: float, largura: float) -> float:
        """Calcula área retangular para plantio de café"""
        return comprimento * largura
    
    def calcular_area_circular(self, raio: float) -> float:
        """Calcula área circular para plantio de soja (pivô central)"""
        return math.pi * (raio ** 2)
    
    def calcular_numero_ruas(self, largura: float, espacamento: float) -> int:
        """Calcula número de ruas baseado na largura e espaçamento"""
        return int(largura / espacamento)
    
    def calcular_insumo_necessario(self, area: float, dosagem_por_m2: float) -> float:
        """Calcula quantidade total de insumo necessário"""
        return area * dosagem_por_m2
    
    def entrada_dados_area(self):
        """Entrada de dados para cálculo de área de plantio"""
        print("\n=== CADASTRO DE ÁREA DE PLANTIO ===")
        print("Culturas disponíveis:")
        for i, cultura in enumerate(self.culturas_disponiveis, 1):
            print(f"{i}. {cultura}")
        
        try:
            escolha = int(input("Escolha a cultura (número): "))
            if escolha < 1 or escolha > len(self.culturas_disponiveis):
                print("❌ Opção inválida!")
                return
            
            cultura = self.culturas_disponiveis[escolha - 1]
            nome_area = input("Nome/Identificação da área: ")
            
            if self.parametros_culturas[cultura]["formato_area"] == "retangular":
                comprimento = float(input("Comprimento da área (metros): "))
                largura = float(input("Largura da área (metros): "))
                area_total = self.calcular_area_retangular(comprimento, largura)
                num_ruas = self.calcular_numero_ruas(largura, 
                    self.parametros_culturas[cultura]["espacamento_ruas"])
                
                dados_area = {
                    "id": len(self.areas_plantio) + 1,
                    "nome": nome_area,
                    "cultura": cultura,
                    "formato": "retangular",
                    "comprimento": comprimento,
                    "largura": largura,
                    "area_total": area_total,
                    "numero_ruas": num_ruas,
                    "data_cadastro": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
            else:  # circular
                raio = float(input("Raio da área circular (metros): "))
                area_total = self.calcular_area_circular(raio)
                
                dados_area = {
                    "id": len(self.areas_plantio) + 1,
                    "nome": nome_area,
                    "cultura": cultura,
                    "formato": "circular",
                    "raio": raio,
                    "area_total": area_total,
                    "data_cadastro": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
            
            self.areas_plantio.append(dados_area)
            self.historico_operacoes.append(f"Área cadastrada: {nome_area}")
            
            print(f"\n✅ Área cadastrada com sucesso!")
            print(f"📊 Área total: {area_total:.2f} m²")
            print(f"📍 Equivalente a {area_total/10000:.2f} hectares")
            
            if "numero_ruas" in dados_area:
                print(f"🚜 Número de ruas: {dados_area['numero_ruas']}")
                
        except ValueError:
            print("❌ Erro: Digite valores numéricos válidos!")
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
    
    def entrada_dados_manejo(self):
        """Entrada de dados para manejo de insumos"""
        print("\n=== CADASTRO DE MANEJO DE INSUMOS ===")
        
        if not self.areas_plantio:
            print("❌ Nenhuma área cadastrada! Cadastre uma área primeiro.")
            return
        
        print("Áreas disponíveis:")
        for area in self.areas_plantio:
            print(f"{area['id']}. {area['nome']} - {area['cultura']} ({area['area_total']:.2f} m²)")
        
        try:
            id_area = int(input("Escolha a área (ID): "))
            area_selecionada = None
            
            for area in self.areas_plantio:
                if area['id'] == id_area:
                    area_selecionada = area
                    break
            
            if not area_selecionada:
                print("❌ Área não encontrada!")
                return
            
            cultura = area_selecionada['cultura']
            print(f"\nInsumos recomendados para {cultura}:")
            insumos = self.parametros_culturas[cultura]["insumos_recomendados"]
            
            for i, insumo in enumerate(insumos, 1):
                print(f"{i}. {insumo}")
            
            escolha_insumo = int(input("Escolha o insumo (número): "))
            if escolha_insumo < 1 or escolha_insumo > len(insumos):
                print("❌ Opção inválida!")
                return
            
            insumo = insumos[escolha_insumo - 1]
            
            print("\nTipo de aplicação:")
            print("1. Pulverização (mL/m²)")
            print("2. Adubação sólida (kg/hectare)")
            
            tipo_aplicacao = int(input("Escolha o tipo: "))
            
            if tipo_aplicacao == 1:
                dosagem_ml_m2 = float(input("Dosagem (mL/m²): "))
                quantidade_total = self.calcular_insumo_necessario(
                    area_selecionada['area_total'], dosagem_ml_m2
                )
                quantidade_litros = quantidade_total / 1000
                
                dados_manejo = {
                    "id": len(self.manejos_insumos) + 1,
                    "area_id": id_area,
                    "area_nome": area_selecionada['nome'],
                    "cultura": cultura,
                    "insumo": insumo,
                    "tipo_aplicacao": "Pulverização",
                    "dosagem": f"{dosagem_ml_m2} mL/m²",
                    "quantidade_total_ml": quantidade_total,
                    "quantidade_total_litros": quantidade_litros,
                    "data_aplicacao": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                
                print(f"\n✅ Manejo cadastrado com sucesso!")
                print(f"💧 Quantidade total necessária: {quantidade_litros:.2f} litros")
                
                if "numero_ruas" in area_selecionada:
                    litros_por_rua = quantidade_litros / area_selecionada['numero_ruas']
                    print(f"🚜 Quantidade por rua: {litros_por_rua:.2f} litros/rua")
                    dados_manejo["litros_por_rua"] = litros_por_rua
                    
            else:
                dosagem_kg_ha = float(input("Dosagem (kg/hectare): "))
                area_hectares = area_selecionada['area_total'] / 10000
                quantidade_total_kg = dosagem_kg_ha * area_hectares
                
                dados_manejo = {
                    "id": len(self.manejos_insumos) + 1,
                    "area_id": id_area,
                    "area_nome": area_selecionada['nome'],
                    "cultura": cultura,
                    "insumo": insumo,
                    "tipo_aplicacao": "Adubação sólida",
                    "dosagem": f"{dosagem_kg_ha} kg/ha",
                    "quantidade_total_kg": quantidade_total_kg,
                    "data_aplicacao": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                
                print(f"\n✅ Manejo cadastrado com sucesso!")
                print(f"⚖️ Quantidade total necessária: {quantidade_total_kg:.2f} kg")
            
            self.manejos_insumos.append(dados_manejo)
            self.historico_operacoes.append(f"Manejo cadastrado: {insumo} em {area_selecionada['nome']}")
            
        except ValueError:
            print("❌ Erro: Digite valores numéricos válidos!")
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
    
    def visualizar_dados(self):
        """Visualiza todos os dados cadastrados"""
        print("\n" + "="*60)
        print("📊 RELATÓRIO COMPLETO DO SISTEMA")
        print("="*60)
        
        print("\n🌱 ÁREAS DE PLANTIO CADASTRADAS:")
        if self.areas_plantio:
            for area in self.areas_plantio:
                print(f"\n  ID: {area['id']}")
                print(f"  Nome: {area['nome']}")
                print(f"  Cultura: {area['cultura']}")
                print(f"  Formato: {area['formato']}")
                print(f"  Área Total: {area['area_total']:.2f} m² ({area['area_total']/10000:.2f} ha)")
                if 'numero_ruas' in area:
                    print(f"  Número de Ruas: {area['numero_ruas']}")
                print(f"  Data Cadastro: {area['data_cadastro']}")
        else:
            print("  Nenhuma área cadastrada.")
        
        print("\n💊 MANEJOS DE INSUMOS CADASTRADOS:")
        if self.manejos_insumos:
            for manejo in self.manejos_insumos:
                print(f"\n  ID: {manejo['id']}")
                print(f"  Área: {manejo['area_nome']}")
                print(f"  Cultura: {manejo['cultura']}")
                print(f"  Insumo: {manejo['insumo']}")
                print(f"  Tipo: {manejo['tipo_aplicacao']}")
                print(f"  Dosagem: {manejo['dosagem']}")
                if 'quantidade_total_litros' in manejo:
                    print(f"  Quantidade Total: {manejo['quantidade_total_litros']:.2f} litros")
                    if 'litros_por_rua' in manejo:
                        print(f"  Por Rua: {manejo['litros_por_rua']:.2f} litros/rua")
                elif 'quantidade_total_kg' in manejo:
                    print(f"  Quantidade Total: {manejo['quantidade_total_kg']:.2f} kg")
                print(f"  Data: {manejo['data_aplicacao']}")
        else:
            print("  Nenhum manejo cadastrado.")
        
        print("\n📈 ESTATÍSTICAS GERAIS:")
        if self.areas_plantio:
            total_area = sum(area['area_total'] for area in self.areas_plantio)
            print(f"  Área Total Cultivada: {total_area:.2f} m² ({total_area/10000:.2f} ha)")
            print(f"  Número de Áreas: {len(self.areas_plantio)}")
            
            for cultura in self.culturas_disponiveis:
                areas_cultura = [a for a in self.areas_plantio if a['cultura'] == cultura]
                if areas_cultura:
                    area_cultura_total = sum(a['area_total'] for a in areas_cultura)
                    print(f"  {cultura}: {area_cultura_total:.2f} m² ({len(areas_cultura)} áreas)")
        
        if self.manejos_insumos:
            print(f"  Total de Aplicações: {len(self.manejos_insumos)}")
        
        print("\n" + "="*60)
    
    def atualizar_dados(self):
        """Atualiza dados em uma posição específica"""
        print("\n=== ATUALIZAÇÃO DE DADOS ===")
        print("1. Atualizar Área de Plantio")
        print("2. Atualizar Manejo de Insumos")
        
        try:
            opcao = int(input("Escolha a opção: "))
            
            if opcao == 1:
                if not self.areas_plantio:
                    print("❌ Nenhuma área cadastrada!")
                    return
                
                print("\nÁreas cadastradas:")
                for area in self.areas_plantio:
                    print(f"ID {area['id']}: {area['nome']} - {area['cultura']}")
                
                id_area = int(input("Digite o ID da área a atualizar: "))
                
                for i, area in enumerate(self.areas_plantio):
                    if area['id'] == id_area:
                        print(f"\nAtualizando: {area['nome']}")
                        novo_nome = input("Novo nome (Enter para manter): ")
                        
                        if novo_nome:
                            self.areas_plantio[i]['nome'] = novo_nome
                            print("✅ Área atualizada com sucesso!")
                            self.historico_operacoes.append(f"Área atualizada: ID {id_area}")
                            
                        return
                
                print("❌ Área não encontrada!")
                
            elif opcao == 2:
                if not self.manejos_insumos:
                    print("❌ Nenhum manejo cadastrado!")
                    return
                
                print("\nManejos cadastrados:")
                for manejo in self.manejos_insumos:
                    print(f"ID {manejo['id']}: {manejo['insumo']} em {manejo['area_nome']}")
                
                id_manejo = int(input("Digite o ID do manejo a atualizar: "))
                
                for i, manejo in enumerate(self.manejos_insumos):
                    if manejo['id'] == id_manejo:
                        print(f"\nAtualizando manejo de {manejo['insumo']}")
                        
                        if manejo['tipo_aplicacao'] == "Pulverização":
                            nova_dosagem = input("Nova dosagem em mL/m² (Enter para manter): ")
                            if nova_dosagem:
                                dosagem_ml_m2 = float(nova_dosagem)
                                area_id = manejo['area_id']
                                
                                # Encontrar a área correspondente
                                for area in self.areas_plantio:
                                    if area['id'] == area_id:
                                        quantidade_total = self.calcular_insumo_necessario(
                                            area['area_total'], dosagem_ml_m2
                                        )
                                        quantidade_litros = quantidade_total / 1000
                                        
                                        self.manejos_insumos[i]['dosagem'] = f"{dosagem_ml_m2} mL/m²"
                                        self.manejos_insumos[i]['quantidade_total_ml'] = quantidade_total
                                        self.manejos_insumos[i]['quantidade_total_litros'] = quantidade_litros
                                        
                                        if 'numero_ruas' in area:
                                            litros_por_rua = quantidade_litros / area['numero_ruas']
                                            self.manejos_insumos[i]['litros_por_rua'] = litros_por_rua
                                        
                                        print("✅ Manejo atualizado com sucesso!")
                                        self.historico_operacoes.append(f"Manejo atualizado: ID {id_manejo}")
                                        break
                        return
                
                print("❌ Manejo não encontrado!")
                
        except ValueError:
            print("❌ Erro: Digite valores válidos!")
        except Exception as e:
            print(f"❌ Erro: {e}")
    
    def deletar_dados(self):
        """Deleta dados do sistema"""
        print("\n=== DELEÇÃO DE DADOS ===")
        print("1. Deletar Área de Plantio")
        print("2. Deletar Manejo de Insumos")
        
        try:
            opcao = int(input("Escolha a opção: "))
            
            if opcao == 1:
                if not self.areas_plantio:
                    print("❌ Nenhuma área cadastrada!")
                    return
                
                print("\nÁreas cadastradas:")
                for area in self.areas_plantio:
                    print(f"ID {area['id']}: {area['nome']} - {area['cultura']}")
                
                id_area = int(input("Digite o ID da área a deletar: "))
                
                for i, area in enumerate(self.areas_plantio):
                    if area['id'] == id_area:
                        confirmacao = input(f"⚠️ Confirmar deleção de '{area['nome']}'? (S/N): ")
                        if confirmacao.upper() == 'S':
                            # Remove manejos associados
                            self.manejos_insumos = [m for m in self.manejos_insumos 
                                                   if m['area_id'] != id_area]
                            # Remove a área
                            del self.areas_plantio[i]
                            print("✅ Área deletada com sucesso!")
                            self.historico_operacoes.append(f"Área deletada: ID {id_area}")
                        return
                
                print("❌ Área não encontrada!")
                
            elif opcao == 2:
                if not self.manejos_insumos:
                    print("❌ Nenhum manejo cadastrado!")
                    return
                
                print("\nManejos cadastrados:")
                for manejo in self.manejos_insumos:
                    print(f"ID {manejo['id']}: {manejo['insumo']} em {manejo['area_nome']}")
                
                id_manejo = int(input("Digite o ID do manejo a deletar: "))
                
                for i, manejo in enumerate(self.manejos_insumos):
                    if manejo['id'] == id_manejo:
                        confirmacao = input(f"⚠️ Confirmar deleção? (S/N): ")
                        if confirmacao.upper() == 'S':
                            del self.manejos_insumos[i]
                            print("✅ Manejo deletado com sucesso!")
                            self.historico_operacoes.append(f"Manejo deletado: ID {id_manejo}")
                        return
                
                print("❌ Manejo não encontrado!")
                
        except ValueError:
            print("❌ Erro: Digite valores válidos!")
        except Exception as e:
            print(f"❌ Erro: {e}")
    
    def exportar_dados_csv(self):
        """Exporta dados para CSV para análise em R"""
        print("\n=== EXPORTAÇÃO DE DADOS ===")
        
        try:
            # Exportar áreas
            if self.areas_plantio:
                with open('areas_plantio.csv', 'w') as f:
                    f.write("id,nome,cultura,area_total_m2,area_total_ha\n")
                    for area in self.areas_plantio:
                        f.write(f"{area['id']},{area['nome']},{area['cultura']},")
                        f.write(f"{area['area_total']:.2f},{area['area_total']/10000:.2f}\n")
                print("✅ Arquivo 'areas_plantio.csv' exportado!")
            
            # Exportar manejos
            if self.manejos_insumos:
                with open('manejos_insumos.csv', 'w') as f:
                    f.write("id,area_nome,cultura,insumo,tipo_aplicacao,quantidade\n")
                    for manejo in self.manejos_insumos:
                        quantidade = manejo.get('quantidade_total_litros', 
                                               manejo.get('quantidade_total_kg', 0))
                        f.write(f"{manejo['id']},{manejo['area_nome']},{manejo['cultura']},")
                        f.write(f"{manejo['insumo']},{manejo['tipo_aplicacao']},{quantidade:.2f}\n")
                print("✅ Arquivo 'manejos_insumos.csv' exportado!")
            
            print("\n📊 Dados prontos para análise em R!")
            
        except Exception as e:
            print(f"❌ Erro ao exportar: {e}")
    
    def menu_principal(self):
        """Menu principal do sistema"""
        print("\n" + "="*60)
        print("🌾 FARMTECH SOLUTIONS - SISTEMA DE GESTÃO AGRÍCOLA 🌾")
        print("="*60)
        
        while True:
            print("\n📋 MENU PRINCIPAL:")
            print("1. 📝 Entrada de Dados - Área de Plantio")
            print("2. 💊 Entrada de Dados - Manejo de Insumos")
            print("3. 📊 Visualizar Todos os Dados")
            print("4. ✏️ Atualizar Dados")
            print("5. 🗑️ Deletar Dados")
            print("6. 💾 Exportar Dados para CSV")
            print("7. 🚪 Sair do Programa")
            
            try:
                opcao = int(input("\nEscolha uma opção: "))
                
                if opcao == 1:
                    self.entrada_dados_area()
                elif opcao == 2:
                    self.entrada_dados_manejo()
                elif opcao == 3:
                    self.visualizar_dados()
                elif opcao == 4:
                    self.atualizar_dados()
                elif opcao == 5:
                    self.deletar_dados()
                elif opcao == 6:
                    self.exportar_dados_csv()
                elif opcao == 7:
                    print("\n👋 Obrigado por usar o FarmTech Solutions!")
                    print("🌱 Agricultura Digital para o Futuro!")
                    break
                else:
                    print("❌ Opção inválida! Tente novamente.")
                    
            except ValueError:
                print("❌ Por favor, digite apenas números!")
            except KeyboardInterrupt:
                print("\n\n⚠️ Programa interrompido pelo usuário.")
                break
            except Exception as e:
                print(f"❌ Erro inesperado: {e}")


# Função principal para executar o sistema
def main():
    sistema = SistemaAgricola()
    sistema.menu_principal()


if __name__ == "__main__":
    main()