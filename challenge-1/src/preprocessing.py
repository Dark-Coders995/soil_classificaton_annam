import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def load_and_split_data(label_path):
    labels = pd.read_csv(label_path)
    train_df, valid_df = train_test_split(
    labels,
    test_size=0.2,
    stratify=labels['soil_type'], 
    random_state=42
    )
    return train_df, valid_df

def create_generators(train_df, valid_df, train_path, target_size=(331, 331), batch_size=32):
    gen = ImageDataGenerator(
                  rescale=1./255.,
                  horizontal_flip = True,
                 )
    train_generator = gen.flow_from_dataframe(
    train_df,
    directory = train_path,
    x_col = 'image_id',
    y_col = 'soil_type',
    color_mode="rgb",
    target_size = (331,331), 
    class_mode="categorical",
    batch_size=32,
    shuffle=True,
    seed=42,
    )
    
    validation_generator = gen.flow_from_dataframe(
    valid_df,
    directory = train_path, 
    x_col = 'image_id',
    y_col = 'soil_type',
    color_mode="rgb",
    target_size = (331,331),
    class_mode="categorical",
    batch_size=32,
    shuffle=False,
    seed=42,
)

    return train_generator , validation_generator
