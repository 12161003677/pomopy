from app.Models import Model

class Guilds(Model):
    def __init__(self) -> None:
        super().__init__()
        self.table = 'guilds'
        self.fillable = [
            'name',
            'description',
            'users_id',
        ]