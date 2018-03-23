from rv2.core.label_source import LabelSource
from rv2.labels.object_detection_labels import (
    ObjectDetectionLabels)


class ObjectDetectionLabelSource(LabelSource):
    def get_labels(self, window, ioa_thresh=1.0):
        return self.labels.get_subwindow(
            window, ioa_thresh=ioa_thresh)

    def get_all_labels(self):
        return self.labels

    def extend(self, window, labels):
        self.labels = self.labels.concatenate(
            window, labels)

    def post_process(self, options):
        self.labels = self.labels.prune_duplicates(
            options.object_detection_options.score_thresh,
            options.object_detection_options.merge_thresh)

    def clear(self):
        self.labels = ObjectDetectionLabels.make_empty()
