variable "host" {
}

variable "client_certificate" {
}

variable "client_key" {
}

variable "cluster_ca_certificate" {
}

variable "docker-image" {
  type        = string
  description = "name of the docker image to deploy"
  default     = "example/example:latest"
}