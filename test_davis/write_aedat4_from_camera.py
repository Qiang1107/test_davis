import dv_processing as dv

capture = dv.io.CameraCapture()

# file path is relative to the git code directory
writer = dv.io.MonoCameraWriter("./test_davis/data/mono_writer_sample1.aedat4", capture)

print(f"Is event stream available? {str(writer.isEventStreamConfigured())}")
print(f"Is frame stream available? {str(writer.isFrameStreamConfigured())}")
print(f"Is imu stream available? {str(writer.isImuStreamConfigured())}")
print(f"Is trigger stream available? {str(writer.isTriggerStreamConfigured())}")