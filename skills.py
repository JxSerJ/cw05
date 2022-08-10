from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from unit import BaseUnit


class Skill(ABC):
    """
    Базовый класс умения
    """
    _stamina: float
    user = None
    target = None

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def stamina(self):
        return round(self._stamina, 1)

    @property
    @abstractmethod
    def damage(self):
        return round(self.damage, 1)


    @abstractmethod
    def skill_effect(self) -> str:
        pass

    def _is_stamina_enough(self):
        return self.user.stamina > self.stamina

    def use(self, user: BaseUnit, target: BaseUnit) -> str:
        """
        Проверка, достаточно ли выносливости у игрока для применения умения.
        Для вызова скилла везде используем просто use
        """
        self.user = user
        self.target = target
        if self._is_stamina_enough():
            return self.skill_effect()
        return f"{self.user.name} попытался использовать {self.name} но у него не хватило выносливости."


class FuryPunch(Skill):
    name = 'Свирепый пинок'
    stamina = 6
    damage = 15

    def skill_effect(self):
        self.user.stamina -= self.stamina
        self.target.hp -= self.damage
        return f'{self.user.name} использует {self.name} и наносит {self.damage} урона сопернику.'


class HardShot(Skill):
    name = 'Мощный укол'
    stamina = 5
    damage = 15

    def skill_effect(self):
        self.user.stamina -= self.stamina
        self.target.hp -= self.damage
        return f'{self.user.name} использует {self.name} и наносит {self.damage} урона сопернику.'
