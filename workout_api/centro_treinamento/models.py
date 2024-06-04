from sqlalchemy import Integer, String
from WORKOUT_API.workout_api.contrib.models import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship

class CentroTreinamentoModels(BaseModel):
    __tablename__ = 'centro_treinamento'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    endereco: Mapped[str] = mapped_column(String(60), nullable=False)
    proprietario: Mapped[str] = mapped_column(String(30), nullable=False)
    atleta: Mapped['AtletaModel'] = relationship(back_populates='centro_treinamento')