from typing import List

import pandas as pd

path_to_dataset = "netflix_titles.csv"

def load_dataset(path=path_to_dataset):
    df = pd.read_csv(path_to_dataset)
    return df

def build_textual_repr(row):
    textual_repr = f'''Title: {row['title']}
    Type: {row['type']}
    Director: {row['director']}
    Cast: {row['cast']}
    Genres: {row['listed_in']},
    Released: {row["release_year"]},
    Description: {row['description']}'''
    return textual_repr


def add_textual_repr(df): 
    df["text_repr"] = df.apply(build_textual_repr, axis=1)
    
class DataLoader():
    def __init__(self, dataset_path=path_to_dataset) -> None:
        self.dataset_path = dataset_path
        self.df = None
    
    def __repr__(self):
        return f"Dataset Path: {self.dataset_path}"
    
    def _load_dataset(self) -> None:
        self.df = pd.read_csv(self.dataset_path)
        
    def _add_text_repr(self) -> None:
        self.df["text_repr"] = self.df.apply(self._build_textual_repr, axis=1)
    
    def get_movie_repr(self) -> List:
        self._load_dataset()
        self._add_text_repr()
        
        text_reprs = self.df["text_repr"].to_list()
        return text_reprs 
    
    @staticmethod    
    def _build_textual_repr(row) -> str:
        textual_repr = f'''Title: {row['title']}
        Type: {row['type']}
        Director: {row['director']}
        Cast: {row['cast']}
        Genres: {row['listed_in']},
        Released: {row["release_year"]},
        Description: {row['description']}'''
        return textual_repr