def validate_percentage_split(splits):
    total_percentage = sum(split.percentage for split in splits if split.split_type == "percentage")
    if total_percentage != 100:
        raise ValueError("Percentages must add up to 100%")
