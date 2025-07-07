{
  description = "A Nix-flake-based Python development environment";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-25.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
        python = pkgs.python312;
        pythonPackages = with pkgs.python312Packages; [ ];
      in {
        devShells.default = pkgs.mkShell {
          packages = [ python ] ++ pythonPackages;
          shellHook = ''
            echo "Entering DevShell with Python Virtual Environement"
            echo "Python : $(python --version)"
            export PATH="${python}/bin:$PATH"

            if [ -d 'venv' ]; then
              # Activate the virtual environment
              source venv/bin/activate
            else
              # Create virtual environment if not found and activate the virtual environment
              python -m venv venv
              # TODO: install requirements through pip is requirement.txt is found in the directory
              source venv/bin/activate
            fi
          '';
        };
      });
}
