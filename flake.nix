{
  description = "Frame counter CLI for speedrun verification";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        python = pkgs.python3;
        frame-counter = python.pkgs.buildPythonApplication {
          pname = "frame-counter";
          version = "0.1.1";
          pyproject = true;

          src = ./.;

          build-system = with python.pkgs; [ setuptools ];

          pythonImportsCheck = [ "frame_counter" ];

          meta = with pkgs.lib; {
            description = "Frame counter CLI for speedrun verification";
            homepage = "https://github.com/yesseruser/frame-counter";
            license = licenses.mit;
            mainProgram = "frame-counter";
          };
        };
      in {
        packages.default = frame-counter;

        devShells.default = pkgs.mkShell {
          packages = [ pkgs.uv python frame-counter ];
        };
      });
}
