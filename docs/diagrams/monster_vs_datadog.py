from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.monitoring import Datadog
from diagrams.k8s.compute import Pod
from diagrams.custom import Custom

# Configurações visuais de alta definição
graph_attr = {
    "fontsize": "28",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "spline"
}

with Diagram("Estratégia de Observabilidade: SaaS vs The Monster IDP", show=False, filename="vs_datadog", direction="LR", graph_attr=graph_attr):

    # --- LADO DATADOG (MUITO CARO E FECHADO) ---
    with Cluster("MODELO SaaS TRADICIONAL (DATADOG/DYNATRACE)"):
        pods_dd = Pod("Apps com Agente\nProprietário (Lock-in)")
        saas_dd = Datadog("Cloud do Fornecedor\n(Fatura Variável $$$)")
        
        pods_dd >> Edge(label="Dados SAEM da sua rede", color="red", style="bold") >> saas_dd

    # --- LADO MONSTER (SOBERANO E COMPLETO) ---
    with Cluster("NOSSO MODELO (THE MONSTER IDP)"):
        pods_monster = Pod("Apps com OTel\n(Padrão CNCF)")
        
        with Cluster("Sua Infraestrutura Privada (AWS/Local)"):
            with Cluster("Governance & Security"):
                rancher = Custom("Rancher", "./rancher.png")
                cert = Custom("Cert-Manager", "./Cert-Manager.png")
                argo = Custom("ArgoCD", "./argocd.png")

            with Cluster("Observability & AIOps"):
                otel = Custom("OTel Collector", "./otel_logo.png")
                zbx = Custom("Zabbix", "./zabbix.png")
                n8n = Custom("n8n AI Engine", "./n8n_logo.png")
                kuma = Custom("Uptime Kuma", "./kuma.png")
                
            monster_stack = [otel, zbx, n8n, argo, rancher, cert, kuma]

        # A linha de valor: O tráfego de dados é interno e padronizado
        pods_monster >> Edge(label="Dados FICAM na empresa", color="darkgreen", style="bold") >> otel
        otel >> [zbx, argo, n8n]