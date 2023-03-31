class Fsv < Formula
  include Language::Python::Virtualenv

  url "https://github.com/Joao-Filh0/flutter_super_version/archive/refs/tags/0.0.4.tar.gz"
  sha256 "add58bedc33350eec4f8cbe92ca4c6392d6980e054f10fdcc964589fcbf9717f"
  version "1.0.4"
  head "https://github.com/Joao-Filh0/flutter_super_version.git", branch: "main"

  depends_on "python@3.10"

  def install
    venv = virtualenv_create(libexec, "python3")
    venv.pip_install_and_link buildpath
    bin.install "main.py" => "fsv"
  end

  def post_install
    (bin/"fsv").write <<~EOS
      #!/bin/bash
      exec "#{libexec}/bin/python" "#{libexec}/lib/python3.10/site-packages/main.py" "$@"
    EOS
  end

  test do
    system "#{bin}/fsv", "-pg"
  end
end
