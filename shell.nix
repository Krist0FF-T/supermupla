{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python313
    pkgs.python313Packages.pygame-ce
  ];

  shellHook = ''
    echo "Run 'python3 main.py' to run the game!"
  '';
}
