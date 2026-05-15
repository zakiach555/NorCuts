import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKING_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(WORKING_DIR)

from i18n.i18n import I18nAuto
i18n = I18nAuto()

badges = ""

description = f"""
<div style="text-align: center; padding: 24px 0 8px;">
    <div style="display: inline-block; position: relative;">
        <h1 style="font-size: 3em; font-weight: 900; background: linear-gradient(135deg, #f59e0b 0%, #fbbf24 50%, #f97316 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin: 0 0 4px; letter-spacing: -2px; line-height: 1;">
            ✂️ NorCuts
        </h1>
    </div>
    <p style="color: #64748b; font-size: 0.9em; margin: 0 0 20px; letter-spacing: 2px; text-transform: uppercase; font-weight: 500;">
        {i18n('100% local • open source • no subscription required')}
    </p>

    <div style="display: flex; justify-content: center; gap: 12px; flex-wrap: wrap; max-width: 860px; margin: 0 auto;">
        <div style="background: linear-gradient(135deg, rgba(245,158,11,0.07), rgba(245,158,11,0.03)); border: 1px solid rgba(245,158,11,0.15); border-radius: 12px; padding: 14px 18px; text-align: center; min-width: 150px; flex: 1; max-width: 200px; backdrop-filter: blur(4px);">
            <div style="font-size: 1.6em; margin-bottom: 6px;">✂️</div>
            <div style="font-size: 0.82em; font-weight: 700; color: #f59e0b; margin-bottom: 4px; letter-spacing: 0.5px;">{i18n('Auto Cuts')}</div>
            <div style="font-size: 0.7em; color: #64748b; line-height: 1.3;">{i18n('Detect and cut the best viral moments automatically.')}</div>
        </div>
        <div style="background: linear-gradient(135deg, rgba(245,158,11,0.07), rgba(245,158,11,0.03)); border: 1px solid rgba(245,158,11,0.15); border-radius: 12px; padding: 14px 18px; text-align: center; min-width: 150px; flex: 1; max-width: 200px; backdrop-filter: blur(4px);">
            <div style="font-size: 1.6em; margin-bottom: 6px;">📝</div>
            <div style="font-size: 0.82em; font-weight: 700; color: #f59e0b; margin-bottom: 4px; letter-spacing: 0.5px;">{i18n('Dynamic Subtitles')}</div>
            <div style="font-size: 0.7em; color: #64748b; line-height: 1.3;">{i18n('Generate aesthetic subtitles (Hormozi style) automatically.')}</div>
        </div>
        <div style="background: linear-gradient(135deg, rgba(245,158,11,0.07), rgba(245,158,11,0.03)); border: 1px solid rgba(245,158,11,0.15); border-radius: 12px; padding: 14px 18px; text-align: center; min-width: 150px; flex: 1; max-width: 200px; backdrop-filter: blur(4px);">
            <div style="font-size: 1.6em; margin-bottom: 6px;">🤖</div>
            <div style="font-size: 0.82em; font-weight: 700; color: #f59e0b; margin-bottom: 4px; letter-spacing: 0.5px;">{i18n('Advanced AI')}</div>
            <div style="font-size: 0.7em; color: #64748b; line-height: 1.3;">Gemini · G4F · Local LLM</div>
        </div>
        <div style="background: linear-gradient(135deg, rgba(245,158,11,0.07), rgba(245,158,11,0.03)); border: 1px solid rgba(245,158,11,0.15); border-radius: 12px; padding: 14px 18px; text-align: center; min-width: 150px; flex: 1; max-width: 200px; backdrop-filter: blur(4px);">
            <div style="font-size: 1.6em; margin-bottom: 6px;">📱</div>
            <div style="font-size: 0.82em; font-weight: 700; color: #f59e0b; margin-bottom: 4px; letter-spacing: 0.5px;">{i18n('Vertical Focus')}</div>
            <div style="font-size: 0.7em; color: #64748b; line-height: 1.3;">TikTok · Shorts · Reels</div>
        </div>
    </div>
</div>
"""
