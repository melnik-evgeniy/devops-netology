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
