# DevBox

DevBox is a lightweight, rootless project helper for **Termux on Android**. It detects existing project files and only invokes build systems that are already configured. It does not need Termux:X11, Android Studio, AIDE, or downloaded binaries.

## Install

```sh
git clone <your-devbox-repository> && cd devbox/devbox
chmod +x install.sh uninstall.sh bin/devbox
./install.sh
devbox help
```

`install.sh` intentionally runs only in Termux, installs Python if absent, and copies DevBox to `$PREFIX/bin` and `$PREFIX/lib/devbox`. Use `devbox doctor` before adding optional toolchains.

## Commands

`devbox help`, `version`, `doctor`, `detect`, `create NAME`, `init`, `build`, `run`, `package`, `apk`, `web`, `clean`, `info`, `install`, `update`, `android`, and `gamepack` are available. Run `devbox` with no arguments for the small interactive menu.

Create without overwriting a directory:

```sh
devbox create demo --python
devbox create game --pygame
devbox create native --cpp
devbox create hello --java
devbox create game --godot
devbox create site --web
```

## Usage by project type

* **Python:** put `main.py` in the project and run `devbox run`. For nonstandard builds/runs set `[build] command` or `[run] command` in `devbox.toml`.
* **Pygame / Pygbag:** install Pygame with `devbox install pygame`; install the published Python package yourself with `pip install pygbag`, then `devbox web --serve --port 8000`. A valid `main.py` is required and pygbag produces `build/web/`.
* **C++:** use a `CMakeLists.txt` (or sources) and `devbox build`; CMake projects are configured into the project-local `build/` directory. Install required tools with `pkg install clang cmake`.
* **Java:** Maven and Gradle projects run their existing build files. Plain Java projects should set a `[build] command`; install `openjdk-17` with `devbox install java`.
* **Godot:** `project.godot` is detected and `devbox run` invokes `godot --path . --editor` when Godot is installed. DevBox makes no claim that Godot export is available without your configured export templates.
* **Android:** an existing Android Gradle project is built with `devbox apk`; discovered APKs are copied to `dist/`. Use `devbox android doctor`, `devbox android adb devices`, `devbox android sign ...`, or `devbox android install app.apk`. Missing tools are reported rather than invented.
* **Minecraft Fabric / Forge:** `fabric.mod.json` and `mods.toml` are detected. Their Gradle builds can run if their checked-in wrapper/toolchain works; add an explicit build command if needed.

## Safety and dependencies

`devbox install` maps only these feature names to real packages: `python` → `python`, `pygame` → `python python-pygame`, `java` → `openjdk-17`, `android` → `android-tools`, and `web` → `python` (then it prints the optional pygbag command). Package manager confirmation remains visible. `clean` only removes this project's `build/` and `dist/`; creation refuses existing paths. DevBox never uses sudo.

For Python/Pygame, DevBox deliberately refuses native APK generation unless it finds an actual Android Gradle packaging project. `aapt`, `apksigner`, and `zipalign` availability varies with configured Termux repositories; `doctor` prints their exact known package names when absent.
