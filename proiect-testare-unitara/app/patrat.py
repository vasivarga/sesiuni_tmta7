from app.forma_geometrica import FormaGeometrica


class Patrat(FormaGeometrica):
    _latura = None

    def __init__(self, latura):
        self._latura = latura

    def get_arie(self):
        aria = self._latura * self._latura
        return aria

    def get_perimetru(self):
        perimetru = self._latura * 4
        return perimetru


