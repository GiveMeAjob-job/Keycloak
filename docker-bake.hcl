group "default" {
  targets = ["bear-review", "mech-exo"]
}

target "bear-review" {
  dockerfile = "Dockerfile"
  tags = ["ghcr.io/org/bear-review:${GITHUB_SHA}"]
  platforms = ["linux/amd64", "linux/arm64"]
}

target "mech-exo" {
  dockerfile = "Dockerfile"
  tags = ["ghcr.io/org/mech-exo:${GITHUB_SHA}"]
  platforms = ["linux/amd64", "linux/arm64"]
}
