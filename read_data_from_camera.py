import dv_processing as dv
import cv2 as cv
import time

# Open any camera
capture = dv.io.CameraCapture()

# Initiate a preview window
cv.namedWindow("Preview", cv.WINDOW_NORMAL)

# Read next frame from the camera
while capture.isRunning():
    # Read a frame from the camera
    frame = capture.getNextFrame()
    events = capture.getNextEventBatch()
    imu_batch = capture.getNextImuBatch()

    if frame is not None and events is not None:
        # Print received packet time range
        print(f"********************************************** \n [{frame}]")
        print(f"Received a frame at time [{frame.timestamp}]")
        print(f"********************************************** \n [{events}]")
        print(f"Received events within time range [{events.getLowestTime()}; {events.getHighestTime()}]")
        print(f"********************************************** \n [{imu_batch}]")
        print(f"Received imu data within time range [{imu_batch[0].timestamp}; {imu_batch[-1].timestamp}]")
        # break

        # Show a preview of the image
        cv.imshow("Preview", frame.image)

    else:
        # No data has arrived yet, short sleep to reduce CPU load
        time.sleep(0.001)
    cv.waitKey(2)
