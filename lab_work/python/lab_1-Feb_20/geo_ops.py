import math

class Geometry3D:

    @staticmethod
    def cube(side):
        return {"Lateral Surface Area": 4 * side ** 2,"Total Surface Area": 6 * side ** 2, "Volume": side ** 3}

    @staticmethod
    def cuboid(l,w, h):
        lsa=2 * h * (l + w)
        tsa=2 * (l * w + w * h + h * l)
        vol=l * w * h
        return {"Lateral Surface Area": lsa,"Total Surface Area": tsa, "Volume": vol}

    @staticmethod
    def cylinder(r,h):
        csa=2 * math.pi * r * h
        tsa=2 * math.pi * r * (r + h)
        vol=math.pi * r ** 2 * h
        return {"Curved Surface Area": csa,"Total Surface Area": tsa, "Volume": vol}

    @staticmethod
    def cone(r,h):
        s_height=math.sqrt(r ** 2 + h ** 2)
        csa=math.pi * r * s_height
        tsa=math.pi * r * (r + s_height)
        vol=1 / 3 * math.pi * r ** 2 * h
        return {"Curved Surface Area": csa,"Total Surface Area": tsa, "Volume": vol}

    @staticmethod
    def sphere(r):
        sa=4 * math.pi * r ** 2
        vol=4 / 3 * math.pi * r ** 3
        return {"Surface Area": sa,"Volume": vol}

    @staticmethod
    def hemisphere(r):
        csa=2 * math.pi * r ** 2
        tsa=3 * math.pi * r ** 2
        vol=2 / 3 * math.pi * r ** 3
        return {"Curved Surface Area": csa,"Total Surface Area": tsa, "Volume": vol}

def run_lab_work():
    print("--- 3D Geometry Calculator ---")
    print("1. Cylinder | 2. Cone | 3. Cuboid | 4. Cube | 5. Sphere | 6. Hemisphere")
    try:
        choice=int(input("Enter your choice (1-6): "))
    except ValueError:
        print("Please enter a valid number.")
        return
    geo=Geometry3D()
    if choice == 1:
        r_cyl,h_cyl = (5, 10)
        cyl=geo.cylinder(r_cyl,h_cyl)
        print(f'Cylinder -> Radius: {r_cyl},Height: {h_cyl}')
        print(f"Curved Surface Area: {cyl['Curved Surface Area']:.2f} | TSA: {cyl['Total Surface Area']:.2f} | Volume: {cyl['Volume']:.2f}")
    elif choice == 2:
        r_cone,h_cone = (3, 4)
        cone=geo.cone(r_cone,h_cone)
        print(f'Cone -> Radius: {r_cone},Height: {h_cone}')
        print(f"Curved Surface Area: {cone['Curved Surface Area']:.2f} | Total Surface Area: {cone['Total Surface Area']:.2f} | Volume: {cone['Volume']:.2f}")
    elif choice == 3:
        l,w, h = (10, 5, 2)
        cbd=geo.cuboid(l,w, h)
        print(f'Cuboid -> L: {l},W: {w}, H: {h}')
        print(f"Curved Surface Area: {cbd['Curved Surface Area']:.2f} | Total Surface Area: {cbd['Total Surface Area']:.2f} | Volume: {cbd['Volume']:.2f}")
    elif choice == 4:
        side=5
        cube=geo.cube(side)
        print(f'Cube -> Side: {side}')
        print(f"Curved Surface Area: {cube['Curved Surface Area']:.2f} | Total Surface Area: {cube['Total Surface Area']:.2f} | Volume: {cube['Volume']:.2f}")
    elif choice == 5:
        r=5
        sph=geo.sphere(r)
        print(f'Sphere -> Radius: {r}')
        print(f"Surface Area: {sph['Surface Area']:.2f} | Volume: {sph['Volume']:.2f}")
    elif choice == 6:
        r=5
        hms=geo.hemisphere(r)
        print(f'Hemisphere -> Radius: {r}')
        print(f"Curved Surface Area: {hms['Curved Surface Area']:.2f} | Total Surface Area: {hms['Total Surface Area']:.2f} | Volume: {hms['Volume']:.2f}")
    else:
        print("Invalid Choice!")
