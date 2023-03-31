 class Fsv < Formula
  include Language::Python::Virtualenv

  url "https://github.com/Joao-Filh0/flutter_super_version/archive/refs/tags/0.0.1.tar.gz"
  sha256 "9d023bd2e4f965025412fe55620e97a941de123d1f91e2fa9374f62850eed1df"
  version "1.0.1"
  head "https://github.com/Joao-Filh0/flutter_super_version.git", branch: "main"

  depends_on "python@3.9"

  def install
    virtualenv_install_with_resources
    bin.install "fsv"
  end

  def post_install
    (bin/"meu_programa").write <<~EOS
      #!/bin/bash
      exec "#{libexec}/bin/python" "#{libexec}/lib/python3.9/site-packages/main.py" "$@"
    EOS
  end

  test do
    # Aqui você pode adicionar um teste simples para o seu script Python, por exemplo:
    system "#{bin}/fsv", "-pg"
  end
end
