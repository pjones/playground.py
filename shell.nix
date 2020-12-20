{ pkgs ? import <nixpkgs> { }
}:
let
  pythonEnv = pkgs.python3.withPackages (ps: with ps; [
    flask
    sqlalchemy
  ]);
in
pkgs.mkShell {
  buildInputs = with pkgs; [
    black
  ]
  ++ [ pythonEnv ];
}
