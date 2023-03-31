 class Fsv < Formula
  include Language::Python::Virtualenv

  url "https://github.com/Joao-Filh0/flutter_super_version/archive/refs/tags/0.0.2.tar.gz"
  sha256 "a59af1e00abec015050caa3b41fdb71ccb5e9c93b70b52e3106a00a3c834e4f0"
  version "1.0.2"
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
    system "#{bin}/fsv", "-pg"
  end
end
