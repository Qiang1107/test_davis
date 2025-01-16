import dv_processing as dv
import cv2 as cv
import os
from datetime import timedelta

reader = dv.io.MonoCameraRecording("./test_davis/data/getAllDataFromCamera_4.aedat4")

# 保存图片和视频的目录
output_dir = "./test_davis/data/outputImage_getAllDataFromCamera_4"
os.makedirs(output_dir, exist_ok=True)

# 为视频创建子文件夹
video_output_dir = os.path.join(output_dir, "videos")
os.makedirs(video_output_dir, exist_ok=True)

frame_video_path = os.path.join(video_output_dir, "frame_Camera_4.mp4")
event_video_path = os.path.join(video_output_dir, "event_Camera_4.mp4")
blended_video_path = os.path.join(video_output_dir, "blended_Camera_4.mp4")

# 获取分辨率和帧率
resolution = reader.getEventResolution()
fps = 30  # 每秒显示帧数

# 初始化视频写入器
fourcc = cv.VideoWriter_fourcc(*'mp4v')  # 使用 MP4 编码器

frame_writer = cv.VideoWriter(frame_video_path, fourcc, fps, (resolution[0], resolution[1]))
event_writer = cv.VideoWriter(event_video_path, fourcc, fps, (resolution[0], resolution[1]))
blended_writer = cv.VideoWriter(blended_video_path, fourcc, fps, (resolution[0], resolution[1]))
frame_counter = 0

slicer = dv.EventMultiStreamSlicer("events")
slicer.addFrameStream("frames")
visualizer = dv.visualization.EventVisualizer(reader.getEventResolution())
visualizer.setBackgroundColor(dv.visualization.colors.white())
visualizer.setPositiveColor(dv.visualization.colors.red())
visualizer.setNegativeColor(dv.visualization.colors.green())


# 保存图像和视频的函数
def save_images_and_videos(frame_image, event_image, blended_image):
    global frame_counter

    # 保存图片
    cv.imwrite(os.path.join(output_dir, f"frame_{frame_counter:04d}.png"), frame_image)
    cv.imwrite(os.path.join(output_dir, f"event_{frame_counter:04d}.png"), event_image)
    cv.imwrite(os.path.join(output_dir, f"blended_{frame_counter:04d}.png"), blended_image)

    # 写入视频帧
    frame_writer.write(frame_image)
    event_writer.write(event_image)
    blended_writer.write(blended_image)

    # 更新帧计数器
    frame_counter += 1

def display_preview(data):
    global frame_counter
    frames = data.getFrames("frames")
    events = data.getEvents("events")

    latest_image = None
    if len(frames) > 0:
        latest_image = frames[-1].image
        if len(frames[-1].image.shape) != 3:
            latest_image = cv.cvtColor(latest_image, cv.COLOR_GRAY2BGR)
        frame_copy = latest_image.copy()
        # cv.imshow("Frame Preview", frame_copy)
    else:
        return

    if len(events) > 0:
        print(f"********************************************** \n [{events.shape}]")
        event_image = visualizer.generateImage(events)
        event_image = cv.resize(event_image, (latest_image.shape[1], latest_image.shape[0]))
        # cv.imshow("Event Preview", event_image)
    else:
        return

    blended_image = visualizer.generateImage(events, latest_image)
    blended_image = cv.resize(blended_image, (latest_image.shape[1], latest_image.shape[0]))
    # cv.imshow("Blended Preview", blended_image)
    # cv.imshow("Preview", cv.hconcat([blended_image, event_image, frame_copy]))
    # cv.waitKey(33)

    # 保存图片和视频
    # print(f"********************************************** \n [{event_image.shape}]")
    # print(f"event_image: [{event_image}]")
    save_images_and_videos(frame_copy, event_image, blended_image)

    if cv.waitKey(2) == 27: # 按 ESC 键退出
        frame_writer.release()
        event_writer.release()
        blended_writer.release()
        # cv.destroyAllWindows()
        exit(0)

def main():
    slicer.doEveryTimeInterval(timedelta(milliseconds=33), display_preview)

    while reader.isRunning():
        events = reader.getNextEventBatch()
        if events is not None:
            slicer.accept("events", events)

        frame = reader.getNextFrame()
        if frame is not None:
            slicer.accept("frames", [frame])

if __name__ == '__main__':
    main()