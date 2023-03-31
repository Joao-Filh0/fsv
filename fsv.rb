 class Fsv < Formula
  include Language::Python::Virtualenv

  url "https://github.com/Joao-Filh0/flutter_super_version/archive/refs/tags/0.0.4.tar.gz"
  sha256 "add58bedc33350eec4f8cbe92ca4c6392d6980e054f10fdcc964589fcbf9717f"
  version "1.0.4"
  head "https://github.com/Joao-Filh0/flutter_super_version.git", branch: "main"

  depends_on "python@3.9"

  def install
    virtualenv_install_with_resources
    bin.install "fsv"
  end

  def post_install
    (bin/"fsv").write <<~EOS
      #!/bin/bash
      exec "#{libexec}/bin/python" "#{libexec}/lib/python3.9/site-packages/main.py" "$@"
    EOS
  end

  test do
    system "#{bin}/fsv", "-pg"
  end
end
