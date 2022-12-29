# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/kiirastuli/blob/default/sbom.json) with SHA256 checksum ([86855d29 ...](https://git.sr.ht/~sthagen/kiirastuli/blob/default/sbom.json.sha256 "sha256:86855d293f71e9f4d296190412e234f36383ebf4a5978fb142ba548c3b51563b")).
<!--[[[end]]] (checksum: bf0dcb02a3215d7ea0cef320bbf7ddc7)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                      | Version                                                        | License     | Author                                                              | Description (from packaging data)                                                                                                     |
|:----------------------------------------------------------|:---------------------------------------------------------------|:------------|:--------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------|
| [puhdistusalue](https://git.sr.ht/~sthagen/puhdistusalue) | [2022.7.24](https://pypi.org/project/puhdistusalue/2022.7.24/) | MIT License | Stefan Hagen                                                        | Puhdistusalue (Finnish for clean area here meaning purge range) - Purge monotonically named files in folders keeping range endpoints. |
| [scooby](https://github.com/banesullivan/scooby)          | [0.7.0](https://pypi.org/project/scooby/0.7.0/)                | MIT License | Dieter Werthmüller, Bane Sullivan, Alex Kaszynski, and contributors | A Great Dane turned Python environment detective                                                                                      |
| [typer](https://github.com/tiangolo/typer)                | [0.7.0](https://pypi.org/project/typer/0.7.0/)                 | MIT License | Sebastián Ramírez                                                   | Typer, build great CLIs. Easy to code. Based on Python type hints.                                                                    |
<!--[[[end]]] (checksum: ec2630d1870ff4da727af79a3cc9c79c)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                            | Version                                                   | License     | Author         | Description (from packaging data)                                                        |
|:------------------------------------------------|:----------------------------------------------------------|:------------|:---------------|:-----------------------------------------------------------------------------------------|
| [click](https://palletsprojects.com/p/click/)   | [8.1.3](https://pypi.org/project/click/8.1.3/)            | BSD License | Armin Ronacher | Composable command line interface toolkit                                                |
| [puristaa](https://git.sr.ht/~sthagen/puristaa) | [2022.7.24](https://pypi.org/project/puristaa/2022.7.24/) | MIT License | Stefan Hagen   | Puristaa (Finnish for compress) - shared prefix compression of ordered string sequences. |
<!--[[[end]]] (checksum: f5bd7773210308bff472939b2fe906c0)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
puhdistusalue==2022.7.24
  - puristaa [required: >=2022.7.24, installed: 2022.7.24]
scooby==0.7.0
typer==0.7.0
  - click [required: >=7.1.1,<9.0.0, installed: 8.1.3]
````
<!--[[[end]]] (checksum: 803bafb0ee62cc5cde25297b5493de2f)-->
