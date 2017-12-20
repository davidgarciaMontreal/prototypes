package com.industries.garcam.androidgames.framework;

import com.industries.garcam.androidgames.framework.Graphics.PixmapFormat;

public interface Pixmap  {
    /**
     *
     * @return Width in pixels
     */
    public int  getWidth();

    /**
     *
     * @return Height in pixels
     */
    public int  getHeight();

    /**
     *
     * @return the {@link android.graphics.PixelFormat} that this pixmap is stored with in RAM
     */
    public PixmapFormat getFormat();

    /**
     *
     */
    public void  dispose();
}