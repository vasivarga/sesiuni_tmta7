from app.forma_geometrica import FormaGeometrica


class Cerc(FormaGeometrica):
    _raza = None

    def __init__(self, raza):
        self._raza = raza

    def get_arie(self):
        aria = self.PI * self._raza * self._raza
        return aria

    def get_diametru(self):
        return 2 * self._raza

