## Pasta para simular o aplicativo com o banco de dados em oracle

**Migração para a Oracle Cloud Infrastructure (OCI)**

1. Configuração do Ambiente OCI
Criar VCN e Sub-redes:


``` bash
oci network vcn create --compartment-id <compartment_ocid> --cidr-block "10.0.0.0/16" --display-name "VCN"
oci network subnet create --compartment-id <compartment_ocid> --vcn-id <vcn_ocid> --cidr-block "10.0.1.0/24" --display-name "Public Subnet" --prohibit-public-ip-on-vnic false
oci network subnet create --compartment-id <compartment_ocid> --vcn-id <vcn_ocid> --cidr-block "10.0.2.0/24" --display-name "Private Subnet" --prohibit-public-ip-on-vnic true
```

Configurar Regras de Segurança:


``` bash
oci network security-list create --compartment-id <compartment_ocid> --vcn-id <vcn_ocid> --display-name "Security List" --egress-security-rules '[{"destination": "0.0.0.0/0", "protocol": "all"}]' --ingress-security-rules '[{"source": "0.0.0.0/0", "protocol": "6", "tcp-options": {"destination-port-range": {"max": 80, "min": 80}}}]'
```

2. Migração do Banco de Dados
Configurar Oracle Autonomous Database:

``` bash
oci db autonomous-database create --compartment-id <compartment_ocid> --db-name "SurveyDB" --cpu-core-count 2 --data-storage-size-in-tbs 1 --admin-password <password> --display-name "SurveyDB"
```
Migrar Dados: Use ferramentas como Oracle Data Pump para migrar dados do banco de dados local para o Autonomous Database.

3. Migração do Aplicativo
Configurar OKE para Contêineres:

``` bash
oci ce cluster create --compartment-id <compartment_ocid> --name "SurveyCluster" --vcn-id <vcn_ocid> --kubernetes-version "v1.21.5"
```

Deploy do Aplicativo:

Crie um arquivo deployment.yaml para definir o deployment do contêiner.
Use kubectl para aplicar a configuração:

``` bash
kubectl apply -f deployment.yaml
```

4. Configuração do Load Balancer
Criar e Configurar Load Balancer:


``` bash
oci lb load-balancer create --compartment-id <compartment_ocid> --display-name "SurveyLB" --shape "100Mbps" --subnet-ids '["<public_subnet_ocid>"]'
oci lb backend-set create --load-balancer-id <lb_ocid> --name "SurveyBackendSet" --policy "ROUND_ROBIN" --backends '[{"ip-address": "<instance_ip>", "port": 80}]'
oci lb listener create --load-balancer-id <lb_ocid> --default-backend-set-name "SurveyBackendSet" --name "SurveyListener" --port 80 --protocol "HTTP"
```

Conclusão
Seguindo esses passos, você pode simular o programa localmente e migrar a solução para a Oracle Cloud Infrastructure (OCI). Isso permitirá que você aproveite a escalabilidade, desempenho e confiabilidade da OCI para hospedar sua aplicação de pesquisa anônima.