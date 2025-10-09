## Custom Transformer Class: saved in a module to support "Model Pipeline" 

from sklearn.base import BaseEstimator, TransformerMixin         ## for creating Custom Transformer Class...

## Custom Transformer Class for Adding new feature to Data:       ## Used in Pipeline....
class Sector_Locality_PD_Adder(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.PD_records = None

    def fit(self, X, y=None):
        X = X.copy()   
        ## We are creating Historical Median Price Density Records from Property data: 
        self.PD_records = X.groupby(by = 'Sector_Locality').agg({'Avg_price_rupee_per_sqft': 'median'
                                                                  }).to_dict()['Avg_price_rupee_per_sqft']
        return self

    def transform(self, X):
        X = X.copy()   
        values = X['Sector_Locality'].replace(self.PD_records)   ## Using saved records...

        ## Creating a new feature with name "Sector_Locality_Price_Density" in X:
        X.insert(4, "Sector_Locality_Price_Density", values, allow_duplicates = False)
        
        ## Removing "Avg_price_rupee_per_sqft" from X as it can potentially cause Data Leakage:
        X = X[['Flat', 'Sector_Locality', 'Locality', 'Built_up_area_in_sqft', 'Sector_Locality_Price_Density', 
               'Age_Category', 'Floor_Category', 'Building_Height_Category', 'Furnishing', 'Bedrooms', 'Bathrooms', 
               'Covered_parking', 'Open_parking', 'Balcony', 'Sector_Amenity_Score']]
        
        return X


    def fit_transform(self, X, y=None, **fit_params):
        self.fit(X, y, **fit_params)
        return self.transform(X)


