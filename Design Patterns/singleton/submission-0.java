static class Singleton {
    private static Singleton singletonInstance = null;
    private String value;

    private Singleton() {
        value = null;
    }

    public static Singleton getInstance() {
        if (singletonInstance == null) {
            singletonInstance = new Singleton();
        }
        return singletonInstance;
    }

    public String getValue() {
        return this.value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    
}
