# devops-netology
!!!START!!!
Porsche
add new line
**/.terraform/* игнорируем все директории до и все что угодно после слеша

*.tfstate - игнорирует все файлы с расширением .tfstate, например А.tfstate
*.tfstate.* - игнорирует все файлы с именами sdfsfd.tfstate.bbhdsd

crash.log - игнорируем лог

*.tfvars - игнорируем все файлы с расширением .tfvars, например abcd.tfvars

override.tf - игнорируем файл с таким именем
override.tf.json - игнорируем файл с таким именем
*_override.tf - игнорируем файл, который заканчивается на _override.tf, например adc_override.tf
*_override.tf.json - игнорируем файл, который заканчивается на _override.tf.json, например test_override.tf.json

.terraformrc - игнорируем файл, который начинается с точки и дальше terraformrc
terraform.rc - игнорируем файл terrafo




Melnik@Melnik-E Desktop %vboxmanage --version                    
6.1.22r144080
Melnik@Melnik-E Desktop %vagrant version             
Installed Version: 2.2.19
Latest Version: 2.2.19
 
You're running an up-to-date version of Vagrant!
Melnik@Melnik-E Desktop % ansible --version   
ansible [core 2.12.1]
  config file = None
  configured module search path = ['/Users/Melnik/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/local/Cellar/ansible/5.2.0/libexec/lib/python3.10/site-packages/ansible
  ansible collection location = /Users/Melnik/.ansible/collections:/usr/share/ansible/collections
  executable location = /usr/local/bin/ansible
  python version = 3.10.1 (main, Dec  6 2021, 23:19:43) [Clang 12.0.0 (clang-1200.0.32.29)]
  jinja version = 3.0.3
  libyaml = True