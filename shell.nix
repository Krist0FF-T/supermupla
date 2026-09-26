let
  pkgs = import <nixpkgs> {};
in pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (python-pkgs: [
      python-pkgs.pygame-ce
      # add more deps here
    ]))
  ];

  shellHook = ''
    echo "Run 'python3 -m supermupla' to run the game!"
  '';
}

