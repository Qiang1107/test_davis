import dv_processing as dv
import cv2 as cv
from datetime import timedelta

# Open a file
reader = dv.io.MonoCameraRecording("./test_davis/data/getAllDataFromCamera_3.aedat4")

# Get and print the camera name that data from recorded from
print(f"Opened an AEDAT4 file which contains data from [{reader.getCameraName()}] camera")


def slicing_callback(events: dv.EventStore):
    frame = visualizer.generateImage(events)
    cv.imshow("Preview", frame)
    cv.waitKey(33)

slicer = dv.EventStreamSlicer()
cv.namedWindow("Preview", cv.WINDOW_NORMAL)
visualizer = dv.visualization.EventVisualizer(reader.getEventResolution())
visualizer.setBackgroundColor(dv.visualization.colors.white())
visualizer.setPositiveColor(dv.visualization.colors.red())
visualizer.setNegativeColor(dv.visualization.colors.green())
slicer.doEveryTimeInterval(timedelta(milliseconds=33), slicing_callback)

# Read events from the file
while reader.isRunning():
    events = reader.getNextEventBatch()
    if events is not None:
        slicer.accept(events)