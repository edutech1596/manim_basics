#!/bin/bash

echo "📊 Rendering Progress Check"
echo "============================"
echo ""

# Count videos in media folder
MEDIA_COUNT=$(find media/videos -name "*.mp4" 2>/dev/null | wc -l | tr -d ' ')

# Count videos in rendered_videos folder
RENDERED_COUNT=$(find rendered_videos -name "*.mp4" 2>/dev/null | wc -l | tr -d ' ')

echo "✅ Videos rendered so far: $MEDIA_COUNT out of 54"
echo "📦 Videos copied to rendered_videos/: $RENDERED_COUNT"
echo ""

# Show percentage
PERCENTAGE=$((MEDIA_COUNT * 100 / 54))
echo "Progress: $PERCENTAGE%"
echo ""

# Show recent files
echo "📹 Most recently rendered:"
find media/videos -name "*.mp4" -type f 2>/dev/null | head -5 | while read file; do
    echo "  - $(basename "$file")"
done

echo ""
echo "💡 Tip: Run this script anytime to check progress:"
echo "   ./check_progress.sh" 