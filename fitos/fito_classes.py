import transformers

class MyEarlyStoppingCallback(transformers.TrainerCallback):
    def __init__(self, metric_name,early_stopping_patience,lower_is_better):
        self.metric_name = metric_name
        self.early_stopping_patience = early_stopping_patience
        self.lower_is_better = lower_is_better
        self.best_metric = None
        self.patience_counter = 0

    def on_evaluate(self, args, state, control, metrics=None, **kwargs):
        if metrics is None:
            return

        current_metric = metrics.get(self.metric_name)

        if self.best_metric is None:
            self.best_metric = current_metric
        elif (self.lower_is_better & (current_metric < self.best_metric))|(~self.lower_is_better & (current_metric > self.best_metric)):
            self.best_metric = current_metric
            self.patience_counter = 0
        else:
            self.patience_counter += 1

            if self.patience_counter >= self.early_stopping_patience:
                control.should_training_stop = True