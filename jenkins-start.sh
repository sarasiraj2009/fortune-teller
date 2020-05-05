# Installing Terraform

sudo apt update && sudo apt upgrade -y

sudo apt install -y unzip wget

sudo wget https://releases.hashicorp.com/terraform/0.12.24/terraform_0.12.24_linux_amd64.zip

sudo unzip terraform_*_linux_*.zip
    
sudo mv terraform /usr/local/bin

sudo rm terraform_*_linux_*.zip

sudo git clone https://github.com/sarasiraj2009/fortune-teller/

sudo cd fortune-teller/terraform

sudo terraform fmt

sudo terraform init

sudo terraform validate

sudo terraform apply -yes