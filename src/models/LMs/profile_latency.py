from transformers import Trainer, TrainingArguments
import time

import logging

LOG_DIR='/scratch/ns_ksinha45/graphllms/GLEM-baseline/logs'

logging.basicConfig(level=logging.DEBUG, filename=f'{LOG_DIR}/lm_latency.log')
logger = logging.getLogger(__name__)

class LatencyTrainer(Trainer):
    def training_step(self, model, inputs):
        start_time = time.time()
        loss = super().training_step(model, inputs)
        end_time = time.time()
        iteration_latency = end_time - start_time
        logger.debug(f"Iteration latency: {iteration_latency:.4f} seconds")
        return loss