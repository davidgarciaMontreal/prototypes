package com.industries.garcam.androidgames.framework;

public interface Graphics {

    public static enum PixmapFormat   {
        ARGB8888,  ARGB4444,  RGB565
    }

    /**
     * Loads image given in either JPEG or PNG
     * @param fileName Asset in the applications's APK File
     * @param format {@link PixmapFormat}
     * @return a new Pixmap as specified by format
     */
    public Pixmap  newPixmap(String fileName,  PixmapFormat format);

    /**
     * Clear the with the given color
     * @param color
     */
    public void  clear(int color);

    /**
     * Draw a Pixel to the FrameBuffer
     * @param x
     * @param y
     * @param color
     */
    public void  drawPixel(int  x, int y, int color);

    /**
     * Draw a line to the FrameBuffer
     * @param x
     * @param y
     * @param x2
     * @param y2
     * @param color
     */
    public void  drawLine(int  x, int y, int x2,  int y2,  int color);

    /**
     * Draw rectactangle to the FrameBuffer
     * @param x
     * @param y
     * @param width
     * @param height
     * @param color
     */
    public void  drawRect(int  x, int y, int width, int height, int color);

    /**
     * Draw PixMap
     * @param pixmap
     * @param x
     * @param y
     * @param srcX
     * @param srcY
     * @param srcWidth
     * @param srcHeight
     */
    public void  drawPixmap(Pixmap pixmap, int x, int y, int srcX,  int srcY,
                            int srcWidth,  int srcHeight);

    /**
     * Draws rectangular portions of a pixmas
     * @param pixmap
     * @param x
     * @param y
     */
    public void  drawPixmap(Pixmap pixmap, int x, int y);

    /**
     *
     * @return Width of the framebutter in pixels
     */
    public int  getWidth();

    /**
     *
     * @return Height of the framebuffer in pixels
     */
    public int  getHeight();
}