import os
import subprocess
import sys

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def burn_video_file(video_path, subtitle_path, output_path):
    """
    Burns subtitles into a single video file.
    """
    subtitle_file_ffmpeg = subtitle_path.replace('\\', '/').replace(':', '\\:')

    def run_ffmpeg(encoder, preset, additional_args=[]):
        cmd = [
            "ffmpeg", "-y", "-loglevel", "error", "-hide_banner",
            '-i', video_path,
            '-vf', f"subtitles='{subtitle_file_ffmpeg}'",
            '-c:v', encoder,
            '-preset', preset,
            '-b:v', '5M',
            '-pix_fmt', 'yuv420p',
            '-c:a', 'copy',
            output_path
        ] + additional_args
        subprocess.run(cmd, check=True, capture_output=True)

    try:
        run_ffmpeg("h264_nvenc", "p1")
        return True, "NVENC Success"
    except subprocess.CalledProcessError as e:
        print(f"NVENC error ({str(e)}). Falling back to CPU (libx264)...")
        try:
            run_ffmpeg("libx264", "ultrafast")
            return True, "CPU Success"
        except subprocess.CalledProcessError as e2:
            err_msg = f"FATAL ERROR burning subtitles on {os.path.basename(video_path)}: {e2}"
            if e2.stderr:
                err_msg += f" | FFmpeg Log: {e2.stderr.decode('utf-8')}"
            print(err_msg)
            return False, err_msg
    except Exception as e:
        return False, str(e)

def burn(project_folder="tmp"):
    if project_folder and not os.path.isabs(project_folder):
        project_folder_abs = os.path.abspath(project_folder)
    else:
        project_folder_abs = project_folder

    subs_folder = os.path.join(project_folder_abs, 'subs_ass')
    videos_folder = os.path.join(project_folder_abs, 'final')
    output_folder = os.path.join(project_folder_abs, 'burned_sub')

    os.makedirs(output_folder, exist_ok=True)

    if not os.path.exists(videos_folder):
        print(f"Final videos folder not found: {videos_folder}")
        return

    files = os.listdir(videos_folder)
    if not files:
        print("No files found in 'final' folder to burn subtitles.")
        return

    for video_file in files:
        if video_file.endswith(('.mp4', '.mkv', '.avi')):
            if "temp_video_no_audio" in video_file:
                continue

            video_name = os.path.splitext(video_file)[0]
            subtitle_file = os.path.join(subs_folder, f"{video_name}.ass")

            if not os.path.exists(subtitle_file):
                subtitle_file_processed = os.path.join(subs_folder, f"{video_name}_processed.ass")
                if os.path.exists(subtitle_file_processed):
                    subtitle_file = subtitle_file_processed

            if os.path.exists(subtitle_file):
                output_file = os.path.join(output_folder, f"{video_name}_subtitled.mp4")
                print(f"Burning: {video_name}...")
                success, msg = burn_video_file(os.path.join(videos_folder, video_file), subtitle_file, output_file)
                if success:
                    print(f"Done: {output_file}")
                else:
                    print(f"Fail: {msg}")
            else:
                print(f"Subtitle not found for: {video_name} at {subtitle_file}")
