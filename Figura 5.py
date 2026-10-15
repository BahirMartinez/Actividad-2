import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import math

# ============================
# 1. DEFINIR LOS VÉRTICES
# ============================

vertices = []

# Radio del hexágono
radio = 3

# Altura del prisma
altura = 4

# Crear los vértices de las dos bases
for z in [0, altura]:

    for i in range(6):

        angulo = math.radians(60 * i)

        x = radio * math.cos(angulo)
        y = radio * math.sin(angulo)

        vertices.append((x, y, z))

# Vértices de la primera base
A = vertices[0]
B = vertices[1]
C = vertices[2]
D = vertices[3]
E = vertices[4]
F = vertices[5]

# Vértices de la segunda base
G = vertices[6]
H = vertices[7]
I = vertices[8]
J = vertices[9]
K = vertices[10]
L = vertices[11]

# ============================
# 2. CREAR LA FIGURA 3D
# ============================

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# ============================
# 3. DIBUJAR LAS CARAS
# ============================

caras = [
    [A, B, C, D, E, F],
    [G, H, I, J, K, L],

    [A, B, H, G],
    [B, C, I, H],
    [C, D, J, I],
    [D, E, K, J],
    [E, F, L, K],
    [F, A, G, L]
]

figura = Poly3DCollection(
    caras,
    alpha=0.4,
    edgecolor="black"
)

ax.add_collection3d(figura)

# ============================
# 4. DIBUJAR LOS VÉRTICES
# ============================

nombres = [
    "A", "B", "C", "D", "E", "F",
    "G", "H", "I", "J", "K", "L"
]

for nombre, vertice in zip(nombres, vertices):

    x, y, z = vertice

    ax.scatter(x, y, z, s=80)

    ax.text(
        x,
        y,
        z + 0.1,
        nombre,
        fontsize=12
    )

# ============================
# 5. DIBUJAR LAS ARISTAS
# ============================

aristas = [
    (A, B),
    (B, C),
    (C, D),
    (D, E),
    (E, F),
    (F, A),

    (G, H),
    (H, I),
    (I, J),
    (J, K),
    (K, L),
    (L, G),

    (A, G),
    (B, H),
    (C, I),
    (D, J),
    (E, K),
    (F, L)
]

for inicio, fin in aristas:

    ax.plot(
        [inicio[0], fin[0]],
        [inicio[1], fin[1]],
        [inicio[2], fin[2]],
        linewidth=2
    )

# ============================
# 6. CONFIGURAR LA ESCENA
# ============================

ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_zlim(-1, 5)

ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_zlabel("Eje Z")

ax.set_title(
    "Prisma hexagonal"
)

plt.show()