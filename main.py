from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage_01_data_ingestion import (
    DataIngestionTrainingPipeline as ingestion,
)
from src.textSummarizer.pipeline.stage_02_data_validation import (
    DataValidationTrainingPipeline as validation,
)
from src.textSummarizer.pipeline.stage_03_data_transformation import (
    DataTransformationTrainingPipeline as transformation,
)
from src.textSummarizer.pipeline.stage_04_model_trainer import (
    ModelTrainerPipeline as trainer,
)
from src.textSummarizer.pipeline.stage_05_model_evaluation import (
    ModelEvaluationPipeline as evaluation,
)


# stage_name = "Data Ingestion stage"

# try:
#     logger.info(f">>>>>> stage {stage_name} started <<<<<<")
#     data_ingestion = DataIngestionTrainingPipeline()
#     data_ingestion.main()
#     logger.info(f">>>>>> stage {stage_name} completed <<<<<<\n\nx==========x")
# except Exception as e:
#     logger.exception(e)
#     raise e

# stage_name = "Data Validation stage"

# try:
#     logger.info(f">>>>>> stage {stage_name} started <<<<<<")
#     data_validation = DataValidationTrainingPipeline()
#     data_validation.main()
#     logger.info(f">>>>>> stage {stage_name} completed <<<<<<\n\nx==========x")
# except Exception as e:
#     logger.exception(e)
#     raise e

# stage_name = "Data Transformation stage"
# try:
#     logger.info(f">>>>>> stage {stage_name} started <<<<<<")
#     data_transformation = DataTransformationTrainingPipeline()
#     data_transformation.main()
#     logger.info(f">>>>>> stage {stage_name} completed <<<<<<\n\nx==========x")
# except Exception as e:
#     logger.exception(e)
#     raise e

# stage_name = "Model Trainer stage"
# try:
#     logger.info(f">>>>>> stage {stage_name} started <<<<<<")
#     data_transformation = ModelTrainerPipeline()
#     data_transformation.main()
#     logger.info(f">>>>>> stage {stage_name} completed <<<<<<\n\nx==========x")
# except Exception as e:
#     logger.exception(e)
#     raise e


if __name__ == "__main__":
    list_of_stages = [ingestion, validation, transformation, trainer, evaluation]
    for stage in list_of_stages:
        stage_name = stage.__name__
        try:
            (
                logger.info(f"***************************************")
                if stage_name in ["ModelTrainerPipeline", "ModelEvaluationPipeline"]
                else None
            )
            logger.info(f">>>>>> stage {stage_name} started <<<<<<")
            class_stage = stage()
            class_stage.main()
            logger.info(f">>>>>> stage {stage_name} completed <<<<<<\n\nx==========x")
        except Exception as e:
            logger.exception(e)
            raise e
