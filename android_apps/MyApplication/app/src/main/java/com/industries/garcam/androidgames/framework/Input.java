package com.industries.garcam.androidgames.framework;
import java.util.List;

public interface Input {
    // Dalvik is still slow when calling methods
    // so forget about encapsulation
    public class KeyEvent {

        public static final int KEY_DOWN = 0;
        public static final int KEY_UP = 0;
        public int type;
        public int keyCode;
        public char keyChar;
    }

    public static class TouchEvent {
        /**
         * TouchEvent’s type, the position of the finger relative
         * to the UI component’s origin, and the pointer ID that
         * was given to the finger by the touchscreen driver.
         */
        public static final int TOUCH_DOWN = 0;
        public static final int TOUCH_UP = 1;
        public static final int TOUCH_DRAGGED = 2;
        public int type;
        public int x, y;
        public int pointer;
    }

    // Polling methods
    public boolean isKeyPressed(int keyCode);
    public boolean isTouchDown(int pointer);
    public int getTouchX(int pointer);
    public int getTouchY(int pointer);
    public float getAccelX();
    public float getAccelY();
    public float getAccelZ();

    // Event-based handling
    public List<KeyEvent> getKeyEvents();
    public List<TouchEvent> getTouchEvents();
}
