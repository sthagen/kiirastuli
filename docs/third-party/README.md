# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://github.com/sthagen/pilli/blob/default/sbom.json) with SHA256 checksum ([e6a19766 ...](https://raw.githubusercontent.com/sthagen/pilli/default/sbom.json.sha256 "sha256:e6a19766d5278135255b231a6a89bd3e006e781ff44c722f695e75d4fa5bfc89")).
<!--[[[end]]] (checksum: 87ac2da97f79bfe78013c1f5dbb2ae05)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                             | Version                                         | License     | Author                             | Description (from packaging data)                                  |
|:-------------------------------------------------|:------------------------------------------------|:------------|:-----------------------------------|:-------------------------------------------------------------------|
| [scooby](https://github.com/banesullivan/scooby) | [0.6.0](https://pypi.org/project/scooby/0.6.0/) | MIT License | Dieter Werthmüller & Bane Sullivan | A Great Dane turned Python environment detective                   |
| [typer](https://github.com/tiangolo/typer)       | [0.6.1](https://pypi.org/project/typer/0.6.1/)  | MIT License | Sebastián Ramírez                  | Typer, build great CLIs. Easy to code. Based on Python type hints. |
<!--[[[end]]] (checksum: 5a8409b54b8a123f7f96e64e5016f49a)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                          | Version                                        | License     | Author         | Description (from packaging data)         |
|:----------------------------------------------|:-----------------------------------------------|:------------|:---------------|:------------------------------------------|
| [click](https://palletsprojects.com/p/click/) | [8.1.3](https://pypi.org/project/click/8.1.3/) | BSD License | Armin Ronacher | Composable command line interface toolkit |
<!--[[[end]]] (checksum: dc3a866a7aa3332404bde3da87727cb9)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="https://raw.githubusercontent.com/sthagen/pilli/default/docs/third-party/package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
scooby==0.6.0
typer==0.6.1
  - click [required: >=7.1.1,<9.0.0, installed: 8.1.3]
````
<!--[[[end]]] (checksum: 3cf41318fc2f8070382c26da8f6d6722)-->
