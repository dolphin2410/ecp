import pandas as pd
import math

class CompoundDataNotFound(Exception):
    pass

class CompoundData:
    def __init__(self, dataset: pd.DataFrame, solution_name: str):
        self.dataset = dataset
        self.solution_name = solution_name
        self.ions = self.get_ions()
        self.ion_charge = self.get_ion_charge()
        self.ion_num = self.get_ion_num()
        self.ion_mass = self.get_ion_mass()

    def from_grams_to_molar_conductivity(self, grams: float) -> float:
        molar_mass = sum(self.ion_mass)
        volume = 0.05 # in liters
        return grams / molar_mass / volume
    
    def get_data_of(self, key: str):
        """requires manual nan filtering"""
        search_key = f'{self.solution_name}'

        if len(self.dataset[self.dataset['compound_name'] == search_key]) == 0:
            print(self.solution_name)
            raise CompoundDataNotFound()

        return self.dataset[self.dataset['compound_name'] == search_key].reset_index().iloc[0][key]
    
    def get_ions(self) -> list[str]:
        return str(self.get_data_of("ions")).split(", ")
    
    def get_ion_charge(self) -> list[int]:
        raw = str(self.get_data_of("ion_charge")).split(", ")
        return list(map(int, raw))
    
    def get_ion_num(self) -> list[int]:
        raw = str(self.get_data_of("ion_num")).split(", ")
        return list(map(int, raw))
    
    def get_ion_mass(self) -> list[float]:
        raw = str(self.get_data_of("ion_mass")).split(", ")
        return list(map(float, raw))

    def get_ionization_concentration(self, initial_molar_concentration) -> list[float]:
        equilibrium_constant = float(self.get_data_of("Ka"))
        m, n = tuple(self.ion_num)

        if math.isnan(equilibrium_constant):
            return [m * initial_molar_concentration, n * initial_molar_concentration]
        else:
            y = (-equilibrium_constant + math.sqrt(math.pow(equilibrium_constant, 2) + 4 * equilibrium_constant * m * n * initial_molar_concentration)) / (2 * m * n)
            return [m * y, n * y]
        
    def get_data(self, initial_molar_concentration: float):
        cation_charge, anion_charge = tuple(self.ion_charge)
        cation_num, anion_num = tuple(self.ion_num)
        cation_mass, anion_mass = tuple(self.ion_mass)
        cation_concentration, anion_concentration = tuple(self.get_ionization_concentration(initial_molar_concentration))
        return [cation_charge, cation_num, cation_mass, cation_concentration]
    
