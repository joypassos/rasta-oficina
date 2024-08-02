## Migraçtion for  Oracle Cloud Infrastructure (OCI)

1. OCI Environment Configuration

Create VCN and Subnets:


``` bash
oci network vcn create --compartment-id <compartment_ocid> --cidr-block "10.0.0.0/16" --display-name "VCN"
oci network subnet create --compartment-id <compartment_ocid> --vcn-id <vcn_ocid> --cidr-block "10.0.1.0/24" --display-name "Public Subnet" --prohibit-public-ip-on-vnic false
oci network subnet create --compartment-id <compartment_ocid> --vcn-id <vcn_ocid> --cidr-block "10.0.2.0/24" --display-name "Private Subnet" --prohibit-public-ip-on-vnic true
```

Configure Security Rules:

``` bash
oci network security-list create --compartment-id <compartment_ocid> --vcn-id <vcn_ocid> --display-name "Security List" --egress-security-rules '[{"destination": "0.0.0.0/0", "protocol": "all"}]' --ingress-security-rules '[{"source": "0.0.0.0/0", "protocol": "6", "tcp-options": {"destination-port-range": {"max": 80, "min": 80}}}]'
```

2. Database Migration
Configure Oracle Autonomous Database:


``` bash
oci db autonomous-database create --compartment-id <compartment_ocid> --db-name "SurveyDB" --cpu-core-count 2 --data-storage-size-in-tbs 1 --admin-password <password> --display-name "SurveyDB"
```
Migrate Data: Use tools like Oracle Data Pump to migrate data from the local database to the Autonomous Database.
![image](https://github.com/user-attachments/assets/44f90a9f-e322-456f-befc-237e888ea5b7)



3. Application Migration
 
Configure OKE for Containers:


``` bash
oci ce cluster create --compartment-id <compartment_ocid> --name "SurveyCluster" --vcn-id <vcn_ocid> --kubernetes-version "v1.21.5"
```

Deploy the Application:

Create a deployment.yaml file to define the container deployment. Use kubectl to apply the configuration:
This option: I1m use GitHub Action, for monitoring deploy.

``` bash
kubectl apply -f deployment.yaml
```

4. Load Balancer Configuration

``` bash
oci lb load-balancer create --compartment-id <compartment_ocid> --display-name "SurveyLB" --shape "100Mbps" --subnet-ids '["<public_subnet_ocid>"]'
oci lb backend-set create --load-balancer-id <lb_ocid> --name "SurveyBackendSet" --policy "ROUND_ROBIN" --backends '[{"ip-address": "<instance_ip>", "port": 80}]'
oci lb listener create --load-balancer-id <lb_ocid> --default-backend-set-name "SurveyBackendSet" --name "SurveyListener" --port 80 --protocol "HTTP"
```


You can simulate the program locally and migrate the solution to Oracle Cloud Infrastructure (OCI). This will allow you to leverage the scalability, performance, and reliability of OCI to host your anonymous survey application.
