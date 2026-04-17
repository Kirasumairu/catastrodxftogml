# Catastro DXL a GSML

## Install

```sh
docker run -it --rm --name python3 -v $PWD:/app -w /app ubuntu:22.04 /bin/bash

apt update
apt install python3 gdal-bin
```

## Run

```sh
# python3 dxf2gmlv4.py [in] [out] [EPSG]
python3 dxf2gmlv4.py in.dxf out.gml 25828
```

## ES.LOCAL.CP

- Asignar UID: ES.LOCAL.CP.1A -> ES.LOCAL.CP.XYZ
- Asignar referencia catastral: ES.SDGC.CP 

## Info

---

## References

1. [Debian GDAL](https://tracker.debian.org/pkg/gdal) -> [GDAL bin](https://packages.debian.org/unstable/gdal-bin)
1. [Blog gvSIG](https://blog.gvsig.org/2016/03/16/script-para-convertir-dxf-a-gml-con-gvsig-2-3-gracias-a-sigdeletras/) -> [Sigdeletras](https://sigdeletras.com/2016/dxf2gmlcatastro-script-python-para-convertir-de-dxf-a-gml-parcela-catastral/) -> [dxf2gmlcatastro](https://github.com/sigdeletras/dxf2gmlcatastro) -> [Windows GDAL](https://sigdeletras.com/2016/instalacion-de-python-y-gdal-en-windows/)
1. [Generador GML](https://generador-gml.xyz/)
1. []()
1. [Validar](https://www.youtube.com/watch?v=V1TlG5zv2ik)
1. [AutoCAD GML plugin](https://github.com/chapulincatastral/generador-gml)
1. [Formato GML](https://www.catastro.hacienda.gob.es/documentos/formatos_intercambio/Formato%20GML%20parcela%20catastral.pdf)
