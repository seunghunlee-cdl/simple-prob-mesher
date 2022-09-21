import gmsh


def cantilever(L: float, H: float, h: float, filename: str = 'cantilever.msh') -> None:
    """
    L: longitudinal length 
    H: Height
    h: Mesh size
    """
    gmsh.initialize()
    gmsh.model.geo.addPoint(0,0,0,h,1)
    gmsh.model.geo.addPoint(L,0,0,h,2)
    gmsh.model.geo.addPoint(L,H,0,h,3)
    gmsh.model.geo.addPoint(0,H,0,h,4)

    gmsh.model.geo.addPoint(L,0.45*H,0,h,5) #physical group Point
    gmsh.model.geo.addPoint(L,0.55*H,0,h,6)

    gmsh.model.geo.addLine(1,2,1)
    gmsh.model.geo.addLine(2,5,2)
    gmsh.model.geo.addLine(5,6,3)
    gmsh.model.geo.addLine(6,3,4)
    gmsh.model.geo.addLine(3,4,5)
    gmsh.model.geo.addLine(4,1,6)

    gmsh.model.geo.addCurveLoop([1,2,3,4,5,6],1)
    gmsh.model.geo.addPlaneSurface([1],1)

    gmsh.model.addPhysicalGroup(1,[3], name = "load")
    gmsh.model.addPhysicalGroup(1,[6], name = "spc0")
    gmsh.model.addPhysicalGroup(1,[6], name = "spc1")
    gmsh.model.geo.synchronize()
    gmsh.model.mesh.generate(2)
    gmsh.write(filename)
    gmsh.finalize()